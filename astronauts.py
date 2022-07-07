# Exercise: Magic Methods in Python

import csv

file_location = ("astronauts.csv")
astronauts_list = []

class Astronauts:
    """Astronauts class"""
    global astronauts_list

    def __init__(self, name, status, spaceflights, spaceflighthrs):
        self.__name = name
        self.__status = status
        self.__spaceflights = spaceflights
        self.__spaceflighthrs = spaceflighthrs
        
    def __gt__(self, other):
        print("gt called to evaluate %s > %s" % (self.__name, other.__name))
        return self.__spaceflighthrs > other.__spaceflighthrs

    def __ge__(self, other):
        print("ge called to evaluate %s >= %s" % (self.__name, other.__name))
        return self.__spaceflighthrs >= other.__spaceflighthrs

    def __eq__(self, other):
        print("eq called to evaluate %s == %s" % (self.__name, other.__name))
        return self.__spaceflighthrs == other.__spaceflighthrs

    def __str__(self):
        return self.__name, self.__status

    def __repr__(self):
        return ("Name: %s, Status: %s, Flights: %s, Flight Hours: %s" 
        % (self.__name, self.__status, str(self.__spaceflights), str(self.__spaceflighthrs)))

def loadAstronautsData(file_location):
    with open(file_location) as astronautsFile:
        astronauts = csv.reader(astronautsFile, delimiter = ',')
        next (astronauts)
        for person in astronauts:
            aname = person[0]
            astatus = person[3]
            aflights = int(person[12])
            aflighthrs = int(person[13])
             
            astronaut = Astronauts(aname, astatus, aflights, aflighthrs)

            astronauts_list.append([astronaut])

    # print("Let's see the list")
    # print(repr(astronauts_list))

loadAstronautsData(file_location)
# help(Astronauts)
print("\n") 
print(astronauts_list[0])
print(astronauts_list[5])
gtTest = (astronauts_list[0] > astronauts_list[5])
print(gtTest)
print("\n")
print(astronauts_list[4])
print(astronauts_list[19])
geTest = (astronauts_list[4] >= astronauts_list[19])
print(geTest)
print("\n")
print(astronauts_list[7])
print(astronauts_list[11])
eqTest = (astronauts_list[7] == astronauts_list[11])
print(eqTest)
print("\n")
print(repr(astronauts_list))