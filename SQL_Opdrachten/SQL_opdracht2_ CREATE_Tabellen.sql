CREATE TABLE PERSON (
    ID INT PRIMARY KEY,                  -- Unieke ID voor de persoon (Kan niet NULL zijn)
    Code				 -- Personelservicenummer (Uniek), kan geen NULL zijn
    TCNumber VARCHAR(11) UNIQUE,         -- Burgerlijke ID nummer (Uniek), kan geen NULL zijn
    Name VARCHAR(50) NOT NULL,           -- Voornaam van de persoon, kan niet NULL zijn
    Surname VARCHAR(50) NOT NULL,        -- Achternaam van de persoon, kan niet NULL zijn
    Gender CHAR(1) NULL,                 -- Geslacht ('E' voor man, 'K' voor vrouw), kan NULL zijn
    BirthDate DATE NULL,                 -- Geboortedatum van de persoon, kan NULL zijn
    InDate DATE NOT NULL,              -- Datum waarop de persoon in dienst is gekomen, kan niet NULL zijn
    OutDate DATE NULL,                   -- Datum van uitdiensttreding, kan NULL zijn (als de persoon nog in dienst is)
    DepartmentID INT NULL,               -- Departement ID, kan NULL zijn (als de persoon geen afdeling heeft)
    PositionID INT NULL,                 -- Positie ID, kan NULL zijn (als de persoon geen functie heeft)
    ParentPositionID INT NULL,           -- Bovenliggende positie ID, kan NULL zijn (als er geen hogere functie is)
    ManagerID INT NULL,                  -- Manager ID, kan NULL zijn (als de persoon geen manager heeft)
    Telnr VARCHAR(15) NULL,              -- Telefoonnummer van de persoon, kan NULL zijn
    Salary DECIMAL(18, 2) NULL,          -- Salaris van de persoon, kan NULL zijn
    
    CONSTRAINT FK_Department FOREIGN KEY (DepartmentID) REFERENCES DEPARTMENT(DepartmentID), -- Verwijzing naar het Departement
    CONSTRAINT FK_Position FOREIGN KEY (PositionID) REFERENCES POSITION(PositionID)  -- Verwijzing naar de Positie
);

CREATE TABLE POSITION (
    PositionID INT IDENTITY(1,1) PRIMARY KEY,  -- Unieke ID voor de positie, wordt automatisch gegenereerd voor elke rij.
    PositionName NVARCHAR(50) NOT NULL         -- Naam van de positie, kan niet NULL zijn.
);

CREATE TABLE DEPARTMENT (
    DepartmentID INT IDENTITY(1,1) PRIMARY KEY,  -- Unieke ID voor het departement, wordt automatisch gegenereerd voor elke rij.
    DepartmentName NVARCHAR(50) NOT NULL         -- Naam van het departement, kan niet NULL zijn.
);

