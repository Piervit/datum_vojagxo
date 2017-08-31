def db_encode(vorto):
    if vorto is None:
        return ""
    else :
        return vorto.encode('utf-8')



class TabelTransiro:


    def __init__(self):
        self.tabelaro = {} #aro de objektoj preta por esti metita en la datumbazo

    #devas esti implementita de fila klaso por funkcii
    def konverti(self):
        assert False 

    #devas esti implementita de fila klaso por funkcii
    def konverti(self,arg1):
        assert False 

    #devas esti implementita de fila klaso por funkcii
    def konverti(self,arg1, arg2):
        assert False 

    def commit(self,session_novuea):
        session_novuea.begin()
        i = 0
        for sxlosilo, ento in self.tabelaro.items():
            session_novuea.add(ento)
            i = i +1
            if (i == 1000):
                session_novuea.commit()
                session_novuea.begin()
                i = 0
        session_novuea.commit()

    def add(self, sxlosilo, ento):
        self.tabelaro[sxlosilo] = ento
    
    def trovi(self, sxlosilo):
        try:
            return self.tabelaro[sxlosilo]
        except : 
            return None

    def ene(self, sxlosilo):
        return sxlosilo in self.tabelaro

