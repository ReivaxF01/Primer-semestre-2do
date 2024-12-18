REATE OR REPLACE FUNCTION PASSWORD_VALIDA(CONT VARCHAR2)
RETURN BOOLEAN
IS
    RESULTADO BOOLEAN := TRUE; -- Asumimos que es v�lida hasta que se demuestre lo contrario
    CURSOR CAR_NA IS SELECT CARACTER FROM DICCIONARIO; -- Suponiendo que la tabla tiene una columna llamada 'CARACTER'
    CHAR_IN_DICCIONARIO BOOLEAN;
    HAS_UPPERCASE BOOLEAN := FALSE; -- Para verificar si hay al menos una may�scula
    HAS_NUMBER BOOLEAN := FALSE; -- Para verificar si hay al menos un n�mero
BEGIN
    -- Verificamos que la longitud de la contrase�a sea al menos 8 caracteres
    IF LENGTH(CONT) < 8 THEN
        RETURN FALSE;
    END IF;

    -- Iteramos sobre cada car�cter de la contrase�a
    FOR i IN 1..LENGTH(CONT) LOOP
        CHAR_IN_DICCIONARIO := FALSE; -- Reiniciamos la variable para cada car�cter

        -- Comprobamos si hay al menos una may�scula y un n�mero
        IF SUBSTR(CONT, i, 1) BETWEEN 'A' AND 'Z' THEN
            HAS_UPPERCASE := TRUE;
        ELSIF SUBSTR(CONT, i, 1) BETWEEN '0' AND '9' THEN
            HAS_NUMBER := TRUE;
        END IF;

        -- Comparamos el car�cter actual de la contrase�a con los caracteres en el diccionario
        FOR CAR IN CAR_NA LOOP
            IF SUBSTR(CONT, i, 1) = CAR.CARACTER THEN
                CHAR_IN_DICCIONARIO := TRUE; -- Encontramos el car�cter en el diccionario
                EXIT; -- Salimos del bucle ya que no necesitamos seguir buscando
            END IF;
        END LOOP;

        -- Si el car�cter no est� en el diccionario, la contrase�a no es v�lida
        IF NOT CHAR_IN_DICCIONARIO THEN
            RESULTADO := FALSE;
            EXIT; -- Salimos del bucle ya que ya sabemos que la contrase�a no es v�lida
        END IF;
    END LOOP;

    -- Verificamos si se encontraron al menos una may�scula y un n�mero
    IF NOT HAS_UPPERCASE OR NOT HAS_NUMBER THEN
        RESULTADO := FALSE;
    END IF;

    RETURN RESULTADO; -- Retornamos el resultado de la validaci�n
END PASSWORD_VALIDA