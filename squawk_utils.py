EMERGENCY_CODES = {"7500":"Hijack", "7600":"Radio Failure", "7700":"General Emergency"} #that's all emergencies i could think of

def classify_emergencies(squawk):
    return EMERGENCY_CODES.get(squawk, "Normal")

def is_emergency(squawk):
    return squawk in ["7500", "7600", "7700"]

def extract_emergencies(aircraft_list):
    emergencies = []
    for ac in aircraft_list:
        squawk = ac.get("squawk")
        if squawk and is_emergency(squawk):
            emergencies.append({"hex":ac.get("hex"), "squawk":squawk, "type":classify_squawk(squawk), "flight": ac.get("flight", "N/A"), "altitude": ac.get("altitude", "N/A")})
    return emergencies