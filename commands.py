import pickle

class redisCommands:
    def __init__(self):
        self.data = self.loadPickle()
        
    def loadPickle(self):
        with open('Database/dict.pickle', 'rb') as handle:
            return(pickle.load(handle))


    def setPickle(self, obj):
        with open('Database/dict.pickle', 'wb') as handle:
            pickle.dump(obj, handle, protocol=pickle.HIGHEST_PROTOCOL)


    def echoCommand(self, query):
        return " ".join(query.split(" ")[1:])

    def pingCommand(self):
        return("PONG")

    def resetDatabase(self):
        self.setPickle({})
        return("Reset Database successfully")
    
    def setCommand(self, query):
        _, key, value = query.split(" ")
        self.data[key] = value
        self.setPickle(self.data)
        return(f"SET {key} to {value} successfully")

    def getCommand(self, query):
        _, key = query.split(" ")
        if key in self.data:
            return self.data[key]
        return("-ERROR key not present")

    
    def driver(self, query):
        funcName = query.split(" ")[0]
        switcher = {
            "ECHO": lambda: self.echoCommand(query),
            "PING": lambda: self.pingCommand(),
            "SET": lambda: self.setCommand(query),
            "GET": lambda: self.getCommand(query),
            "RESET": lambda: self.resetDatabase()
        }

        if funcName in switcher:
            return switcher.get(funcName, lambda: "Invalid arg")()
        