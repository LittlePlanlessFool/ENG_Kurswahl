"""very bad, but iiwdfi
TODO: fix repitition of if statements"""
import os
from xml.dom import minidom


class Kurswaehler:
    """AFII entspricht Politikwissenschaften, Geografie, Geschichte
    NW entspricht Physik, Chemie, Biologie
    Fremdsprachen entspricht Englisch, Französisch, Latein, Spanisch
    """

    def __init__(self):
        self.nextcourse = {"Englisch", "Mathematik", "NW", "Deutsch"}

        self.read_lk1 = lambda node: (node
                                      .getElementsByTagName('leistungskurs1')[0]
                                      .childNodes[0]
                                      .nodeValue
                                     )
        self.read_lk2 = lambda node: (node
                                      .getElementsByTagName('leistungskurs2')[0]
                                      .childNodes[0]
                                      .nodeValue
                                     )
        self.read_pf3 = lambda node: (node
                                      .getElementsByTagName('prüfungsfach3')[0]
                                      .childNodes[0]
                                      .nodeValue
                                     )
        self.read_pf4 = lambda node: (node
                                      .getElementsByTagName('prüfungsfach4')[0]
                                      .childNodes[0]
                                      .nodeValue
                                     )
        self._query()

    def _clear(self):
        os.system('cls||clear')
        self.nextcourse.clear()

    def _printem(self, node):
        print(f"""
            ----- Passender Kurs -----
            {node.getAttribute('id')}
            {self.read_lk1(node)}
            {self.read_lk2(node)}
            {self.read_pf3(node)}
            {self.read_pf4(node)}
            {node.getElementsByTagName('prüfungskomponente5')[0].childNodes[0].nodeValue}
            """)

    def _query(self):

        os.system('cls||clear')

        # load document into RAM
        document = (minidom
                    .parse(
                        os.path.join(os.path.dirname(os.path.abspath(__file__)), 'kurse.xml')
                        )
                    )
        self.elements = document.getElementsByTagName('kurs')

        self.lk1 = input(f"Wählen Sie den ersten Leistungskurs: {self.nextcourse}\n")
        self._clear()
        for node in self.elements:
            if self.read_lk1(node) == self.lk1:
                self.nextcourse.add(self.read_lk2(node))


        self.lk2 = input(f"Wählen Sie den zweiten Leistungskurs aus einem der folgenden Kurse: {self.nextcourse}\n")
        self._clear()
        for node in self.elements:
            if (self.read_lk1(node) == self.lk1 and
                    self.read_lk2(node) == self.lk2):
                self.nextcourse.add(self.read_pf3(node))

        self.pf3 = input(f"Wählen Sie das dritte Prüfungsfach aus einem der folgenden Kurse: {self.nextcourse}\n")
        self._clear()
        for node in self.elements:
            if (self.read_lk1(node) == self.lk1 and
                    self.read_lk2(node) == self.lk2 and
                    self.read_pf3(node) == self.pf3):
                self.nextcourse.add(self.read_pf4(node))

        self.pf4 = input(f"Wählen Sie das vierte Prüfungsfach aus einem der folgenden Kurse: {self.nextcourse}\n")
        self._clear()
        for node in self.elements:
            if (self.read_lk1(node) == self.lk1 and
                    self.read_lk2(node) == self.lk2 and
                    self.read_pf3(node) == self.pf3 and
                    self.read_pf4(node) == self.pf4):
                self._printem(node)
        # wait for enter to prevent closing on windows
        input()

if __name__ == "__main__":
    k = Kurswaehler()
