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
        import os
        from xml.dom import minidom

        nextcourse = {"Englisch", "Mathematik", "NW", "Deutsch"}
        os.system('cls||clear')


        document = minidom.parse(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'kurse.xml'))         #load document into RAM
        elements = document.getElementsByTagName('kurs')

        lk1 = input(f"Wählen Sie den ersten Leistungskurs: {nextcourse}\n")                                     #wait for user to input
        nextcourse.clear()                                                                                      #clear next possible course set
        os.system('cls||clear')                                                                                 #clear terminal
        for node in elements:                                                                                   #search all elements
            if node.getElementsByTagName('leistungskurs1')[0].childNodes[0].nodeValue == lk1:                   #check if first child node of element equals user input
                nextcourse.add(node.getElementsByTagName('leistungskurs2')[0].childNodes[0].nodeValue)          #add all elements to set where above condition is met


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
        input()                                                                                                 #wait for enter to prevent closing on windows

if __name__ == "__main__":
    k = Kurswaehler()
    k.query()
