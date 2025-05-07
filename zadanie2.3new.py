# zadanie 1
# John, Michael, Terry, Eric, Graham
namelist = ["John", "Michael", "Terry", "Eric", "Graham"]
li = [len(im)for im in namelist]
name_dictionary = {n: qua for n,qua in zip (namelist,li)
}
print (name_dictionary)

# zadanie 2
# 
liczby = [1, 2, 3, 5, 6, 11, 12, 18, 19, 21]
pierwsze = []
t = True
for i in liczby:
    s = i%2 !=0
    if s == t:
        pierwsze.append(i)
        
print (pierwsze)


#zadanie 3

dni = ['pon','śro','pią','sob']
dni.insert(1,"wto")
dni.insert(3,"czw")
dni.append("nie")
print(dni)


#zadanie 4
sek = ["włącz czajnik","znajdź opakowanie herbaty","zalej herbatę","nalej wody do czajnika","wyjmij kubek","włóż herbatę do kubka"]
nowa = [sek[3], sek[0], sek[1], sek[4], sek [5], sek[2]]
print (nowa)

# Zadanie 3.4
print ("ABDCD - 3.4")
