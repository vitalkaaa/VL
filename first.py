import json

json_string1 = '{"b": 1.000001, "a": 1, "d": {"db": [1, 2, 3], "da": 99999.999999}, "c": "string"}'

json_string2 = '{"b": 1.0000010, "a": 1, "d": {"db": [1, 2, 3], "da": 99999.999999000}, "c": "string"}'  # True
json_string3 = '{"b": 1.000002, "a": 2, "d": {"db": [1, 2, 3], "da": 99999.123654}, "c": "string"}'  # False
json_string4 = '{"d": {"db": [1, 2, 3], "da": 99999.999999}, "b": 1.000001, "c": "string", "a": 1}'  # True
json_string5 = '{"b": 1.000001, "a": 1, "d": {"db": ["3", "2", "1"], "da": 99999.123456}, "c": "string"}'  # False


def normalize_json(json_string):
    return json.dumps(json.loads(json_string), sort_keys=True)


json1 = normalize_json(json_string1)
json2 = normalize_json(json_string2)
json3 = normalize_json(json_string3)
json4 = normalize_json(json_string4)
json5 = normalize_json(json_string5)


print(json1 == json2)
print(json1 == json3)
print(json1 == json4)
print(json1 == json5)

