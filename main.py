import random
from dataclasses import replace

print("============================ 1 uzduotis =======================")
# Sukurti du kintamuosius. Jiems priskirti savo mylimo aktoriaus vardą ir pavardę kaip stringus (Jonas Jonaitis).
# Atspausdinti trumpesnį stringą.

name = "Will"
surname = "Smith"

if len(name) > len(surname):
    print(name)
if len(surname) > len(name):
    print(surname)
else:
    print(f"Vardas ir pavarde turi toki pati simboliu kieki: {name}, {surname}")

print("============================ 2 uzduotis =======================")
# Sukurti du kintamuosius. Jiems priskirti savo mylimo aktoriaus vardą ir pavardę kaip stringus.
# Vardą atspausdinti tik didžiosiom raidėm, o pavardę tik mažosioms. (LEONARDO dicaprio)

name = "Will"
surname = "Smith"
x = name.upper()
y = surname.lower()

print(x,y)

print("============================ 3 uzduotis =======================")
# Sukurti du kintamuosius. Jiems priskirti savo mylimo aktoriaus vardą ir pavardę kaip stringus.
# Sukurti trečią kintamąjį ir jam priskirti stringą, sudarytą iš pirmų vardo ir pavardės kintamųjų reikšmių raidžių.
# Jį atspausdinti. (LD)

name = "Will"
surname = "Smith"
initials = name[0] + surname[0]
print(initials)

print("============================ 4 uzduotis =======================")
# Sukurti du kintamuosius. Jiems priskirti savo mylimo aktoriaus vardą ir pavardę kaip stringus.
# Sukurti trečią kintamąjį ir jam priskirti stringą, sudarytą iš trijų paskutinių vardo ir pavardės kintamųjų raidžių.
# Jį atspausdinti.

name = "Will"
surname = "Smith"
ns3 = name[-3:] + " " + surname[-3:]
print(ns3)

print("============================ 5 uzduotis =======================")
# Sukurti kintamąjį su stringu: "An American in Paris". Jame visas “a” (didžiąsias ir mažąsias) pakeisti žvaigždutėm “*”.
# Rezultatą atspausdinti.

tekstas = "An American in Paris"
tekstas = tekstas.replace("a", "*").replace("A", "*") #pakeiciame a, tada pakeistame tekse pakeiciame "A"

print(tekstas)

print("============================ 6 uzduotis =======================")
# Sukurti kintamąjį su stringu: "An American in Paris". Jame ištrinti visas balses.
# Rezultatą atspausdinti.
# Kodą pakartoti su stringais: "Breakfast at Tiffany's", "2001: A Space Odyssey" ir "It's a Wonderful Life".

tekstas1 = "An American in Paris"
tekstas2 = "Breakfast at Tiffany's"
tekstas3 ="2001: A Space Odyssey"
tekstas4 ="It's a Wonderful Life"
vowels ="a,e,i,o,u,A,E,I,O,U"

tekstas1 = tekstas1.translate(str.maketrans("","",vowels))
print(tekstas1)

tekstas2 = tekstas2.translate(str.maketrans("","",vowels))
print(tekstas2)

tekstas3 = tekstas3.translate(str.maketrans("","",vowels))
print(tekstas3)

tekstas4 = tekstas4.translate(str.maketrans("","",vowels))
print(tekstas4)

print("============================ 7 uzduotis =======================")
# Stringe, kurį generuoja toks kodas:
# starWars = "Star Wars: Episode " + (" " * random.randint(1, 9)) + str(random.randint(1, 7)) + " - A New Hope"
# Surasti ir atspausdinti epizodo numerį.


starWars = "Star Wars: Episode " + (" " * random.randint(1, 9)) + str(random.randint(1, 7)) + " - A New Hope"
splited = starWars.split()
episode = splited[3]

print("Epizodas:", episode)

print("============================ 8 uzduotis =======================")
# Sukurk stringą su žodžiu. Atspausdink „Sutampa“, jei pirmoji ir paskutinė raidė vienoda (naudok word[0] ir word[-1]), kitaip „Nesutampa“.
#
text = "Anakonda"

if text[0].lower() == text[-1].lower():
    print("Sutampa")
else:
    print("Nesutampa")

# galima ta pati su upper

print("============================ 9 uzduotis =======================")
# Sukurk kintamąjį su bet kokiu žodžiu.
# Atspausdink tą patį žodį, bet visos raidės išskyrus pirmą ir paskutinę turi būti pakeistos į _.
# Pvz. Python → P____n.

text2 = "Coding"
letters_to_replace = "Cg"

# text2 = text2.replace("C","_").replace("g","_")

for letter in letters_to_replace:
    text2 = text2.replace(letter, "_")
print(text2)

print("============================ 10 uzduotis =======================")
# Sukurk kintamąjį text = "Man 24 metai".
# Patikrink, ar stringe yra bent vienas skaitmuo (naudok in '0123456789' logiką be ciklų).
# Jei yra – išvesk „Yra skaičių“, jei ne – „Tik raidės“

text3 = "Man 24 metai"
skaiciai = "0,1,2,3,4,5,6,7,8,9"
if any(character in skaiciai for character in text3):
    print("Yra skaičių")
else:
    print("Tik raides")

print("============================ 11 uzduotis =======================")
# Suskaičiuoti kiek stringe “Don't Be a Menace to South Central While Drinking Your Juice in the Hood” yra žodžių trumpesnių arba lygių nei 5 raidės. Pakartokite kodą su stringu “Tik nereikia gąsdinti Pietų Centro, geriant sultis pas save kvartale”.

word = "Don't Be a Menace to South Central While Drinking Your Juice in the Hood"
word2 = "Tik nereikia gąsdinti Pietų Centro, geriant sultis pas save kvartale"
word = word.split()
word2 = word2.split()

word_count = 0
n = 5

for character in word2:
    if len(character) <= n:
        word_count += 1

print("Tekste yra", word_count, "žodžių trumpesnių arba lygių nei 5 raidės")

print("============================ 12 uzduotis =======================")
# Parašyti kodą, kuris generuotų atsitiktinį stringą iš lotyniškų mažųjų raidžių. Stringo ilgis 3 simboliai.





print("============================ 13 uzduotis =======================")
# Parašykite kodą, kuris generuotų atsitiktinį stringą su 10 atsitiktine tvarka išdėliotų žodžių, o žodžius generavimui imtų iš 11-me uždavinyje pateiktų dviejų stringų. Žodžiai neturi kartotis. (reikės masyvo)











