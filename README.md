#SQL OPDRACHTEN

# SQL Queries en Resultaten

Deze repository bevat een verzameling van SQL-query's en hun bijbehorende resultaat schermafbeeldingen.


### Uitleg van de Commands:
- **SELECT**: Wordt gebruikt om gegevens op te halen uit de database.
- **INSERT INTO**: Wordt gebruikt om nieuwe gegevens in een tabel toe te voegen.
- **UPDATE**: Wordt gebruikt om bestaande gegevens in een tabel bij te werken.
- **DELETE**: Verwijdert gegevens uit een tabel.
- **WHERE**: Wordt gebruikt om een voorwaarde toe te passen bij het ophalen of bijwerken van gegevens.
- **COUNT(DISTINCT)**: Telt het aantal unieke waarden.
- **TOP**: Beperkt het aantal geretourneerde records.

Met deze uitleg en SQL-query's zou je goed voorbereid moeten zijn om de gewenste gegevens op te halen, in te voegen, bij te werken of te verwijderen.

## Algemeen Overzicht van de Resultaten

In deze repository zijn de resultaten van de SQL-opdrachten weergegeven, inclusief de bijbehorende schermopnames voor elke vraag. 
Elke vraag bevat een SQL-query die is uitgevoerd in een SQL Server Management Studio (SSMS)-omgeving, en de resulterende gegevens 
of de verwachte uitkomsten worden gedocumenteerd via de schermopname.

Elke afbeelding toont de resultaten van de specifieke query en biedt een visueel overzicht van de uitvoering van de SQL-opdracht. 
Dit maakt het makkelijker om te begrijpen hoe de query's werken, wat de verwachte resultaten zijn, en hoe deze resultaten kunnen worden geanalyseerd voor verdere inzichten.

Klik op de links om de resultaten van de individuele vragen te bekijken en te begrijpen hoe de SQL-query's zijn uitgevoerd en de gegevens zijn opgehaald.

---

**Let op:** De query's kunnen afwijken afhankelijk van de specifieke gegevens en de SQL Server-configuratie. 
De screenshots bieden echter een betrouwbare weergave van hoe de query's in de opgegeven omgeving zouden moeten functioneren.

* Het diagram van de Tabellen bij SSMS
  ![sql_Opdracht2_Diagram Screenshot](https://github.com/FTurkanKaya/Data-Science-Opdrachten/blob/main/SQL_Opdrachten/sql_Opdracht2_Resultaten_Screenshots/Tabellen_Diagraam.png)





- Vraag1: Alle medewerkers
* ![sql_Opdracht2_Vraag1 Screenshot](https://github.com/FTurkanKaya/Data-Science-Opdrachten/blob/main/SQL_Opdrachten/sql_Opdracht2_Resultaten_Screenshots/sql_Opdracht2_Vraag1.png)
Deze query haalt de gegevens van alle medewerkers uit de PERSON tabel.
Het resultaat bevat de basisinformatie van de medewerkers, inclusief hun salarissen.


- Vraag2: Alle vrouwelijke medewerkers opvragen:
* ![sql_Opdracht2_Vraag2 Screenshot](https://github.com/FTurkanKaya/Data-Science-Opdrachten/blob/main/SQL_Opdrachten/sql_Opdracht2_Resultaten_Screenshots/sql_Opdracht2_Vraag2.png) 
Deze query haalt alleen de naam, achternaam en geboortedatum op van medewerkers wiens geslacht gelijk is aan 'K' (vrouwelijk).
Het WHERE-gedeelte zorgt ervoor dat alleen vrouwelijke medewerkers worden geselecteerd.


- Vraag3: Medewerkers die na 2017 zijn begonnen:
* ![sql_Opdracht2_Vraag3 Screenshot](https://github.com/FTurkanKaya/Data-Science-Opdrachten/blob/main/SQL_Opdrachten/sql_Opdracht2_Resultaten_Screenshots/sql_Opdracht2_Vraag3.png) 
Deze query haalt de naam en de datum van indiensttreding van medewerkers op die na het jaar 2017 zijn begonnen.
De YEAR(HireDate) > 2017 conditie filtert medewerkers die na 2017 zijn aangenomen.


- Vraag4: Een nieuwe medewerker toevoegen:
* ![sql_Opdracht2_Vraag4 Screenshot](https://github.com/FTurkanKaya/Data-Science-Opdrachten/blob/main/SQL_Opdrachten/sql_Opdracht2_Resultaten_Screenshots/sql_Opdracht2_Vraag4.png) 
Deze query voegt een nieuwe medewerker toe met de naam 'Ali Veli'. De medewerker heeft een geboortedatum van 1985-12-05 en is op 2022-01-15 in dienst gekomen.
Het salaris is ingesteld op 6000 en de afdeling en positie zijn respectievelijk 3 en 40.


- Vraag5: Ferhat Cinar's salaris bijwerken naar 6000:
* ![sql_Opdracht2_Vraag5 Screenshot](https://github.com/FTurkanKaya/Data-Science-Opdrachten/blob/main/SQL_Opdrachten/sql_Opdracht2_Resultaten_Screenshots/sql_Opdracht2_Vraag5.png)
Deze query werkt het salaris van de medewerker 'Ferhat Cinar' bij naar 6000.
De WHERE-clausule zorgt ervoor dat alleen de medewerker 'Ferhat Cinar' wordt bijgewerkt.


- Vraag7: Medewerkers die voor 1960 geboren zijn:
* ![sql_Opdracht2_Vraag7 Screenshot](https://github.com/FTurkanKaya/Data-Science-Opdrachten/blob/main/SQL_Opdrachten/sql_Opdracht2_Resultaten_Screenshots/sql_Opdracht2_Vraag7.png) 
Deze query haalt de naam, achternaam en geboortedatum op van medewerkers die vóór 1960 zijn geboren.


- Vraag8: Medewerkers die voor 1960 geboren zijn en een salaris van meer dan 5000 hebben:
* ![sql_Opdracht2_Vraag8 Screenshot](https://github.com/FTurkanKaya/Data-Science-Opdrachten/blob/main/SQL_Opdrachten/sql_Opdracht2_Resultaten_Screenshots/sql_Opdracht2_Vraag8.png)
Deze query haalt de naam, achternaam, geboortedatum en salaris op van medewerkers die vóór 1960 zijn geboren en een salaris hebben van meer dan 5000.


- Vraag9: Medewerkers met DepartementID 4 of een salaris van meer dan 5500:
* ![sql_Opdracht2_Vraag9 Screenshot](https://github.com/FTurkanKaya/Data-Science-Opdrachten/blob/main/SQL_Opdrachten/sql_Opdracht2_Resultaten_Screenshots/sql_Opdracht2_Vraag9.png)
Deze query haalt de naam, achternaam, afdeling-ID en salaris op van medewerkers die in afdeling 4 werken of een salaris van meer dan 5500 verdienen.



- Vraag12: Aantal verschillende departementen in de dataset:
* ![sql_Opdracht2_Vraag12 Screenshot](https://github.com/FTurkanKaya/Data-Science-Opdrachten/blob/main/SQL_Opdrachten/sql_Opdracht2_Resultaten_Screenshots/sql_Opdracht2_Vraag12_1.png) 
Deze query telt het aantal verschillende afdelingen waartoe medewerkers behoren.
Het DISTINCT-sleutelwoord zorgt ervoor dat dubbele afdelingen niet geteld worden.


  De andere optie: De namen van de verschillende departementen in de dataset:
  ![sql_Opdracht2_Vraag12 Screenshot](https://github.com/FTurkanKaya/Data-Science-Opdrachten/blob/main/SQL_Opdrachten/sql_Opdracht2_Resultaten_Screenshots/sql_Opdracht2_Vraag12_2.png)



- Vraag13: Medewerkers gesorteerd op salaris, van hoog naar laag:
* ![sql_Opdracht2_Vraag13 Screenshot](https://github.com/FTurkanKaya/Data-Science-Opdrachten/blob/main/SQL_Opdrachten/sql_Opdracht2_Resultaten_Screenshots/sql_Opdracht2_Vraag13.png)
Deze query sorteert de medewerkers op hun salaris van hoog naar laag.


- Vraag14: Top 5 medewerkers met het hoogste salaris:
* ![sql_Opdracht2_Vraag14 Screenshot](https://github.com/FTurkanKaya/Data-Science-Opdrachten/blob/main/SQL_Opdrachten/sql_Opdracht2_Resultaten_Screenshots/sql_Opdracht2_Vraag14.png)
 Deze query haalt de top 5 medewerkers op met de hoogste salarissen.










  
