CREATE TABLE asignacion (
    cod_proyecto NUMBER NOT NULL,
    id_empleado  NUMBER NOT NULL,
    num_tarea    NUMBER NOT NULL,
    costo        NUMBER NOT NULL
);

ALTER TABLE asignacion
    ADD CONSTRAINT asignacion_pk PRIMARY KEY ( cod_proyecto,
                                               num_tarea,
                                               id_empleado );

CREATE TABLE empleado (
    identificador    NUMBER NOT NULL,
    apellido_paterno VARCHAR2(50) NOT NULL,
    apellido_materno VARCHAR2(50) NOT NULL,
    nombre           VARCHAR2(70) NOT NULL,
    fecha_nacimiento DATE NOT NULL
);

ALTER TABLE empleado ADD CONSTRAINT empleado_pk PRIMARY KEY ( identificador );

CREATE TABLE proyecto (
    codigo       NUMBER NOT NULL,
    nombre       VARCHAR2(70) NOT NULL,
    fecha_inicio DATE NOT NULL,
    fecha_fin    DATE NOT NULL,
    presupuesto  NUMBER NOT NULL
);

ALTER TABLE proyecto ADD CONSTRAINT proyecto_pk PRIMARY KEY ( codigo );

CREATE TABLE tarea (
    numero         NUMBER NOT NULL,
    nombre         VARCHAR2(70) NOT NULL,
    duracion_horas NUMBER NOT NULL
);

ALTER TABLE tarea ADD CONSTRAINT tarea_pk PRIMARY KEY ( numero );

ALTER TABLE asignacion
    ADD CONSTRAINT asignacion_empleado_fk FOREIGN KEY ( id_empleado )
        REFERENCES empleado ( identificador );

ALTER TABLE asignacion
    ADD CONSTRAINT asignacion_proyecto_fk FOREIGN KEY ( cod_proyecto )
        REFERENCES proyecto ( codigo );

ALTER TABLE asignacion
    ADD CONSTRAINT asignacion_tarea_fk FOREIGN KEY ( num_tarea )
        REFERENCES tarea ( numero );

INSERT INTO EMPLEADO VALUES (1,'VARGAS','HERNANDEZ','FRANCISCO','12-03-1998');
INSERT INTO EMPLEADO VALUES (2,'FAUNDEZ','VERGARA','HERNAN','16-08-1995');
INSERT INTO EMPLEADO VALUES (3,'MONSALVE','HERRERA','ANDRES','22-05-1984');
INSERT INTO EMPLEADO VALUES (4,'PEREZ','MONARTE','MAURICIO','02-01-1975');
INSERT INTO EMPLEADO VALUES (5,'MARTINEZ','FERRADA','HECTOR','23-08-2000');

INSERT INTO TAREA VALUES (1,'PROGRAMACION',800);
INSERT INTO TAREA VALUES (2,'DISE�O',350);
INSERT INTO TAREA VALUES (3,'PLANIFICACION',600);
INSERT INTO TAREA VALUES (4,'TESTEO',400);
INSERT INTO TAREA VALUES (5,'PUBLICIDAD',300);

INSERT INTO PROYECTO VALUES (1,'PAGINA WEB','18-06-2021','20-10-2021',2500000);
INSERT INTO PROYECTO VALUES (2,'BASE DE DATOS','13-02-2022','18-02-2023',5000000);
INSERT INTO PROYECTO VALUES (3,'SISTEMA WEB','14-04-2022','16-03-2024',10000000);
INSERT INTO PROYECTO VALUES (4,'SISTEMA DE GESTION','16-03-2023','26-05-2024',9500000);
INSERT INTO PROYECTO VALUES (5,'LIBRERIA DIGITAL','01-02-2021','01-03-2023',14000000);

INSERT INTO ASIGNACION VALUES (1,3,5,650000);
INSERT INTO ASIGNACION VALUES (1,2,3,700000);
INSERT INTO ASIGNACION VALUES (2,1,1,1200000);
INSERT INTO ASIGNACION VALUES (3,2,5,800000);
INSERT INTO ASIGNACION VALUES (4,2,2,850000);

SELECT * FROM PROYECTO
WHERE PRESUPUESTO BETWEEN 2000000 AND 5000000; --A

SELECT * FROM EMPLEADO
WHERE APELLIDO_PATERNO = APELLIDO_MATERNO; --B

SELECT NOMBRE,DURACION_HORAS FROM TAREA
WHERE NOMBRE LIKE '%DISE�O%'; --C

UPDATE TAREA
SET DURACION_HORAS = DURACION_HORAS+5; --D

SELECT AVG(PRESUPUESTO)FROM PROYECTO
WHERE FECHA_INICIO BETWEEN '01-01-2023' AND '31-12-2023'; --E

SELECT COUNT(ID_EMPLEADO) FROM ASIGNACION
WHERE COD_PROYECTO IN(1,2,3); --F
