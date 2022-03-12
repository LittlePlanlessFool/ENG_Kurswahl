import os, sys
from time import sleep

af1 = ["Deutsch", "Englisch", "Französisch", "Latein", "Spanisch", "Musik", "Bildende Kunst", "Darstellendes Spiel"]    #definition block
af1_bool = False
af2 = ["Politikwissenschaften", "Geschichte", "Geographie", "Philosophie"]
af2_bool = False
af3 = ["Mathematik", "Physik", "Chemie", "Biologie", "Informatik"]
af3_bool = False
alles = ["Deutsch", "Englisch", "Französisch", "Latein", "Spanisch", "Musik", "Bildende Kunst", "Darstellendes Spiel", "Politikwissenschaften", "Geschichte", "Geographie", "Philosophie", "Mathematik", "Physik", "Chemie", "Biologie", "Informatik", "Sport"]

def in_feld(fach:str):
    """Überprüft, ob <fach> Element der Listen <af1>, <af2>. <af3> ist und setzt ggf. den zugehörigen Bool auf True."""
    if fach in af1:
        global af1_bool
        af1_bool = True
    if fach in af2:
        global af2_bool
        af2_bool = True
    if fach in af3:
        global af3_bool
        af3_bool = True

def feld_fehlt():
    """Überprüft,ob die Booleans der AFs True sind, und gibt ggf. den Hinweis darauf aus."""
    if not af1_bool:
        print("\nEs fehlt noch ein Fach für Aufgabenfeld 1.")
    if not af2_bool:
        print("\nEs fehlt noch ein Fach für Aufgabenfeld 2.")
    if not af3_bool:
        print("\nEs fehlt noch ein Fach für Aufgabenfeld 3.")

def kursprüfer():
    """Überprüft, ob Fachkombinationen möglich sind, oder gibt Hinweise was fehlt"""
    lks = ["Englisch", "Französisch", "Spanisch", "Mathematik", "Physik", "Chemie", "Biologie", "Deutsch"]
    pfs = ["Englisch", "Französisch", "Spanisch", "Mathematik", "Deutsch"]
    pfs_c = 0
    vorraussetzungen_erfüllt = False

    os.system('cls||clear')
    print("""
    Bitte beachten!
    Sie müssen jedes Aufgabenfeld mindestens einmal in Ihren Prüfungsfächern wählen.
    Ihre Prüfungsfächer müssen mindestens zwei der folgenden Fächer beinhalten: Deutsch, Mathematik, Fremdsprachen.
    Ihr Referenzfach für die fünfte Prüfungskomponente darf nicht bereits Prüfungsfach sein, wenn Sie eine Präsentationsprüfung anstreben.
    Sollten Sie eine besondere Lernleistung erbringen wollen, können Sie jedes Fach wählen, auch wenn es dieses Programm nicht anzeigt.
    Gegebenenfalls können Sie bei falschen Kombinationen die Leistungskurse vertauschen, um eine gültige Kombination zu erhalten.
    Je nach Prüfungsfach können weitere Pflichtfächer anfallen; diese entnehmen Sie bitte der Präsentation.
    """)

    while not vorraussetzungen_erfüllt:

        while True:    #get 1. Leistungskurs
            lk1 = input(f"\nWählen Sie ein Fach als ersten Leistungskurs: {lks}\n")    
        
            try:
                lks.remove(lk1)
                alles.remove(lk1)
                break
            except ValueError:
                print(f"{lk1} ist keine Option!")
                continue

        in_feld(lk1)
        feld_fehlt()

        while True:    #get 1. Leistungskurs
            lk2 = input(f"\nWählen Sie ein Fach als zweiten Leistungskurs: {lks + af2}\n")
            try:
                alles.remove(lk2)
                break
            except ValueError:
                print(f"{lk2} ist keine Option!")
                continue

        in_feld(lk2)
        feld_fehlt()

        while True:    #get 3. PF
            pf3 = input(f"\nWählen Sie das dritte Prüfungsfach: {alles}\n")
            try:
                alles.remove(pf3)
                break
            except ValueError:
                print(f"{pf3} ist keine Option!")
                continue

        in_feld(pf3)
        feld_fehlt()

        while True:    #get 4. PF
            pf4 = input(f"\nWählen Sie das vierte Prüfungsfach: {alles}\n")
            try:
                alles.remove(pf4)
                break
            except ValueError:
                print(f"{pf4} ist keine Option!")
                continue

        in_feld(pf4)
        feld_fehlt()

        while True:    #get 5. PK
            pk5 = input(f"\nWählen Sie das Referenzfach ihrer fünften Prüfungskomponente für Präsentationsprüfungen: {alles}\n")
            try:
                alles.remove(pk5)
                break
            except ValueError:
                print(f"{pk5} ist keine Option!")
                continue
        
        in_feld(pk5)

        
        for e in [lk1, lk2, pf3, pf4, pk5]:    #logic block Prüfungsfächer erfüllt
            if e in pfs:
                pfs_c += 1
        
        if [af1_bool, af2_bool, af3_bool] == [True, True, True] and pfs_c >= 2 and pk5 not in [lk1, lk2, pf3, pf4]:   #logic block Vorraussetzungen
            vorraussetzungen_erfüllt = True
            print(f"\nSie haben {lk1, lk2, pf3, pf4, pk5} gewählt. Bitte beachten Sie die weiteren Pflichtkurse für Ihre Fächerwahl.")
        else:
            print("Ihre Kurskombination entsprach nicht den Vorgaben!\nBeende!")
            sleep(1)
            os.system('cls||clear')
            sleep(1)
            exit()


if __name__ == "__main__":
    kursprüfer()