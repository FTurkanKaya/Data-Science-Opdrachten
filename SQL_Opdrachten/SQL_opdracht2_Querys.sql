--1 Alle medewerkers hun naam, achternaam en salaris ophalen
select Name_ , SURNAME, SALARY from PERSON

--2 Alleen vrouwelijke medewerkers (GENDER = 'K') naam, achternaam en geboortedatum ophalen
select Name_ , SURNAME, BIRTHDATE from PERSON
where  GENDER = 'K'

--3 Medewerkers die na 2017 zijn aangenomen, hun naam en in dienst datum ophalen
select concat(Name_ ,SURNAME) as 'NAME AND SURNAME', BIRTHDATE from PERSON
WHERE YEAR(INDATE) > 2017;

--4 Voeg een nieuwe medewerker toe (bijvoorbeeld: Ali Veli, TC No: 12345678901, Man, Geboortedatum: 1985-12-05, In dienst: 2022-01-15, Afdeling: 3, Positie: 40, Salaris: 6000)
INSERT INTO PERSON (CODE, TCNUMBER, NAME_, SURNAME, Gender, BirthDate, INDATE, OUTDATE, DepartmentID, PositionID, PARENTPOSITIONID, MANAGERID, TELNR, Salary)
VALUES (1781, '12345678901', 'Ali', 'Veli', 'E', '1985-12-05', '2022-01-15', NULL, 3, 40, NULL, NULL, NULL, 6000);

select * from person
where code = 1781


--5 Werk het salaris van Ferhat Cinar bij naar 6000
update person
set salary =6000
where name_ = 'Ferhat' and SURNAME = 'Cinar'

select NAME_, SURNAME, SALARY from person
where NAME_= 'FERHAT' and SURNAME= 'CINAR'


--6 Verwijder Deniz Eravcı uit de database
delete from person
where name_ = 'Deniz' and SURNAME = 'Eravci'

select NAME_, SURNAME, SALARY from person
where NAME_= 'Deniz' and SURNAME= 'ERAVCI'


--7 Medewerkers die voor 1960 zijn geboren, ophalen
select NAME_, SURNAME, SALARY from person
where year(BIRTHDATE) < 1960

--8  Medewerkers die voor 1960 zijn geboren en een salaris hoger dan 5000 hebben, ophalen
select NAME_, SURNAME, BIRTHDATE, SALARY from person
where year(BIRTHDATE) < 1960 and salary < 5000

--9 Medewerkers met een DepartmentID van 4 of een salaris van meer dan 5500, ophalen
select NAME_, SURNAME, BIRTHDATE, SALARY from person
where DEPARTMENTID = 4 and salary > 5500

--10 Medewerkers met een NULL exit datum (OUTDATE), een salarisverhoging van 10% geven
update person
set salary = salary * 1.10
where OUTDATE IS NULL

--11 Medewerkers die vóór 2015 zijn aangenomen en een salaris lager dan 5000 hebben, verwijderen 
delete from person
where year(indate) < 2015 and salary < 5000

--12 Het aantal verschillende afdelingen in de dataset ophalen
select count(distinct Departmentid) as 'Het aantal van Afdelingen' from PERSON

select distinct DepartmentName from DEPARTMENT

--13 Medewerkers sorteren op salaris van hoog naar laag
select NAME_, SURNAME, BIRTHDATE, SALARY from person
order by salary desc

--14 De 5 medewerkers met het hoogste salaris ophalen
select top 5 NAME_, SURNAME, BIRTHDATE, SALARY from person
order by salary desc