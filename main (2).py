# Leap Year

"""
year%4==0&
year%100!=0/
year%400==0

"""
def is Leap Year(year):
if(year%4==0andyear%100!=0)or year%400==0:
return  True
  else:
return  false 

year=int(input("enter a year:"))

if is Leap Year(year):
print('{} is a leap year,',format(year))
else:
print('{} is  not a leap year,',format(year))