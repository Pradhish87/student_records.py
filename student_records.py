import json

student =\
     {
     'name': 'pradhish',
     'age': 20,
     'mark' : 75

     }
print(student)
age = student['age']
print(age)
student["name"] ='PRADHISH M'
update_name = student['name']
print(update_name)
print(student)
n = {}
val = int(input('Number of values you need : '))
for i in range (val):
    user = input('Enter your Key: ')
    user2 = input('Enter your value: ')

    n[user] = user2

print(n)


student1 =\
     {
     'name': 'json',
     'age': 20,
     'mark' : 75

     }
stu_json = json.dumps(student1,indent = 4,sort_keys = True)
print(stu_json)
print(type(stu_json))

with open('student1.json','w',) as file:
    json.dump(student1,file)

print('json file has saved')

with open('student1.json','r') as file:
    load = json.load(file)

print(load)
print(type(load))







