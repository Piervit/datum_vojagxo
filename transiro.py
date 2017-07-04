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

def db_encode(vorto):
    if vorto is None:
        return ""
    else :
        return vorto.encode('utf-8')

def konverti_landon(session_ueadb):
    session_novuea.begin()
    landkodojlist = session_ueadb.query(ueadb.t_landkodoj).all()
    for lando in landkodojlist:
        print("Land: {}, ".format(db_encode(lando.landoradiko)))
        novlando = novuea.Lando(
                nomoLoka=db_encode(lando.landotraduko), 
                radikoEo=db_encode(lando.landoradiko), 
                finajxoEo=db_encode(lando.landofinajxo), 
                landkodo=db_encode(lando.landduliter))
        session_novuea.add(novlando)
    session_novuea.commit()

class Lando(Base):
    __tablename__ = 'lando'

    id = Column(Integer, primary_key=True)
    nomoLoka = Column(String(255, 'utf8_unicode_ci'))
    radikoEo = Column(String(255, 'utf8_unicode_ci'))
    finajxoEo = Column(String(255, 'utf8_unicode_ci'))
    landkodo = Column(String(255, 'utf8_unicode_ci'))



def get_id_lando(landkodo):
    if landkodo == "nev":
        raise NeValidaLando("nev")
    if landkodo == "mrt":
        print("mrt "+landkodo)
        raise NeValidaLando("mrt")
    if landkodo is None:
        print("ne devus None")
        raise NeDevusEstiNone("landkodo is None, cannot get id lando")
    res = session_novuea.execute(select([Lando]).where(Lando.landkodo == landkodo))
    if(res.rowcount == 0):
        print("no rezult for "+landkodo)
        raise MalplenaError("get lando: ne-unika rezulto: "+landkodo)
    elif(res.rowcount > 1):
        print("tro da rezult for "+landkodo)
        raise NeUnikaError("get lando: ne-unika rezulto: "+landkodo)
    else :
        print("scal")
        return res.scalar()




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


    


################### URBO ########################
#Ni ne tuj metas datumojn en la db, sed atendas kolekti ĉiujn el ili por meti
#en la db. Atendanto, ili estas en urboj_fresxaj



urboj_fresxaj = {} #urbo aldonita sed ne "commited"

def add_urbo(unomo, unomoEo, uProvinco, ulandokodo):
    global urboj_fresxaj 
    if unomo in urboj_fresxaj:
        #Ni vidas ĉu ni povas riĉigi la objekton
        nunaUrbo = urboj_fresxaj[unomo]
        if nunaUrbo.nomoEo is None:
            nunaUrbo.nomoEo = unomoEo
        if nunaUrbo.provinco is None:
            nunaUrbo.provinco = uProvinco 
        if nunaUrbo.idLando is None:
            try: 
                nunaUrbo.idlando = get_id_lando(ulandokodo)
            except : 
                nunaUrbo.idLando = None
        urboj_fresxaj[unomo] = nunaUrbo
        return
    try:
        idlando = get_id_lando(ulandokodo)
        novurbo = novuea.Urbo(
                nomoLoka=unomo, 
                nomoEo=unomoEo, 
                provinco=uProvinco, 
                idLando=idlando
                )
        urboj_fresxaj[unomo] = novurbo
    except :
       if unomo is not None and ulandokodo is None:
           print("Urbo "+str(unomo)+" ne havas validan landokodon. Aldonita sen ligilo al lando)")
           novurbo = novuea.Urbo(
                nomoLoka=unomo, 
                nomoEo=unomoEo, 
                provinco=uProvinco, 
                idLando=None
                )
           urboj_fresxaj[unomo] = novurbo
       elif unomo is not None:
            print("Ne povis ligi "+str(unomo)+" al lando (landokodo "+str(ulandokodo)+" ne valida)")
       else :
           print("Urbo ne havas nomon: ne-konsiderita.")

def purigu_fresxaj_urboj():
    global urboj_fresxaj 
    urboj_fresxaj.clear()

class Urbo(Base):
    __tablename__ = 'urbo'

    id = Column(Integer, primary_key=True)
    nomoLoka = Column(String(255, 'utf8_unicode_ci'))
    nomoEo = Column(String(255, 'utf8_unicode_ci'))
    provinco= Column(String(255, 'utf8_unicode_ci'))
    idLando = Column(Integer)



def get_id_urbo(urbonomo):
    res = session_novuea.execute(select([Urbo]).where(Urbo.nomoLoka == urbonomo))
    if(res.rowcount == 0):
        raise MalplenaError("get urbo: ne trovita "+str(urbonomo))
    elif(res.rowcount > 1):
        raise NeUnikaError("get urbo: ne-unika rezulto: "+urbonomo)
    else :
        return res.scalar()



def konverti_urbon(session_ueadb):
    #el tabelo urboj
    urbolist = session_ueadb.query(ueadb.t_urboj).all()
    for urbo in urbolist:
            add_urbo(db_encode(urbo.nomo), "", 
                db_encode(urbo.provinco), urbo.landokodo)
    #el tabelo asocio
    uzantolist = session_ueadb.query(ueadb.t_tuta1).all()
    for uzanto in uzantolist:
            add_urbo(db_encode(uzanto.urbo), "", "", uzanto.landokodo)
    #el tabelo tuta1 (uzanto)
    asociolist = session_ueadb.query(ueadb.t_tuta1).all()
    for asocio in asociolist:
            add_urbo(db_encode(asocio.urbo), "", "", None)
    session_novuea.begin()
    for urbonomo, urbo in urboj_fresxaj.items():
        session_novuea.add(urbo)
    session_novuea.commit()
    purigu_fresxaj_urboj()

################### URBO FINO ########################

def konverti_faktemon(session_retdb):
    session_novuea.begin()
    fakasociolist = session_retdb.query(retdb.t_fakasocioj).add_column("kategorio").distinct()
    for fakasocio in fakasociolist:
        novfako = novuea.Faktemo(
                nomo=db_encode(fakasocio.kategorio), 
                priskribo=db_encode(fakasocio.kategorio)
                )
        session_novuea.add(novfako)
    session_novuea.commit()


################### ILOJ RILATE AL GRUPOJ ########################

class Grupo(Base):
    __tablename__ = 'grupo'

    id = Column(Integer, primary_key=True)
    mallongigilo= Column(String(255, 'utf8_unicode_ci'))
    nomo = Column(String(255, 'utf8_unicode_ci'))
    priskribo = Column(String(255, 'utf8_unicode_ci'))
    idAsocio = Column(Integer)


def get_grupojn():
    return transir_grupoj.get_grupojn()

def konverti_grupojn(grupoj):
    session_novuea.begin()
    for k_mlg, grupo in grupoj.items() :
        session_novuea.add(grupo)
    session_novuea.commit()

def get_id_grupo(mallongigilo):
    res = session_novuea.execute(select([Grupo]).where(Grupo.mallongigilo == mallongigilo))
    if(res.rowcount == 0):
        raise MalplenaError("get grupo: ne konata grupo: "+ mallongigilo)
    elif(res.rowcount > 1):
        raise NeUnikaError("get grupo: ne-unika rezulto: "+ mallongigilo)
    else :
        return res.scalar()


def konstkat_konvertilo(string, grupoj):
    sep =';'
    i = 0
    konstkat_grupoj = set()
    for code in string.split(sep):
        code = re.sub('#[0-9]*', "", code)
        if code in grupoj:
            konstkat_grupoj.add(get_id_grupo(code))
            i = i+1
        else:
            print(code+" ne trovita en la grupoj sed atendita.")
    return konstkat_grupoj 


################### FINO ILOJ RILATE AL GRUPOJ ########################
###################  RILATE AL ASOCIOJ ########################

def estas_faka(ueadb_asocio):
    set_grupoj = konstkat_konvertilo(ueadb_asocio.konstkat , get_grupojn())
    #if intersection is not empty, then True
    return len ({"fa.a", "fa.k", "fa.n", "fs.a"} & set_grupoj) != 0

def estas_landa(ueadb_asocio):
    set_grupoj = konstkat_konvertilo(ueadb_asocio.konstkat , get_grupojn())
    #if intersection is not empty, then True
    return len ({"la.a", "la.n", "ls.a", "ls.n"} & set_grupoj) != 0

def estas_junulara(ueadb_asocio):
    set_grupoj = konstkat_konvertilo(ueadb_asocio.konstkat , get_grupojn())
    #if intersection is not empty, then True
    return len ({"fs.a", "ls.a", "ls.n"} & set_grupoj) != 0


#globala variablo: permesas sinkronigi la id de la tabeloj uzantoAuxAsocio, asocio kaj uzanto.
venonta_id_uzantoAuxAsocio = 1

def konverti_asocion(session_ueadb):
    global venonta_id_uzantoAuxAsocio
    session_novuea.begin()
    asociolist = session_ueadb.query(ueadb.t_asocioj).all()
    #fakasociolist = session_retdb.query(retdb.t_fakasocioj).add_column("kategorio").distinct()
    for asocio in asociolist:
        novUzantoAuxAsocio = novuea.UzantoAuxAsocio(
                id = venonta_id_uzantoAuxAsocio,
                ueakodo = asocio.ueakodo
                )
        idurbo = None
        try :
            idurbo = get_id_urbo(asocio.urbo)
        except (NeUnikaError, MalplenaError) :
            if asocio.urbo is None:
                print("Asocio: la asocio "+asocio.familianomo+" ne estas ligita al iu urbo")
            else:
                print("Asocio "+asocio.familianomo+": Ne povis ligi "+asocio.urbo+" al urbo ĉar la nomo estas plurfoje trovita en la datumbazo")
            idurbo= None
        
        session_novuea.add(novUzantoAuxAsocio)
        novAsocio = novuea.Asocio(
                id = venonta_id_uzantoAuxAsocio ,
                nomo= asocio.familianomo,
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
                junulara= estas_junulara(asocio),
                faka= estas_faka(asocio),
                landa= estas_landa(asocio),
                abc= asocio.abc
                )
        venonta_id_uzantoAuxAsocio = venonta_id_uzantoAuxAsocio + 1
        print("int :"+str(venonta_id_uzantoAuxAsocio))
        session_novuea.add(novAsocio)
    session_novuea.commit()

###################  FINO RILATE AL ASOCIOJ ########################
###################  RILATE AL UZANTOJ ########################

def konverti_uzanto(session_ueadb):
    global venonta_id_uzantoAuxAsocio
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

    session_novuea.begin()
    uzantolist = session_ueadb.query(ueadb.t_tuta1).all()
    for uzanto in uzantolist:
        novUzantoAuxAsocio = novuea.UzantoAuxAsocio(
                id = venonta_id_uzantoAuxAsocio,
                ueakodo = uzanto.ueakodo
                )
        lando = None
        valida = True
        morta = False
        try: 
            lando = get_id_lando(uzanto.landokodo) 
        except NeValidaLando as e: 
            lando = None
            if str(e) == "nev":
                valida = False
            if str(e) == "mrt":
                morta = True
        urbo = None
        try:
            urbo = get_id_urbo(uzanto.urbo)
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
        session_novuea.add(novUzanto)
        venonta_id_uzantoAuxAsocio = venonta_id_uzantoAuxAsocio + 1
    session_novuea.commit()

def get_id_uzanto_aux_asocio(familinomo, personanomo):
    #ni unue rigardas ene de la asocioj
    res = session_novuea.execute(select([Asocio]).where(Asocio.nomo == familianomo))
    if(res.rowcount == 0):
        #ni rigardu ĉe uzantoj
        res = session_novuea.execute(select([Uzanto]).where(Uzanto.familianomo == familianomo).where(Uzanto.personanomo == personanomo))
        if(res.rowcount == 0):
            raise MalplenaError("uzanto ne trovita: "+personanomo+" "+familianomo)
        elif(res.rowcount > 1):
            raise NeUnikaError("Pluraj homoj havas saman nomon, ne povas identigi certecen: "+personanomo+" "+familianomo)
        else :
            return res.scalar()
    elif(res.rowcount > 1):
        raise NeUnikaError("get uzanto_aux_asocio : ne-unika rezulto (sufice problema): la sama asocio plurfoje trovita: "+familianomo)
    else :
        return res.scalar()




def konverti_peranton():
    perantolist = session_ueadb.query(ueadb.perant).all()
    for peranto in perantolist:
        (titolo, personanomo) = get_titolon_personan_nomon(peranto.personanomo)
        id_uzantoAuxAsocio = get_id_uzanto_aux_asocio(peranto.familianomo, personanomo)
        novPeranto = novuea.Peranto(
                idUeaKodo = id_uzantoAuxAsocio,
                idLando = get_id_lando(peranto.landokodo)
                )
        session_novuea.add(novPeranto)
    session_novuea.commit()



#konverti_landon(session_ueadb)
#konverti_urbon(session_ueadb)
#konverti_faktemon(session_retdb)
#konverti_grupojn(get_grupojn())
#konverti_asocion(session_ueadb)
konverti_uzanto(session_ueadb)
