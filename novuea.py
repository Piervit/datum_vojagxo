# coding: utf-8
from sqlalchemy import Column, Date, Index, Integer, String, Table, Text, text
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Administranto(Base):
    __tablename__ = 'administranto'

    id = Column(Integer, primary_key=True)
    idUzantoAuxAsocio = Column(Integer)
    uzantnomo = Column(String(255, 'utf8_unicode_ci'))
    pasvorto = Column(String(255, 'utf8_unicode_ci'))


class Adminrajto(Base):
    __tablename__ = 'adminrajto'

    id = Column(Integer, primary_key=True)
    nomo = Column(String(255, 'utf8_unicode_ci'))
    priskribo = Column(String(255, 'utf8_unicode_ci'))


class Aligxkotizo(Base):
    __tablename__ = 'aligxkotizo'

    id = Column(Integer, primary_key=True)
    idKongreso = Column(Integer)
    prezo = Column(Integer)
    gxis_naskigxjaro = Column(Date)
    landKategorio = Column(Integer)
    priskribo = Column(String(255, 'utf8_unicode_ci'))


class Aneckotizo(Base):
    __tablename__ = 'aneckotizo'

    id = Column(Integer, primary_key=True)
    prezo = Column(Integer)
    priskribo = Column(String(255, 'utf8_unicode_ci'))
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
    tasko = Column(String(255, 'utf8_unicode_ci'))
    respondeco = Column(String(255, 'utf8_unicode_ci'))
    idAsocio = Column(Integer)
    idUrbo = Column(Integer)
    idFako = Column(Integer)
    observoj = Column(String(255, 'utf8_unicode_ci'))


class Asocio(Base):
    __tablename__ = 'asocio'

    id = Column(Integer, primary_key=True)
    nomo = Column(String(255, 'utf8_unicode_ci'))
    siglo = Column(String(255, 'utf8_unicode_ci'))
    adreso = Column(String(255, 'utf8_unicode_ci'))
    fondigxdato = Column(Date)
    posxtkodo = Column(String(255, 'utf8_unicode_ci'))
    urbo = Column(Integer)
    fako = Column(Integer)
    lando = Column(String(255, 'utf8_unicode_ci'))
    telhejmo = Column(String(255, 'utf8_unicode_ci'))
    retposxto = Column(String(255, 'utf8_unicode_ci'))
    delegFako = Column(String(255, 'utf8_unicode_ci'))
    tttpagxo = Column(String(255, 'utf8_unicode_ci'))
    junulara = Column(Integer)
    faka = Column(Integer)
    landa = Column(Integer)
    abc = Column(String(255, 'utf8_unicode_ci'))


class AsocioSangxpropono(Base):
    __tablename__ = 'asocio_sangxpropono'

    id = Column(Integer, primary_key=True)
    idAsocio = Column(Integer)
    nomo = Column(String(255, 'utf8_unicode_ci'))
    siglo = Column(String(255, 'utf8_unicode_ci'))
    adreso = Column(String(255, 'utf8_unicode_ci'))
    fondigxdato = Column(Date)
    posxtkodo = Column(String(255, 'utf8_unicode_ci'))
    urbo = Column(Integer)
    telhejmo = Column(String(255, 'utf8_unicode_ci'))
    landokodo = Column(String(255, 'utf8_unicode_ci'))
    retposxto = Column(String(255, 'utf8_unicode_ci'))
    delegFako = Column(String(255, 'utf8_unicode_ci'))
    tttpagxo = Column(String(255, 'utf8_unicode_ci'))
    abc = Column(String(255, 'utf8_unicode_ci'))


class Dissendo(Base):
    __tablename__ = 'dissendo'

    id = Column(Integer, primary_key=True)
    dissendanto = Column(Integer)
    nomede = Column(String(255, 'utf8_unicode_ci'))
    dato = Column(Date)
    temo = Column(String(255, 'utf8_unicode_ci'))
    teksto = Column(String(255, 'utf8_unicode_ci'))


class DissendoDemandero(Base):
    __tablename__ = 'dissendo_demandero'

    id = Column(Integer, primary_key=True)
    idDissendo = Column(Integer)
    demNum = Column(Integer)
    demTeksto = Column(String(255, 'utf8_unicode_ci'))


class Faktemo(Base):
    __tablename__ = 'faktemo'

    id = Column(Integer, primary_key=True)
    nomo = Column(String(255, 'utf8_unicode_ci'))
    priskribo = Column(String(1600, 'utf8_unicode_ci'))


class GrupaKategorio(Base):
    __tablename__ = 'grupa_kategorio'

    id = Column(Integer, primary_key=True)
    nomo = Column(String(255, 'utf8_unicode_ci'))


class Grupo(Base):
    __tablename__ = 'grupo'

    id = Column(Integer, primary_key=True)
    nomo = Column(String(255, 'utf8_unicode_ci'))
    priskribo = Column(String(255, 'utf8_unicode_ci'))
    idAsocio = Column(Integer)


class GxenSpezraportero(Base):
    __tablename__ = 'gxen_spezraportero'

    id = Column(Integer, primary_key=True)
    idGxenSpezraporto = Column(Integer)
    enspezo = Column(Integer)
    priskribo = Column(String(255, 'utf8_unicode_ci'))
    sumo = Column(Integer)


class GxenSpezraporto(Base):
    __tablename__ = 'gxen_spezraporto'

    id = Column(Integer, primary_key=True)
    dato = Column(Date)
    idPeranto = Column(Integer)
    valuto = Column(String(255, 'utf8_unicode_ci'))
    noto = Column(String(255, 'utf8_unicode_ci'))
    validita = Column(Integer)
    printita = Column(Integer)


class GxenSpezraportoKotizo(Base):
    __tablename__ = 'gxen_spezraporto_kotizo'

    id = Column(Integer, primary_key=True)
    idGxenSpezraporto = Column(Integer)
    idUzanto = Column(Integer)
    nomoUzanto = Column(String(255, 'utf8_unicode_ci'))
    idAnoGrupo = Column(Integer)


class Gxirpropono(Base):
    __tablename__ = 'gxirpropono'

    id = Column(Integer, primary_key=True)
    idGxiranto = Column(Integer)
    idRicevanto = Column(Integer)
    konto = Column(String(255, 'utf8_unicode_ci'))
    kialo = Column(String(1600, 'utf8_unicode_ci'))


class KongresaAligxinto(Base):
    __tablename__ = 'kongresa_aligxinto'

    id = Column(Integer, primary_key=True)
    kongresaNumero = Column(Integer)
    idUzanto = Column(Integer)
    idAligxkotizo = Column(Integer)
    idKongreso = Column(Integer)


class KongresaDormcxambro(Base):
    __tablename__ = 'kongresa_dormcxambro'

    id = Column(Integer, primary_key=True)
    nomo = Column(String(255, 'utf8_unicode_ci'))
    logxejo = Column(Integer)
    id_dormcxambrsxablono = Column(Integer)


class KongresaDormcxambrsxablono(Base):
    __tablename__ = 'kongresa_dormcxambrsxablono'

    id = Column(Integer, primary_key=True)
    litKvanto = Column(Integer)
    personKvanto = Column(Integer)
    prezo = Column(Integer)
    nomo = Column(String(255, 'utf8_unicode_ci'))


class KongresaEkskurso(Base):
    __tablename__ = 'kongresa_ekskurso'

    id = Column(Integer, primary_key=True)
    idKongreso = Column(Integer)
    titolo = Column(String(255, 'utf8_unicode_ci'))
    priskribo = Column(String(255, 'utf8_unicode_ci'))
    dato = Column(Date)
    prezo = Column(Integer)
    kvanto = Column(Integer)


class KongresaLogxejo(Base):
    __tablename__ = 'kongresa_logxejo'

    id = Column(Integer, primary_key=True)
    kongreso = Column(Integer)
    ordig = Column(Integer)
    rango = Column(Integer)
    adreso = Column(String(255, 'utf8_unicode_ci'))
    foreco = Column(String(255, 'utf8_unicode_ci'))
    priskribo = Column(String(255, 'utf8_unicode_ci'))
    retejo = Column(String(255, 'utf8_unicode_ci'))
    retadreso = Column(String(255, 'utf8_unicode_ci'))
    telefono = Column(String(255, 'utf8_unicode_ci'))
    fakso = Column(String(255, 'utf8_unicode_ci'))
    notoj = Column(String(255, 'utf8_unicode_ci'))


class KongresaProgramejo(Base):
    __tablename__ = 'kongresa_programejo'

    id = Column(Integer, primary_key=True)
    idKongreso = Column(Integer)
    nomo = Column(String(255, 'utf8_unicode_ci'))
    priskribo = Column(String(255, 'utf8_unicode_ci'))


class KongresaProgramo(Base):
    __tablename__ = 'kongresa_programo'

    id = Column(Integer, primary_key=True)
    idKongreso = Column(Integer)
    komenctempo = Column(Date)
    fintempo = Column(Date)
    evento = Column(String(255, 'utf8_unicode_ci'))
    priskribo = Column(String(1600, 'utf8_unicode_ci'))
    programejo = Column(Integer)


class KongresaSpezraportero(Base):
    __tablename__ = 'kongresa_spezraportero'

    id = Column(Integer, primary_key=True)
    idKongresaSpezraporto = Column(Integer)
    idUzanto = Column(Integer)
    nomoUzanto = Column(String(255, 'utf8_unicode_ci'))
    kongresaKotizo = Column(Integer)
    kongresajMendoj = Column(Integer)


class KongresaSpezraporto(Base):
    __tablename__ = 'kongresa_spezraporto'

    id = Column(Integer, primary_key=True)
    dato = Column(Date)
    idPeranto = Column(Integer)
    valuto = Column(String(255, 'utf8_unicode_ci'))
    noto = Column(String(255, 'utf8_unicode_ci'))
    validita = Column(Integer)
    printia = Column(Integer)


class Kongreso(Base):
    __tablename__ = 'kongreso'

    id = Column(Integer, primary_key=True)
    titolo = Column(String(255, 'utf8_unicode_ci'))
    idUrbo = Column(Integer)
    jaro = Column(Date)
    numero = Column(Integer)
    komencdato = Column(Date)
    temo = Column(String(255, 'utf8_unicode_ci'))
    priskribo = Column(String(255, 'utf8_unicode_ci'))
    findato = Column(Date)


class KsPagKampo(Base):
    __tablename__ = 'ks_pag_kampo'

    id = Column(Integer, primary_key=True)
    priskribo = Column(String(255, 'utf8_unicode_ci'))
    defauxltaValuto = Column(Integer, server_default=text("'0'"))


class LandKategorio(Base):
    __tablename__ = 'landKategorio'

    id = Column(Integer, primary_key=True)
    titolo = Column(String(255, 'utf8_unicode_ci'))
    priskribo = Column(String(1500, 'utf8_unicode_ci'))


class Lando(Base):
    __tablename__ = 'lando'

    id = Column(Integer, primary_key=True)
    nomoLoka = Column(String(255, 'utf8_unicode_ci'))
    radikoEo = Column(String(255, 'utf8_unicode_ci'))
    finajxoEo = Column(String(255, 'utf8_unicode_ci'))
    landkodo = Column(String(255, 'utf8_unicode_ci'))


class Opcio(Base):
    __tablename__ = 'opcio'

    id = Column(Integer, primary_key=True)
    priskribo = Column(String(255, 'utf8_unicode_ci'))
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
    Column('kunkogxantoj', String(255, 'utf8_unicode_ci')),
    Index('idAligxinto', 'idAligxinto', 'idDormcxambro', unique=True)
)


class RefDissendoGrupo(Base):
    __tablename__ = 'ref_dissendo_grupo'

    idDissendo = Column(Integer, primary_key=True, nullable=False)
    idGrupo = Column(Integer, primary_key=True, nullable=False)


class RefDissendoRespondoj(Base):
    __tablename__ = 'ref_dissendo_respondoj'

    idUzantoAuxAsocio = Column(Integer, primary_key=True, nullable=False)
    idDissendoDemandero = Column(Integer, primary_key=True, nullable=False)


class RefGrupoGrupaKategorio(Base):
    __tablename__ = 'ref_grupo_grupa_kategorio'

    idGrupo = Column(Integer, primary_key=True, nullable=False)
    idGrupaKategorio = Column(Integer, primary_key=True, nullable=False)


class RefKongresaEkskursoMendo(Base):
    __tablename__ = 'ref_kongresa_ekskurso_mendo'

    idKAligxinto = Column(Integer, primary_key=True, nullable=False)
    idKEkskurso = Column(Integer, primary_key=True, nullable=False)


class RefKongresaSpezraporteroKsPagKampo(Base):
    __tablename__ = 'ref_kongresa_spezraportero_ks_pag_kampo'

    idKongresaSpezraportero = Column(Integer, primary_key=True, nullable=False)
    idKsPagKampo = Column(Integer, primary_key=True, nullable=False)
    sumo = Column(Integer)


class RefKongresoKromaKongreso(Base):
    __tablename__ = 'ref_kongreso_kroma_kongreso'

    id_cxefa_kongreso = Column(Integer, primary_key=True, nullable=False)
    id_kroma_kongreso = Column(Integer, primary_key=True, nullable=False)


class RefLandoLandKategorio(Base):
    __tablename__ = 'ref_lando_landKategorio'

    idLando = Column(Integer, primary_key=True, nullable=False)
    idLandkategorio = Column(Integer, primary_key=True, nullable=False)


class RefTekoGrupo(Base):
    __tablename__ = 'ref_teko_grupo'

    id = Column(Integer, primary_key=True)
    idTeko = Column(Integer)
    idgrupo = Column(Integer)
    jaro = Column(Integer)


class RetlistAbono(Base):
    __tablename__ = 'retlist_abono'

    id = Column(Integer, primary_key=True)
    ekde = Column(Date)
    abono = Column(Integer)
    id_uzanto = Column(Integer)
    formato_html = Column(Integer)
    kodigxo_utf8 = Column(Integer)
    retadreso = Column(String(255, 'utf8_unicode_ci'))


class Retlisto(Base):
    __tablename__ = 'retlisto'

    id = Column(Integer, primary_key=True)
    nomo = Column(String(255, 'utf8_unicode_ci'))
    priskribo = Column(String(255, 'utf8_unicode_ci'))


class Sxangxhistorio(Base):
    __tablename__ = 'sxangxhistorio'

    id = Column(Integer, primary_key=True)
    tabelo = Column(String(255, 'utf8_unicode_ci'))
    kampo = Column(String(255, 'utf8_unicode_ci'))
    antauxa_valoro = Column(String(255, 'utf8_unicode_ci'))
    farita_de = Column(Integer)
    dato = Column(Date)


class Teko(Base):
    __tablename__ = 'teko'

    id = Column(Integer, primary_key=True)
    titolo = Column(String(255, 'utf8_unicode_ci'))
    elnomo = Column(String(255, 'utf8_unicode_ci'))
    kodnomo = Column(String(255, 'utf8_unicode_ci'))
    jaro = Column(Integer)
    absnum = Column(String(255, 'utf8_unicode_ci'))
    vido = Column(Integer)


class Urbo(Base):
    __tablename__ = 'urbo'

    id = Column(Integer, primary_key=True)
    nomoLoka = Column(String(255, 'utf8_unicode_ci'))
    nomoEo = Column(String(255, 'utf8_unicode_ci'))
    provinco= Column(String(255, 'utf8_unicode_ci'))
    idLando = Column(Integer)


class Uzanto(Base):
    __tablename__ = 'uzanto'

    id = Column(Integer, primary_key=True)
    personanomo = Column(String(255, 'utf8_unicode_ci'))
    familianomo = Column(String(255, 'utf8_unicode_ci'))
    titolo = Column(String(255, 'utf8_unicode_ci'))
    bildo = Column(String(255, 'utf8_unicode_ci'))
    personanomoIdentigilo = Column(String(255, 'utf8_unicode_ci'))
    familianomoIdentigilo = Column(String(255, 'utf8_unicode_ci'))
    adreso = Column(String(255, 'utf8_unicode_ci'))
    posxtkodo = Column(String(255, 'utf8_unicode_ci'))
    logxurbo = Column(Integer)
    nacialando = Column(Integer)
    naskigxtago = Column(Date)
    mortdatekscio = Column(Date)
    mortdato = Column(Date)
    notoj = Column(String(255, 'utf8_unicode_ci'))
    profesio = Column(String(255, 'utf8_unicode_ci'))
    retposxto = Column(String(255, 'utf8_unicode_ci'))
    telhejmo = Column(String(255, 'utf8_unicode_ci'))
    teloficejo = Column(String(255, 'utf8_unicode_ci'))
    telportebla = Column(String(255, 'utf8_unicode_ci'))
    kerekzameno = Column(Integer)
    kernivelo = Column(String(2, 'utf8_unicode_ci'))
    kerdato = Column(Date)
    tttpagxo = Column(String(255, 'utf8_unicode_ci'))
    validaKonto = Column(Integer)
    abc = Column(String(255, 'utf8_unicode_ci'))


class UzantoAuxAsocio(Base):
    __tablename__ = 'uzantoAuxAsocio'

    id = Column(Integer, primary_key=True)
    ueakodo = Column(String(255, 'utf8_unicode_ci'))
    uzantnomo = Column(String(255, 'utf8_unicode_ci'))
    pasvorto = Column(Text(collation='utf8_unicode_ci'))


class UzantoSangxpropono(Base):
    __tablename__ = 'uzanto_sangxpropono'

    id = Column(Integer, primary_key=True)
    idUzanto = Column(Integer)
    personanomo = Column(String(255, 'utf8_unicode_ci'))
    familianomo = Column(String(255, 'utf8_unicode_ci'))
    personanomoIdentigilo = Column(String(255, 'utf8_unicode_ci'))
    familianomoIdentigilo = Column(String(255, 'utf8_unicode_ci'))
    adreso = Column(String(255, 'utf8_unicode_ci'))
    posxtkodo = Column(String(255, 'utf8_unicode_ci'))
    logxurbo = Column(Integer)
    nacialando = Column(Integer)
    naskigxtago = Column(Date)
    mortdatekscio = Column(Date)
    mortdato = Column(Date)
    notoj = Column(String(255, 'utf8_unicode_ci'))
    profesio = Column(String(255, 'utf8_unicode_ci'))
    retposxto = Column(String(255, 'utf8_unicode_ci'))
    telhejmo = Column(String(255, 'utf8_unicode_ci'))
    teloficejo = Column(String(255, 'utf8_unicode_ci'))
    telportebla = Column(String(255, 'utf8_unicode_ci'))
    tttpagxo = Column(String(255, 'utf8_unicode_ci'))
    validakonto = Column(Integer)
    abc = Column(String(255, 'utf8_unicode_ci'))


class Vocxdonado(Base):
    __tablename__ = 'vocxdonado'

    id = Column(Integer, primary_key=True)
    titolo = Column(String(255, 'utf8_unicode_ci'))
    priskribo = Column(String(1600, 'utf8_unicode_ci'))
    pluraj_opcioj = Column(Integer)
    anonima = Column(Integer)
    aperdato = Column(Date)
    limdato = Column(Date)


class Vocxo(Base):
    __tablename__ = 'vocxo'

    id = Column(Integer, primary_key=True)
    idUzanto = Column(Integer)
    idOpcio = Column(Integer)
