# Comandos MongoDB:
## **use <nombre de la base de datos>**:
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
## **db.NombreColección.find({campo:{$gt:{valor}})**:
se usa para buscar "algo mayor que" respecto al campo que le indicamos. _**NOTA**: se usa solo para variables numericas._
## **db.NombreColección.find({campo:{$lt:{valor}})**:
se usa para buscar "algo menor que" respecto al campo que le indicamos. _**NOTA**: se usa solo para variables numericas._
## **db.NombreColección.find({campo:{$eq:{valor}})**:
se usa para buscar "algo igual que" respecto al campo que le indicamos. _**NOTA**: se usa solo para variables numericas._
## **db.NombreColección.find({campo:{$ne:{valor}})**:
se usa para buscar "algo no igual que" respecto al campo que le indicamos. _**NOTA**: se usa solo para variables numericas._
## **db.NombreColección.find({campo:{$gte:{valor}})**:
se usa para buscar "algo mayor o igual que" respecto al campo que le indicamos. _**NOTA**: se usa solo para variables numericas._
## **db.NombreColección.find({campo:{$lte:{valor}})**:
se usa para buscar "algo menor o igual que" respecto al campo que le indicamos. _**NOTA**: se usa solo para variables numericas._

## **para memorizarlo mejor**: 
gt (Greater Than, mayor que), lt (Less Than, Menor que), eq (equal, igual que), ne (not equal, distinto que), gte (Greater Than Equal, mayor o igual que). lte (Less Than Equal, menor o igual que)
