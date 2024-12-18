REATE OR REPLACE FUNCTION PASSWORD_VALIDA(CONT VARCHAR2)
RETURN BOOLEAN
IS
    RESULTADO BOOLEAN := TRUE; -- Asumimos que es válida hasta que se demuestre lo contrario
    CURSOR CAR_NA IS SELECT CARACTER FROM DICCIONARIO; -- Suponiendo que la tabla tiene una columna llamada 'CARACTER'
    CHAR_IN_DICCIONARIO BOOLEAN;
    HAS_UPPERCASE BOOLEAN := FALSE; -- Para verificar si hay al menos una mayúscula
    HAS_NUMBER BOOLEAN := FALSE; -- Para verificar si hay al menos un número
BEGIN
    -- Verificamos que la longitud de la contraseña sea al menos 8 caracteres
    IF LENGTH(CONT) < 8 THEN
        RETURN FALSE;
    END IF;

    -- Iteramos sobre cada carácter de la contraseña
    FOR i IN 1..LENGTH(CONT) LOOP
        CHAR_IN_DICCIONARIO := FALSE; -- Reiniciamos la variable para cada carácter

        -- Comprobamos si hay al menos una mayúscula y un número
        IF SUBSTR(CONT, i, 1) BETWEEN 'A' AND 'Z' THEN
            HAS_UPPERCASE := TRUE;
        ELSIF SUBSTR(CONT, i, 1) BETWEEN '0' AND '9' THEN
            HAS_NUMBER := TRUE;
        END IF;

        -- Comparamos el carácter actual de la contraseña con los caracteres en el diccionario
        FOR CAR IN CAR_NA LOOP
            IF SUBSTR(CONT, i, 1) = CAR.CARACTER THEN
                CHAR_IN_DICCIONARIO := TRUE; -- Encontramos el carácter en el diccionario
                EXIT; -- Salimos del bucle ya que no necesitamos seguir buscando
            END IF;
        END LOOP;

        -- Si el carácter no está en el diccionario, la contraseña no es válida
        IF NOT CHAR_IN_DICCIONARIO THEN
            RESULTADO := FALSE;
            EXIT; -- Salimos del bucle ya que ya sabemos que la contraseña no es válida
        END IF;
    END LOOP;

    -- Verificamos si se encontraron al menos una mayúscula y un número
    IF NOT HAS_UPPERCASE OR NOT HAS_NUMBER THEN
        RESULTADO := FALSE;
    END IF;

    RETURN RESULTADO; -- Retornamos el resultado de la validación
END PASSWORD_VALIDA