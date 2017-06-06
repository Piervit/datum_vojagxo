import os
import sys
import sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import create_session

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

Base = declarative_base()
#Connect to the old ueadb
engine_ueadb = create_engine('postgresql://postgres:kukurbeto@127.0.0.1:5432/ueadb')
#Create a session to use the tables    
session_ueadb = create_session(bind=engine_ueadb)

#Connect to the old retdb
engine_retdb = create_engine('postgresql://postgres:kukurbeto@127.0.0.1:5432/retdb')
#Create a session to use the tables    
session_retdb = create_session(bind=engine_retdb)



#Connect to the new db
engine_novuea = create_engine('mysql://root:@127.0.0.1:3306/novuea' )
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
    res = session_novuea.execute(select([Lando]).where(Lando.landkodo == landkodo))
    if(res.rowcount == 0):
        raise MalplenaError("get lando: ne-unika rezulto: "+landokodo)
    elif(res.rowcount > 1):
        raise NeUnikaError("get lando: ne-unika rezulto: "+landokodo)
    else :
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

################### URBO ########################

def add_urbo(session, unomo, unomoEo, uProvinco, ulandokodo):
    idlando = get_id_lando(ulandokodo)
    novurbo = novuea.Urbo(
               nomoLoka=unomo, 
               nomoEo=unomoEo, 
               provinco=uProvinco, 
               idLando=idlando
               )
   except TransirError:
       if urbo.nomo is not None:
           print("Ne povis ligi "+urbo.nomo+"al lando (kodo "+urbo.landokodo+" ne valida)")
       else:
           print("Urbo ne havas nomon: ne-konsiderita.")
   session.add(novurbo)


def get_id_urbo(urbonomo):
    res = session_novuea.execute(select([Urbo]).where(Urbo.nomo == urbonomo))
    if(res.rowcount == 0):
        raise MalplenaError("get urbo: ne-unika rezulto: "+urbonomo)
    elif(res.rowcount > 1):
        raise NeUnikaError("get urbo: ne-unika rezulto: "+urbonomo)
    else :
        return res.scalar()

def konverti_urbon(session_ueadb):
    session_novuea.begin()
    #el tabelo urboj
    urbolist = session_ueadb.query(ueadb.t_urboj).all()
    for urbo in urbolist:
        add_urbo(session_novuea, db_encode(urbo.nomo), "", 
                db_encode(urbo.provinco), urbo.landkodo)
    #el tabelo asocio
    session_novuea.commit()
    session_novuea.begin()
    asolist = session_ueadb.query(ueadb.t_asocioj).all()
    for asocio in asociolist:
        try :
            idurbo = get_id_urbo(asocio.urbo)
        except MalplenaError :
            add_urbo(db_encode(asocio.nomo), "", "", None)
        except NeUnikaError :
            print("Asocio: Ne povis ligi "+asocio.urbo+"al urbo ĉar la nomo estas plurfoje trovita en la datumbazo")
    session_novuea.commit()

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


def krei_grupon():
    novKat = novuea.Grupo (

            )


def konstkat_konvertilo(string):



def konverti_asocion(session_ueadb):
    session_novuea.begin()
    asociolist = session_ueadb.query(ueadb.t_asocioj).all()
    #fakasociolist = session_retdb.query(retdb.t_fakasocioj).add_column("kategorio").distinct()
    for asocio in asociolist:
        novUzantoAuxAsocio = novuea.UzantoAuxAsocio(
                ueakodo = asocio.ueakodo
                )
        idurbo = NULL
        try :
            idurbo = get_id_urbo(asocio.urbo)
        except NeUnikaError, MalplenaError :
            print("Asocio: Ne povis ligi "+asocio.urbo+"al urbo ĉar la nomo estas plurfoje trovita en la datumbazo")
            idurbo= NULL
        
        novAsocio = novuea.Faktemo(
                id = novUzantoAuxAsocio.id 
                nomo= asocio.familianomo
                siglo= ""
                adreso= asocio.adreso
                fondigxdato= None
                posxtkodo= asocio.posxtkodo
                urbo= idurbo 
                fako= None
                lando= None
                telhejmo= asocio.telhejmo
                retposxto= asocio.retposxto
                delegFako= asocio.deleg_fako
                tttpagxo= asocio.tttpagxo
                junulara= False
                faka= 
                landa=
                abc=



                )
        session_novuea.add(novfako)
    session_novuea.commit()




#konverti_landon(session_ueadb)
#konverti_urbon(session_ueadb)
konverti_faktemon(session_retdb)
