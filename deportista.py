class Deportista:

    def __init__(self,deporte="Futbol" , anosPracticando):
        self._deporte = deporte
        self._anosPracticando = anosPracticando

    def getDeporte(self):
        return self._deporte

    def getanosPracticando(self):
        return self._anosPracticando

    def setDeporte(self,deporte):
        self._deporte= deporte

    def setAnosPracticando(self,anosPracticando):
        self._anosPracticando= anosPracticando
