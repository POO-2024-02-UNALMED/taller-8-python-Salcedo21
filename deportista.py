class Deportista:

    def __init__(self, añosPracticando, deporte="Futbol"):
        self._deporte = deporte
        self._añosPracticando = añosPracticando

    def getDeporte(self):
        return self._deporte

    def getAñosPracticando(self):
        return self._añosPracticando

    def setDeporte(self,deporte):
        self._deporte= deporte

    def setAñosPracticando(self,anosPracticando):
        self._añosPracticando= anosPracticando
