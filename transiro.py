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
# sqlacodegen mysql://root:@127.0.0.1/novuea > novuea.py
#
###############
import novuea


Base = declarative_base()
#Connect to the old ueadb
engine_ueadb = create_engine('postgresql://postgres:kukurbeto@127.0.0.1:5432/ueadb')


#Connect to the new db
engine_novuea = create_engine('mysql://root:@127.0.0.1:3306/novuea' )
session_novuea = create_session(bind=engine_novuea)

#Create a session to use the tables    
session_ueadb = create_session(bind=engine_ueadb)

def db_encode(vorto):
    if vorto is None:
        return ""
    else :
        return vorto.encode('utf-8').decode('utf-8')

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

konverti_landon(session_ueadb)



