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

    def deleteDeadline(self, name):
        updated_deadlines = []
        deleted = False
        with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()
        with open(filename, "w", encoding="utf-8") as f:
        for line in lines:
            if line.startswith(name + ","):
            deleted = True
            continue
            f.write(line)
        return deleted

    def modifyDeadline(self, name, new_name=None, new_date=None, new_time=None, new_location=None, new_note=None):
        modified = False
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
        with open(filename, "w", encoding="utf-8") as f:
            for line in lines:
                if line.startswith(name + ","):
                    parts = line.strip().split(",")
                    if new_name is not None:
                        parts[0] = new_name
                    if new_date is not None:
                        parts[1] = new_date
                    if new_time is not None:
                        parts[2] = new_time
                    if new_location is not None:
                        parts[3] = new_location
                    if new_note is not None:
                        parts[4] = new_note
                    f.write(",".join(parts) + "\n")
                    modified = True
                else:
                    f.write(line)
        return modified
    
    def searchDeadlinebyName(self, name):
        results = []
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith(name + ","):
                    results.append(line.strip())
        return results
        
    def listDeadlinesbyDate(self, date):
        results = []
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) > 1 and parts[1] == date:
                    results.append(line.strip())
        return results
        
    def listDeadlinesbyWeek(self, week_date):
        import datetime
        results = []
        week_date_obj = datetime.datetime.strptime(week_date, "%Y-%m-%d")
        week_start = week_date_obj - datetime.timedelta(days=week_date_obj.weekday())
        week_end = week_start + datetime.timedelta(days=6)
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) > 1:
                    try:
                        deadline_date_obj = datetime.datetime.strptime(parts[1], "%Y-%m-%d")
                        if week_start.date() <= deadline_date_obj.date() <= week_end.date():
                            results.append(line.strip())
                    except Exception:
                        continue
        return results

    def listDeadlinesbyMonth(self, month):
        results = []
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) > 1:
                    try:
                        deadline_month = parts[1][:7]
                        if deadline_month == month:
                            results.append(line.strip())
                    except Exception:
                        continue
        return results
        