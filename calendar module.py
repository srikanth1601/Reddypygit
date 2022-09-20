import calendar
import datetime

n = input()
m,d,y = (int(i) for i in n.split(" ")) 
x = calendar.weekday(y,m,d)
if x == 0:
    print("MONDAY")
if x == 1:
    print("TUESDAY")
if x == 2:
    print("WEDNESDAY")
if x == 3:
    print("THURSDAY")
if x == 4:
    print("FRIDAY")
if x == 5:
    print("SATURDAY")
if x == 6:
    print("SUNDAY"
