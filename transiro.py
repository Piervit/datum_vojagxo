import os
import re
import sys
import sqlalchemy
import datetime
import time 

from datetime import date



from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import create_session

import transir_grupoj
import transir_uk

from TabelTransiro import TabelTransiro

################
# ueadb module was generated using
# sqlacodegen postgresql://postgres:kukurbeto@127.0.0.1/ueadb_11072017 > ueadb.py
#
###############
import ueadb

################
# ueadb module was generated using
# sqlacodegen postgresql://postgres:kukurbeto@127.0.0.1/retdb > retdb.py
#
###############
import retdb

################
# ueadb module was generated using
# sqlacodegen mysql://root:@127.0.0.1/uea_11072017 > ueamsql.py
#
###############
import ueamsql


################
# ueadb module was generated using
# sqlacodegen mysql://root:@127.0.0.1/novuea > novuea.py
#
###############
import novuea


class TransirError(Exception):
    """Base class for exceptions in this module."""
    pass

class NeUnikaError(TransirError):
    """Kiam ni uzas datumbazon kaj la rezulto devus esti unika sed ne estas."""
    pass

class MalplenaError(TransirError):
    """Kiam ni uzas datumbazon, ni atendas rezulton sed ĝi malplenas."""
    pass
class DevusEkzistiError(TransirError):
    """Kiam ni uzas datumbazon, ni atendas rezulton sed ĝi malplenas."""
    pass
class NeDevusEstiNone(TransirError):
    """Variable kiu ne devus esti None, estas."""
    pass
class NeValidaLando(TransirError):
    """Ne valida datumo."""
    pass

class NeValidaUeaKodo(TransirError):
    """Ne valida ueakodo."""
    pass




Base = declarative_base()
#Connect to the old ueadb
engine_ueadb = create_engine('postgresql://postgres:kukurbeto@127.0.0.1:5432/ueadb_11072017')
#Create a session to use the tables    
session_ueadb = create_session(bind=engine_ueadb)

#Connect to the old retdb
engine_retdb = create_engine('postgresql://postgres:kukurbeto@127.0.0.1:5432/retdb')
#Create a session to use the tables    
session_retdb = create_session(bind=engine_retdb)

#Connect to the old uea_mysql
engine_ueamsql = create_engine('mysql://root@127.0.0.1:3306/uea_11072017')
#Create a session to use the tables    
session_ueamsql = create_session(bind=engine_ueamsql)





#bonvolu kredi la bazon kun la collation utf8_bin

#Connect to the new db
engine_novuea = create_engine('mysql://root:@127.0.0.1:3306/novuea?charset=utf8' )
session_novuea = create_session(bind=engine_novuea)

metadata = MetaData()
metadata.create_all(engine_novuea)


############################# HELPAJ FUNKCIOJ #############################

def db_encode(vorto):
    if vorto is None:
        return ""
    else :
        return vorto.encode('utf-8')


#Por nun, ni nur havas landkategorio A kaj B.
#Mi ne trovis tiun informon en datumbazo do mi mane metas
def konverti_landkategorio(session_ueadb):
    session_novuea.begin()
    titolo = "A"
    priskribo = "" 
#TODO

def konverti_lando_landkategorion(session_ueadb):
    nop
#TODO

def valid_ueakodo(ueakodo):
    if(len(ueakodo) == 4):
        return ueakodo
    if(len(ueakodo) == 6):
        return ueakodo[:4]
    else :
        raise NeValidaUeaKodo


date_pattern = re.compile('([0-9]{4})\/([0-9]{2})\/([0-9]{2})')
def karakteroj_al_dato(karakteroj):
    global date_pattern
    if karakteroj is None:
        return None
    res = date_pattern.match(karakteroj)
    if res is None:
        print("Ne povis krei daton "+karakteroj)
        return None
    (jaro, monato, tago) = (int(res.group(1)), int(res.group(2)), int(res.group(3)))
    if monato == 0:
        monato = 1
    if tago == 0:
        tago = 1
    return datetime.date(jaro, monato, tago)



############################# HELPAJ FUNKCIOJ FINO #############################

class Lando(Base):
    __tablename__ = 'lando'

    id = Column(Integer, primary_key=True)
    nomoLoka = Column(String(255, 'utf8_unicode_ci'))
    radikoEo = Column(String(255, 'utf8_unicode_ci'))
    finajxoEo = Column(String(255, 'utf8_unicode_ci'))
    landkodo = Column(String(255, 'utf8_unicode_ci'))

class TabelTransirLando(TabelTransiro):

    def __init__(self):
        TabelTransiro.__init__(self)

    def konverti(self, session_ueadb):
        landkodojlist = session_ueadb.query(ueadb.t_landkodoj).all()
        for lando in landkodojlist:
            print("Land: {}, ".format(db_encode(lando.landoradiko)))
            novlando = novuea.Lando(
                    nomoLoka=db_encode(lando.landotraduko), 
                    radikoEo=db_encode(lando.landoradiko), 
                    finajxoEo=db_encode(lando.landofinajxo), 
                    landkodo=lando.landduliter)
            self.add(novlando.landkodo, novlando)

    def get_id(self, landkodo):
        if type(landkodo) is bytes:
            landkodo = str(landkodo)
        if landkodo == "nev":
            raise NeValidaLando("nev")
        if landkodo == "mrt":
            raise NeValidaLando("mrt")
        if landkodo is None:
            print("ne devus None")
            raise NeDevusEstiNone("landkodo is None, cannot get id lando")
        res = self.trovi(landkodo)
        if(res is None):
            print("no rezult for "+str(landkodo))
            raise MalplenaError("get lando: malplena rezulto: "+str(landkodo))
        else :
            return res.id


################### URBO ########################

class Urbo(Base):
    __tablename__ = 'urbo'

    id = Column(Integer, primary_key=True)
    nomoLoka = Column(String(255, 'utf8_unicode_ci'))
    nomoEo = Column(String(255, 'utf8_unicode_ci'))
    provinco= Column(String(255, 'utf8_unicode_ci'))
    idLando = Column(Integer)


class TabelTransirUrbo(TabelTransiro):
    def __init__(self, transir_lando):
        TabelTransiro.__init__(self)
        self.transir_lando = transir_lando

    def add_urbo(self, unomo, unomoEo, uProvinco, ulandokodo):
        if self.ene(unomo) :
            #Ni vidas ĉu ni povas riĉigi la objekton
            nunaUrbo = self.trovi(unomo)
            if nunaUrbo.nomoEo is None:
                nunaUrbo.nomoEo = unomoEo
            if nunaUrbo.provinco is None:
                nunaUrbo.provinco = uProvinco 
            if nunaUrbo.idLando is None:
                try: 
                    nunaUrbo.idlando = self.transir_lando.get_id(ulandokodo)
                except (NeValidaLando, NeDevusEstiNone, MalplenaError): 
                    nunaUrbo.idLando = None
            print("create type :"+str(type(unomo)))
            print("create val :"+str((unomo)))

            self.add(unomo, nunaUrbo)
            return
        try:
            idlando = self.transir_lando.get_id(ulandokodo)
            novurbo = novuea.Urbo(
                    nomoLoka=unomo, 
                    nomoEo=unomoEo, 
                    provinco=uProvinco, 
                    idLando=idlando
                    )
            print("create type :"+str(type(unomo)))
            print("create val :"+str((unomo)))
            self.add(unomo, novurbo)
        except (MalplenaError, NeValidaLando, NeDevusEstiNone):
           if unomo is not None and ulandokodo is None:
               print("Urbo "+str(unomo)+" ne havas validan landokodon. Aldonita sen ligilo al lando)")
               novurbo = novuea.Urbo(
                    nomoLoka=unomo, 
                    nomoEo=unomoEo, 
                    provinco=uProvinco, 
                    idLando=None
                    )
               print("create type :"+str(type(unomo)))
               print("create val :"+str((unomo)))
               self.add(unomo, novurbo)
           elif unomo is not None:
                print("Ne povis ligi "+str(unomo)+" al lando (landokodo "+str(ulandokodo)+" ne valida)")
           else :
               print("Urbo ne havas nomon: ne-konsiderita.")

    def get_id(self, urbonomo):
        if type(urbonomo) is str:
            urbonomo = bytes(urbonomo, 'utf8')
        res = self.trovi(urbonomo)
        if(res is None):
            print ("get urbo: ne trovita "+str(type(urbonomo)))
            print ("get urbo: ne trovita "+str(urbonomo))
            raise MalplenaError("get urbo: ne trovita "+str(urbonomo))
        else :
            return res.id
    
    def konverti(self, session_ueadb):
        #el tabelo urboj
        urbolist = session_ueadb.query(ueadb.t_urboj).all()
        for urbo in urbolist:
                self.add_urbo(db_encode(urbo.nomo), "", 
                    db_encode(urbo.provinco), urbo.landokodo)
        #el tabelo asocio
        uzantolist = session_ueadb.query(ueadb.t_tuta1).all()
        for uzanto in uzantolist:
                self.add_urbo(db_encode(uzanto.urbo), "", "", uzanto.landokodo)
        #el tabelo tuta1 (uzanto)
        asociolist = session_ueadb.query(ueadb.t_tuta1).all()
        for asocio in asociolist:
                self.add_urbo(db_encode(asocio.urbo), "", "", None)


################### URBO FINO ########################

class TabelTransirFaktemo(TabelTransiro):
    def __init__(self):
        TabelTransiro.__init__(self)

    def konverti(self, session_retdb):
        fakasociolist = session_retdb.query(retdb.t_fakasocioj).add_column("kategorio").distinct()
        for fakasocio in fakasociolist:
            novfako = novuea.Faktemo(
                    nomo=db_encode(fakasocio.kategorio), 
                    priskribo=db_encode(fakasocio.kategorio)
                    )
            self.add(novfako.nomo, novfako)


################### ILOJ RILATE AL GRUPAJ KATEGORIOJ ########################

def get_grupkategorioj():
    return transir_grupoj.grupa_kategorio()

class Kategorioj(Base):
    __tablename__ = 'grupo'

    id = Column(Integer, primary_key=True)
    nomo = Column(String(255, 'utf8_unicode_ci'))


class TabelTransirKategorio(TabelTransiro):

    def __init__(self):
        TabelTransiro.__init__(self)

    def konverti(self, katj):
        for k_nomo, kat in katj.items() :
            self.add(k_nomo, kat)

    def get_id(self, nomo):
        res = self.trovi(nomo)
        if(res is None):
            raise MalplenaError("get kategorio: ne konata kategorio: "+ nomo)
        else :
            return res.id



################### ILOJ RILATE AL GRUPOJ ########################


def get_grupojn():
    return transir_grupoj.get_grupojn()

def get_grupojn_no_kat():
    grupoj = {}
    for kat, kat_grupoj in transir_grupoj.get_grupojn().items():
        grupoj.update(kat_grupoj)
    return grupoj


def in_grupoj(grupo, grupoj):
    for kat_grupoj in grupoj:
        if grupo in kat_grupoj:
            return True
    return False


class TabelTransirGrupo(TabelTransiro):

    def konstkat_konvertilo(self, string, grupoj):
        sep =';'
        i = 0
        konstkat_grupoj = set()
        for code in string.split(sep):
            code = re.sub('#[0-9]*', "", code)
            if in_grupoj(code, grupoj):
                konstkat_grupoj.add(self.get_id(code))
                i = i+1
            else:
                print(code+" ne trovita en la grupoj sed atendita.")
        return konstkat_grupoj 
    
    def __init__(self):
        TabelTransiro.__init__(self)

    def konverti(self, katgrupoj):
        for k_kat, grupoj in katgrupoj.items() :
            for k_mlg, grupo in grupoj.items() :
                self.add(k_mlg, grupo)
            

    def get_id(self, mallongigilo):
        res = self.trovi(mallongigilo)
        if(res is None):
            raise MalplenaError("get grupo: ne konata grupo: "+ mallongigilo)
        else :
            return res.id


class TabelTransirGrupo_Kategorio(TabelTransiro):
    def __init__(self):
        TabelTransiro.__init__(self)

    def konverti(self, katgrupoj, tabelGrupoj, tabelKatj):
        i = 0
        for k_kat, grupoj in katgrupoj.items() :
            for k_mlg, grupo in grupoj.items() :
                id_kat = tabelKatj.get_id(k_kat)
                id_grup = tabelGrupoj.get_id(k_mlg)
                self.add(i , novuea.RefGrupoGrupaKategorio(
                                            idGrupo = id_grup,
                                            idGrupaKategorio = id_kat ,
                    ))
                i = i + 1



################### FINO ILOJ RILATE AL GRUPOJ ########################

#Iom specifa ĉar plenigita nur de TabelTransirAsocio kaj TabelTransirUzanto
def TabelTransirAsocioAuxUzanto(TabelTransiro):

    def __init__(self):
        TabelTransiro.__init__(self)
    


###################  RILATE AL ASOCIOJ ########################

#globala variablo: permesas sinkronigi la id de la tabeloj uzantoAuxAsocio, asocio kaj uzanto.
venonta_id_uzantoAuxAsocio = 1


venonta_id_uzantoAuxAsocio  =  1 
class TabelTransirAsocio(TabelTransiro):

    def __init__(self, transir_urbo, transir_asocioAuxUzanto, transir_grupoj):
        TabelTransiro.__init__(self)
        self.transir_urbo = transir_urbo
        self.transir_asocioAuxUzanto = transir_asocioAuxUzanto
        self.transir_grupoj = transir_grupoj
        self.email2asocio = {}
    
    def estas_faka(self, ueadb_asocio):
        set_grupoj = self.transir_grupoj.konstkat_konvertilo(ueadb_asocio.konstkat , get_grupojn())
        #if intersection is not empty, then True
        return len ({"fa.a", "fa.k", "fa.n", "fs.a"} & set_grupoj) != 0
    
    def estas_landa(self, ueadb_asocio):
        set_grupoj = self.transir_grupoj.konstkat_konvertilo(ueadb_asocio.konstkat , get_grupojn())
        #if intersection is not empty, then True
        return len ({"la.a", "la.n", "ls.a", "ls.n"} & set_grupoj) != 0
    
    def estas_junulara(self, ueadb_asocio):
        set_grupoj = self.transir_grupoj.konstkat_konvertilo(ueadb_asocio.konstkat , get_grupojn())
        #if intersection is not empty, then True
        return len ({"fs.a", "ls.a", "ls.n"} & set_grupoj) != 0

    def get_asocio_el_retadreso(self, retadreso):
        return self.email2asocio[retadreso]

    def konverti(self, session_ueadb ):
        global venonta_id_uzantoAuxAsocio
        asociolist = session_ueadb.query(ueadb.t_asocioj).all()
        #fakasociolist = session_retdb.query(retdb.t_fakasocioj).add_column("kategorio").distinct()
        for asocio in asociolist:
            novUzantoAuxAsocio = novuea.UzantoAuxAsocio(
                    id = venonta_id_uzantoAuxAsocio,
                    ueakodo = asocio.ueakodo
                    )
            idurbo = None
            asocia_nomo = asocio.familianomo
            if(asocia_nomo is None):
                asocia_nomo = asocio.personanomo
            try : 
                print("use type :"+str(type(asocio.urbo)))
                print("use val :"+str((asocio.urbo)))
                idurbo = self.transir_urbo.get_id(asocio.urbo)
            except (NeUnikaError, MalplenaError) :
                if asocio.urbo is None:
                    print("Asocio: la asocio "+asocia_nomo+" ne estas ligita al iu urbo")
                else:
                    print("Asocio "+asocia_nomo+": Ne povis ligi "+asocio.urbo+" al urbo ĉar la nomo estas plurfoje trovita en la datumbazo")
                idurbo= None
            
            self.transir_asocioAuxUzanto.add(novUzantoAuxAsocio.ueakodo, novUzantoAuxAsocio)
            novAsocio = novuea.Asocio(
                    id = venonta_id_uzantoAuxAsocio ,
                    nomo= asocia_nomo,
                    siglo= "",
                    adreso= asocio.adreso,
                    fondigxdato= None,
                    posxtkodo= asocio.posxtkodo,
                    idUrbo= idurbo ,
                    idFako= None,
                    lando= None,
                    telhejmo= asocio.telhejmo,
                    retposxto= asocio.retposxto,
                    delegFako= asocio.deleg_fako,
                    tttpagxo= asocio.tttpagxo,
                    junulara= self.estas_junulara(asocio),
                    faka= self.estas_faka(asocio),
                    landa= self.estas_landa(asocio),
                    abc= asocio.abc
                    )
            self.email2asocio[asocio.retposxto] = venonta_id_uzantoAuxAsocio
            venonta_id_uzantoAuxAsocio = venonta_id_uzantoAuxAsocio + 1
            self.add(novAsocio.nomo, novAsocio)

###################  FINO RILATE AL ASOCIOJ ########################
###################  RILATE AL UZANTOJ ########################

def get_titolon_personan_nomon(personanomo):
    abrevs = ["S-ro", "S-ino", "D-ro", "D-ino", "F-o", "F-ino", "Prof.", "Mag.", "Inĝ.", "G-o", "G-ino", "D-o", "D-ino" ]
    def check_abrev (nomo, abrev):
        if personanomo is None:
            return (None, None)
        pattern = re.compile(abrev+' (.*)')
        res = pattern.match(personanomo)
        if res is None:
            return (None, personanomo)
        else:
            return (abrev, res.group(1))
    titolo = ""
    found = 1 
    while found == 1:
        found = 0 
        for abrev in abrevs:
            (novtitolo, personanomo) = check_abrev(personanomo, abrev)
            if novtitolo is not None:
                found = 1
                titolo = titolo +" "+ novtitolo
    return (titolo, personanomo)
 

class TabelTransirUzanto(TabelTransiro):

    def __init__(self, transir_lando, transir_urbo, transir_asocioAuxUzanto):
        TabelTransiro.__init__(self)
        self.transir_lando = transir_lando
        self.transir_urbo = transir_urbo
        self.transir_asocioAuxUzanto = transir_asocioAuxUzanto
        self.email2uzanto = {}

    def konverti(self, session_ueadb ):
        global venonta_id_uzantoAuxAsocio
   
        uzantolist = session_ueadb.query(ueadb.t_tuta1).all()
        for uzanto in uzantolist:
            novUzantoAuxAsocio = novuea.UzantoAuxAsocio(
                    id = venonta_id_uzantoAuxAsocio,
                    ueakodo = uzanto.ueakodo
                    )
            self.transir_asocioAuxUzanto.add(novUzantoAuxAsocio.ueakodo,novUzantoAuxAsocio)
            lando = None
            valida = True
            morta = False
            try: 
                lando = self.transir_lando.get_id(uzanto.landokodo) 
            except NeValidaLando as e: 
                lando = None
                if str(e) == "nev":
                    valida = False
                if str(e) == "mrt":
                    morta = True
            except MalplenaError : 
                lando = None
            urbo = None
            try:
                urbo = self.transir_urbo.get_id(uzanto.urbo)
            except MalplenaError:
                urbo = None
    
            (titolo, personanomo) = get_titolon_personan_nomon(uzanto.personanomo)
            novUzanto = novuea.Uzanto(
                id = venonta_id_uzantoAuxAsocio,
                personanomo = personanomo,
                familianomo = uzanto.familianomo,
                titolo = titolo,
                bildo = "",
                personanomoIdentigilo = "", 
                familianomoIdentigilo = "",
                adreso = uzanto.adreso,
                posxtkodo = uzanto.posxtkodo,
                idLogxurbo = urbo,
                idlando = lando,
                naskigxtago = karakteroj_al_dato(uzanto.naskigxtago),
                morta = morta,
                mortdatekscio = None,
                mortdato = None,
                notoj = uzanto.notoj,
                profesio = uzanto.profesio,
                retposxto = uzanto.retposxto,
                telhejmo  = uzanto.telhejmo,
                teloficejo = uzanto.teloficejo,
                telportebla = uzanto.portebla,
                kerekzameno = False,
                kernivelo = None,
                kerdato = None,
                tttpagxo = uzanto.tttpagxo,
                validaKonto = valida,
                abc = uzanto.abc
            )
            self.email2uzanto[uzanto.retposxto] = venonta_id_uzantoAuxAsocio
            self.add((novUzanto.personanomo, novUzanto.familianomo), novUzanto)
            venonta_id_uzantoAuxAsocio = venonta_id_uzantoAuxAsocio + 1

def get_id_uzanto_aux_asocio(familianomo, personanomo, transir_asocio, transir_uzanto):
    #ni unue rigardas ene de la asocioj
    res = transir_asocio.trovi(familianomo)
    if(res is None ):
        #ni rigardu ĉe uzantoj
        res = transir_uzanto.trovi((personanomo, familianomo))
        if(res is None):
            raise MalplenaError("uzanto ne trovita: "+personanomo+" "+familianomo)
        else :
            return res.id
    else :
        return res.id

def get_id_uzanto_aux_asocio_from_ueakodo(ueakodo, transir_asocioAuxUzanto):
    print("ueakodo: "+ueakodo)
    res=transir_asocioAuxUzanto.trovi(ueakodo)
    if(res is None):
        raise MalplenaError("uzanto ne trovita: "+ueakodo)
    return res.id

def get_id_uzanto_aux_asocio_from_retadreso(retadreso, transir_asocio, transir_uzanto):
    res = transir_asocio.get_asocio_el_retadreso(retadreso)
    if(res is None ):
        #ni rigardu ĉe uzantoj
        res = transir_uzanto.get_uzanto_el_retadreso(retadreso)
        if(res is None):
            raise MalplenaError("uzanto ne trovita laû retadreso: "+retadreso)
        else :
            return res.id
    else :
        return res.id



def print_uzanto_aux_asocio(familianomo, personanomo):
    if familianomo is None:
        return personanomo
    elif personanomo is None:
        return familianomo
    else:
        return personanomo +" "+ familianomo

class TabelTransirPeranto(TabelTransiro):
    def __init__(self, transir_asocio, transir_uzanto, transir_lando):
        TabelTransiro.__init__(self)
        self.transir_asocio = transir_asocio
        self.transir_uzanto = transir_uzanto
        self.transir_lando = transir_lando


    def konverti(self, session_ueadb):
        perantolist = session_ueadb.query(ueadb.t_perant).all()
        for peranto in perantolist:
            (titolo, personanomo) = get_titolon_personan_nomon(peranto.personanomo)
            id_uzantoAuxAsocio = get_id_uzanto_aux_asocio(peranto.familianomo, personanomo, self.transir_asocio, self.transir_uzanto)

            novPeranto = novuea.Peranto(
                    idUeakodo = id_uzantoAuxAsocio,
                    idLando = self.transir_lando.get_id(peranto.landokodo)
                    )
            self.add(novPeranto.idUeakodo, novPeranto)

###################  RILATE AL ANECO ########################


#Iom specifa ĉar plenigita nur de TabelTransirAsocio kaj TabelTransirUzanto
class TabelTransirAneco(TabelTransiro):

    def __init__(self):
        TabelTransiro.__init__(self)
        self.jarkat_pattern = re.compile('([a-zA-Z]*)([0-9]*)')
    
    def jarkat_konvertilo(self, string, grupoj):
        sep =';'
        kat_grupoj = {}
        if string is None:
            return kat_grupoj
        for code in string.split(sep):
            pat_jaro = re.match(self.jarkat_pattern, code)
            if pat_jaro is None:
                print("None for " + string )
                print("specifically " + code)
            else:
                grupo= pat_jaro.group(1)
                jaro = None
                try:
                    jaro = pat_jaro.group(2)
                except:
                    jaro = None
                #por korekti pasintecon
                if grupo == "mak":
                    grupo = "mat";
                if grupo == "mjk":
                    grupo = "mjt";
                if grupo in grupoj:
                    kat_grupo = set()
                    try:
                        kat_grupo = kat_grupoj[grupo]
                    except:
                        kat_grupo = set()
                    kat_grupo.add(jaro)
                    kat_grupoj[grupo] = kat_grupo
                else:
                    print(code+" ne trovita en la grupoj sed atendita.")
        return kat_grupoj 
 

    def konverti(self, session_ueadb, tabel_grupo, tabel_asocio, tabel_uzanto):
        uzantolist = session_ueadb.query(ueadb.t_tuta1).all()
        i = 0
        for uzanto in uzantolist:
            #enhavas la grupojn de la uzanto laû jaroj
            uzanto_personanomo = get_titolon_personan_nomon(uzanto.personanomo)[1]
            tbl_jar_grup = self.jarkat_konvertilo(uzanto.jarkat, get_grupojn_no_kat())
            idAno = get_id_uzanto_aux_asocio(uzanto.familianomo, uzanto_personanomo, tabel_asocio, tabel_uzanto)
            for grupo, jaroj in tbl_jar_grup.items():
                id_grupo = tabel_grupo.get_id(grupo)
                for jaro in jaroj:
                    komencadato = None
                    findato = None
                    if jaro is not None :
                        komencdato =  karakteroj_al_dato(jaro+"/01/01")
                        findato = karakteroj_al_dato(jaro+"/12/31")
                    try : 
                        aneco = novuea.Aneco (
                            idAno = idAno,
                            idGrupo = id_grupo, 
                            komencdato = komencdato,
                            findato = findato,
                            dumviva = False
                        )
                        self.add(i, aneco)
                        i = i+1
                    except: 
                        print("Malvalidan grupon por uzanto " + print_uzanto_aux_asocio(uzanto.familianomo, uzanto.personanomo) + ": " + grupo)


###################  FINO RILATE AL ANECO ########################

###################  RILATE AL DISSENDO ########################
class TabelTransirDissendo(TabelTransiro):

    def __init__(self):
        TabelTransiro.__init__(self)

    def get_ueakodo_from_retuzanto(self, session_ueamsql, uznomo):
        print("uznomo: "+uznomo)
        if (uznomo == "manuela"):
            return "ronc"
        elif (uznomo == "osmo"):
            return "osmo"
        elif (uznomo == "maritza"):
            return "itza"
        elif (uznomo == "james"):
            return "jrpi"
        elif (uznomo == "rocxjo"):
            return "uurm"
        elif (uznomo == "fiskot"):
            return "pfko"
        elif (uznomo == "mevamevo"):
            return "mevc"
        elif (uznomo == "Roxane"):
            return "rfrn"
        else:
            uzanto = session_ueamsql.query(ueamsql.Uzantoj).filter(ueamsql.Uzantoj.uznomo == uznomo).first()
            if uzanto is None:
                print ("Ne Valida uzanto: "+uznomo)
                raise NeValidaUeaKodo
            return uzanto.kodo

    def konverti(self, session_ueamsql, transir_asocioAuxUzanto):
        dissendolist = session_ueamsql.query(ueamsql.Dissendoj).all()
        for dissendo in dissendolist:
            try:
                novdissendo = novuea.Dissendo (
                    id= dissendo.id,
                    dissendanto = get_id_uzanto_aux_asocio_from_ueakodo(
                        self.get_ueakodo_from_retuzanto(session_ueamsql, dissendo.nomo),
                        transir_asocioAuxUzanto
                        ),
                    nomede = dissendo.nomede, 
                    dato = dissendo.kiam,
                    temo = dissendo.temo,
                    teksto = dissendo.teksto
                    )
                self.add(dissendo.id, novdissendo)
            except NeValidaUeaKodo:
                print ("ne povis aldono dissendo pro nevalida nomo de dissendanto: " + dissendo.nomo)
 
class TabelTransirDissendoDemanderoj(TabelTransiro):

    def __init__(self):
        TabelTransiro.__init__(self)

    def konverti(self, session_ueamsql):
        demanderojlist = session_ueamsql.query(ueamsql.DissendojEnketoj).all()
        for demandero in demanderojlist:
            novdemandero = novuea.DissendoDemandero(
                id= demandero.id,
                idDissendo = demandero.dissendo,
                demNum = demandero.dem_num,
                demTeksto = demandero.dem_teksto
                )
            self.add(id, novdemandero)
 
 
class TabelTransirDissendoRespondoj(TabelTransiro):

    def __init__(self):
        TabelTransiro.__init__(self)

    def konverti(self, session_ueamsql, transir_asocio, transir_uzanto):
        respondojlist = session_ueamsql.query(ueamsql.DissendojRespondoj).all()
        for respondo in respondojlist:
            retposxto = None
            idUzantoAuxAsocio = None
            try:
                idUzantoAuxAsocio = get_id_uzanto_aux_asocio_from_retadreso(
                    respondo.retposxto,
                    transir_asocio,
                    transir_uzanto)
            except MalplenaError:
                retposxto = respondo.retposxto
                idUzantoAuxAsocio= None
            novrespondo = novuea.RefDissendoRespondoj(
                idUzantoAuxAsocio = idUzantoAuxAsocio,
                retposxto = retposxto,
                idDissendoDemandero = respondo.enketo
                )
            self.add(i, novrespondo)
 

class TabelTransirRetlisto(TabelTransiro):
 
    def __init__(self):
        TabelTransiro.__init__(self)

    def konverti(self, session_retdb):
        retlistolist= session_retdb.query(retdb.t_abonoj).add_column("abono").distinct()
        i = 0
        for retlisto in retlistolist:
            novretlisto= novuea.Retlisto(
                id = i,
                nomo = retlisto.abono,
                priskribo = None
                )
            self.add(novretlisto.nomo, novrespondo)
            i = i+1
 

class TabelTransirRetlistoAbono(TabelTransiro):
 
    def __init__(self):
        TabelTransiro.__init__(self)

    def konverti(self, session_retdb, transir_retlisto):
        list= session_retdb.query(retdb.t_abonoj).add_column("abono").distinct()
        retlistolist= session_retdb.query(retdb.t_abonoj).add_column("abono").distinct()
        i = 0
        for retlisto in retlistolist:
            novretlisto= novuea.Retlisto(
                ekde = retlisto.tempo,
                abono = transir_retlisto.trovi(retlisto.abono),
                idUzanto = get_id_uzanto_aux_asocio_from_ueakodo(
                    valid_ueakodo(retlisto.ueakodo)),
                formato_html = retlisto.formato == "html",
                kodigxo_utf8 = retlisto.kodigo == "utf",
                retadreso = retlisto.retadreso
                )
            self.add(i, novretlisto)
            i = i+1
 
class TabelTransirKongreso (TabelTransiro):
 
    def __init__(self):
        TabelTransiro.__init__(self)

    def konverti(self, transir_urbo):
        kongreso_kat_uk = novuea.KongresaKategorio(
                    id = 1,
                    nomo = "UK"
                )
        self.add("UK", kongreso_kat_uk)
        kongresolist = transir_uk.get_ukj()
        id_kongreso = 0
        for kongreso in retlistolist:
            novkongreso = novuea.Kongreso(
                id = id_kongreso,
                titolo= kongreso.titolo,
                bildo = "",
                idUrbo = transir_urbo.get_id(kongreso.urbo),
                jaro = kongreso.jaro,
                numero = kongreso.numero ,
                komencdato= NULL,
                temo = kongreso.temo,
                priskribo = "",
                aligxinto= kongreso.aligxinto,
                findato = NULL
                )
            ref_kongreso_kat_kongreso = novuea.RefKongresaKategorioKongreso(
                    idKongresaKategorio = 1,
                    idKongreso= id_kongreso
                    )
            id_kongreso = id_kongreso +1
            self.add(kongreso.jaro, novkongreso)
 
#class TabelTransirAntauxPostKongreso (TabelTransiro):
# 
#    def __init__(self):
#        TabelTransiro.__init__(self)
#
#    def konverti(self, transir_urbo):
#        akpklist= session_ueamsql.query(ueamsql.t_akpk).all()
#        for akpk in akpklist:
#            novkongreso = novuea.Kongreso(
#                titolo= akpk.titolo,
#                bildo = "",
#                idUrbo = ,
#                jaro = kongreso.jaro,
#                numero = ,
#                komencdato= NULL,
#                temo = kongreso.temo,
#                priskribo = "",
#                aligxinto= kongreso.aligxinto,
#                findato = NULL
#                )
#            self.add(kongreso.jaro, novkongreso)
 



###################  FINO RILATE AL DISENDO ########################


def clear_db():
    session_novuea.begin()
    for table in reversed(metadata.sorted_tables):
        con.execute(table.delete())
        print (table + "cleared")
        session_novuea.commit()
    session_novuea.close()

clear_db()


komenco  = time.clock()

konv_landon = TabelTransirLando()
konv_landon.konverti(session_ueadb)
konv_landon.commit(session_novuea)

post_lando = time.clock()
print("time post lando : "+ str(post_lando - komenco))

konv_urbon = TabelTransirUrbo(konv_landon)
konv_urbon.konverti(session_ueadb)
konv_urbon.commit(session_novuea)

post_urbo = time.clock()
print("time post urbo : "+ str(post_urbo - post_lando))


konv_faktemon = TabelTransirFaktemo()
konv_faktemon.konverti(session_retdb)
konv_faktemon.commit(session_novuea)

post_faktemo= time.clock()
print("time post faktemo: "+ str(post_faktemo - post_urbo))

#konv_kategorion = TabelTransirKategorio()
#konv_kategorion.konverti(get_grupkategorioj())
#konv_kategorion.commit(session_novuea)
#
#post_kategorio= time.clock()
#print("time post kategorio: "+ str(post_kategorio - post_faktemo))
#
konv_grupon = TabelTransirGrupo()
konv_grupon.konverti(get_grupojn())
konv_grupon.commit(session_novuea)

post_grupo= time.clock()
#print("time post grupo: "+ str(post_grupo - post_kategorio))


#konv_grupon_kat = TabelTransirGrupo_Kategorio()
#konv_grupon_kat.konverti(get_grupojn(), konv_grupon, konv_kategorion)
#konv_grupon_kat.commit(session_novuea)
#
#post_grupo_kat= time.clock()
#print("time post grupo_kat: "+ str(post_grupo_kat - post_grupo))

konv_asocionAuxUzanto = TabelTransiro()

konv_asocion = TabelTransirAsocio(konv_urbon, konv_asocionAuxUzanto, konv_grupon)
konv_asocion.konverti(session_ueadb, )
konv_asocion.commit(session_novuea)

post_asocio= time.clock()
#print("time post asocio: "+ str(post_asocio - post_grupo_kat))

konv_uzanton = TabelTransirUzanto(konv_landon, konv_urbon, konv_asocionAuxUzanto)
konv_uzanton.konverti(session_ueadb)
konv_uzanton.commit(session_novuea)
konv_asocionAuxUzanto.commit(session_novuea)

post_uzanto= time.clock()
print("time post uzanto: "+ str(post_uzanto - post_asocio))


#konv_peranto = TabelTransirPeranto(konv_asocion, konv_uzanton, konv_landon)
#konv_peranto.konverti(session_ueadb)
#konv_peranto.commit(session_novuea)
#
#post_peranto= time.clock()
#print("time post peranto: "+ str(post_peranto - post_asocio))

#konv_aneco = TabelTransirAneco()
#konv_aneco.konverti(session_ueadb, konv_grupon, konv_asocion, konv_uzanton)
#konv_aneco.commit(session_novuea)
#
#post_aneco= time.clock()
#print("time post aneco: "+ str(post_aneco - post_peranto))

konv_dissendo = TabelTransirDissendo()
konv_dissendo.konverti(session_ueamsql, konv_asocionAuxUzanto)
konv_dissendo.commit(session_novuea)

post_dissendo= time.clock()
#print("time post dissendo: "+ str(post_dissendo - post_aneco))

konv_dissendoDemanderoj = TabelTransirDissendoDemanderoj()
konv_dissendoDemanderoj.konverti(session_ueamsql )
konv_dissendoDemanderoj.commit(session_novuea)



konv_dissendoRespondoj = TabelTransirDissendoRespondoj()
konv_dissendoRespondoj.konverti(session_ueamsql, konv_asocion, konv_uzanton )
konv_dissendoRespondoj.commit(session_novuea)



konv_kongreso = TabelTransirKongreso()
konv_kongreso.konverti(konv_urbon)
konv_kongreso.commit(session_novuea)


