from xml.dom import minidom
import os

def query():
    """Vor.: <lk1>, <lk2>, <pf3>, <pf4>, <pk5> sind Fächergruppenbezeichnungen und vom Typ String.
       Eff.: Alle Kurse, die die angegebenen Fächergruppen an den entsprechenden Stellen enthalten, sind ausgegeben.
       Erg.: -"""


    os.system('cls||clear')

    def printem(node):
        print(f"""
            matched:
            {node.getAttribute('id')}
            {node.getElementsByTagName('leistungskurs1')[0].childNodes[0].nodeValue}
            {node.getElementsByTagName('leistungskurs2')[0].childNodes[0].nodeValue}
            {node.getElementsByTagName('prüfungsfach3')[0].childNodes[0].nodeValue}
            {node.getElementsByTagName('prüfungsfach4')[0].childNodes[0].nodeValue}
            {node.getElementsByTagName('prüfungskomponente5')[0].childNodes[0].nodeValue}
            """)

    document = minidom.parse(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'kurse.xml'))         #load document into RAM
    elements = document.getElementsByTagName('kurs')

    lk1 = input("Wählen Sie den ersten Leistungskurs: Englisch, Mathematik, NW, Deutsch.\n")                #wait for user to input
    os.system('cls||clear')                                                                                 #clear terminal
    for node in elements:                                                                                   #search all elements
        if node.getElementsByTagName('leistungskurs1')[0].childNodes[0].nodeValue == lk1:                   #check if first child node of element equals user input
            printem(node)                                                                                   #print all elements where above condition is met
            

    lk2 = input("Wählen Sie den zweiten Leistungskurs aus einem der angegebenen Kurse.\n")
    os.system('cls||clear')
    for node in elements:
        if (node.getElementsByTagName('leistungskurs1')[0].childNodes[0].nodeValue == lk1 and
                node.getElementsByTagName('leistungskurs2')[0].childNodes[0].nodeValue == lk2):
            printem(node)

    pf3 = input("Wählen Sie das dritte Prüfungsfach aus einem der angegebenen Kurse.\n")
    os.system('cls||clear')
    for node in elements:
        if (node.getElementsByTagName('leistungskurs1')[0].childNodes[0].nodeValue == lk1 and
                node.getElementsByTagName('leistungskurs2')[0].childNodes[0].nodeValue == lk2 and
                node.getElementsByTagName('prüfungsfach3')[0].childNodes[0].nodeValue == pf3):
            printem(node)

    pf4 = input("Wählen Sie das vierte Prüfungsfach aus einem der angegebenen Kurse.\n")
    os.system('cls||clear')
    for node in elements:
        if (node.getElementsByTagName('leistungskurs1')[0].childNodes[0].nodeValue == lk1 and 
                node.getElementsByTagName('leistungskurs2')[0].childNodes[0].nodeValue == lk2 and 
                node.getElementsByTagName('prüfungsfach3')[0].childNodes[0].nodeValue == pf3 and 
                node.getElementsByTagName('prüfungsfach4')[0].childNodes[0].nodeValue == pf4):
            printem(node)
            input()                                                                                         #wait for enter to prevent closing on windows

if __name__ == "__main__":
    query()