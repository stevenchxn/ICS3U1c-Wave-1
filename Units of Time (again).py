seconds = int(input("Enter seconds here: "))

while seconds > 60:
    if seconds >= 86400:
        days = (seconds // 86400)
        seconds = (seconds % 86400)
    elif seconds >= 3600:
        hours = (seconds // 3600)
        seconds = (seconds % 3600)
    elif seconds >= 60:
        minutes = (seconds // 60)
        seconds = (seconds % 60)
hours = str(hours).zfill(2)
minutes = str(minutes).zfill(2)
seconds = str(seconds).zfill(2)

print (str(days) + ":" + str(hours) + ":" + str(minutes) + ":" + str(seconds))