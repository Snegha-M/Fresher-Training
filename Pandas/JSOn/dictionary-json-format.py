import json

data = {
    "key1" : "value1",
    "key2" : "value2",
}
result = json.dumps(data, indent = 20)
print(result)