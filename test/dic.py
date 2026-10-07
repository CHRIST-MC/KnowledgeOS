import json


a = '{ "name":"Rahul", "age":21, "city":"Banglore"}'
b = json.loads(a)
print(b["age"])

dic = {'color': 'blue', 'car': 'farari', 'flower': 'jasmine'}
print(dic["flower"])

json_string = '''
{
    "student" : [
        {
            "id":"1", 
            "name":"John", 
            "age":30, 
            "full-time":"true"
        },
        {
            "id":"2", 
            "name":"Anna", 
            "age":22, 
            "full-time":"false"
        }
        ]
}'''

data = json.loads(json_string)
data["test"] =True
json_string = json.dumps(data, indent=2)
#print(json_string)

with open("test/datas.json", "r") as f:
    data = json.load(f)
    
with open("test/datas2.json", "w") as f:
    json.dump(data, f)

print(data)