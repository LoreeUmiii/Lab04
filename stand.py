#Classe padre da cui creo le calssi figlie



class Stand():
    def __init__(self, codice, area, padiglione, prezzo):
        self.__codice = codice
        self.__area = float(area)
        self.__padiglione = int(padiglione)
        self.__prezzo = float(prezzo)
        self.__espositore = None
        self.__disponibile = True

    #GETTER
    @property
    def codice(self):
        return self.__codice
    @property
    def area(self):
        return self.__area
    @property
    def padiglione(self):
        return self.__padiglione
    @property
    def prezzo(self):
        return self.__prezzo
    @property
    def espositore(self):
        return self.__espositore
    @property
    def disponibile(self):
        return self.__disponibile

    #SETTER
    @codice.setter
    def codice(self, codice):
        self.__codice = codice
    @area.setter
    def area(self, area):
        self.__area = float(area)
    @padiglione.setter
    def padiglione(self, padiglione):
        self.__padiglione = int(padiglione)
    @prezzo.setter
    def prezzo(self, prezzo):
        self.__prezzo = float(prezzo)
    @espositore.setter
    def espositore(self, espositore):
        self.__espositore = espositore
    @disponibile.setter
    def disponibile(self, disponibile):
        self.__disponibile = disponibile

    #Metodo equal
    def __eq__(self, other):
        if isinstance(other, Stand):
            return self.__codice == other.codice
        return False

    #Metodo LT
    def __lt__(self, other):
        if isinstance(other, Stand):
            return self.__prezzo < other.prezzo
        return None

    #Metodo str
    def __str__(self):
        stato = None
        if self.__disponibile:
            stato = "Disponibile"
        else:
            if self.__espositore:
                stato = f"Occupato da: {self.__espositore.codice}"
            else:
                stato = "Non ha un espositore"
        return f"{self.__codice}: Standard | {self.__area} mq - Padiglione {self.__padiglione} - Prezzo {self.__prezzo}€ - {stato}"

#Classe Derivata da Stand (Attributo prese in più)
class StandPreseExtra(Stand):
    def __init__(self, codice, area, padiglione, prezzo, prese):
        super().__init__(codice, area, padiglione, prezzo)
        self.__prese = int(prese)

    #Getter
    @property
    def prese(self):
        return self.__prese
    @property
    def prezzo_finale(self):
        return f"{self.prezzo * (1 + 0.07*self.__prese)}"

    #Setter
    @prese.setter
    def prese(self, prese):
        self.__prese = int(prese)

    #Stampa
    def __str__(self):
        str_base = super().__str__()
        return f"{self.codice}: Prese Extra | {self.area} mq - Padiglione {self.padiglione} - Prezzo {self.prezzo_finale}€ - Prese aggiuntive: {self.__prese} - {'Disponibile' if self.disponibile else 'Occupato'}"


#Classe derivata da Stand (Attr. Posizione)
class StandPremium(Stand):
    def __init__(self,codice, area, padiglione, prezzo, posizione):
        super().__init__(codice, area, padiglione, prezzo)
        self.__posizione = posizione

    #Getter
    @property
    def posizione(self):
        return self.__posizione
    @property
    def prezzo_finale(self):
        return self.prezzo * 1.30

    #Setter
    @posizione.setter
    def posizione(self, posizione):
        self.__posizione = posizione

    #Metodo stampa
    def __str__(self):
        return f"{self.codice}: Premium ({self.__posizione}) | {self.area} mq - Padiglione {self.padiglione} - Prezzo {self.prezzo_finale}€ - {'Disponibile' if self.disponibile else 'Occupato'}"