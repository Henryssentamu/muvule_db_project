import pprint; print = pprint.pprint
def extractDataFromTextFile():
    """extract data from text file insert data into specified data structure
    and it return flittered data from text file"""

    with open("henryData.txt", "r") as file:
        sorted_data = {}
        still_at = None
        value = []

        for line in file:
            current_line = line
            current_line_indentation = current_line.index(current_line.strip())
            if current_line_indentation is None:
                continue

            current_line = current_line.strip()
            if current_line_indentation == 0:
                category = current_line
                sorted_data[category] = {}
                value = []
                value2 =[]
            elif current_line_indentation == 4 and current_line.strip() == "fields":
                subcategory = current_line
                sorted_data[category] = {subcategory:[]}

            if current_line_indentation == 8 and still_at == "fields":
                value.append(current_line)

                sorted_data[category] = {subcategory: value}
            elif current_line_indentation == 4 and current_line.strip() == "data":
                subcategory2 = current_line
                sorted_data[category] = {subcategory: value, subcategory2:[]}

            if current_line_indentation == 8 and still_at == "data":
                value2.append(current_line)
                newValue2 =DataTypeConverter(value2)

                sorted_data[category] = {subcategory: value,subcategory2:newValue2}


            if current_line_indentation == 4:
                still_at = current_line
    return sorted_data



def DataTypeConverter(givenlist):
    """split items of a list by ',' delimiter
    and convert each item to it's respective datatype
    then it returns a list of converted data in their respective data type"""
    formatedList = []
    for item in givenlist:
        splittedItemsInList = item.split(',')
        """splited items in the list by coma"""
        cleenedList = [itemValue.strip().strip('"') for itemValue in splittedItemsInList]
        clearedList = []
        for itm in cleenedList:
            try:
                cleared = int(itm)
            except ValueError:
                try:
                    cleared = float(itm)
                except ValueError:
                    cleared = itm
            clearedList.append(cleared)

        formatedList.append(clearedList)

    return formatedList

print(extractDataFromTextFile())