import modul_einsortieren
import modul_listen_zusammenfügen
import modul_liste_sortieren
import modul_array_summieren
import modul_anzahl_gerade
import modul_index_finden

mes=modul_einsortieren
mlz=modul_listen_zusammenfügen
mls=modul_liste_sortieren
mas=modul_array_summieren
mgz=modul_anzahl_gerade
mif=modul_index_finden

liste1=[]
liste2=[]

while True:
    zahl1=int(input("gebe eine Zahl ein: \n> "))
    zahl2=int(input("gebe eine weitere Zahl ein: \n> "))
    suche_zahl=int(input("welche zahl wird gesucht?: \n> "))

    mes.sort_in(liste1,zahl1)
    mes.sort_in(liste2,zahl2)

    liste3 = mls.sort_array(mlz.combine_list(liste1, liste2))
    print("------------------------------------------")
    print(f"Liste 1: \t {liste1} \nSumme Liste 1: \t{mas.summe(liste1)} \nAnzahl gerader Zahlen: \t{mgz.cout_even(liste1)}")
    print("------------------------------------------")
    print(f"Liste 2: \t {liste2} \nSumme Liste 2: \t{mas.summe(liste2)} \nAnzahl gerader Zahlen: \t{mgz.cout_even(liste2)}")
    print("------------------------------------------")
    print(f"Die beiden listen zusammengeführt und sortiert: \n{liste3} \nSumme Liste 1 und liste 2: \t{mas.summe(liste3)} \nAnzahl gerader Zahlen: \t{mgz.cout_even(liste3)}")
    print(f"Die gesuchte Zahl {suche_zahl} in der Liste3 ist unter index {mif.search_for_index(liste3,suche_zahl)} zu findenden")
    print("------------------------------------------")
    if input("möchtest du weitere Werte einfügen? (j/n) \n> ").lower() == "n":
        print("Program wird beendet.")
        break
