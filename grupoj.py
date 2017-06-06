
import novuea


def krei_grupojn () :
    grupoj = {}
    ## membrokategorio
    grupoj["dm"] = novuea.Grupo("dm","dumviva membro", "")
    grupoj["dmj"] = novuea.Grupo("dmj","dumviva membro kun jarlibro", "")
    grupoj["dm-t"] = novuea.Grupo("dm-t","dumviva membro kun kontakto", "")
    grupoj["dp"] = novuea.Grupo("dp","dumviva patrono de UEA", "")
    grupoj["dpt"] = novuea.Grupo("dp","dumviva patrono de TEJO", "")
    grupoj["fc"] = novuea.Grupo("fc","membro pere de Fondaĵo Canuto" , "")
    grupoj["hm"] = novuea.Grupo("hm","honora membro" , "")
    grupoj["hpk"] = novuea.Grupo("hpk","honora patrono" , "")
    grupoj["ma"] = novuea.Grupo("ma","membro-abonanto", "")
    grupoj["ma-k"] = novuea.Grupo("ma-k","membro-abonanto kun kontako (juna)", "")
    grupoj["mg"] = novuea.Grupo("mg","membro kun gvidlibro", "")
    grupoj["mj"] = novuea.Grupo("mj","membro kun jarlibro", "")
    grupoj["mj-k"] = novuea.Grupo("mj","membro kun karlibro kaj Kontakto", "")
    grupoj["t.hm"] = novuea.Grupo("t.hm","honora membro de TEJO", "")
    grupoj["t.hp"] = novuea.Grupo("t.hp","honora prezidanto de TEJO", "")

    ##abonaĵo
    grupoj["eda"] = novuea.Grupo("eda","abono al 'Esperanto Dokumentoj' angle", "")
    grupoj["ede"] = novuea.Grupo("ede","abono al 'Esperanto Dokumentoj' esperante", "")
    grupoj["def"] = novuea.Grupo("edf","abono al 'Esperanto Dokumentoj' france", "")
    grupoj["edi"] = novuea.Grupo("edi","abono al 'Esperanto en Irlando", "")
    grupoj["edi"] = novuea.Grupo("edi","abono al 'Esperanto en Irlando", "")
    grupoj["eem"] = novuea.Grupo("eem","abono al 'Esperanto en Marche / esperanto en Afrique" , "")
    grupoj["eo"] = novuea.Grupo("eo","senpaga ricevanto de Esperanto" , "")

    grupoj["ka"] = novuea.Grupo("ka","kolektiva abono Kontakto, grupa distribuanto","")
    grupoj["kak"] = novuea.Grupo("kak","kolektiva abono Kontakto, individua ricevanto", "")
    grupoj["kto"] = novuea.Grupo("kto","Abonanto de kontakto", "")
    grupoj["kze"] = novuea.Grupo("kze","Senpaga ricevanto de Koncize", "")
    grupoj["nna"] = novuea.Grupo("nna","ricevanto de bulteno NNN e la angla", "")
    grupoj["nnf"] = novuea.Grupo("nnf","ricevanto de bulteno NNN e la franca", "")
    grupoj["nnh"] = novuea.Grupo("nnh","ricevanto de bulteno NNN e la hispana", "")
    grupoj["sa"] = novuea.Grupo("sa","simpla abonanto de Esperanto", "")
    grupoj["un"] = novuea.Grupo("un","ricevanto de 'UN kaj ni'", "")
 
 ## rilate al UEA/TEJO roloj
    grupoj["ĉd"] = novuea.Grupo("ĉd","ĉefdelegito", "ĉefdelegito aŭ peranto")
    grupoj["d"] = novuea.Grupo("d","delegito", "")
    grupoj["es"] = novuea.Grupo("es","estrarano" , "")
    grupoj["fd"] = novuea.Grupo("fd","fakdelegito" , "")
    grupoj["jd"] = novuea.Grupo("jd","junulara delegito" , "")
    grupoj["kfa"] = novuea.Grupo("kfa","ano de komisiono KFA", "")
    grupoj["kom.a"] = novuea.Grupo("kom.a","Komitatano A", "Komitatano A")
    grupoj["kom.b"] = novuea.Grupo("kom.b","Komitatano B", "Komitatano B")
    grupoj["kom.c"] = novuea.Grupo("kom.c","Komitatano C", "Komitatano C")
    grupoj["obs"] = novuea.Grupo("obs","observanto ĉe la komitato de UEA", "")
    grupoj["per"] = novuea.Grupo("per","kotizperanto de UEA", "")
    grupoj["t.es"] = novuea.Grupo("t.es","estrarano de TEJO", "")
    grupoj["t.kom"] = novuea.Grupo("t.kom","komitatano de TEJO", "")
    grupoj["vd"] = novuea.Grupo("vd","vicdelegito", "")

    ##rilate al aliaj asocioj
    grupoj["fa.a"] = novuea.Grupo("fa.a","faka asocio, aliĝinta" , "")
    grupoj["fa.k"] = novuea.Grupo("fa.k","faka asocio, kunlaboranta kontrakte" , "")
    grupoj["fa.n"] = novuea.Grupo("fa.n","faka asocio, sendependa (nealiĝinta)" , "")
    grupoj["la.a"] = novuea.Grupo("la.a","Landa asocio aliĝinta al UEA", "")
    grupoj["la.n"] = novuea.Grupo("la.n","Landa asocio nealiĝinta al UEA", "")
    grupoj["lg"] = novuea.Grupo("lg","Loka grupo anoncanta en la Jarlibro", "")
    grupoj["lk"] = novuea.Grupo("lk","loka klubo", "")
    grupoj["ls.a"] = novuea.Grupo("ls.a","Landa sekcio de TEJO, aliĝinta", "")
    grupoj["ls.n"] = novuea.Grupo("ls.n","Landa junulara organizaĵo, nealiĝinta", "aŭ junulara kontaktadreso")

    ## rilate al UK
    grupoj["bdo"] = novuea.Grupo("bdo","mendinto de kongresa bankedo", "")
    grupoj["kk"] = novuea.Grupo("kk","ricevanto de Kongresa Komuniko", "")
    grupoj["lkk"] = novuea.Grupo("lkk","membro de la Loka Kongresa Komitato", "")
    grupoj["sa.uk"] = novuea.Grupo("sa.uk","kongresa abonanto de 'Esperanto'", "")
    grupoj["uk"] = novuea.Grupo("uk","aliĝinto al la UK", "")

    ## ne ligita rekten al UEA /TEJO
    grupoj["ak"] = novuea.Grupo("ak","akademiano", "")
    grupoj["bl"] = novuea.Grupo("bl","blindulo", "")
    grupoj["ced"] = novuea.Grupo("ced","estrarano de CED", "")
    grupoj["igs.a"] = novuea.Grupo("igs.a","Kunlaboranto de Internacia Gazetara Servo, Angla" , "")
    grupoj["igs.e"] = novuea.Grupo("igs.e","Kunlaboranto de Internacia Gazetara Servo, Esperanto" , "")
    grupoj["igs.f"] = novuea.Grupo("igs.f","Kunlaboranto de Internacia Gazetara Servo, Franca" , "")
    grupoj["ih.d"] = novuea.Grupo("ih.d","donacinto al Instucio Hodler" , "")
    grupoj["ih.e"] = novuea.Grupo("ih.e","estrarano de Instucio Hodler" , "")
    grupoj["ih.p"] = novuea.Grupo("ih.p","pruntinto al Instucio Hodler" , "")
    grupoj["ipi"] = novuea.Grupo("ipi","ricevanto de Informilo por Interlingvistoj" , "")
    grupoj["sz"] = novuea.Grupo("sz","membro de societo zamenhof", "")

    #pri membroj
    grupoj["ĝir"] = novuea.Grupo("ĝir","partoprenanto de ĝirsistemo de UEA" , "")
    grupoj["ijk"] = novuea.Grupo("ijk","aliĝinto de IJK" , "")
    grupoj["jl"] = novuea.Grupo("jl","senpaga ricevanto de Jarlibro" , "")
    grupoj["kls"] = novuea.Grupo("kls","kliento de libroservo", "")
    grupoj["mec"] = novuea.Grupo("mec","mecenatoj", "gravaj donacintoj, ktp..")
    grupoj["nja"] = novuea.Grupo("nja","Amiko de novjorka oficejo", "")
    grupoj["njd"] = novuea.Grupo("njd","donacinto de novjorka oficejo", "")
    grupoj["njp"] = novuea.Grupo("njp","patrono de novjorka oficejo", "")
    grupoj["njs"] = novuea.Grupo("njs","subtenanto de novjorka oficejo", "")
    grupoj["pt"] = novuea.Grupo("pt","patrono de TEJO", "")

    ##aliaj
    grupoj["fl"] = novuea.Grupo("fl","flugpasaĝero" , "")
    grupoj["gaz"] = novuea.Grupo("gaz","grava Esperanto-gazeto" , "")
    grupoj["gaz.b"] = novuea.Grupo("gaz.b","malpli grava Esperanto-gazeto" , "")
    grupoj["eld"] = novuea.Grupo("eld","eldonejo" , "")
    grupoj["eld.b"] = novuea.Grupo("eld.b","eldonejo malpli grava" , "")
    grupoj["lib"] = novuea.Grupo("lib","libroservo", "")
    grupoj["nv"] = novuea.Grupo("nv","nevalida adreso", "plej ofte malaktuala")
    grupoj["nv.eo"] = novuea.Grupo("nv.eo","nevalida adreso", "plej ofte malaktuala")
    grupoj["nv.kto"] = novuea.Grupo("nv.kto","nevalida adreso", "plej ofte malaktuala")
    grupoj["nv.kze"] = novuea.Grupo("nv.kze","nevalida adreso", "plej ofte malaktuala")
    grupoj["nv.mem"] = novuea.Grupo("nv.mem","nevalida adreso", "plej ofte malaktuala")
    grupoj["nv.tt"] = novuea.Grupo("nv.tt","nevalida adreso", "plej ofte malaktuala")
    grupoj["rad"] = novuea.Grupo("rad","radio-stacio", "")
    grupoj["of"] = novuea.Grupo("of","esperanto-oficejo", "")



    






