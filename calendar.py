import calendar
month,day,year=map(int,input().split())
weekday_index=calendar.weekday(year,month,day)
print(calendar.day_name[weekday_index].upper())
