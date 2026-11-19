robot = {
    "name": "Atlas",
    "model": "RX-7",
    "battery": 85,
    "speed": 6,
    "mode": "exploration"
}
print(robot["name"])
print(robot["model"])
robot["battery"] = 100.0
print(robot["battery"])
robot["color"] = "Red"
print(robot["color"])
robot.pop("mode")
length = len(robot)
print(f"The amount of key-value pairs are {length}")
for key, value in robot.items():
    print("Here is the robots...")
    print(f"{key}: {value}")