import pickle

class redisCommands:
    def __init__(self):
        pass
    
    def echoCommand(self, query):
        return " ".join(query.split(" ")[1:])

    def pingCommand(self):
        return("PONG")

    def setCommand(self, query):
        pass

    def getCommand(self, query):
        pass
    
    def driver(self, query):
        funcName = query.split(" ")[0]
        switcher = {
            "ECHO": lambda: self.echoCommand(query),
            "PING": lambda: self.pingCommand(),
            "SET": lambda: self.setCommand(query)
        }

        if funcName in switcher:
            return switcher.get(funcName, lambda: "Invalid arg")()
        