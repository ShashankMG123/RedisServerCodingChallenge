from enum import Enum

class dataType(Enum):
    STRING = 1,
    BULKSTRING = 2,
    INTEGER = 3,
    ARRAY = 4,
    ERROR = 8

class parser:
    def getType(self, query):
        switcher = {
            "+": dataType.STRING,
            "-": dataType.ERROR,
            ":": dataType.INTEGER,
            "$": dataType.BULKSTRING,
            "*": dataType.ARRAY
        }

        if(len(query) > 0):
            firstChar = query[0]
            if(firstChar in switcher):
                return switcher[firstChar]
            else:
                return "InvalidType"
        else:
                return "InvalidType"

    def getTypeSymbol(self, value):
        dataType = type(value).__name__
        switcher = {
            "str": "+",
            "error": "-",
            "int": ":",
            "bulkString": "$",
            "list": "*"
        }
        return switcher[dataType]

    def shouldThrowError(self, query):
        if(self.getType(query) == "InvalidType"):
            return True
        return False

    def deSerialize(self, query):
        typeOfQuery = self.getType(query)
        if(query == "$-1\r\n"): 
            return (("", dataType.BULKSTRING))
        if(query == "*-1\r\n"): 
            return (("", dataType.ARRAY))
        query = query[1:]
        newQuery = query.split("\r\n")

        if(typeOfQuery == dataType.STRING):
            return((newQuery[0], typeOfQuery))
        
        if(typeOfQuery == dataType.INTEGER):
            return((int(newQuery[0]), typeOfQuery))
        
        if(typeOfQuery == dataType.BULKSTRING):
            return((newQuery[1], typeOfQuery))

        if(typeOfQuery == dataType.ARRAY):
            queryItems = []
            j = 1
            for i in range(int(newQuery[0])):
                queryItems.append((newQuery[j+1], self.getType(newQuery[j])))
                j += 2
            return queryItems
    
if(__name__ == "__main__"):
    parse = parser()
    print(parse.deSerialize("*2\r\n$5\r\nhello\r\n$5\r\nworld\r\n"))