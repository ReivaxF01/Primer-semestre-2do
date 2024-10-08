CREATE TABLE TRABAJADORES(
RUT VARCHAR(12),
FECHA_CONTRATO VARCHAR(8),
FECHA_FINIQUITO VARCHAR(8),
SUELDO NUMBER,
CONSTRAINT TRABAJADORES_PK PRIMARY KEY(RUT)); 

CREATE TABLE ALUMNOS(
RUT VARCHAR(12),
ALUMNO VARCHAR(50) NOT NULL,
NOTA NUMBER,
CONSTRAINT ALUMNOS_PK PRIMARY KEY(RUT)); 

CREATE TABLE PRUEBA(
RUT VARCHAR(12),
NUMERO_CORRECTAS NUMBER,
NUMERO_INCORRECTAS NUMBER,
TIPO CHAR,
CONSTRAINT PRUEBA_PK PRIMARY KEY(RUT)); 
/*EJERCICIO 1*/
/*A_*/
SELECT * FROM ALUMNOS
ORDER BY LENGTH(ALUMNO);
/*B_*/
SELECT SUBSTR(ALUMNO,1,INSTR(ALUMNO,',',1)-1)AS APELLIDOS,
SUBSTR(ALUMNO,-INSTR(REVERSE(ALUMNO),',',1)+2)AS NOMBRES 
FROM ALUMNOS;
/*C_*/
SELECT UPPER(SUBSTR(ALUMNO,1,INSTR(ALUMNO,',',1)-1))AS APELLIDOS,
LOWER(SUBSTR(ALUMNO,-INSTR(REVERSE(ALUMNO),',',1)+2))AS NOMBRES
FROM ALUMNOS;
/*D_*/
SELECT RUT,REPLACE(RUT,SUBSTR(RUT,1,5),'*****')AS RUT_SECRETO FROM ALUMNOS;
/*E_*/
SELECT COUNT(*) TOTAL_NOTAS_PALINDROMAS FROM ALUMNOS
WHERE TO_CHAR(NOTA) = REVERSE(TO_CHAR(NOTA));
/*EJERCICIO 2*/
/*A_*/
SELECT COUNT(*) FROM TRABAJADORES
WHERE FECHA_FINIQUITO IS NOT NULL AND
MONTHS_BETWEEN(TO_DATE(FECHA_FINIQUITO),TO_DATE(FECHA_CONTRATO))/12 >10;

/* EJERCICIO 3*/
/*A_*/
SELECT RUT,NUMERO_CORRECTAS,
CASE
    WHEN (NUMERO_CORRECTAS /30) >= 0.6 THEN ROUND((NUMERO_CORRECTAS/30)*7.5-0.5,1)
    ELSE ROUND((NUMERO_CORRECTAS/30)*5+1,1)
END NOTA
FROM PRUEBA;
/*B_*/
SELECT RUT,NUMERO_CORRECTAS,
NUMERO_CORRECTAS*2-(TRUNC(NUMERO_INCORRECTAS/3))PUNTAJE,
CASE
    WHEN (NUMERO_CORRECTAS*2-(TRUNC(NUMERO_INCORRECTAS/3)))/60 >= 0.6 THEN
    ROUND((NUMERO_CORRECTAS*2-(TRUNC(NUMERO_INCORRECTAS/3)))/60*7.5-0.5,1)
    ELSE
    ROUND((NUMERO_CORRECTAS*2-(TRUNC(NUMERO_INCORRECTAS/3)))/60*5+1,1)
END NOTA
FROM PRUEBA;
/*C_*/
SELECT *
FROM
(SELECT RUT,NUMERO_CORRECTAS,
3*NUMERO_CORRECTAS PUNTAJE,
CASE
    WHEN (3*NUMERO_CORRECTAS/90) >= 0.6 THEN ROUND((3*NUMERO_CORRECTAS/90)*7.5-0.5,1)
    ELSE ROUND((3*NUMERO_CORRECTAS/90)*5+1,1)
END NOTA
FROM PRUEBA) TABLA
WHERE TABLA.NOTA BETWEEN 3.5 AND 3.9;