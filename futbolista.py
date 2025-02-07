from deportista import Deportista
from persona import Persona


class Futbolista(Persona,Deportista):
     listaFutbolistas = []


     def __init__(self,nombre,edad,altura,sexo,añosPracticando , golesMarcados,tarjetasRojas,piernaHabil):
         Persona.__init__(self,nombre,edad,altura,sexo)
         Deportista.__init__(self,añosPracticando,"Futbol")
         self._golesMarcados = golesMarcados
         self._tarjetasRojas= tarjetasRojas
         self._piernaHabil = piernaHabil

         Futbolista.listaFutbolistas.append(self)

     def getGolesMarcados(self):
         return self._golesMarcados

     def setGolesMarcados(self, golesMarcados):
         self._golesMarcados= golesMarcados

     def getTarjetasRojas(self):
         return self._tarjetasRojas

     def setTarjetasRojas(self, tarjetasRojas):
         self._tarjetasRojas = tarjetasRojas

     def getPiernaHabil(self):
         return self._piernaHabil

     def setPiernaHabil(self, piernaHabil):
         self._piernaHabil = piernaHabil

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

     def getAñosPracticando(self):
        return self._añosPracticando

     def setDeporte(self,deporte):
        self._deporte= Deportista.setDeporte(self,deporte)

     def setAñosPracticando(self,añosPracticando):
        self._añosPracticando= Deportista.setAñosPracticando(self,añosPracticando)


     def __str__(self):
         return (
                 "Mi nombre es " + self._nombre +
                 " soy profesional en el deporte " + self._deporte +
                 " Tengo " + str(self._edad) + " años de edad y llevo " +
                 str(self._añosPracticando) + " años en el deporte"
         )
