//1_contar los vehiculos con transmisión mécanica
use("automotora")
db.vehiculo.find({'opciones.transmision':'mecanica'}).count()
//2_Mostrar el tipo y las opciones de vehiculos con 4 puertas
use("automotora")
db.vehiculo.find({'opciones.numeroPuertas':4},{_id:0,'tipo':1,'opciones':1})
//3_Mostrar el tipo, precio, kilometros recorridos, color y mercado de los vehiculos comercializados en la ciudad de Talca o Rancagua
use("automotora")
db.vehiculo.find({mercado:{$in:['Talca','Rancagua']}},{_id:0,'tipo':1,'precio':1,'kmRecorridos':1,'color':1,'mercado':1})
//alternativa:
use("automotora")

//4_mostrar el precio maximo de los vehiculos tipo automovil a gasolina con color distinto al blanco
use("automotora")
db.vehiculo.find({$and:[{tipo:'automovil'},{'opciones.combustible':'gasolina'},{color:{$nin:['blanco']}}]},{_id:0,'precio':1}).sort({'precio':-1}).limit(1)
//5_Calcular el total de vehiculos diésel que tienen un valor mayor a los 10 millones
use("automotora")
db.vehiculo.find({$and:[{'opciones.combustible':'diesel'},{precio:{$gt:10000000}}]}).count()
//6.Para el mercado de Concepción mostrar los tipos de vehículo y el kilometraje recorrido de menor a mayor.
use("automotora")
db.vehiculo.find({mercado:'Concepcion'},{_id:0,'tipo':1,'kmRecorridos':1,'mercado':1}).sort({'kmRecorridos':1})
//7.Por cada vehículo modificar el atributo precio al 90% del precio actual, cuando la transmisión es automática y el mercado es Talca.
use("automotora")
db.vehiculo.updateMany({$and:[{mercado:'Talca'},{'opciones.transmision':'automatica'}]},
    {$set:{precio:{$mul:0.9}}})
//8.Mostrar los vehículos cuando el precio de los vehículos a excepción de las camionetas se encuentran entre los 9 millones y 13 millones ambos inclusive y se comercializa exactamente en tres ciudades.
use("automotora")

db.vehiculo.find({$and: [{precio: {$gte:9000000}},{precio: {$lte:13000000}},
    {tipo:{$nin:['camioneta']}}, {mercado: {$size:3}}]})

//9.Para los mercados de Santiago y Concepción mostrar los datos de los vehículos // ordenados por precio (de mayor a menor) cuando la transmisión es automática.
use("automotora")
db.vehiculo.find({$and: [{mercado: {$all: ['Santiago', 'Concepcion']}},
    {'opciones.transmision':'automatica'}]}).sort({precio:-1})

//10.Listar por precio todos los vehículos cuando la transmisión es automática,
// el combustible es gasolina y el color es blanco o rojo.
use("automotora")
db.vehiculo.find({$and: [{'opciones.transmision': 'automatica'},
{'opciones.combustible': 'gasolina'}, {color:{$in: ['blanco', 'rojo']}}]}).sort({precio:1})
