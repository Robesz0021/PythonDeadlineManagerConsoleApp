from deadline import Deadline

filename = "database.dtb"

class Operations:
    def __init__(self):
        self.deadlines = []
        
    def createDeadline(self, name, date, time, location, note):
        deadlines = Deadline(name, date, time, location, note)
        with open(filename, "a", encoding="utf-8") as f:
            f.write(f"{str(deadlines)}\n")
        return deadlines

    def deleteDeadline():
        return "asd"

    def modifyDeadline():
        return "asd"
    
    def searchDeadlinebyName():
        return "asd"
    
    def listDeadlinesbyDate():
        return "asd"
    
    def listDeadlinesbyWeek():
        return "asd"
    
    def litDeadlinesbyMonth():
        return "asd"