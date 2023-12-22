import csv

rec = []

# enter courses you want eg ["MAT150", "CCC683"]
wantedCourses = []
# enter your student group(s) eg ["CSD11", "CSD12"]
studentGroups = ["CSD1"] # gives all for csd1* eg csd11, csd12 ....


with open("calendar.csv", "r") as calendar:
    rows = csv.reader(calendar)
    for i in rows:
        if i[1] in wantedCourses:
            rec.append(i)
            continue
        for j in studentGroups:
            if j in i[3]:
                rec.append(i)
print(rec)
with open("wantedCalendar.csv", "w") as wCalendar:
    writer = csv.writer(wCalendar)
    for i in rec:
        writer.writerow(i)