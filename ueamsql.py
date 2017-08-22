# coding: utf-8
from sqlalchemy import BINARY, Column, Date, DateTime, Enum, Float, Integer, Numeric, SmallInteger, String, Table, Text, Time, text
from sqlalchemy.dialects.mysql.base import YEAR
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Abonoj(Base):
    __tablename__ = 'abonoj'

    numero = Column(Integer, primary_key=True)
    titolo = Column(Text, nullable=False)
    kodo = Column(String(6), nullable=False, server_default=text("''"))
    klarigo = Column(Text)
    ofteco = Column(Text)
    prezo = Column(Numeric(5, 2), nullable=False, server_default=text("'0.00'"))
    aerposxto = Column(Numeric(5, 2))
    rete = Column(Numeric(5, 2))
    difinebla = Column(Text)
    dprez = Column(Numeric(5, 2))


t_akpk = Table(
    'akpk', metadata,
    Column('kodo', String(3), nullable=False, server_default=text("''")),
    Column('titolo', Text, nullable=False),
    Column('dato1', Integer),
    Column('dato2', Integer),
    Column('unulita', Integer),
    Column('dulita', Integer),
    Column('e_unulita', Integer),
    Column('ex_unulita', Integer),
    Column('e_dulita', Integer),
    Column('ex_dulita', Integer),
    Column('reven', Text, nullable=False),
    Column('ex_reven', Text),
    Column('dist', String(30), nullable=False, server_default=text("''")),
    Column('priskribo', Text, nullable=False),
    Column('kvanto', Integer),
    Column('jaro', Integer),
    Column('aldonaj_ejoj', Text),
    Column('nkvantoj', Text)
)


t_akpk06 = Table(
    'akpk06', metadata,
    Column('kodo', String(3), nullable=False, server_default=text("''")),
    Column('titolo', Text, nullable=False),
    Column('dato1', Integer),
    Column('dato2', Integer),
    Column('unulita', Integer),
    Column('dulita', Integer),
    Column('e_unulita', Integer),
    Column('e_dulita', Integer),
    Column('reven', Text, nullable=False),
    Column('dist', String(30), nullable=False, server_default=text("''")),
    Column('priskribo', Text, nullable=False),
    Column('kvanto', Integer)
)


t_akpk07 = Table(
    'akpk07', metadata,
    Column('kodo', String(3), nullable=False, server_default=text("''")),
    Column('titolo', Text, nullable=False),
    Column('dato1', Integer),
    Column('dato2', Integer),
    Column('unulita', Integer),
    Column('dulita', Integer),
    Column('e_unulita', Integer),
    Column('e_dulita', Integer),
    Column('reven', Text, nullable=False),
    Column('dist', String(30), nullable=False, server_default=text("''")),
    Column('priskribo', Text, nullable=False),
    Column('kvanto', Integer)
)


t_akpk08 = Table(
    'akpk08', metadata,
    Column('kodo', String(3), nullable=False, server_default=text("''")),
    Column('titolo', Text, nullable=False),
    Column('dato1', Integer),
    Column('dato2', Integer),
    Column('unulita', Integer),
    Column('dulita', Integer),
    Column('e_unulita', Integer),
    Column('e_dulita', Integer),
    Column('reven', Text, nullable=False),
    Column('dist', String(30), nullable=False, server_default=text("''")),
    Column('priskribo', Text, nullable=False),
    Column('kvanto', Integer)
)


t_akpk09 = Table(
    'akpk09', metadata,
    Column('kodo', String(3), nullable=False, server_default=text("''")),
    Column('titolo', Text, nullable=False),
    Column('dato1', Integer),
    Column('dato2', Integer),
    Column('unulita', Integer),
    Column('dulita', Integer),
    Column('e_unulita', Integer),
    Column('e_dulita', Integer),
    Column('reven', Text, nullable=False),
    Column('dist', String(30), nullable=False, server_default=text("''")),
    Column('priskribo', Text, nullable=False),
    Column('kvanto', Integer)
)


t_akpk2009 = Table(
    'akpk2009', metadata,
    Column('kodo', String(3), nullable=False, server_default=text("''")),
    Column('titolo', Text, nullable=False),
    Column('dato1', Integer),
    Column('dato2', Integer),
    Column('unulita', Integer),
    Column('dulita', Integer),
    Column('e_unulita', Integer),
    Column('e_dulita', Integer),
    Column('reven', Text, nullable=False),
    Column('dist', String(30), nullable=False, server_default=text("''")),
    Column('priskribo', Text, nullable=False),
    Column('kvanto', Integer)
)


class Anoncoj(Base):
    __tablename__ = 'anoncoj'

    numero = Column(Integer, primary_key=True)
    ueakodo = Column(String(6))
    nomo = Column(String(50), nullable=False, server_default=text("''"))
    hotelo = Column(String(50), nullable=False, server_default=text("''"))
    chambro = Column(String(12), nullable=False, server_default=text("''"))
    speco = Column(String(12), nullable=False, server_default=text("''"))
    retadreso = Column(String(50), nullable=False, server_default=text("''"))
    sinprezento = Column(String(200), nullable=False, server_default=text("''"))
    valideco = Column(Integer)
    dato = Column(Date)


class Artikoloj(Base):
    __tablename__ = 'artikoloj'

    id = Column(Integer, primary_key=True)
    titolo = Column(String(255), nullable=False, server_default=text("''"))
    subtitolo = Column(String(255), nullable=False, server_default=text("''"))
    autoro = Column(String(255))
    dewey = Column(String(20))
    revuo = Column(String(255))
    jaro = Column(String(10))
    numero = Column(String(50))
    pagxoj = Column(String(100))
    aliajxoj = Column(String(50))
    organizo = Column(String(255))
    persono = Column(String(255))
    lando = Column(String(55))
    tradukintoj = Column(String(255))
    ligilo = Column(String(255))
    abc = Column(Text)


class Brok(Base):
    __tablename__ = 'brok'

    bvar = Column(Integer, primary_key=True)
    tit = Column(Text, nullable=False)
    ghenro = Column(Text)
    aut = Column(Text)
    traduk = Column(Text)
    eldonlok = Column(Text)
    eldonjar = Column(Text)
    eld_i = Column(Text)
    pagxoj = Column(Text)
    prezo = Column(Numeric(6, 2))
    kvant = Column(SmallInteger)
    bind = Column(String(20))
    aldone = Column(Text)
    posedanto = Column(Text)
    ret = Column(Text)
    loko = Column(Text)


class BrokPeriodajhoj(Base):
    __tablename__ = 'brok_periodajhoj'

    num = Column(Integer, primary_key=True)
    kodo = Column(String(7))
    titolo = Column(Text, nullable=False)
    subtitolo = Column(Text)
    tipo = Column(Text)
    notoj = Column(Text)
    stato = Column(Text)
    aktualigo = Column(Date)
    prezkategorio = Column(String(20))
    bildo = Column(Text)
    jaro = Column(Text)
    numero = Column(Text)
    absnumero = Column(Text)
    monato = Column(Text)
    kvanto = Column(SmallInteger)
    deponloko = Column(Text)
    enskribitade = Column(Text)


class Broshuroj(Base):
    __tablename__ = 'broshuroj'

    brn = Column(Integer, primary_key=True)
    titolo = Column(Text)
    lando = Column(Text)
    loko = Column(Text)
    eldonloko = Column(Text)
    jaro = Column(SmallInteger)
    prezo = Column(SmallInteger)
    kvanto = Column(SmallInteger)
    bildo = Column(String(40))
    formato = Column(Text)
    paghoj = Column(SmallInteger)
    stato = Column(Text)
    notoj = Column(Text)
    deponloko = Column(Text)
    lastemodifitade = Column(Text)


class Dissendoj(Base):
    __tablename__ = 'dissendoj'

    id = Column(Integer, primary_key=True)
    nomo = Column(String(20), nullable=False, server_default=text("''"))
    nomede = Column(String)
    kiam = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    alkiu = Column(Text)
    kiom = Column(Integer, nullable=False, server_default=text("'0'"))
    temo = Column(String)
    teksto = Column(Text)


class DissendojEnketoj(Base):
    __tablename__ = 'dissendoj_enketoj'

    id = Column(Integer, primary_key=True)
    dissendo = Column(Integer, nullable=False)
    dem_num = Column(Integer, nullable=False)
    dem_teksto = Column(Text)


class DissendojRespondoj(Base):
    __tablename__ = 'dissendoj_respondoj'

    id = Column(Integer, primary_key=True)
    ukodo = Column(String(4))
    retposxto = Column(Text)
    enketo = Column(Integer, nullable=False)
    kiam = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class Gazkom(Base):
    __tablename__ = 'gazkom'

    num = Column(Integer, primary_key=True)
    numero = Column(Integer, nullable=False, server_default=text("'0'"))
    dato = Column(Date)
    ordo = Column(Integer)
    titolo = Column(String(255))
    ttit = Column(String(255))
    hteksto = Column(Text)
    tteksto = Column(Text)
    sendita = Column(Enum('jes', 'ne'))


t_hotel05 = Table(
    'hotel05', metadata,
    Column('numero', Integer, nullable=False, server_default=text("'0'")),
    Column('hotelo', String(50), nullable=False, server_default=text("''")),
    Column('ordo', String(5)),
    Column('ordig', Integer),
    Column('rango', Integer),
    Column('unulita', Integer),
    Column('dulita', Integer),
    Column('dif1', Integer),
    Column('dif2', Integer),
    Column('dif3', Integer),
    Column('kvanto_unu', Integer),
    Column('kvanto_du', Integer),
    Column('kvanto_d1', Integer),
    Column('kvanto_d2', Integer),
    Column('kvanto_d3', Integer),
    Column('difino1', String(12), nullable=False, server_default=text("''")),
    Column('difino2', String(12), nullable=False, server_default=text("''")),
    Column('difino3', String(12), nullable=False, server_default=text("''")),
    Column('s1', String(30), nullable=False, server_default=text("''")),
    Column('s2', String(30), nullable=False, server_default=text("''")),
    Column('s3', String(30), nullable=False, server_default=text("''")),
    Column('adre', Text),
    Column('foreco', String(30)),
    Column('priskribo', Text)
)


t_hotel06 = Table(
    'hotel06', metadata,
    Column('numero', Integer, nullable=False, server_default=text("'0'")),
    Column('hotelo', String(50), nullable=False, server_default=text("''")),
    Column('ordo', String(5)),
    Column('ordig', Integer),
    Column('rango', Integer),
    Column('unulita', Integer),
    Column('dulita', Integer),
    Column('dif1', Integer),
    Column('dif2', Integer),
    Column('dif3', Integer),
    Column('kvanto_unu', Integer),
    Column('kvanto_du', Integer),
    Column('kvanto_d1', Integer),
    Column('kvanto_d2', Integer),
    Column('kvanto_d3', Integer),
    Column('difino1', String(12), nullable=False, server_default=text("''")),
    Column('difino2', String(12), nullable=False, server_default=text("''")),
    Column('difino3', String(12), nullable=False, server_default=text("''")),
    Column('s1', String(30), nullable=False, server_default=text("''")),
    Column('s2', String(30), nullable=False, server_default=text("''")),
    Column('s3', String(30), nullable=False, server_default=text("''")),
    Column('adre', Text),
    Column('foreco', String(30)),
    Column('priskribo', Text)
)


t_hotel07 = Table(
    'hotel07', metadata,
    Column('numero', Integer, nullable=False, server_default=text("'0'")),
    Column('hotelo', String(50), nullable=False, server_default=text("''")),
    Column('ordo', String(5)),
    Column('ordig', Integer),
    Column('rango', Integer),
    Column('unulita', Integer),
    Column('dulita', Integer),
    Column('dif1', Integer),
    Column('dif2', Integer),
    Column('dif3', Integer),
    Column('kvanto_unu', Integer),
    Column('kvanto_du', Integer),
    Column('kvanto_d1', Integer),
    Column('kvanto_d2', Integer),
    Column('kvanto_d3', Integer),
    Column('difino1', String(12), nullable=False, server_default=text("''")),
    Column('difino2', String(12), nullable=False, server_default=text("''")),
    Column('difino3', String(12), nullable=False, server_default=text("''")),
    Column('s1', String(30), nullable=False, server_default=text("''")),
    Column('s2', String(30), nullable=False, server_default=text("''")),
    Column('s3', String(30), nullable=False, server_default=text("''")),
    Column('adre', Text),
    Column('foreco', String(30)),
    Column('priskribo', Text)
)


t_hotel08 = Table(
    'hotel08', metadata,
    Column('numero', Integer, nullable=False, server_default=text("'0'")),
    Column('hotelo', String(50), nullable=False, server_default=text("''")),
    Column('ordo', String(5)),
    Column('ordig', Integer),
    Column('rango', Integer),
    Column('unulita', Integer),
    Column('dulita', Integer),
    Column('dif1', Integer),
    Column('dif2', Integer),
    Column('dif3', Integer),
    Column('kvanto_unu', Integer),
    Column('kvanto_du', Integer),
    Column('kvanto_d1', Integer),
    Column('kvanto_d2', Integer),
    Column('kvanto_d3', Integer),
    Column('difino1', String(12), nullable=False, server_default=text("''")),
    Column('difino2', String(12), nullable=False, server_default=text("''")),
    Column('difino3', String(12), nullable=False, server_default=text("''")),
    Column('s1', String(30), nullable=False, server_default=text("''")),
    Column('s2', String(30), nullable=False, server_default=text("''")),
    Column('s3', String(30), nullable=False, server_default=text("''")),
    Column('adre', Text),
    Column('foreco', String(30)),
    Column('priskribo', Text)
)


t_hotel09 = Table(
    'hotel09', metadata,
    Column('numero', Integer, nullable=False, server_default=text("'0'")),
    Column('hotelo', String(50), nullable=False, server_default=text("''")),
    Column('ordo', String(5)),
    Column('ordig', Integer),
    Column('rango', Integer),
    Column('unulita', Integer),
    Column('dulita', Integer),
    Column('dif1', Integer),
    Column('dif2', Integer),
    Column('dif3', Integer),
    Column('kvanto_unu', Integer),
    Column('kvanto_du', Integer),
    Column('kvanto_d1', Integer),
    Column('kvanto_d2', Integer),
    Column('kvanto_d3', Integer),
    Column('difino1', String(12), nullable=False, server_default=text("''")),
    Column('difino2', String(12), nullable=False, server_default=text("''")),
    Column('difino3', String(12), nullable=False, server_default=text("''")),
    Column('s1', String(30), nullable=False, server_default=text("''")),
    Column('s2', String(30), nullable=False, server_default=text("''")),
    Column('s3', String(30), nullable=False, server_default=text("''")),
    Column('adre', Text),
    Column('foreco', String(30)),
    Column('priskribo', Text)
)


class Hoteloj(Base):
    __tablename__ = 'hoteloj'

    numero = Column(Integer, primary_key=True)
    hotelo = Column(Text)
    ordo = Column(String(5))
    ordig = Column(Integer)
    rango = Column(Integer)
    kvanto_unu = Column(Integer)
    kvanto_du = Column(Integer)
    kvanto_d1 = Column(Integer)
    kvanto_d2 = Column(Integer)
    kvanto_d3 = Column(Integer)
    difino1 = Column(String(12), nullable=False, server_default=text("''"))
    difino2 = Column(String(12), nullable=False, server_default=text("''"))
    difino3 = Column(String(12), nullable=False, server_default=text("''"))
    s1 = Column(String(30), nullable=False, server_default=text("''"))
    s2 = Column(String(30), nullable=False, server_default=text("''"))
    s3 = Column(String(30), nullable=False, server_default=text("''"))
    adre = Column(Text)
    foreco = Column(String(30))
    priskribo = Column(Text)
    jaro = Column(Integer)
    retejo = Column(Text)
    retadreso = Column(Text)
    tel = Column(Text)
    fakso = Column(Text)
    pliaj_dif_kampoj = Column(Text)
    unulita = Column(Float)
    dulita = Column(Float)
    dif1 = Column(Float)
    dif2 = Column(Float)
    dif3 = Column(Float)


t_hoteloj2009 = Table(
    'hoteloj2009', metadata,
    Column('numero', Integer, nullable=False, server_default=text("'0'")),
    Column('hotelo', String(50), nullable=False, server_default=text("''")),
    Column('ordo', String(5)),
    Column('ordig', Integer),
    Column('rango', Integer),
    Column('unulita', Integer),
    Column('dulita', Integer),
    Column('dif1', Integer),
    Column('dif2', Integer),
    Column('dif3', Integer),
    Column('kvanto_unu', Integer),
    Column('kvanto_du', Integer),
    Column('kvanto_d1', Integer),
    Column('kvanto_d2', Integer),
    Column('kvanto_d3', Integer),
    Column('difino1', String(12), nullable=False, server_default=text("''")),
    Column('difino2', String(12), nullable=False, server_default=text("''")),
    Column('difino3', String(12), nullable=False, server_default=text("''")),
    Column('s1', String(30), nullable=False, server_default=text("''")),
    Column('s2', String(30), nullable=False, server_default=text("''")),
    Column('s3', String(30), nullable=False, server_default=text("''")),
    Column('adre', Text),
    Column('foreco', String(30)),
    Column('priskribo', Text)
)


class Informiloj(Base):
    __tablename__ = 'informiloj'

    num = Column(Integer, primary_key=True)
    kodo = Column(String(10))
    ueakodo = Column(String(7))
    numero = Column(Integer, nullable=False)
    dato = Column(Date)
    ordo = Column(Integer)
    titolo = Column(String(255))
    ttit = Column(String(255))
    hteksto = Column(Text)
    tteksto = Column(Text)
    sendita = Column(Enum('jes', 'ne'))


t_kongresanoj = Table(
    'kongresanoj', metadata,
    Column('kn', Integer, nullable=False, server_default=text("'0'")),
    Column('tempo', DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")),
    Column('ueakodo', String(6), nullable=False, server_default=text("''")),
    Column('familianomo', String(50), nullable=False, server_default=text("''")),
    Column('personanomo', String(50), nullable=False, server_default=text("''")),
    Column('sekso', Enum('S-ro', 'S-ino', '')),
    Column('titolo', String(7), nullable=False, server_default=text("''")),
    Column('adreso', String(100), nullable=False, server_default=text("''")),
    Column('landokodo', String(4), nullable=False, server_default=text("''")),
    Column('naskightago', String(10), nullable=False, server_default=text("''")),
    Column('notoj', String(150), nullable=False, server_default=text("''")),
    Column('posxtkodo', String(10), nullable=False, server_default=text("''")),
    Column('profesio', String(30), nullable=False, server_default=text("''")),
    Column('retposxto', String(50), nullable=False, server_default=text("''")),
    Column('telkodo', String(10), nullable=False, server_default=text("''")),
    Column('telhejmo', String(15), nullable=False, server_default=text("''")),
    Column('teloficejo', String(15), nullable=False, server_default=text("''")),
    Column('fakso', String(15), nullable=False, server_default=text("''")),
    Column('urbo', String(30), nullable=False, server_default=text("''")),
    Column('pago', String(30), nullable=False, server_default=text("''")),
    Column('rabato', String(30), nullable=False, server_default=text("''")),
    Column('kunulo', String(30), nullable=False, server_default=text("''")),
    Column('atestilo', String(30), nullable=False, server_default=text("''")),
    Column('kotizo', Integer),
    Column('pagite', Integer),
    Column('donacoj', String(30), nullable=False, server_default=text("''")),
    Column('konglib', Enum('n', '')),
    Column('konf', String(3)),
    Column('enhavo', Text),
    Column('numero', Integer, nullable=False, index=True),
    Column('aperigo', Enum('jes', 'ne')),
    Column('neDB', Enum('jes', 'ne'))
)


t_kvantoj = Table(
    'kvantoj', metadata,
    Column('num', Integer, nullable=False),
    Column('kvanto', Integer, nullable=False),
    Column('komisiakvanto', Integer, nullable=False)
)


t_ls = Table(
    'ls', metadata,
    Column('varnumero', Integer, nullable=False),
    Column('jaro', Date),
    Column('kodo', String(9), nullable=False),
    Column('prezo', Numeric(6, 2), nullable=False),
    Column('rabatoricevita', SmallInteger, nullable=False),
    Column('rabatodonata', SmallInteger, nullable=False),
    Column('fakturtitolo', String(25), nullable=False),
    Column('titolo', Text, nullable=False),
    Column('aldonatitolo', Text, nullable=False),
    Column('auxtoro', Text, nullable=False),
    Column('kontribuantoj', Text, nullable=False),
    Column('kategorio', String(10), nullable=False),
    Column('subkategorio', Text, nullable=False),
    Column('tradukisto', Text, nullable=False),
    Column('lingvajinformoj', Text, nullable=False),
    Column('eldonloko', Text, nullable=False),
    Column('eldonitade', Text, nullable=False),
    Column('eldonjaro', Text, nullable=False),
    Column('imposto', Integer, nullable=False),
    Column('isbnissn', Text, nullable=False),
    Column('alteco', String(8), nullable=False),
    Column('pagxnombro', String(20), nullable=False),
    Column('acxetprezo', Numeric(6, 2), nullable=False),
    Column('acxetvaluto', String(6), nullable=False),
    Column('stokvaloro', Numeric(6, 2), nullable=False),
    Column('sxlosilvortoj', Text, nullable=False),
    Column('eldonfaka', Text, nullable=False),
    Column('dato', String(6), nullable=False),
    Column('enirukat', String(3), nullable=False),
    Column('mendoloko', Text, nullable=False),
    Column('dato2', String(5), nullable=False),
    Column('ald_inf', Text, nullable=False),
    Column('la_de_re', String(50), nullable=False),
    Column('rec_en_re', String(10), nullable=False),
    Column('specialaj_inf', Text, nullable=False),
    Column('kataloga_klar', Text, nullable=False),
    Column('dato_au', Date),
    Column('kvanto', Integer, nullable=False),
    Column('komisiakvanto', Integer, nullable=False)
)


t_ls1 = Table(
    'ls1', metadata,
    Column('varnumero', Integer, nullable=False),
    Column('jaro', Date),
    Column('kodo', String(9), nullable=False),
    Column('prezo', Numeric(6, 2), nullable=False),
    Column('rabatoricevita', SmallInteger, nullable=False),
    Column('rabatodonata', SmallInteger, nullable=False),
    Column('fakturtitolo', String(25), nullable=False),
    Column('titolo', Text, nullable=False),
    Column('aldonatitolo', Text, nullable=False),
    Column('auxtoro', Text, nullable=False),
    Column('kontribuantoj', Text, nullable=False),
    Column('kategorio', String(10), nullable=False),
    Column('subkategorio', Text, nullable=False),
    Column('tradukisto', Text, nullable=False),
    Column('lingvajinformoj', Text, nullable=False),
    Column('eldonloko', Text, nullable=False),
    Column('eldonitade', Text, nullable=False),
    Column('eldonjaro', Text, nullable=False),
    Column('imposto', Integer, nullable=False),
    Column('isbnissn', Text, nullable=False),
    Column('alteco', String(8), nullable=False),
    Column('pagxnombro', String(20), nullable=False),
    Column('acxetprezo', Numeric(6, 2), nullable=False),
    Column('acxetvaluto', String(6), nullable=False),
    Column('stokvaloro', Numeric(6, 2), nullable=False),
    Column('sxlosilvortoj', Text, nullable=False),
    Column('eldonfaka', Text, nullable=False),
    Column('dato', String(6), nullable=False),
    Column('enirukat', String(3), nullable=False),
    Column('mendoloko', Text, nullable=False),
    Column('dato2', String(5), nullable=False),
    Column('ald_inf', Text, nullable=False),
    Column('la_de_re', String(50), nullable=False),
    Column('rec_en_re', String(10), nullable=False),
    Column('specialaj_inf', Text, nullable=False),
    Column('kataloga_klar', Text, nullable=False),
    Column('dato_au', Date)
)


t_ls2 = Table(
    'ls2', metadata,
    Column('varnumero', Integer, nullable=False, server_default=text("'0'")),
    Column('jaro', String(11), nullable=False, server_default=text("''")),
    Column('kodo', String(9), nullable=False, server_default=text("''")),
    Column('prezo', Numeric(5, 2), nullable=False, server_default=text("'0.00'")),
    Column('rabatoricevita', SmallInteger, nullable=False, server_default=text("'0'")),
    Column('rabatodonata', SmallInteger, nullable=False, server_default=text("'0'")),
    Column('kvanto', SmallInteger, nullable=False, server_default=text("'0'")),
    Column('komisiakvanto', SmallInteger, nullable=False, server_default=text("'0'")),
    Column('fakturtitolo', String(25), nullable=False, server_default=text("''")),
    Column('titolo', String(100), nullable=False, server_default=text("''")),
    Column('aldonatitolo', String(100), nullable=False, server_default=text("''")),
    Column('auxtoro', String(70), nullable=False, server_default=text("''")),
    Column('kontribuantoj', String(100), nullable=False, server_default=text("''")),
    Column('kategorio', String(10), nullable=False, server_default=text("''")),
    Column('subkategorio', String(20), nullable=False, server_default=text("''")),
    Column('tradukisto', String(100), nullable=False, server_default=text("''")),
    Column('lingvajinformoj', String(50), nullable=False, server_default=text("''")),
    Column('eldonloko', String(30), nullable=False, server_default=text("''")),
    Column('eldonitade', String(50), nullable=False, server_default=text("''")),
    Column('eldonjaro', String(20), nullable=False, server_default=text("''")),
    Column('imposto', Integer, nullable=False, server_default=text("'0'")),
    Column('isbnissn', String(20), nullable=False, server_default=text("''")),
    Column('alteco', String(8), nullable=False, server_default=text("''")),
    Column('pagxnombro', SmallInteger, nullable=False, server_default=text("'0'")),
    Column('acxetprezo', Numeric(5, 2), nullable=False, server_default=text("'0.00'")),
    Column('acxetvaluto', String(6), nullable=False, server_default=text("''")),
    Column('stokvaloro', Numeric(5, 2), nullable=False, server_default=text("'0.00'")),
    Column('sxlosilvortoj', String(50), nullable=False, server_default=text("''")),
    Column('eldonfaka', String(50), nullable=False, server_default=text("''")),
    Column('dato', String(5), nullable=False, server_default=text("''")),
    Column('enirukat', String(3), nullable=False, server_default=text("''")),
    Column('mendoloko', String(10), nullable=False, server_default=text("''")),
    Column('dato2', String(5), nullable=False, server_default=text("''")),
    Column('ald_inf', String(50), nullable=False, server_default=text("''")),
    Column('la_de_re', String(50), nullable=False, server_default=text("''")),
    Column('rec_en_re', String(10), nullable=False, server_default=text("''")),
    Column('specialaj_inf', String(50), nullable=False, server_default=text("''")),
    Column('kataloga_klar', String(150), nullable=False, server_default=text("''"))
)


class Membroj(Base):
    __tablename__ = 'membroj'

    numero = Column(Integer, primary_key=True)
    tempo = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    ueakodo = Column(String(6), nullable=False, server_default=text("''"))
    familianomo = Column(String(50), nullable=False, server_default=text("''"))
    personanomo = Column(String(50), nullable=False, server_default=text("''"))
    sekso = Column(Enum('S-ro', 'S-ino', ''))
    titolo = Column(String(7), nullable=False, server_default=text("''"))
    adreso = Column(String(100), nullable=False, server_default=text("''"))
    landokodo = Column(String(4), nullable=False, server_default=text("''"))
    naskightago = Column(String(10), nullable=False, server_default=text("''"))
    notoj = Column(Text)
    posxtkodo = Column(String(10), nullable=False, server_default=text("''"))
    profesio = Column(String(30), nullable=False, server_default=text("''"))
    retposxto = Column(Text)
    telkodo = Column(String(10), nullable=False, server_default=text("''"))
    telhejmo = Column(String(15), nullable=False, server_default=text("''"))
    teloficejo = Column(String(15), nullable=False, server_default=text("''"))
    fakso = Column(String(15), nullable=False, server_default=text("''"))
    urbo = Column(String(30), nullable=False, server_default=text("''"))
    pago = Column(String(30), nullable=False, server_default=text("''"))
    memkat = Column(String(70))
    subten = Column(String(50))
    sumo = Column(Integer, nullable=False, server_default=text("'0'"))
    valuto = Column(String(30))
    portebla = Column(String(50))


t_novvar = Table(
    'novvar', metadata,
    Column('vn', Integer, nullable=False, server_default=text("'0'")),
    Column('dato3', Date)
)


class Opinioj(Base):
    __tablename__ = 'opinioj'

    id = Column(Integer, primary_key=True)
    num = Column(Integer, nullable=False, server_default=text("'0'"))
    dato = Column(Date, nullable=False, server_default=text("'0000-00-00'"))
    opinio = Column(String(255), nullable=False, server_default=text("''"))
    nomo = Column(String(50))


class Paghoj(Base):
    __tablename__ = 'paghoj'

    num = Column(Integer, primary_key=True)
    dato = Column(Date)
    urlo = Column(String(255))
    titolo = Column(String(255))
    teksto = Column(Text)
    html = Column(Text)
    vidita = Column(Integer)
    rajtoj = Column(Integer)


t_programo = Table(
    'programo', metadata,
    Column('jaro', YEAR(4), nullable=False),
    Column('tempo_komenca', Time, nullable=False),
    Column('tempo_fina', Time, nullable=False),
    Column('tago', Integer, nullable=False),
    Column('evento', Text, nullable=False),
    Column('loko', Text),
    Column('abc', Text)
)


t_rec = Table(
    'rec', metadata,
    Column('vnum', Integer, nullable=False, server_default=text("'0'")),
    Column('dato', Date, nullable=False, server_default=text("'0000-00-00'")),
    Column('rectit', String(255), nullable=False, server_default=text("''")),
    Column('recautor', String(255), nullable=False, server_default=text("''")),
    Column('fonto', String(100)),
    Column('ligilo', String(100)),
    Column('recenzo', Text, nullable=False),
    Column('nomo', String(50), nullable=False, server_default=text("''")),
    Column('rajto', String(3)),
    Column('id', Integer, nullable=False, server_default=text("'0'"))
)


class Rec1(Base):
    __tablename__ = 'rec1'

    vnum = Column(Integer, nullable=False, server_default=text("'0'"))
    dato = Column(Date, nullable=False, server_default=text("'0000-00-00'"))
    rectit = Column(String(255), nullable=False, server_default=text("''"))
    recautor = Column(String(255), nullable=False, server_default=text("''"))
    fonto = Column(String(100))
    ligilo = Column(String(100))
    recenzo = Column(Text, nullable=False)
    nomo = Column(String(50), nullable=False, server_default=text("''"))
    rajto = Column(String(3))
    id = Column(Integer, primary_key=True)
    kodo = Column(String(9), nullable=False, server_default=text("''"))


class Recenzoj(Base):
    __tablename__ = 'recenzoj'

    vnum = Column(Integer, nullable=False, server_default=text("'0'"))
    dato = Column(Date, nullable=False, server_default=text("'0000-00-00'"))
    rectit = Column(String(255), nullable=False, server_default=text("''"))
    recautor = Column(String(255), nullable=False, server_default=text("''"))
    fonto = Column(String(100))
    ligilo = Column(String(100))
    recenzo = Column(Text, nullable=False)
    nomo = Column(String(50), nullable=False, server_default=text("''"))
    rajto = Column(String(3))
    id = Column(Integer, primary_key=True)
    kodo = Column(String(9), nullable=False, server_default=text("''"))


t_registro = Table(
    'registro', metadata,
    Column('id', Integer),
    Column('numero', Text, nullable=False),
    Column('dato', Date)
)


class Revuoj(Base):
    __tablename__ = 'revuoj'

    num = Column(Integer, primary_key=True)
    titolo = Column(String(255), nullable=False, server_default=text("''"))
    komento = Column(String(50))
    kod = Column(String(4))
    aper = Column(Integer)


t_spe2 = Table(
    'spe2', metadata,
    Column('num', Integer, nullable=False, server_default=text("'0'")),
    Column('numero', Integer, nullable=False, server_default=text("'0'")),
    Column('kodo', String(4), nullable=False, server_default=text("''")),
    Column('ueakodo', String(4), nullable=False, server_default=text("''")),
    Column('pnomo', Text, nullable=False),
    Column('fnomo', Text, nullable=False),
    Column('kat', Text, nullable=False),
    Column('tipo', Integer, nullable=False, server_default=text("'0'")),
    Column('jaro', YEAR(4))
)


t_spezaro = Table(
    'spezaro', metadata,
    Column('num', Integer, nullable=False, index=True),
    Column('numero', Integer, nullable=False, server_default=text("'0'")),
    Column('kodo', String(4), nullable=False, server_default=text("''")),
    Column('ueakodo', String(4), nullable=False, server_default=text("''")),
    Column('pnomo', Text, nullable=False),
    Column('fnomo', Text, nullable=False),
    Column('kat', Text, nullable=False),
    Column('tipo', Integer, nullable=False, server_default=text("'0'")),
    Column('jaro', YEAR(4)),
    Column('komento', Text)
)


t_spezaro1 = Table(
    'spezaro1', metadata,
    Column('num', Integer, nullable=False, server_default=text("'0'")),
    Column('numero', Integer, nullable=False, server_default=text("'0'")),
    Column('kodo', String(4), nullable=False, server_default=text("''")),
    Column('ueakodo', String(4), nullable=False, server_default=text("''")),
    Column('pnomo', Text, nullable=False),
    Column('fnomo', Text, nullable=False),
    Column('kat', Text, nullable=False),
    Column('tipo', Integer, nullable=False, server_default=text("'0'"))
)


t_spezaro_rez = Table(
    'spezaro_rez', metadata,
    Column('num', Integer, nullable=False, server_default=text("'0'")),
    Column('numero', Integer, nullable=False, server_default=text("'0'")),
    Column('kodo', String(4), nullable=False, server_default=text("''")),
    Column('ueakodo', String(4), nullable=False, server_default=text("''")),
    Column('pnomo', Text, nullable=False),
    Column('fnomo', Text, nullable=False),
    Column('kat', Text, nullable=False),
    Column('tipo', Integer, nullable=False, server_default=text("'0'")),
    Column('jaro', YEAR(4))
)


class Spezoj(Base):
    __tablename__ = 'spezoj'

    id = Column(Integer, primary_key=True)
    dato = Column(Date)
    jaro = Column(YEAR(4))
    numero = Column(Integer, nullable=False, server_default=text("'0'"))
    kodo = Column(String(4), nullable=False, server_default=text("''"))
    valuto = Column(String(30), nullable=False, server_default=text("''"))
    reg = Column(Text, nullable=False)
    nreg = Column(Text, nullable=False)
    nsumo = Column(Float(16))
    lreg = Column(Text, nullable=False)
    lsum = Column(Float(16))
    tot = Column(Float(16))
    indikoj = Column(Text, nullable=False)
    tipo = Column(Integer, nullable=False, server_default=text("'0'"))
    notoj = Column(Text)


class Teko(Base):
    __tablename__ = 'teko'

    num = Column(Integer, primary_key=True)
    titolo = Column(String(255), nullable=False, server_default=text("''"))
    elnomo = Column(String(50))
    kodnomo = Column(String(25))
    jaro = Column(Integer)
    monato = Column(Integer)
    numero = Column(String(15))
    absnum = Column(String(15))
    vido = Column(String(3))


t_uk2004 = Table(
    'uk2004', metadata,
    Column('kn', Integer, nullable=False, server_default=text("'0'")),
    Column('tempo', DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")),
    Column('ueakodo', String(6), nullable=False, server_default=text("''")),
    Column('familianomo', String(50), nullable=False, server_default=text("''")),
    Column('personanomo', String(50), nullable=False, server_default=text("''")),
    Column('sekso', Enum('S-ro', 'S-ino', '')),
    Column('titolo', String(7), nullable=False, server_default=text("''")),
    Column('adreso', String(100), nullable=False, server_default=text("''")),
    Column('landokodo', String(4), nullable=False, server_default=text("''")),
    Column('naskightago', String(10), nullable=False, server_default=text("''")),
    Column('notoj', String(150), nullable=False, server_default=text("''")),
    Column('posxtkodo', String(10), nullable=False, server_default=text("''")),
    Column('profesio', String(30), nullable=False, server_default=text("''")),
    Column('retposxto', Text),
    Column('telkodo', String(10), nullable=False, server_default=text("''")),
    Column('telhejmo', String(15), nullable=False, server_default=text("''")),
    Column('teloficejo', String(15), nullable=False, server_default=text("''")),
    Column('fakso', String(15), nullable=False, server_default=text("''")),
    Column('urbo', String(30), nullable=False, server_default=text("''")),
    Column('pago', String(30), nullable=False, server_default=text("''")),
    Column('rabato', String(30), nullable=False, server_default=text("''")),
    Column('kunulo', String(30), nullable=False, server_default=text("''")),
    Column('atestilo', String(30)),
    Column('kotizo', Integer, nullable=False, server_default=text("'0'")),
    Column('pagite', Integer, nullable=False, server_default=text("'0'")),
    Column('konglib', Enum('n', '')),
    Column('konf', Enum('ne', 'jes', 'mal'))
)


t_uk2005 = Table(
    'uk2005', metadata,
    Column('kn', Integer, nullable=False, server_default=text("'0'")),
    Column('tempo', DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")),
    Column('ueakodo', String(6), nullable=False, server_default=text("''")),
    Column('familianomo', String(50), nullable=False, server_default=text("''")),
    Column('personanomo', String(50), nullable=False, server_default=text("''")),
    Column('sekso', Enum('S-ro', 'S-ino', '')),
    Column('titolo', String(7), nullable=False, server_default=text("''")),
    Column('adreso', String(100), nullable=False, server_default=text("''")),
    Column('landokodo', String(4), nullable=False, server_default=text("''")),
    Column('naskightago', String(10), nullable=False, server_default=text("''")),
    Column('notoj', String(150), nullable=False, server_default=text("''")),
    Column('posxtkodo', String(10), nullable=False, server_default=text("''")),
    Column('profesio', String(30), nullable=False, server_default=text("''")),
    Column('retposxto', String(50), nullable=False, server_default=text("''")),
    Column('telkodo', String(10), nullable=False, server_default=text("''")),
    Column('telhejmo', String(15), nullable=False, server_default=text("''")),
    Column('teloficejo', String(15), nullable=False, server_default=text("''")),
    Column('fakso', String(15), nullable=False, server_default=text("''")),
    Column('urbo', String(30), nullable=False, server_default=text("''")),
    Column('pago', String(30), nullable=False, server_default=text("''")),
    Column('rabato', String(30), nullable=False, server_default=text("''")),
    Column('kunulo', String(30), nullable=False, server_default=text("''")),
    Column('atestilo', String(30), nullable=False, server_default=text("''")),
    Column('kotizo', Integer),
    Column('pagite', Integer),
    Column('donacoj', String(30), nullable=False, server_default=text("''")),
    Column('konglib', Enum('n', '')),
    Column('konf', String(3)),
    Column('enhavo', Text),
    Column('numero', Integer, nullable=False, server_default=text("'0'"))
)


t_uk2006 = Table(
    'uk2006', metadata,
    Column('kn', Integer, nullable=False, server_default=text("'0'")),
    Column('tempo', DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")),
    Column('ueakodo', String(6), nullable=False, server_default=text("''")),
    Column('familianomo', String(50), nullable=False, server_default=text("''")),
    Column('personanomo', String(50), nullable=False, server_default=text("''")),
    Column('sekso', Enum('S-ro', 'S-ino', '')),
    Column('titolo', String(7), nullable=False, server_default=text("''")),
    Column('adreso', String(100), nullable=False, server_default=text("''")),
    Column('landokodo', String(4), nullable=False, server_default=text("''")),
    Column('naskightago', String(10), nullable=False, server_default=text("''")),
    Column('notoj', String(150), nullable=False, server_default=text("''")),
    Column('posxtkodo', String(10), nullable=False, server_default=text("''")),
    Column('profesio', String(30), nullable=False, server_default=text("''")),
    Column('retposxto', String(50), nullable=False, server_default=text("''")),
    Column('telkodo', String(10), nullable=False, server_default=text("''")),
    Column('telhejmo', String(15), nullable=False, server_default=text("''")),
    Column('teloficejo', String(15), nullable=False, server_default=text("''")),
    Column('fakso', String(15), nullable=False, server_default=text("''")),
    Column('urbo', String(30), nullable=False, server_default=text("''")),
    Column('pago', String(30), nullable=False, server_default=text("''")),
    Column('rabato', String(30), nullable=False, server_default=text("''")),
    Column('kunulo', String(30), nullable=False, server_default=text("''")),
    Column('atestilo', String(30), nullable=False, server_default=text("''")),
    Column('kotizo', Integer),
    Column('pagite', Integer),
    Column('donacoj', String(30), nullable=False, server_default=text("''")),
    Column('konglib', Enum('n', '')),
    Column('konf', String(3)),
    Column('enhavo', Text),
    Column('numero', Integer, nullable=False, server_default=text("'0'"))
)


t_uk2007 = Table(
    'uk2007', metadata,
    Column('kn', Integer, nullable=False, server_default=text("'0'")),
    Column('tempo', DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'")),
    Column('ueakodo', String(6), nullable=False, server_default=text("''")),
    Column('familianomo', String(50), nullable=False, server_default=text("''")),
    Column('personanomo', String(50), nullable=False, server_default=text("''")),
    Column('sekso', Enum('S-ro', 'S-ino', '')),
    Column('titolo', String(7), nullable=False, server_default=text("''")),
    Column('adreso', String(100), nullable=False, server_default=text("''")),
    Column('landokodo', String(4), nullable=False, server_default=text("''")),
    Column('naskightago', String(10), nullable=False, server_default=text("''")),
    Column('notoj', String(150), nullable=False, server_default=text("''")),
    Column('posxtkodo', String(10), nullable=False, server_default=text("''")),
    Column('profesio', String(30), nullable=False, server_default=text("''")),
    Column('retposxto', String(50), nullable=False, server_default=text("''")),
    Column('telkodo', String(10), nullable=False, server_default=text("''")),
    Column('telhejmo', String(15), nullable=False, server_default=text("''")),
    Column('teloficejo', String(15), nullable=False, server_default=text("''")),
    Column('fakso', String(15), nullable=False, server_default=text("''")),
    Column('urbo', String(30), nullable=False, server_default=text("''")),
    Column('pago', String(30), nullable=False, server_default=text("''")),
    Column('rabato', String(30), nullable=False, server_default=text("''")),
    Column('kunulo', String(30), nullable=False, server_default=text("''")),
    Column('atestilo', String(30), nullable=False, server_default=text("''")),
    Column('kotizo', Integer),
    Column('pagite', Integer),
    Column('donacoj', String(30), nullable=False, server_default=text("''")),
    Column('konglib', Enum('n', '')),
    Column('konf', String(3)),
    Column('enhavo', Text),
    Column('numero', Integer, nullable=False, server_default=text("'0'"))
)


class UrbajInformoj(Base):
    __tablename__ = 'urbaj_informoj'

    num = Column(Integer, primary_key=True)
    landokodo = Column(String(2))
    urbo_eo = Column(Text)
    urbo = Column(Text)
    regiono = Column(String(2))
    loghantaro = Column(Integer)
    geo1 = Column(String(10))
    geo2 = Column(String(10))


class Uzantoj(Base):
    __tablename__ = 'uzantoj'

    tempo = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    uznomo = Column(String(15), primary_key=True, server_default=text("''"))
    plenanomo = Column(String(50), nullable=False, server_default=text("''"))
    pasvorto = Column(String(50), nullable=False, server_default=text("''"))
    land = Column(String(2), nullable=False, server_default=text("''"))
    lando = Column(String(3))
    kodo = Column(String(4))


t_uzz = Table(
    'uzz', metadata,
    Column('tempo', DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")),
    Column('uznomo', String(15), nullable=False, server_default=text("''")),
    Column('plenanomo', String(50), nullable=False, server_default=text("''")),
    Column('pasvorto', String(50), nullable=False, server_default=text("''"))
)


class Varbiloj(Base):
    __tablename__ = 'varbiloj'

    num = Column(Integer, primary_key=True)
    elnomo = Column(String(50))
    dato = Column(Date)
    priskribo = Column(Text)
    autoro = Column(String(150))
    eldoninto = Column(String(150))
    jaro = Column(Integer)
    populareco = Column(Integer)
    rekomendita = Column(Integer)
    kodo = Column(String(20))


class Vizitantoj(Base):
    __tablename__ = 'vizitantoj'

    numero = Column(Integer, primary_key=True)
    koda_vorto = Column(String(50))
    lando = Column(String(3))
    lingvo = Column(String(2))
    vizitata_pagho = Column(Text)
    dato = Column(Date)
    tempo = Column(Time)
    intkodo = Column(String(100))
    menuo = Column(String(100))
    mtempo = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class VizitantojDb(Base):
    __tablename__ = 'vizitantoj_db'

    numero = Column(Integer, primary_key=True)
    kodo = Column(String(50))
    lando = Column(String(3))
    ipv4 = Column(String(15))
    ipv6 = Column(BINARY(16))
    dato = Column(Date)
    tempo = Column(Time)
