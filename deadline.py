class Deadline:
    def __init__(self, name, date, time, location, note):
        self.name = name
        self.date = date
        self.time = time
        self.location = location
        self.note = note

    def __str__(self):
        return f"{self.name};{self.date};{self.time};{self.location};{self.note}"
    