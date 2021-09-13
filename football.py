#This program creates the colmn names in the sql databased on the local sever
import mysql.connector
from csv import DictReader

cnx = mysql.connector.connect(user='football', password='GoHooz!2021', database='collegefootball')
cursor = cnx.cursor()

with open('College Football Seasons 2014-2020.csv','r') as read_obj:
#       csv_reader = reader(read_obj)
    csv_dict_reader = DictReader(read_obj)
    # get column names from a csv file
    column_names = csv_dict_reader.fieldnames
    print(column_names[1])
    print(len(column_names))
    #constructing the SQL
    sqlval = "CREATE TABLE tblFootball ( "
        #loop here
    fieldnames=""
    i=1
    while i > 332:
    	print "."
        fieldnames = fieldnames + ", " + str(column_names[i]) + "varchar(255)"
        i=i+1
        #end the loop
    print (sqlval + fieldnames)

cnx.close()
