import json

json_data = '{"firstName": "Larry", "lastName":"Scott", "email": "larry@toricode.com"}'

json_object = json.loads(json_data)

print("Object type: ", type(json_object))
print("First Name: ", json_object['firstName'])
print("Last Name: ", json_object['lastName'])
print("Email Address: ", json_object['email'])
