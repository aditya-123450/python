import json
import datetime

# Using the json module
person_dict = {"name": "Grace Hopper", "id": 9}
json_data = json.dumps(person_dict, indent=4)
print(json_data)

# Using the datetime module
now = datetime.datetime.now()
print(f"\nCurrent time: {now.strftime('%Y-%m-%d %H:%M:%S')}")