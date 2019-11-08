import datetime

# the recommended approach is to use isinstance instead of type == dict

def average(mylist):
    #if type(mylist) == dict:
    if isinstance(mylist, dict):
        return sum(mylist.values())/len(mylist)
    else:
        return sum(mylist)/len(mylist)

def weather_status(temp):
    if temp >27:
        return 'Hot'
    elif temp < 10:
        return 'Cold'
    else:
        return 'Warm'

print ('Today date is', datetime.datetime.now().strftime("%m %d %Y"))
#string = "This is simply for having less because everybody says less is more, I wouldn't know how to prove it whether is true"
#print (string)
temperatures = [4.5, 12, 5.44]
ages = {"Iulian":40, "Alexandru":47, "Cristian":42}
#print (ages["Iulian"])



print('Average age is', average(ages))
print('Average temperature is',average(temperatures))
print ('....')
# input gets a string entered by the user
temperature = int(input('Enter temperature: '))
print(weather_status(temperature))

name = input ('Enter your name: ')
print(f"Hello {name}")
