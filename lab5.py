class Time():
    def __init__(self, h, m, s):
        self.hours = h
        self.minutes = m
        self.seconds = s

    def getHours(self):
        return self.hours
    def getMinutes(self):
        return self.minutes
    def getSeconds(self):
        return self.seconds

    def toString(self):
        return str(self.hours) + ":" + str(self.minutes) + ":" + str(self.seconds)

    def timeInSeconds(self):
        return (self.hours*3600) + (self.minutes*60) + self.seconds

    def changeTheTime(self, h, m, s):
        self.hours = h
        self.minutes = m
        self.seconds = s

    def twelveHourClock(self):
        if (self.hours > 12): #this determines if the time is past noon
            return str(self.hours - 12) + ":" + str(self.minutes) + ":" + str(self.seconds) + " PM"
        return str(self.hours) + ":" + str(self.minutes) + ":" + str(self.seconds) + " AM"

    def whatTimeIsIt(self):
        if (self.hours >= 6 and self.hours < 12): #each if statement checks what timeframe it currently is
            return "Morning"
        if (self.hours >= 12 and self.hours < 17):
            return "Afternoon"
        if (self.hours >= 17 and self.hours < 22):
            return "Evening"
        else:
            return "Nighttime"

    def compareTo(self, t):
        return self.timeInSeconds() - t.timeInSeconds()

