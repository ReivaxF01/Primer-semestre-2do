# Comandos MongoDB:
## **use 'nombre de la base de datos' (sin comillas)**:
sirve para cambiar entre bases de datos. _**NOTA**: la base de datos no se creará hasta que tenga al menos una colección_
## **show dbs o show databases**: 
se usa para mostrar las bases de datos existentes
## **db.createCollection('nombre de la colección')**:
se usa para crear colecciones dentro de una base de datos
## **db.NombreBaseDeDatos.renameCollection('Nombre de la colección')**: 
se usa para editar el nombre de una colección
## **db.NombreColección.drop()**: 
se usa para eliminar una colección
## **db.NombreColección.insertOne({acá se añaden los datos que se quieran agregar a la colección siguiendo el formato JSON})**:
se usa opara insertar documentos dentro de una colección
## **db.NombreColección.find()**: 
se usa para ver los documentos (o articulos) dentro de la colección
## **db.NombreColección.insertMany([{dato1},{dato2},{datoN}])**:
se usa para añadir varios documentos dentro de una colección de una sola vez
## **db.NombreColección.updateOne({un dato dentro del archivo que permita identificar el producto},{$set{acá va el campo y el nuevo valor}})**:
permite actualizar los datos de un documento
## **db.NombreColección.updateMany({},{$set{acá va el campo y el nuevo valor}})**:
se usa para actualizar varios documentos a la vez. _**NOTA**: si los primeros parentesis están vacíos se aplican los cambios a toda la colección_
## **db.NombreColección.updateMany({},{$unset{acá va el campo que se quiera eliminar}})**:
se usa para eliminar un campo dentro de un documento.  _**NOTA**: si los primeros parentesis están vacíos se aplican los cambios a toda la colección_
## **db.NombreColección.updateMany({},{$rename{'nombre antiguo del campo':'nombre nuevo del campo'}})**: 
se usa para renombrar un campo dentro de un documento.  _**NOTA**: si los primeros parentesis están vacíos se aplican los cambios a toda la colección_
## **db.NombreColección.deleteOne({campo:'valor del campo'})**:
se usa para eliminar un documento dentro de una coleccion
## **db.NombreColección.deleteMany({campo:'valor del campo'})**:
se usa para eliminar varios documentos dentro de una coleccion
## **db.NombreColección.deleteOne({})**: 
se usa para eliminar todos los documentos dentro de una coleccion. _**NOTA**: la colección sigue existiendo, pero sin archivos dentro de ella._
## **db.NombreColección.find().count()** o **db.NombreColleción.find().size()**:
se usa para contar los documentos dentro de una colección

# Operaciones Numéricas
## **db.NombreColección.find({campo:{$gt:{valor}})**:
se usa para buscar "algo mayor que" respecto al campo que le indicamos.
## **db.NombreColección.find({campo:{$lt:{valor}})**:
se usa para buscar "algo menor que" respecto al campo que le indicamos.
## **db.NombreColección.find({campo:{$eq:{valor}})**:
se usa para buscar "algo igual que" respecto al campo que le indicamos.
## **db.NombreColección.find({campo:{$ne:{valor}})**:
se usa para buscar "algo no igual que" respecto al campo que le indicamos. 
## **db.NombreColección.find({campo:{$gte:{valor}})**:
se usa para buscar "algo mayor o igual que" respecto al campo que le indicamos. 
## **db.NombreColección.find({campo:{$lte:{valor}})**:
se usa para buscar "algo menor o igual que" respecto al campo que le indicamos. 
## **para memorizarlo mejor**: 
gt (Greater Than, mayor que), lt (Less Than, Menor que), eq (equal, igual que), ne (not equal, distinto que), gte (Greater Than Equal, mayor o igual que). lte (Less Than Equal, menor o igual que)

# Operaciones con Texto
## **db.NombreColección.find({campo:/texto, sin comillas/})**:
se usa para buscar cadenas de texto dentro de la colección
## **db.NombreColección.find({campo:/^Caracter con el que empieza el valor/})**:
se usa para indicar que busque un valor por la letra inicial en el campo que se le indica, **ejemplo**: si tenemos el campo 'texto' con valor 'Hola',también con valor 'Adiós' y con valor 'Hello' (texto:'Hola', texto:'Hello',texto:'Adiós'), y queremos que solo arroje los documemtos cuyo valor indicado inicie con H, se usaría este comando de esta forma: **db.NombreColección.find({campo:/^H/})**
## db.NombreColección.find({campo:/caracter con el que termina el valor$/}):
se usa para indicar que busque un valor por la letra final en el campo que se le indica, **ejemplo**: siguiendo con el ejemplo anterior, supongamos que añadimos 'términos' al campo 'texto'(texto:'Adiós',texto:'términos'), para que nos muestre ambos documentos usariamos el comando de la siguiente manera: **db.NombreColección.find({campo:/s$/})**

# Operadores Lógicos 
## db.NombreColección.find({campo:{$in[valor1,valor2,valor3,etc.]}}):
se usa como operador "y". busca cualquier valor indicado después del operador $in dentro del campo que se le indica. $in proviene de "include"
## db.NombreColección.find({campo:{$nin[valor1,valor2,valor3,etc.]}}):
hace lo contrario al operador anterior. ignora cualquier valor asignado después del operador $nin. $nin proviene de "not include"
## db.NombreColección.find({campo1:valor1},{campo2:valor2}):
también se usa como un operador "y". acá busca documentos que cumplan con los 2 valores indicados. **_NOTA_**: también se pueden aplicar operaciones númericas dentro de los campos, quedando algo así: **db.NombreColección.find({campo1:$gt{valor1}},{campo2:$gt{valor2}})**

## db.NombreColección.find($or:[{campo1:valor1},{campo2:valor2},{campoN:valorN}]):
Operador Lógico 'o'. returnará resultados cuando un documento cumpla con un valor o con otro. 
## db.NombreColección.find($and:[{campo1:valor1},{campo2:valor2},{campoN:valorN}]):
Operador Lógico 'y'. returnará resultados cuando un documento cumpla con un valor y con los otros. 

## $inc:
se usa para incrementar valores en un documento. si se usa con numeros negativos, se reduce el valor (ejemplo: {$inc:{'valor':10}} esto aumenta el valor en 10, en cambio {$inc:{'valor':-10}} esto reduce el valor en 10)
## $mul:
se usa para multiplicar el valor por la cantidad mencionada. (por ejemplo, si usamos {$mul{'valor':2}}, multiplica el valor por 2)
## $max:
igualará los valores inferiores al numero que le asignemos al numero asignado. si el numero es superior, lo mantendrá.(ejemplo: si establecemos {$max:{'valor':200}}, cualquier valor inferior en 'valor' se actualizará, es decir si un producto tuviese el valor de 100, se modificará a 200. si otro producto en cambio, está en 300, este se mantendrá con ese valor)
## $min:
hace lo contrario al $max. si un valor es mayor al valor que le asignamos, este se reducirá al valor asignado.(ejemplo: si establecemos que {$min:{'valor':100}}, cualquier valor sibre 100 se reducirá a este numero. para el ejemplo anterior, ambos numeros se reducirían a 100 ya que son mayores, pero si un numero es menor, suponiendo que tenemos uno de valor 50, este se mantendrá)
