#Base della classe
class Espositore():
    def __init__(self, codice, nome, cognome):
        self.__codice = codice
        self.__nome = nome
        self.__cognome = cognome
        #self.__codS = codS

    #PROPERTY DI CLASSE
    @property
    def codice(self):
        return self.__codice
    @property
    def nome(self):
        return self.__nome
    @property
    def cognome(self):
        return self.__cognome

    #SETTER DI CLASSE:
    @codice.setter
    def codice(self, codice):
        self.__codice = codice
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    @cognome.setter
    def cognome(self, cognome):
        self.__cognome = cognome

    #METODO EQUAL
    def __eq__(self, other):
        if isinstance(other, Espositore):
            return self.__codice == other.codice
        return False

    #METODO PER STAMPARE
    def __str__(self):
        return f"Espositore: {self.__codice}, nome: {self.__nome}, cognome: {self.__cognome}"



