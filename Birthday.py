import calendar
NAME=input('ENTER NAME: ')
days=['Monday', 'Tuesday','Wednesday', 'Thursday',
      'Friday', 'Saturday', 'Sunday']
months=['January','February','March','April','May','June','July',
        'August','September','October','November','December']
endings=['st','nd','rd']+17*['th']+['st','nd','rd']+7*['th']+['st']
print('Hello! '+NAME+', are you interested in the day \
of your Birthday?')
D=input('Enter Day(1-31): ')
M=input('Enter Month(1-12): ')
Y=input('Enter Year: ')
d=int(D)
m=int(M)
y=int(Y)
day_of_date =calendar.weekday(month=m, day=d, year=y)
print(NAME+', you were born on '+ days[day_of_date]+' '+months[m-1]+' '+D+endings[d-1]+'/'+M+'/'+Y)
input('Press <Enter> to Exit')
