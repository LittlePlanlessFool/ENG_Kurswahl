"kurswahl.py"

import os
from xml.dom import minidom


def matches(element: minidom.Element, choices: list[str]) -> bool:
    """helper function, checks if -element-'s subelements contain the same
    respective string as -choice-'s elements"""
    names = (
        "leistungskurs1",
        "leistungskurs2",
        "prüfungsfach3",
        "prüfungsfach4",
        "prüfungskomponente5",
    )
    clap = []

    for i, choice in enumerate(choices):
        clap.append(element.getElementsByTagName(names[i])[0].childNodes[0].nodeValue == choice)
    return all(clap)


def printem(element: minidom.Element):
    """helper function, prints the values of -element-'s subelements"""
    print(
        f"""
        matched:
            {element.getAttribute('id')}
            ---
            {element.getElementsByTagName('leistungskurs1')[0].childNodes[0].nodeValue}
            {element.getElementsByTagName('leistungskurs2')[0].childNodes[0].nodeValue}
            {element.getElementsByTagName('prüfungsfach3')[0].childNodes[0].nodeValue}
            {element.getElementsByTagName('prüfungsfach4')[0].childNodes[0].nodeValue}
            {element.getElementsByTagName('prüfungskomponente5')[0].childNodes[0].nodeValue}
        --------"""
    )


def query():
    "side effecting, blobby"

    os.system("cls || clear")
    found, courses = [], []

    dommy = minidom.parse(
        os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "kurse.xml",
        )
    ).getElementsByTagName("kurs")

    print(
        """Kurs 1: Englisch, ...
Kurs 2: Mathematik, ...
Kurs 3: NW, ...
Kurs 4: Deutsch, ..."""
    )

    for i in range(4):
        courses.append(
            input(
                f"""Wählen Sie ein Fach an der {i + 1}ten Position
aus einem der obenstehenden Kurse.\n"""
            ).upper()
        )
        os.system("cls || clear")

        if not found:
            found = [elli for elli in dommy if matches(elli, courses)]
        else:
            temp = [elli for elli in found if matches(elli, courses)]
            found.clear()
            found = [ele for ele in temp]
            temp.clear()

        for entry in found:
            printem(entry)


def main():
    "entry point"
    query()
    input()


if __name__ == "__main__":
    main()
