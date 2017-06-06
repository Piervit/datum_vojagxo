# coding: utf-8
from sqlalchemy import Column, Date, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, Time, text
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


t_abmendo = Table(
    'abmendo', metadata,
    Column('mendo', Integer, nullable=False),
    Column('titolo', Text, nullable=False),
    Column('kodo', String(4), nullable=False),
    Column('aere', Integer),
    Column('difino', Text),
    Column('pagsumo', Numeric(10, 2), nullable=False),
    Column('avi', Integer, nullable=False)
)


t_abonoj = Table(
    'abonoj', metadata,
    Column('ueakodo', String(7), nullable=False),
    Column('tempo', Date),
    Column('abono', Text),
    Column('formato', String(6)),
    Column('kodigo', String(7)),
    Column('retadreso', Text),
    Column('numero', Integer, unique=True, server_default=text("nextval(('abonoj_numero_seq'::text)::regclass)"))
)


t_ajnaj_informoj = Table(
    'ajnaj_informoj', metadata,
    Column('num', Integer, nullable=False, server_default=text("nextval('ajnaj_informoj_num_seq'::regclass)")),
    Column('kodo', Text),
    Column('unu', Text),
    Column('du', Text),
    Column('tri', Text),
    Column('kvar', Text),
    Column('kvin', Text),
    Column('ses', Text),
    Column('sep', Text),
    Column('ok', Text),
    Column('nau', Text),
    Column('dek', Text),
    Column('n1', Integer),
    Column('n2', Integer),
    Column('n3', Integer),
    Column('n4', Integer),
    Column('n5', Integer),
    Column('landokodo', String(3)),
    Column('d1', Date),
    Column('d2', Date),
    Column('d3', Date),
    Column('d4', Date),
    Column('dato', Date)
)


t_elsxuto = Table(
    'elsxuto', metadata,
    Column('numero', Integer, nullable=False, server_default=text("nextval('elsxuto_numero_seq'::regclass)")),
    Column('dato', Date),
    Column('ueakodo', String(4), nullable=False),
    Column('kio', Text)
)


t_eraroj = Table(
    'eraroj', metadata,
    Column('numero', Integer, nullable=False, server_default=text("nextval('eraroj_numero_seq'::regclass)")),
    Column('dato', Date),
    Column('adreso', Text),
    Column('tipo', Text)
)


t_fakaro = Table(
    'fakaro', metadata,
    Column('numero', Integer, nullable=False),
    Column('dato', Date),
    Column('kiu', String(6), nullable=False),
    Column('vorto', Text),
    Column('fakoj', Text),
    Column('nombro', Integer),
    Column('uligo', Text)
)


t_fakasocioj = Table(
    'fakasocioj', metadata,
    Column('ueakodo', String(6)),
    Column('dato', Date),
    Column('kiu', String(6), nullable=False),
    Column('titolo', Text),
    Column('siglo', Text),
    Column('fondita', Text),
    Column('emblemo', Text),
    Column('celoj', Text),
    Column('kategorio', Text),
    Column('membraro', Text),
    Column('prezidanto', Text),
    Column('jarkotizo', Text),
    Column('kontoj', Text),
    Column('organo', Text),
    Column('diskutgrupo', Text),
    Column('servoj', Text),
    Column('retejo', Text),
    Column('valideco', Integer)
)


class Kontaktoj(Base):
    __tablename__ = 'kontaktoj'

    numero = Column(Integer, primary_key=True, server_default=text("nextval('kontaktoj_numero_seq'::regclass)"))
    kodo = Column(String(7), nullable=False)
    retejo = Column(String(150))
    mesagxilo = Column(String(100))
    skajpo = Column(String(100))
    priskribo = Column(Text)
    klubkont = Column(String(3))
    gastigo = Column(String(3))
    ekskurso = Column(String(3))
    servoj = Column(Text)
    foto = Column(String(50))
    notoj = Column(String(150))
    valido = Column(String(3))


t_kores = Table(
    'kores', metadata,
    Column('numero', Integer, nullable=False, server_default=text("nextval('kores_numero_seq'::regclass)")),
    Column('dato', Date, nullable=False),
    Column('tempo', Time, nullable=False),
    Column('ueakodo', String(4), nullable=False),
    Column('tipo', String(4), nullable=False),
    Column('kiu', String(4), nullable=False),
    Column('notoj', Text)
)


t_mendita = Table(
    'mendita', metadata,
    Column('ukodo', Text),
    Column('kn', Integer),
    Column('alvendato', Text),
    Column('forirdato', Text),
    Column('aluk', Text),
    Column('flugnumero', Text),
    Column('alvenhoro1', Text),
    Column('alimaniere', Text),
    Column('alvenhoro2', Text),
    Column('loghado', Text),
    Column('altern1', Text),
    Column('altern2', Text),
    Column('altern3', Text),
    Column('kunchambrano', Text),
    Column('kunkongnum', Text),
    Column('ak', Text),
    Column('ax', Text),
    Column('axa', Integer),
    Column('akk', Text),
    Column('akn', Text),
    Column('pk', Text),
    Column('px', Text),
    Column('pxf', Integer),
    Column('pkk', Text),
    Column('pkn', Text),
    Column('eksfr', Text),
    Column('dfr', Text),
    Column('bankedsum', Text),
    Column('bankkost', Text),
    Column('pago', Text),
    Column('pagkonf', Integer),
    Column('valideco', Text),
    Column('notoj', Text),
    Column('tempo', DateTime),
    Column('veg', String(3)),
    Column('sumof', Numeric(7, 2)),
    Column('korektita_sumof', Numeric(7, 2)),
    Column('jaro', Integer),
    Column('trans', Text),
    Column('aldonaj', Text)
)


t_mendita04 = Table(
    'mendita04', metadata,
    Column('ukodo', Text, nullable=False),
    Column('kn', Integer),
    Column('alvendato', Text, nullable=False),
    Column('forirdato', Text, nullable=False),
    Column('aluk', Text, nullable=False),
    Column('flugnumero', Text, nullable=False),
    Column('alvenhoro1', Text, nullable=False),
    Column('alimaniere', Text, nullable=False),
    Column('alvenhoro2', Text, nullable=False),
    Column('loghado', Text, nullable=False),
    Column('altern1', Text, nullable=False),
    Column('altern2', Text, nullable=False),
    Column('altern3', Text, nullable=False),
    Column('ch1', Text, nullable=False),
    Column('ch2', Text, nullable=False),
    Column('ch3', Text, nullable=False),
    Column('kunchambrano', Text, nullable=False),
    Column('kunkongnum', Text, nullable=False),
    Column('ak', Text, nullable=False),
    Column('ax', Text, nullable=False),
    Column('ax1a', Text, nullable=False),
    Column('ax2a', Text, nullable=False),
    Column('ax3a', Text, nullable=False),
    Column('pk', Text, nullable=False),
    Column('px', Text, nullable=False),
    Column('px0f', Text, nullable=False),
    Column('px1f', Text, nullable=False),
    Column('px2f', Text, nullable=False),
    Column('px3f', Text, nullable=False),
    Column('eksfr', Text, nullable=False),
    Column('dfr', Text, nullable=False),
    Column('bankedsum', Text, nullable=False),
    Column('transporto', Text, nullable=False),
    Column('bankkost', Text, nullable=False),
    Column('sumof', Integer),
    Column('pago', Text, nullable=False),
    Column('valideco', Text, nullable=False),
    Column('notoj', Text, nullable=False),
    Column('tempo', DateTime),
    Column('veg', String(3)),
    Column('pagkonf', Integer)
)


t_mendita05 = Table(
    'mendita05', metadata,
    Column('ukodo', Text),
    Column('kn', Integer),
    Column('alvendato', Text),
    Column('forirdato', Text),
    Column('aluk', Text),
    Column('flugnumero', Text),
    Column('alvenhoro1', Text),
    Column('alimaniere', Text),
    Column('alvenhoro2', Text),
    Column('loghado', Text),
    Column('altern1', Text),
    Column('altern2', Text),
    Column('altern3', Text),
    Column('kunchambrano', Text),
    Column('kunkongnum', Text),
    Column('ak', Text),
    Column('ax', Text),
    Column('axa', Integer),
    Column('akk', Text),
    Column('akn', Text),
    Column('pk', Text),
    Column('px', Text),
    Column('pxf', Integer),
    Column('pkk', Text),
    Column('pkn', Text),
    Column('eksfr', Text),
    Column('dfr', Text),
    Column('bankedsum', Text),
    Column('bankkost', Text),
    Column('sumof', Integer),
    Column('pago', Text),
    Column('pagkonf', Integer),
    Column('valideco', Text),
    Column('notoj', Text),
    Column('tempo', DateTime),
    Column('veg', String(3))
)


t_mendita06 = Table(
    'mendita06', metadata,
    Column('ukodo', Text),
    Column('kn', Integer),
    Column('alvendato', Text),
    Column('forirdato', Text),
    Column('aluk', Text),
    Column('flugnumero', Text),
    Column('alvenhoro1', Text),
    Column('alimaniere', Text),
    Column('alvenhoro2', Text),
    Column('loghado', Text),
    Column('altern1', Text),
    Column('altern2', Text),
    Column('altern3', Text),
    Column('kunchambrano', Text),
    Column('kunkongnum', Text),
    Column('ak', Text),
    Column('ax', Text),
    Column('axa', Integer),
    Column('akk', Text),
    Column('akn', Text),
    Column('pk', Text),
    Column('px', Text),
    Column('pxf', Integer),
    Column('pkk', Text),
    Column('pkn', Text),
    Column('eksfr', Text),
    Column('dfr', Text),
    Column('bankedsum', Text),
    Column('bankkost', Text),
    Column('sumof', Integer),
    Column('pago', Text),
    Column('pagkonf', Integer),
    Column('valideco', Text),
    Column('notoj', Text),
    Column('tempo', DateTime),
    Column('veg', String(3))
)


t_mendita07 = Table(
    'mendita07', metadata,
    Column('ukodo', Text),
    Column('kn', Integer),
    Column('alvendato', Text),
    Column('forirdato', Text),
    Column('aluk', Text),
    Column('flugnumero', Text),
    Column('alvenhoro1', Text),
    Column('alimaniere', Text),
    Column('alvenhoro2', Text),
    Column('loghado', Text),
    Column('altern1', Text),
    Column('altern2', Text),
    Column('altern3', Text),
    Column('kunchambrano', Text),
    Column('kunkongnum', Text),
    Column('ak', Text),
    Column('ax', Text),
    Column('axa', Integer),
    Column('akk', Text),
    Column('akn', Text),
    Column('pk', Text),
    Column('px', Text),
    Column('pxf', Integer),
    Column('pkk', Text),
    Column('pkn', Text),
    Column('eksfr', Text),
    Column('dfr', Text),
    Column('bankedsum', Text),
    Column('bankkost', Text),
    Column('sumof', Integer),
    Column('pago', Text),
    Column('pagkonf', Integer),
    Column('valideco', Text),
    Column('notoj', Text),
    Column('tempo', DateTime),
    Column('veg', String(3))
)


t_mendita08 = Table(
    'mendita08', metadata,
    Column('ukodo', Text),
    Column('kn', Integer),
    Column('alvendato', Text),
    Column('forirdato', Text),
    Column('aluk', Text),
    Column('flugnumero', Text),
    Column('alvenhoro1', Text),
    Column('alimaniere', Text),
    Column('alvenhoro2', Text),
    Column('loghado', Text),
    Column('altern1', Text),
    Column('altern2', Text),
    Column('altern3', Text),
    Column('kunchambrano', Text),
    Column('kunkongnum', Text),
    Column('ak', Text),
    Column('ax', Text),
    Column('axa', Integer),
    Column('akk', Text),
    Column('akn', Text),
    Column('pk', Text),
    Column('px', Text),
    Column('pxf', Integer),
    Column('pkk', Text),
    Column('pkn', Text),
    Column('eksfr', Text),
    Column('dfr', Text),
    Column('bankedsum', Text),
    Column('bankkost', Text),
    Column('pago', Text),
    Column('pagkonf', Integer),
    Column('valideco', Text),
    Column('notoj', Text),
    Column('tempo', DateTime),
    Column('veg', String(3)),
    Column('sumof', Numeric(7, 2))
)


t_mendita09 = Table(
    'mendita09', metadata,
    Column('ukodo', Text),
    Column('kn', Integer),
    Column('alvendato', Text),
    Column('forirdato', Text),
    Column('aluk', Text),
    Column('flugnumero', Text),
    Column('alvenhoro1', Text),
    Column('alimaniere', Text),
    Column('alvenhoro2', Text),
    Column('loghado', Text),
    Column('altern1', Text),
    Column('altern2', Text),
    Column('altern3', Text),
    Column('kunchambrano', Text),
    Column('kunkongnum', Text),
    Column('ak', Text),
    Column('ax', Text),
    Column('axa', Integer),
    Column('akk', Text),
    Column('akn', Text),
    Column('pk', Text),
    Column('px', Text),
    Column('pxf', Integer),
    Column('pkk', Text),
    Column('pkn', Text),
    Column('eksfr', Text),
    Column('dfr', Text),
    Column('bankedsum', Text),
    Column('bankkost', Text),
    Column('pago', Text),
    Column('pagkonf', Integer),
    Column('valideco', Text),
    Column('notoj', Text),
    Column('tempo', DateTime),
    Column('veg', String(3)),
    Column('sumof', Numeric(7, 2)),
    Column('korektita_sumof', Numeric(7, 2))
)


t_mendita2009 = Table(
    'mendita2009', metadata,
    Column('ukodo', Text),
    Column('kn', Integer),
    Column('alvendato', Text),
    Column('forirdato', Text),
    Column('aluk', Text),
    Column('flugnumero', Text),
    Column('alvenhoro1', Text),
    Column('alimaniere', Text),
    Column('alvenhoro2', Text),
    Column('loghado', Text),
    Column('altern1', Text),
    Column('altern2', Text),
    Column('altern3', Text),
    Column('kunchambrano', Text),
    Column('kunkongnum', Text),
    Column('ak', Text),
    Column('ax', Text),
    Column('axa', Integer),
    Column('akk', Text),
    Column('akn', Text),
    Column('pk', Text),
    Column('px', Text),
    Column('pxf', Integer),
    Column('pkk', Text),
    Column('pkn', Text),
    Column('eksfr', Text),
    Column('dfr', Text),
    Column('bankedsum', Text),
    Column('bankkost', Text),
    Column('pago', Text),
    Column('pagkonf', Integer),
    Column('valideco', Text),
    Column('notoj', Text),
    Column('tempo', DateTime),
    Column('veg', String(3)),
    Column('sumof', Numeric(7, 2)),
    Column('korektita_sumof', Numeric(7, 2))
)


class PgaDiagram(Base):
    __tablename__ = 'pga_diagrams'

    diagramname = Column(String(64), primary_key=True)
    diagramtables = Column(Text)
    diagramlinks = Column(Text)


class PgaForm(Base):
    __tablename__ = 'pga_forms'

    formname = Column(String(64), primary_key=True)
    formsource = Column(Text)


class PgaGraph(Base):
    __tablename__ = 'pga_graphs'

    graphname = Column(String(64), primary_key=True)
    graphsource = Column(Text)
    graphcode = Column(Text)


class PgaImage(Base):
    __tablename__ = 'pga_images'

    imagename = Column(String(64), primary_key=True)
    imagesource = Column(Text)


class PgaLayout(Base):
    __tablename__ = 'pga_layout'

    tablename = Column(String(64), primary_key=True)
    nrcols = Column(SmallInteger)
    colnames = Column(Text)
    colwidth = Column(Text)


class PgaQuery(Base):
    __tablename__ = 'pga_queries'

    queryname = Column(String(64), primary_key=True)
    querytype = Column(String(1))
    querycommand = Column(Text)
    querytables = Column(Text)
    querylinks = Column(Text)
    queryresults = Column(Text)
    querycomments = Column(Text)


class PgaReport(Base):
    __tablename__ = 'pga_reports'

    reportname = Column(String(64), primary_key=True)
    reportsource = Column(Text)
    reportbody = Column(Text)
    reportprocs = Column(Text)
    reportoptions = Column(Text)


class PgaScript(Base):
    __tablename__ = 'pga_scripts'

    scriptname = Column(String(64), primary_key=True)
    scriptsource = Column(Text)


t_rad = Table(
    'rad', metadata,
    Column('uekodo', Text),
    Column('tempo', Date),
    Column('uznomo', Text),
    Column('plu', Text),
    Column('filtro', String(5)),
    Column('subskribo', Text),
    Column('saluto', String(30)),
    Column('konf', Integer)
)


t_radw = Table(
    'radw', metadata,
    Column('uekodo', Text, nullable=False),
    Column('tempo', Date),
    Column('uznomo', Text),
    Column('plu', Text),
    Column('filtro', String(5)),
    Column('subskribo', Text),
    Column('saluto', String(30)),
    Column('konf', String(2))
)


t_respondecoj = Table(
    'respondecoj', metadata,
    Column('ueakodo', String(4)),
    Column('estraro', Text),
    Column('komitato', Text),
    Column('oficistoj', Text),
    Column('volontuloj', Text),
    Column('komisioj', Text),
    Column('tejoes', Text),
    Column('tejokom', Text)
)


t_taskoj = Table(
    'taskoj', metadata,
    Column('ueakodo', String(4)),
    Column('tkodo', Text),
    Column('tasko', Text)
)


t_uz0604 = Table(
    'uz0604', metadata,
    Column('tempo', String(10)),
    Column('ueakodo', String(6)),
    Column('saluto', Text),
    Column('pasvorto', Text),
    Column('validigo', String(4))
)


t_uzantaro = Table(
    'uzantaro', metadata,
    Column('tempo', String(10)),
    Column('ueakodo', String(6)),
    Column('saluto', Text),
    Column('pasvorto', Text),
    Column('validigo', String(4)),
    Column('mtempo', DateTime)
)


t_uzantoj = Table(
    'uzantoj', metadata,
    Column('tempo', String(10)),
    Column('ueakodo', String(6), unique=True),
    Column('saluto', Text),
    Column('pasvorto', Text),
    Column('validigo', String(4))
)


t_uzantoj_rez = Table(
    'uzantoj_rez', metadata,
    Column('tempo', String(10)),
    Column('ueakodo', String(6)),
    Column('saluto', Text),
    Column('pasvorto', Text),
    Column('validigo', String(4))
)


t_varmendintoj = Table(
    'varmendintoj', metadata,
    Column('numero', Integer, nullable=False, server_default=text("nextval('varmendintoj_numero_seq'::regclass)")),
    Column('tempo', DateTime, nullable=False),
    Column('ueakodo', String(6), nullable=False),
    Column('familianomo', Text, nullable=False),
    Column('personanomo', Text, nullable=False),
    Column('adreso', Text, nullable=False),
    Column('urbo', Text, nullable=False),
    Column('landokodo', String(4), nullable=False),
    Column('posxtkodo', String(10), nullable=False),
    Column('telkodo', String(10), nullable=False),
    Column('telhejmo', String(15), nullable=False),
    Column('teloficejo', String(15), nullable=False),
    Column('fakso', String(15), nullable=False),
    Column('retposxto', String(70), nullable=False),
    Column('sumo', Numeric(10, 2), nullable=False),
    Column('pago', Text, nullable=False),
    Column('validigo', String(3), nullable=False),
    Column('notoj', Text, nullable=False)
)


t_varmendo = Table(
    'varmendo', metadata,
    Column('mendo', Integer, nullable=False),
    Column('vnum', Integer, nullable=False),
    Column('kvant', Integer, nullable=False),
    Column('pagsumo', Numeric(10, 2), nullable=False),
    Column('avisumo', Numeric(10, 2), nullable=False)
)


t_vizitoj = Table(
    'vizitoj', metadata,
    Column('numero', Integer, nullable=False, server_default=text("nextval('vizitoj_numero_seq'::regclass)")),
    Column('dato', Date),
    Column('tempo', Time),
    Column('datof', Date),
    Column('tempof', Time),
    Column('ueakodo', String(6), nullable=False),
    Column('rajto', Integer)
)
