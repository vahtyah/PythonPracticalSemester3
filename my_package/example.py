from my_package import func1, func2
import json

func1()
func2()

with open("my_package/data.json", "r") as f:
    data = json.load(f)
print(data)