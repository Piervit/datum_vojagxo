import os
import re
import sys
import sqlalchemy
import datetime

from datetime import date



from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import create_session

import transir_grupoj
from TabelTransiro import TabelTransiro

################
# ueadb module was generated using
# sqlacodegen postgresql://postgres:kukurbeto@127.0.0.1/ueadb > ueadb.py
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




Base = declarative_base()
#Connect to the old ueadb
engine_ueadb = create_engine('postgresql://postgres:kukurbeto@127.0.0.1:5432/ueadb')
#Create a session to use the tables    
session_ueadb = create_session(bind=engine_ueadb)

#Connect to the old retdb
engine_retdb = create_engine('postgresql://postgres:kukurbeto@127.0.0.1:5432/retdb')
#Create a session to use the tables    
session_retdb = create_session(bind=engine_retdb)

#bonvolu kredi la bazon kun la collation utf8_bin

#Connect to the new db
engine_novuea = create_engine('mysql://root:@127.0.0.1:3306/novuea?charset=utf8' )
session_novuea = create_session(bind=engine_novuea)


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


def karakteroj_al_dato(karakteroj):
    if karakteroj is None:
        return None
    sep = "\/"
    print("date: "+karakteroj)
    date_pattern = re.compile('([0-9]{4})'+sep+'([0-9]{2})'+sep+'([0-9]{2})')
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
                    landkodo=(lando.landduliter))
            self.add(novlando.landkodo, novlando)

    def get_id(self, landkodo):
        if landkodo == "nev":
            raise NeValidaLando("nev")
        if landkodo == "mrt":
            raise NeValidaLando("mrt")
        if landkodo is None:
            print("ne devus None")
            raise NeDevusEstiNone("landkodo is None, cannot get id lando")
        res = self.trovi(landkodo)
        if(res is None):
            print("no rezult for "+landkodo)
            raise MalplenaError("get lando: malplena rezulto: "+landkodo)
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
            self.add(unomo, nunaUrbo)
            return
        try:
            print("vivant")
            idlando = self.transir_lando.get_id(ulandokodo)
            novurbo = novuea.Urbo(
                    nomoLoka=unomo, 
                    nomoEo=unomoEo, 
                    provinco=uProvinco, 
                    idLando=idlando
                    )
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
               self.add(unomo, novurbo)
           elif unomo is not None:
                print("Ne povis ligi "+str(unomo)+" al lando (landokodo "+str(ulandokodo)+" ne valida)")
           else :
               print("Urbo ne havas nomon: ne-konsiderita.")

    def get_id(self, urbonomo):
        res = self.trovi(urbonomo)
        if(res is None):
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


################### ILOJ RILATE AL GRUPOJ ########################

def get_grupojn():
    return transir_grupoj.get_grupojn()

class Grupo(Base):
    __tablename__ = 'grupo'

    id = Column(Integer, primary_key=True)
    mallongigilo= Column(String(255, 'utf8_unicode_ci'))
    nomo = Column(String(255, 'utf8_unicode_ci'))
    priskribo = Column(String(255, 'utf8_unicode_ci'))
    idAsocio = Column(Integer)


class TabelTransirGrupo(TabelTransiro):

    def konstkat_konvertilo(self, string, grupoj):
        sep =';'
        i = 0
        konstkat_grupoj = set()
        for code in string.split(sep):
            code = re.sub('#[0-9]*', "", code)
            if code in grupoj:
                konstkat_grupoj.add(self.get_id(code))
                i = i+1
            else:
                print(code+" ne trovita en la grupoj sed atendita.")
        return konstkat_grupoj 
    
    def __init__(self):
        TabelTransiro.__init__(self)

    def konverti(self, grupoj):
        for k_mlg, grupo in grupoj.items() :
            self.add(k_mlg, grupo)

    def get_id(self, mallongigilo):
        res = self.trovi(mallongigilo)
        if(res is None):
            raise MalplenaError("get grupo: ne konata grupo: "+ mallongigilo)
        else :
            return res.id


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
                    idLando = self.transir_lando.get_id(db_encode(peranto.landokodo))
                    )
            self.add(novPeranto.idUeakodo, novPeranto)

konv_landon = TabelTransirLando()
konv_landon.konverti(session_ueadb)

konv_urbon = TabelTransirUrbo(konv_landon)
konv_urbon.konverti(session_ueadb)


konv_faktemon = TabelTransirFaktemo()
konv_faktemon.konverti(session_retdb)

konv_grupon = TabelTransirGrupo()
konv_grupon.konverti(get_grupojn())

konv_asocionAuxUzanto = TabelTransiro()

konv_asocion = TabelTransirAsocio(konv_urbon, konv_asocionAuxUzanto, konv_grupon)
konv_asocion.konverti(session_ueadb, )

konv_uzanton = TabelTransirUzanto(konv_landon, konv_urbon, konv_asocionAuxUzanto)
konv_uzanton.konverti(session_ueadb)

konv_peranto = TabelTransirPeranto(konv_asocion, konv_uzanton, konv_landon)
konv_peranto.konverti(session_ueadb)

  
konv_landon.commit(session_novuea)
konv_urbon.commit(session_novuea)
konv_faktemon.commit(session_novuea)
konv_grupon.commit(session_novuea)
konv_asocion.commit(session_novuea)
konv_asocionAuxUzanto.commit(session_novuea)
konv_uzanton.commit(session_novuea)
konv_asocionAuxUzanto.commit(session_novuea)
konv_peranto.commit(session_novuea)
