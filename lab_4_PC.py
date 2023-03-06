import datetime


#time conversion from std. to military
def to_military_time(time):
    military_time = time.strftime("%H:%M")
    return military_time

#Print military time
current_time = datetime.datetime.now()
military_time = to_military_time(current_time)
print("Current time in military format: " + military_time)