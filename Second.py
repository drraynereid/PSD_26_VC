import csv

def read_cars_file ():
    with open ("cars.csv", mode ="r", encoding ="utf-8", newline ="") as file :
        csv_reader = csv. reader ( file )
        next ( csv_reader , None ) # Skip header , if present
        for row in csv_reader :
            print (row)
read_cars_file ()