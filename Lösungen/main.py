import modul_summieren
import modul_listen_zusammenfügen
import modul_gerade
import modul_nach_index_suchen 
import modul_in_liste_einsortieren
import modul_sortieren

msum=modul_summieren
mlz=modul_listen_zusammenfügen
mger=modul_gerade
mnis=modul_nach_index_suchen
mile=modul_in_liste_einsortieren
msort=modul_sortieren

liste1=[]
liste2=[]

while True:
    zahl_liste1=int(input("gebe eine Zahl ein die in Liste 1 hinzugefügt werden soll: \n> "))
    zahl_liste2=int(input("gebe eine Zahl ein die in Liste 2 hinzugefügt werden soll: \n> "))
    search= int(input("welche zahl wird ind der liste gesuch? \n> "))
    liste1=mile.add_and_sort(liste1,zahl_liste1)
    liste2=mile.add_and_sort(liste2,zahl_liste2)
    liste3=msort.sort_list(mlz.combine_list(liste1,liste2))
    print(f"Die Summe in Liste 1 und Liste 2: \n Liste 1: \t{msum.summe(liste1)} \n Liste 2: \t{msum.summe(liste2)}")
    print(f"Die entstandene sortierte Liste aus Liste 1 und Liste 2: \n{liste3}")
    print(f"Die Summe der beiden Listen lautet: {msum.summe(liste3)}")
    print(f"die Anzahl gerader Zahlen in Liste 1: {mger.count_even(liste1)}")
    print(f"Die Anzahl gerader Zahlen in Liste 2: {mger.count_even(liste2)}")
    print(f"Die Anzahl gerader Zahlen in der kombinierten Liste: {mger.count_even(liste3)}")
    print(f"Gesuchte Zahl {search} ist in der gemeinsamen sortierten liste unter index {mnis.search_for_index(liste3,search)} zu finden")
    if input("nocheine runde? (j/n): \n> ").lower()=="n":
        break
