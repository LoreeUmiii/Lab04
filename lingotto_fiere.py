from espositore import Espositore
from stand import Stand, StandPreseExtra, StandPremium

class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self.__nome = nome
        self.listaStand = []
        self.listaEspositori = []

    """Aggiungere setter e getter se necessari"""
    @property
    def nome(self):
        return self.__nome

    @nome.setter #CAMBIO IL NOME
    def nome(self, nome):
        self.__nome = nome

    #SISTEMATA
    def __str__(self):
        #CREO UN'UNICA STRINGA CONTENENTE TUTTO IL CENTRO CREATO
        centroFieristico = f"Centro fieristico: {self.nome}\n"
        centroFieristico += "Espositori: \n"
        for e in self.listaEspositori:
            centroFieristico += f" -{e}\n"
        centroFieristico += "Stand:\n "
        for s in self.listaStand:
            centroFieristico += f" -{s}\n"

        return centroFieristico

    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        esp = None
        stand = None
        try:
            with open(file_path, "r", encoding="utf_8") as fileIn:
                for row in fileIn:
                    riga = row.strip()
                    if not riga: #controllo generale
                        continue
                    #popolo campi con i singoli valori del csv
                    campi = [c.strip() for c in riga.split(',')]

                    if campi[0].startswith('ES'):
                        if len(campi) >= 3:
                            esp = Espositore(campi[0], campi[1], campi[2])
                            #popolare un struttura per gli espositori
                            self.listaEspositori.append(esp)  #è uguale al puntatore

                    elif campi[0].startswith("ST"):
                        if len(campi) >= 4:
                            stand = Stand(campi[0], campi[1], campi[2], campi[3])
                        elif len(campi) == 5:
                            if campi[4].isdigit(): #è una cifra?
                                stand = StandPreseExtra(campi[0], campi[1], campi[2], campi[3], campi[4])
                            else:
                                stand = StandPremium(campi[0], campi[1], campi[2], campi[3], campi[4])
                    else:
                        continue
                    #popolare un struttura per gli stand
                    if not any(s.codice == stand.codice for s in self.listaStand):
                        self.listaStand.append(stand)
                    #self.listaStand.append(stand)

        except FileNotFoundError:
            print(f"File {file_path} non trovato! Inserirne uno esistente: ")

    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        standTrovato = None
        for s in self.listaStand:
            if codice_stand == s.codice:
                standTrovato = s
                break

        espTrovato = None
        for e in self.listaEspositori:
            if codice_espositore == e.codice:
                espTrovato = e
                break
        #Controlli generali:
        if not standTrovato:
            raise Exception(f"Stand: {codice_stand} non trovato!! ")
        if not espTrovato:
            raise Exception(f"Espositore: {codice_espositore} non trovato!! ")

        if not standTrovato.disponibile:
            raise Exception(f"Stand {codice_stand} non disponibile")

        for s in self.listaStand:
            if hasattr(s, "espositore") and s.espositore == espTrovato:
                raise Exception(f"L'espositore {codice_espositore} già assegnato")

        standTrovato.espositore = espTrovato #riferimento all'espositore
        standTrovato.disponibile = False #Stand occupato


    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """

        if not self.listaEspositori:
            print("Nessun espositore registrato! ")
            return None

        for e in self.listaEspositori:
            standAssociato = None

            for s in self.listaStand:
                if hasattr(s, "espositore") and s.espositore == e:
                    standAssociato = s
                    break

            if standAssociato:
                print(f"Espositore: {e} assegnato a: {standAssociato.codice} ")
            else:
                print("Espositore non assegnato a nessuno stand")

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        return sorted(self.listaStand)