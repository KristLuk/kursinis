Ataskaita apie Kursinį Darbą
Įžanga

Šis projektas yra romėniškų skaičių konverteris, kuris leidžia konvertuoti skaičius tarp dešimtainės (1–3999) ir romėniškos (I, V, X ir t. t.) sistemų. Jis apima šias funkcijas:
• Dvikryptė konversija (romėniški ↔ dešimtainiai skaičiai)
• Konversijų istorijos sekimas
• Failų išsaugojimas / įkėlimas (CSV ir TXT formatais)
Aš pats vykdžiau programą naudodamasis Visual Studio Code. Tam pirmiausia reikia įsidiegti Python plėtinį. Įdiegus, atidarykite failą (Roman_Numeral_Converter.py) ir paleiskite programą terminale.
Norint teisingai naudoti programą, pirmiausia pasirinkite konversijos tipą: iš romėniškų į dešimtainius ar iš dešimtainių į romėniškus skaičius. Tuomet įveskite skaičių arba romėnišką simbolį, kurį norite konvertuoti.
Analysis
Abstraction
•	Sukurtas bazinis NumeralConverter klasės objektas, apibrėžiantis standartinį konvertavimo metodą, kurį naudoja visi konverteriai.
Inheritance
Dvi konverterio klasės paveldi bazinę klasę:
•	 RomanToDecimalConverter (tvarko "IV" → 4)
DecimalToRomanConverter (tvarko 4 → "IV")
Polymorphism
•	Abi kryptys naudoja tą patį convert() metodą (romėniški ↔ dešimtainiai skaičiai).
Encapsulation
•	Konversijų istorija saugoma apsaugotame sąraše (_history), su prieiga per specialius metodus.
Singleton Pattern
•	Vienas globalus fabrikas (ConverterFactory) valdo visus konverterius, kad būtų išvengta pasikartojimų.
File Operations
•	Programa leidžia išsaugoti ir įkelti konversijų istoriją CSV (struktūrizuotas) ir TXT (žmogui suprantamas) formatais.
Results
•	Didžiausias iššūkis buvo iš naujo išmokti visas objektinio programavimo koncepcijas ir jas efektyviai pritaikyti.
•	Kita problema – logikos kūrimas, kaip turėtų veikti konverteriai.
•	Galiausiai, buvo sudėtinga pasirinkti ir pritaikyti tinkamą projektavimo šabloną šiam projektui.
