-- Voeg een Foreign Key toe aan de 'DepartmentID' kolom van de 'DEPARTMENT' tabelALTER TABLE PERSON
ALTER TABLE PERSON
ADD CONSTRAINT FK_Department
FOREIGN KEY (DEPARTMENTID) REFERENCES DEPARTMENT(DepartmentID);

-- Voeg een Foreign Key toe aan de 'PositionID' kolom van de 'POSITION' tabel
ALTER TABLE PERSON
ADD CONSTRAINT FK_Position
FOREIGN KEY (POSITIONID) REFERENCES POSITION(PositionID);


