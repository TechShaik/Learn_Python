import json

data="""{
    "name":"Shaikshavali",
    "age":23
}"""

person=json.loads(data)

# person1=json.loads(person)
  # {"name": "Shaikshavali", "age": 23}

print(person)

json_data = json.dumps(person)