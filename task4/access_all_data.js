// importing mongodb libraries
const {MongoClient, ObjectID} = require('mongodb')

const connection_url = "mongodb://127.0.0.1:27017"
const databaseName = 'climateChange'

MongoClient.connect(
    connection_url,
    { useUnifiedTopology: true },
    (error, client) => {
        if (error) {
            return console.log("Unable to connect database!")
        }
        const db =  client.db(databaseName)


        db.collection('CarFuelAndEmissions').find().toArray(
            (error, CarFuelAndEmissions) => {
                
                CarFuelAndEmissions.forEach(function(CarFuelAndEmissions){
                    console.log("Year         : " +CarFuelAndEmissions.year)
                    console.log("Manufacturer : " +CarFuelAndEmissions.manufacturer)
                    console.log("Model        : " +CarFuelAndEmissions.model)
                    console.log("Description  : " +CarFuelAndEmissions.description)
                    console.log("Fuel Type    : " +CarFuelAndEmissions.fuel_type)
                    console.log("CO2 Emission : " +CarFuelAndEmissions.co2_emissions)
                    console.log("================================================")
                })

            }
        )
    }
)
