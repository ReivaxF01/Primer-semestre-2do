# Comandos MongoDB:
## **use <nombre de la base de datos>**:
sirve para cambiar entre bases de datos. _NOTA: la base de datos no se creará hasta que tenga al menos una colección_
## **show dbs o show databases**: 
se usa para mostrar las bases de datos existentes
## **db.createCollection('nombre de la colección')**:
se usa para crear colecciones dentro de una base de datos
## **db.NombreBaseDeDatos.renameCollection('Nombre de la colección')**: 
se usa para editar el nombre de una colección
## **db.NombreColección.drop()**: 
se usa para eliminar una colección
## **db.NombreColección.insertOne({acá se añaden los datos que se quieran agregar a la colección siguiendo el formato JSON})**:
se usa opara insertar datos dentro de una colección
## **db.NombreColección.find()**: 
se usa para ver los archivos (o articulos) dentro de la colección
## **db.NombreColección.insertMany([{dato1},{dato2},{datoN}])**:
se usa para añadir varios datos dentro de una colección deuna sola vez
## **db.NombreColección.updateOne({un dato dentro del archivo que permita identificar el producto},{$set{acá va el campo y el nuevo valor}})**:
permite actualizar los datos de un archivo
## **db.NombreColección.updateMany({},{$set{acá va el campo y el nuevo valor}})**:
se usa para actualizar varios documentos a la vez. _NOTA: si los primeros parentesis están vacíos se aplican los cambios a toda la colección_
## **db.NombreColección.updateMany({},{$unset{acá va el campo que se quiera eliminar}})**:
se usa para eliminar un campo dentro de un archivo.  _NOTA: si los primeros parentesis están vacíos se aplican los cambios a toda la colección_
## **db.NombreColección.updateMany({},{$rename{'nombre antiguo del campo':'nombre nuevo del campo'}})**: 
se usa para renombrar un campo dentro de un archivo.  _NOTA: si los primeros parentesis están vacíos se aplican los cambios a toda la colección_
## **db.NombreColección.deleteOne({campo:'valor del campo'})**:
se usa para eliminar un archivo dentro de una coleccion
## **db.NombreColección.deleteMany({campo:'valor del campo'})**:
se usa para eliminar varios archivos dentro de una coleccion
## **db.NombreColección.deleteOne({})**: 
se usa para eliminar todos los archivos dentro de una coleccion. _NOTA: la colección sigue existiendo, pero sin archivos dentro de ella._
