import sys, getopt
import csv

def main(argv):
        friendfilelist = []
        fffilelist = []
        inputmode = friendfilelist
        for arg in argv:
            if (arg == '-f'):
                inputmode = friendfilelist
            elif (arg == '--ff'):
                inputmode = fffilelist
            else:
                inputmode.append(arg)

        contactsHash = {}
        numberSetList = []
        resultSet = set()
        for friendfile in friendfilelist:
            numberSet = set()
            with open(friendfile,"rb") as friend:
                itcsv = csv.DictReader(friend)
                for row in itcsv:
                    name = row["First Name"] + row["Last Name"]
                    if row["Home Phone"]:
                        contactsHash[row["Home Phone"]] = name
                        numberSet.add(formatNumber(row["Home Phone"]))
                    if row["Home Phone 2"]:
                        contactsHash[row["Home Phone 2"]] = name
                        numberSet.add(formatNumber(row["Home Phone 2"]))
                    if row["Mobile Phone"]:
                        contactsHash[row["Mobile Phone"]] = name
                        numberSet.add(formatNumber(row["Mobile Phone"]))
            numberSetList.append(numberSet)
        resultSet = reduce(lambda x,y: x.intersection(y), numberSetList)
        
        for fffile in fffilelist:
            numberSet = set()
            with open(fffile,"rb") as ff:
                itcsv = csv.DictReader(ff)
                for row in itcsv:
                    if row["Home Phone"]:
                        numberSet.add(formatNumber(row["Home Phone"]))
                    if row["Home Phone 2"]:
                        numberSet.add(formatNumber(row["Home Phone 2"]))
                    if row["Mobile Phone"]:
                        numberSet.add(formatNumber(row["Mobile Phone"]))
            resultSet = resultSet.difference(numberSet)
        print(resultSet)

def formatNumber(str):
    return str.replace("+86","").replace("-","").replace(" ","")

if __name__ == "__main__":
		#main(sys.argv[1:])
        main(["-f", "contacts.csv", "--ff","contact.csv"])