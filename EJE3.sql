CREATE OR REPLACE PROCEDURE TOP_TRES_PRECIO
IS
    TOP_P1 NUMBER;TOP_P2 NUMBER;TOP_P3 NUMBER;
    CURSOR C_PRODUCTOS IS SELECT * FROM PRODUCTO;
    FILA PRODUCTO%ROWTYPE;
BEGIN
    SELECT MAX(PRECIO)INTO TOP_P1 FROM PRODUCTO;
    SELECT MAX(PRECIO)INTO TOP_P1 FROM PRODUCTO WHERE PRECIO != TOP_P1;
    SELECT MAX(PRECIO)INTO TOP_P1 FROM PRODUCTO WHERE PRECIO != TOP_P1 AND PRECIO != TOP_P2;
    
    OPEN C_PRODUCTOS;
    LOOP
        FETCH C_PRODUCTOS INTO FILA;
        IF (FILA.PRECIO IN(TOP_P1,TOP_P2,TOP_P3)) THEN
            DBMS_OUTPUT.PUT_LINE(FILA.CODIGO||' '||FILA.NOMBRE||' '||FILA.PRECIO||' '||FILA.COD_FABRICANTE);
        END IF;
        EXIT WHEN C_PRODUCTOS%NOTFOUND;
    END LOOP;
    CLOSE C_PRODUCTOS;
END;