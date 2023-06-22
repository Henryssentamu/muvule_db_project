from text_formating import  extractDataFromTextFile,DataTypeConverter
from generateprimarykey import GeneratePrimaryKey
import sqlite3
db = sqlite3.connect("school_db.db")
curser = db.cursor()
datastructures = extractDataFromTextFile()
#print(datastructures)
j = k =  0
listOfPk = []

for table_name in datastructures:
    for category in datastructures[table_name]:
        attribute_list = datastructures[table_name][category]
        if category == "fields":
            stringed_attributes = ",".join([attribute.replace(':', ' ') for attribute in attribute_list])
            if k == 0:
                tb1 = table_name
                stringed_attributes += ",uniqueId  string PRIMARY KEY "
                createdTable = curser.execute(f""" create table IF NOT EXISTS {tb1} (
                         Time_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                         {stringed_attributes})""")
                k += 1
                print(f""" create table IF NOT EXISTS {tb1} (
                         Time_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                         {stringed_attributes})""")
            else:
                stringed_attributes += ",uniqueId_rfd  string "
                # createdTable = curser.execute(f""" create table IF NOT EXISTS {table_name} (
                #   Time_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                #   {stringed_attributes},
                #   FOREIGN KEY(uniqueId_rfd) REFERENCES {tb1}(uniqueId)""")
            #print(stringed_attributes)
            createdTable = curser.execute(f""" create table IF NOT EXISTS {table_name} (
            Time_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            {stringed_attributes},
            FOREIGN KEY(uniqueId_rfd) REFERENCES {tb1}(uniqueId))""")
        else:
            columns = ','.join([_.split(' ')[0] for _ in  stringed_attributes.split(',')])
            value_list = datastructures[table_name][category]
            if j == 0:


                i = len(value_list)
                listIsFull = False
                while not listIsFull:
                    pk = GeneratePrimaryKey()
                    listOfPk.append(pk)
                    if i == 1:
                        listIsFull = True
                    i -= 1

            j += 1
            for i in range(len(value_list)):
                value_list[i].append(listOfPk[i])

            numberOfValuesToInsert = ",".join(["?"] * len(value_list[0] ))
            insertIntotable = curser.executemany(f"insert into {table_name}({columns}) values({numberOfValuesToInsert})",value_list);
            db.commit()
        # #db.close()

