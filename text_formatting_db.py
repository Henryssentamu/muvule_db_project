from text_formating import  extractDataFromTextFile,DataTypeConverter
import sqlite3
db = sqlite3.connect("school_db.db")
curser = db.cursor()
datastructures = extractDataFromTextFile()
print(datastructures)
for table_name in datastructures:
    for category in datastructures[table_name]:
        attribute_list = datastructures[table_name][category]
        if category == "fields":
            stringed_attributes = ",".join([attribute.replace(':', ' ') for attribute in attribute_list])
            createdTable = curser.execute(f""" create table IF NOT EXISTS {table_name} (
            Time_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            {stringed_attributes})""")
        else:
            columns = ','.join([_.split(' ')[0] for _ in  stringed_attributes.split(',')])
            value_list = datastructures[table_name][category]
            numberOfValuesToInsert = ",".join(["?"] * len(value_list[0] ))
            insertIntotable = curser.executemany(f"insert into {table_name}({columns}) values({numberOfValuesToInsert})",value_list);
            db.commit()
        #db.close()

