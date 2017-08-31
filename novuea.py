# coding: utf-8
from sqlalchemy import Column, Date, Index, Integer, String, Table, Text, text
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Administranto(Base):
    __tablename__ = 'administranto'

    id = Column(Integer, primary_key=True)
    idUzantoAuxAsocio = Column(Integer)
    uzantnomo = Column(String(255, 'utf8_bin'))
    pasvortoHash = Column(Text(collation='utf8_bin'))
    pasvortoSalt = Column(Text(collation='utf8_bin'))


class Adminrajto(Base):
    __tablename__ = 'adminrajto'

    id = Column(Integer, primary_key=True)
    nomo = Column(String(255, 'utf8_bin'))
    priskribo = Column(String(255, 'utf8_bin'))


class Aligxperiodo(Base):
    __tablename__ = 'aligxperiodo'

    id = Column(Integer, primary_key=True)
    komencdato = Column(Date)
    findato = Column(Date)


class Aneckotizo(Base):
    __tablename__ = 'aneckotizo'

    id = Column(Integer, primary_key=True)
    prezo = Column(Integer)
    priskribo = Column(String(255, 'utf8_bin'))
    gxis_naskigxjaro = Column(Date)
    landKategorio = Column(Integer)
    idGrupo = Column(Integer)


class Aneco(Base):
    __tablename__ = 'aneco'

    id = Column(Integer, primary_key=True)
    idAno = Column(Integer, nullable=False)
    idGrupo = Column(Integer, nullable=False)
    komencdato = Column(Date)
    findato = Column(Date)
    dumviva = Column(Integer)
    tasko = Column(String(255, 'utf8_bin'))
    respondeco = Column(String(255, 'utf8_bin'))
    idAsocio = Column(Integer)
    idUrbo = Column(Integer)
    idFako = Column(Integer)
    idAneckotizo = Column(Integer)
    observoj = Column(String(255, 'utf8_bin'))
    aprobita = Column(Integer)


class Asocio(Base):
    __tablename__ = 'asocio'

    id = Column(Integer, primary_key=True)
    nomo = Column(String(255, 'utf8_bin'))
    siglo = Column(String(255, 'utf8_bin'))
    adreso = Column(String(255, 'utf8_bin'))
    fondigxdato = Column(Date)
    posxtkodo = Column(String(255, 'utf8_bin'))
    idUrbo = Column(Integer)
    idFako = Column(Integer)
    lando = Column(String(255, 'utf8_bin'))
    telhejmo = Column(String(255, 'utf8_bin'))
    retposxto = Column(String(255, 'utf8_bin'))
    delegFako = Column(String(255, 'utf8_bin'))
    tttpagxo = Column(String(255, 'utf8_bin'))
    junulara = Column(Integer)
    faka = Column(Integer)
    landa = Column(Integer)
    abc = Column(String(255, 'utf8_bin'))


class AsocioSangxpropono(Base):
    __tablename__ = 'asocio_sangxpropono'

    id = Column(Integer, primary_key=True)
    idAsocio = Column(Integer)
    nomo = Column(String(255, 'utf8_bin'))
    siglo = Column(String(255, 'utf8_bin'))
    adreso = Column(String(255, 'utf8_bin'))
    fondigxdato = Column(Date)
    posxtkodo = Column(String(255, 'utf8_bin'))
    idUrbo = Column(Integer)
    telhejmo = Column(String(255, 'utf8_bin'))
    landokodo = Column(String(255, 'utf8_bin'))
    retposxto = Column(String(255, 'utf8_bin'))
    delegFako = Column(String(255, 'utf8_bin'))
    tttpagxo = Column(String(255, 'utf8_bin'))
    abc = Column(String(255, 'utf8_bin'))


class Dissendo(Base):
    __tablename__ = 'dissendo'

    id = Column(Integer, primary_key=True)
    dissendanto = Column(Integer)
    nomede = Column(String(255, 'utf8_bin'))
    dato = Column(Date)
    temo = Column(String(255, 'utf8_bin'))
    teksto = Column(String(255, 'utf8_bin'))


class DissendoDemandero(Base):
    __tablename__ = 'dissendo_demandero'

    id = Column(Integer, primary_key=True)
    idDissendo = Column(Integer)
    demNum = Column(Integer)
    demTeksto = Column(String(255, 'utf8_bin'))


class Faktemo(Base):
    __tablename__ = 'faktemo'

    id = Column(Integer, primary_key=True)
    nomo = Column(String(255, 'utf8_bin'))
    priskribo = Column(String(1600, 'utf8_bin'))


class GrupaKategorio(Base):
    __tablename__ = 'grupa_kategorio'

    id = Column(Integer, primary_key=True)
    nomo = Column(String(255, 'utf8_bin'))


class Grupo(Base):
    __tablename__ = 'grupo'

    id = Column(Integer, primary_key=True)
    mallongigilo = Column(String(255, 'utf8_bin'))
    nomo = Column(String(255, 'utf8_bin'))
    priskribo = Column(String(255, 'utf8_bin'))
    idAsocio = Column(Integer)


class GxenSpezraportero(Base):
    __tablename__ = 'gxen_spezraportero'

    id = Column(Integer, primary_key=True)
    idGxenSpezraporto = Column(Integer)
    enspezo = Column(Integer)
    priskribo = Column(String(255, 'utf8_bin'))
    sumo = Column(Integer)


class GxenSpezraporto(Base):
    __tablename__ = 'gxen_spezraporto'

    id = Column(Integer, primary_key=True)
    dato = Column(Date)
    idPeranto = Column(Integer)
    valuto = Column(String(255, 'utf8_bin'))
    noto = Column(String(255, 'utf8_bin'))
    validita = Column(Integer)
    printita = Column(Integer)


class GxenSpezraportoKotizo(Base):
    __tablename__ = 'gxen_spezraporto_kotizo'

    id = Column(Integer, primary_key=True)
    idGxenSpezraporto = Column(Integer)
    idUzanto = Column(Integer)
    nomoUzanto = Column(String(255, 'utf8_bin'))
    idAnoGrupo = Column(Integer)


class Gxirpropono(Base):
    __tablename__ = 'gxirpropono'

    id = Column(Integer, primary_key=True)
    idGxiranto = Column(Integer)
    idRicevanto = Column(Integer)
    konto = Column(String(255, 'utf8_bin'))
    kialo = Column(String(1600, 'utf8_bin'))


class KongresaAligxinto(Base):
    __tablename__ = 'kongresa_aligxinto'

    id = Column(Integer, primary_key=True)
    kongresaNumero = Column(Integer)
    idUzanto = Column(Integer)
    idAligxkotizo = Column(Integer)
    pagita = Column(Integer)
    idKongreso = Column(Integer)


class KongresaAligxkotizo(Base):
    __tablename__ = 'kongresa_aligxkotizo'

    id = Column(Integer, primary_key=True)
    idKongreso = Column(Integer)
    prezo = Column(Integer)
    gxis_naskigxjaro = Column(Date)
    landKategorio = Column(Integer)
    grupo = Column(Integer)
    aligxperiodo = Column(Integer)
    priskribo = Column(String(1600, 'utf8_bin'))


class KongresaDormcxambro(Base):
    __tablename__ = 'kongresa_dormcxambro'

    id = Column(Integer, primary_key=True)
    nomo = Column(String(255, 'utf8_bin'))
    logxejo = Column(Integer)
    id_dormcxambrsxablono = Column(Integer)


class KongresaDormcxambrsxablono(Base):
    __tablename__ = 'kongresa_dormcxambrsxablono'

    id = Column(Integer, primary_key=True)
    litKvanto = Column(Integer)
    personKvanto = Column(Integer)
    prezo = Column(Integer)
    nomo = Column(String(255, 'utf8_bin'))


class KongresaEkskurso(Base):
    __tablename__ = 'kongresa_ekskurso'

    id = Column(Integer, primary_key=True)
    idKongreso = Column(Integer)
    titolo = Column(String(255, 'utf8_bin'))
    priskribo = Column(String(255, 'utf8_bin'))
    dato = Column(Date)
    prezo = Column(Integer)
    kvanto = Column(Integer)


class KongresaKategorio(Base):
    __tablename__ = 'kongresa_kategorio'

    id = Column(Integer, primary_key=True)
    nomo = Column(String(255, 'utf8_bin'))


class KongresaLogxejo(Base):
    __tablename__ = 'kongresa_logxejo'

    id = Column(Integer, primary_key=True)
    kongreso = Column(Integer)
    ordig = Column(Integer)
    rango = Column(Integer)
    adreso = Column(String(255, 'utf8_bin'))
    foreco = Column(String(255, 'utf8_bin'))
    priskribo = Column(String(255, 'utf8_bin'))
    retejo = Column(String(255, 'utf8_bin'))
    retadreso = Column(String(255, 'utf8_bin'))
    telefono = Column(String(255, 'utf8_bin'))
    fakso = Column(String(255, 'utf8_bin'))
    notoj = Column(String(255, 'utf8_bin'))


class KongresaProgramejo(Base):
    __tablename__ = 'kongresa_programejo'

    id = Column(Integer, primary_key=True)
    idKongreso = Column(Integer)
    nomo = Column(String(255, 'utf8_bin'))
    priskribo = Column(String(255, 'utf8_bin'))


class KongresaProgramo(Base):
    __tablename__ = 'kongresa_programo'

    id = Column(Integer, primary_key=True)
    idKongreso = Column(Integer)
    komenctempo = Column(Date)
    fintempo = Column(Date)
    evento = Column(String(255, 'utf8_bin'))
    priskribo = Column(String(1600, 'utf8_bin'))
    idKategorio = Column(Integer)
    idProgramejo = Column(Integer)


class KongresaProgramoKategorio(Base):
    __tablename__ = 'kongresa_programo_kategorio'

    id = Column(Integer, primary_key=True)
    titolo = Column(String(255, 'utf8_bin'))


class KongresaServo(Base):
    __tablename__ = 'kongresa_servo'

    id = Column(Integer, primary_key=True)
    nomo = Column(String(255, 'utf8_bin'))
    priskribo = Column(String(255, 'utf8_bin'))
    prezo = Column(Integer)


class KongresaSpezraportero(Base):
    __tablename__ = 'kongresa_spezraportero'

    id = Column(Integer, primary_key=True)
    idKongresaSpezraporto = Column(Integer)
    idUzanto = Column(Integer)
    nomoUzanto = Column(String(255, 'utf8_bin'))
    kongresaKotizo = Column(Integer)
    kongresajMendoj = Column(Integer)


class KongresaSpezraporto(Base):
    __tablename__ = 'kongresa_spezraporto'

    id = Column(Integer, primary_key=True)
    dato = Column(Date)
    idPeranto = Column(Integer)
    valuto = Column(String(255, 'utf8_bin'))
    noto = Column(String(255, 'utf8_bin'))
    validita = Column(Integer)
    printia = Column(Integer)


class Kongreso(Base):
    __tablename__ = 'kongreso'

    id = Column(Integer, primary_key=True)
    titolo = Column(String(255, 'utf8_bin'))
    bildo = Column(String(255, 'utf8_bin'))
    idUrbo = Column(Integer)
    jaro = Column(Date)
    numero = Column(Integer)
    komencdato = Column(Date)
    temo = Column(String(255, 'utf8_bin'))
    priskribo = Column(String(255, 'utf8_bin'))
    findato = Column(Date)


class KsPagKampo(Base):
    __tablename__ = 'ks_pag_kampo'

    id = Column(Integer, primary_key=True)
    priskribo = Column(String(255, 'utf8_bin'))
    defauxltaValuto = Column(Integer, server_default=text("'0'"))


class LandKategorio(Base):
    __tablename__ = 'landKategorio'

    id = Column(Integer, primary_key=True)
    titolo = Column(String(255, 'utf8_bin'))
    priskribo = Column(String(1500, 'utf8_bin'))


class Lando(Base):
    __tablename__ = 'lando'

    id = Column(Integer, primary_key=True)
    nomoLoka = Column(String(255, 'utf8_bin'))
    radikoEo = Column(String(255, 'utf8_bin'))
    finajxoEo = Column(String(255, 'utf8_bin'))
    landkodo = Column(String(255, 'utf8_bin'))


class Opcio(Base):
    __tablename__ = 'opcio'

    id = Column(Integer, primary_key=True)
    priskribo = Column(String(255, 'utf8_bin'))
    idVocxdonado = Column(Integer)


class Peranto(Base):
    __tablename__ = 'peranto'

    id = Column(Integer, primary_key=True)
    idUeakodo = Column(Integer)
    idLando = Column(Integer)


class RajtasVocxdoni(Base):
    __tablename__ = 'rajtas_vocxdoni'

    idVocxdonado = Column(Integer, primary_key=True, nullable=False)
    idGrupo = Column(Integer, primary_key=True, nullable=False)


class RefAdministrantoAdminrajto(Base):
    __tablename__ = 'ref_administranto_adminrajto'

    idAdministranto = Column(Integer, primary_key=True, nullable=False)
    idAdminrajto = Column(Integer, primary_key=True, nullable=False)


t_ref_aligxinto_logxejo = Table(
    'ref_aligxinto_logxejo', metadata,
    Column('idAligxinto', Integer),
    Column('idDormcxambro', Integer),
    Column('alvendato', Date),
    Column('forirdato', Date),
    Column('kvanto', Integer),
    Column('kunkogxantoj', String(255, 'utf8_bin')),
    Index('idAligxinto', 'idAligxinto', 'idDormcxambro', unique=True)
)


class RefDissendoGrupo(Base):
    __tablename__ = 'ref_dissendo_grupo'

    idDissendo = Column(Integer, primary_key=True, nullable=False)
    idGrupo = Column(Integer, primary_key=True, nullable=False)


class RefDissendoRespondoj(Base):
    __tablename__ = 'ref_dissendo_respondoj'

    idUzantoAuxAsocio = Column(Integer, primary_key=True, nullable=False)
    retadreso = Column(String(255, 'utf8_bin'), primary_key=True, nullable=False)
    idDissendoDemandero = Column(Integer, primary_key=True, nullable=False)


class RefGrupoGrupaKategorio(Base):
    __tablename__ = 'ref_grupo_grupa_kategorio'

    idGrupo = Column(Integer, primary_key=True, nullable=False)
    idGrupaKategorio = Column(Integer, primary_key=True, nullable=False)


class RefKongresaEkskursoMendo(Base):
    __tablename__ = 'ref_kongresa_ekskurso_mendo'

    idKAligxinto = Column(Integer, primary_key=True, nullable=False)
    idKEkskurso = Column(Integer, primary_key=True, nullable=False)


class RefKongresaKategorioKongreso(Base):
    __tablename__ = 'ref_kongresa_kategorio_kongreso'

    idKongresaKategorio = Column(Integer, primary_key=True, nullable=False)
    idKongreso = Column(Integer, primary_key=True, nullable=False)


t_ref_kongresa_servo_aligxinto = Table(
    'ref_kongresa_servo_aligxinto', metadata,
    Column('idAligxinto', Integer),
    Column('idServo', Integer),
    Column('pagita', Integer)
)


class RefKongresaSpezraporteroKsPagKampo(Base):
    __tablename__ = 'ref_kongresa_spezraportero_ks_pag_kampo'

    idKongresaSpezraportero = Column(Integer, primary_key=True, nullable=False)
    idKsPagKampo = Column(Integer, primary_key=True, nullable=False)
    sumo = Column(Integer)


class RefKongresoKromaKongreso(Base):
    __tablename__ = 'ref_kongreso_kroma_kongreso'

    idCxefaKongreso = Column(Integer, primary_key=True, nullable=False)
    idKromaKongreso = Column(Integer, primary_key=True, nullable=False)


class RefLandoLandKategorio(Base):
    __tablename__ = 'ref_lando_landKategorio'

    idLando = Column(Integer, primary_key=True, nullable=False)
    idLandkategorio = Column(Integer, primary_key=True, nullable=False)


class RefTekoGrupo(Base):
    __tablename__ = 'ref_teko_grupo'

    id = Column(Integer, primary_key=True)
    idTeko = Column(Integer)
    idGrupo = Column(Integer)
    jaro = Column(Integer)


class RefTekoKategorio(Base):
    __tablename__ = 'ref_teko_kategorio'

    idKategorio = Column(Integer, primary_key=True, nullable=False)
    idTeko = Column(Integer, primary_key=True, nullable=False)


class RetlistAbono(Base):
    __tablename__ = 'retlist_abono'

    id = Column(Integer, primary_key=True)
    ekde = Column(Date)
    abono = Column(Integer)
    idUzanto = Column(Integer)
    formato_html = Column(Integer)
    kodigxo_utf8 = Column(Integer)
    retadreso = Column(String(255, 'utf8_bin'))


class Retlisto(Base):
    __tablename__ = 'retlisto'

    id = Column(Integer, primary_key=True)
    nomo = Column(String(255, 'utf8_bin'))
    priskribo = Column(String(255, 'utf8_bin'))


class Sxangxhistorio(Base):
    __tablename__ = 'sxangxhistorio'

    id = Column(Integer, primary_key=True)
    tabelo = Column(String(255, 'utf8_bin'))
    kampo = Column(String(255, 'utf8_bin'))
    antauxa_valoro = Column(String(255, 'utf8_bin'))
    farita_de = Column(Integer)
    dato = Column(Date)


class TekaKategorio(Base):
    __tablename__ = 'teka_kategorio'

    id = Column(Integer, primary_key=True)
    titolo = Column(String(255, 'utf8_bin'))


class Teko(Base):
    __tablename__ = 'teko'

    id = Column(Integer, primary_key=True)
    titolo = Column(String(255, 'utf8_bin'))
    elnomo = Column(String(255, 'utf8_bin'))
    kodnomo = Column(String(255, 'utf8_bin'))
    jaro = Column(Integer)
    absnum = Column(String(255, 'utf8_bin'))
    vido = Column(Integer)


class Urbo(Base):
    __tablename__ = 'urbo'

    id = Column(Integer, primary_key=True)
    nomoLoka = Column(String(255, 'utf8_bin'))
    nomoEo = Column(String(255, 'utf8_bin'))
    provinco = Column(String(255, 'utf8_bin'))
    idLando = Column(Integer)


class Uzanto(Base):
    __tablename__ = 'uzanto'

    id = Column(Integer, primary_key=True)
    personanomo = Column(String(255, 'utf8_bin'))
    familianomo = Column(String(255, 'utf8_bin'))
    titolo = Column(String(255, 'utf8_bin'))
    bildo = Column(String(255, 'utf8_bin'))
    personanomoIdentigilo = Column(String(255, 'utf8_bin'))
    familianomoIdentigilo = Column(String(255, 'utf8_bin'))
    adreso = Column(String(255, 'utf8_bin'))
    posxtkodo = Column(String(255, 'utf8_bin'))
    idLogxurbo = Column(Integer)
    idlando = Column(Integer)
    naskigxtago = Column(Date)
    morta = Column(Integer)
    mortdatekscio = Column(Date)
    mortdato = Column(Date)
    notoj = Column(String(255, 'utf8_bin'))
    profesio = Column(String(255, 'utf8_bin'))
    retposxto = Column(String(255, 'utf8_bin'))
    telhejmo = Column(String(255, 'utf8_bin'))
    teloficejo = Column(String(255, 'utf8_bin'))
    telportebla = Column(String(255, 'utf8_bin'))
    kerekzameno = Column(Integer)
    kernivelo = Column(String(2, 'utf8_bin'))
    kerdato = Column(Date)
    tttpagxo = Column(String(255, 'utf8_bin'))
    validaKonto = Column(Integer)
    abc = Column(String(255, 'utf8_bin'))


class UzantoAuxAsocio(Base):
    __tablename__ = 'uzantoAuxAsocio'

    id = Column(Integer, primary_key=True)
    ueakodo = Column(String(255, 'utf8_bin'), unique=True)
    uzantnomo = Column(String(255, 'utf8_bin'), unique=True)
    pasvortoHash = Column(Text(collation='utf8_bin'))
    pasvortoSalt = Column(Text(collation='utf8_bin'))


class UzantoSangxpropono(Base):
    __tablename__ = 'uzanto_sangxpropono'

    id = Column(Integer, primary_key=True)
    idUzanto = Column(Integer)
    personanomo = Column(String(255, 'utf8_bin'))
    familianomo = Column(String(255, 'utf8_bin'))
    personanomoIdentigilo = Column(String(255, 'utf8_bin'))
    familianomoIdentigilo = Column(String(255, 'utf8_bin'))
    adreso = Column(String(255, 'utf8_bin'))
    posxtkodo = Column(String(255, 'utf8_bin'))
    idLogxurbo = Column(Integer)
    idNacialando = Column(Integer)
    naskigxtago = Column(Date)
    mortdatekscio = Column(Date)
    mortdato = Column(Date)
    notoj = Column(String(255, 'utf8_bin'))
    profesio = Column(String(255, 'utf8_bin'))
    retposxto = Column(String(255, 'utf8_bin'))
    telhejmo = Column(String(255, 'utf8_bin'))
    teloficejo = Column(String(255, 'utf8_bin'))
    telportebla = Column(String(255, 'utf8_bin'))
    tttpagxo = Column(String(255, 'utf8_bin'))
    validakonto = Column(Integer)
    abc = Column(String(255, 'utf8_bin'))


class Vocxdonado(Base):
    __tablename__ = 'vocxdonado'

    id = Column(Integer, primary_key=True)
    titolo = Column(String(255, 'utf8_bin'))
    priskribo = Column(String(1600, 'utf8_bin'))
    pluraj_opcioj = Column(Integer)
    anonima = Column(Integer)
    aperdato = Column(Date)
    limdato = Column(Date)


class Vocxo(Base):
    __tablename__ = 'vocxo'

    id = Column(Integer, primary_key=True)
    idUzanto = Column(Integer)
    idOpcio = Column(Integer)
