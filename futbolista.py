from deportista import Deportista
from persona import Persona


class Futbolista(Persona,Deportista):
     listaFutbolistas = []


     def __init__(self,nombre,edad,altura,sexo,deporte , anosPracticando, golesMarcados,tarjetasRojas,piernaHabil):
         Persona.__init__(self,nombre,edad,altura,sexo)
         Deportista.__init__(self,deporte , anosPracticando,)
         self._golesMarcados = golesMarcados
         self._tarjetasRojas= tarjetasRojas
         self._piernaHabil = piernaHabil

         Futbolista.listaFutbolistas.append(self)

     def getNombre(self):
        return self._nombre

     def setNombre(self,nombre):
         self._nombre= Persona.setNombre(self,nombre)

     def getEdad(self):
         return self._edad

     def setEdad(self,edad):
         self._nombre= Persona.setEdad(self,edad)

     def getAltura(self):
        return self._altura

     def setAltura(self,altura):
         self._altura = Persona.setAltura(self,altura)

     def getSexo(self):
        return self._sexo

     def setSexo(self,sexo):
         self._sexo = Persona.setSexo(self,sexo)

     def getDeporte(self):
        return self._deporte

     def getanosPracticando(self):
        return self._anosPracticando

     def setDeporte(self,deporte):
        self._deporte= Deportista.setDeporte(self,deporte)

     def setAnosPracticando(self,anosPracticando):
        self._anosPracticando= Deportista.setAnosPracticando(self,anosPracticando)


     def __str__(self):
         return "Mi nombre es "+self._nombre +" soy profesional en el deporte "+self._deporte+" Tengo "+ self._edad +" años de edad y llevo "+ self._anosPracticando +" años en el deporte"
