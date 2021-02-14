import csv
import pymongo

clientConnection = pymongo.MongoClient("mongodb://localhost:27017/")
database = clientConnection["climateChange"]
collection = database["CarFuelAndEmissions"]

with open('CarFuelAndEmissions.csv') as csvfile:
    readCSV = csv.reader(csvfile);

    line_num = 0;
    for row in readCSV:
        if (line_num>0) :
            values = {
                    "year": row[0],
                    "manufacturer": row[1],
                    "model": row[2],
                    "description": row[3],
                    "fuel_type": row[4],
                    "co2_emissions": row[5],
            }
            res = collection.insert_one(values);
        line_num += 1;

print("The records imported");
