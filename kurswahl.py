import os
from xml.dom import minidom


class Kurswaehler:

    def _printem(self, node):
        print(f"""
            ----- Passender Kurs -----
            {node.getAttribute('id')}
            {node.getElementsByTagName('leistungskurs1')[0].childNodes[0].nodeValue}
            {node.getElementsByTagName('leistungskurs2')[0].childNodes[0].nodeValue}
            {node.getElementsByTagName('prüfungsfach3')[0].childNodes[0].nodeValue}
            {node.getElementsByTagName('prüfungsfach4')[0].childNodes[0].nodeValue}
            {node.getElementsByTagName('prüfungskomponente5')[0].childNodes[0].nodeValue}
            """)

    def query(self):
        nextcourse = {"Englisch", "Mathematik", "NW", "Deutsch"}
        os.system('cls||clear')

        # load document into RAM
        document = minidom\
            .parse(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'kurse.xml'))
        elements = document.getElementsByTagName('kurs')

        # wait for user to input
        lk1 = input(f"Wählen Sie den ersten Leistungskurs: {nextcourse}\n")
        # clear next possible course set
        nextcourse.clear()
        # clear terminal
        os.system('cls||clear')
        # search all elements
        for node in elements:
            # check if first child node of element equals user input
            if node.getElementsByTagName('leistungskurs1')[0].childNodes[0].nodeValue == lk1:
                # add all elements to set where above condition is met
                nextcourse.add(node.getElementsByTagName('leistungskurs2')[0].childNodes[0].nodeValue)


        lk2 = input(f"Wählen Sie den zweiten Leistungskurs aus einem der folgenden Kurse: {nextcourse}\n")
        nextcourse.clear()
        os.system('cls||clear')
        for node in elements:
            if (node.getElementsByTagName('leistungskurs1')[0].childNodes[0].nodeValue == lk1 and
                    node.getElementsByTagName('leistungskurs2')[0].childNodes[0].nodeValue == lk2):
                nextcourse.add(node.getElementsByTagName('prüfungsfach3')[0].childNodes[0].nodeValue)

        pf3 = input(f"Wählen Sie das dritte Prüfungsfach aus einem der folgenden Kurse: {nextcourse}\n")
        nextcourse.clear()
        os.system('cls||clear')
        for node in elements:
            if (node.getElementsByTagName('leistungskurs1')[0].childNodes[0].nodeValue == lk1 and
                    node.getElementsByTagName('leistungskurs2')[0].childNodes[0].nodeValue == lk2 and
                    node.getElementsByTagName('prüfungsfach3')[0].childNodes[0].nodeValue == pf3):
                nextcourse.add(node.getElementsByTagName('prüfungsfach4')[0].childNodes[0].nodeValue)

        pf4 = input(f"Wählen Sie das vierte Prüfungsfach aus einem der folgenden Kurse: {nextcourse}\n")
        nextcourse.clear()
        os.system('cls||clear')
        for node in elements:
            if (node.getElementsByTagName('leistungskurs1')[0].childNodes[0].nodeValue == lk1 and
                    node.getElementsByTagName('leistungskurs2')[0].childNodes[0].nodeValue == lk2 and
                    node.getElementsByTagName('prüfungsfach3')[0].childNodes[0].nodeValue == pf3 and
                    node.getElementsByTagName('prüfungsfach4')[0].childNodes[0].nodeValue == pf4):
                self._printem(node)
        # wait for enter to prevent closing on windows
        input()

if __name__ == "__main__":
    k = Kurswaehler()
    k.query()
