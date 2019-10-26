import time

import requests

url = 'http://192.168.0.100:5000/rest/items'

last_reached_pin = "11"

pins = {
    "11": {"state": 0, "timestamp": 0},
    "12": 0,
    "13": 0,
    "21": 0,
    "22": 0,
    "23": 0,
    "24": 0,
    "25": 0,
    "26": 0,
    "27": 0,
    "31": 0,
    "32": 0,
    "33": 0,
    "34": 0,
    "35": 0,
}


def continuous_tracking():
    while True:
        tracking()


def startup():
    resp = requests.get(url=url)
    data = resp.json()
    rail_sections = data["track"]["rail_sections"]
    timestamp = int(round(time.time() * 1000))
    for key in pins:
        pins[key]["state"] = rail_sections[key]["state"]
        pins[key]["timestamp"] = timestamp
    time.sleep(0.1)


def tracking():
    global last_reached_pin
    prev_pin = last_reached_pin
    resp = requests.get(url=url)
    data = resp.json()
    rail_sections = data["track"]["rail_sections"]
    timestamp = int(round(time.time() * 1000))
    for key in pins:
        if pins[key]["state"] == 0:
            if rail_sections[key]["state"] == 1 and pins[key]["timestamp"] + 100 < timestamp:
                pins[key]["state"] = 1
                pins[key]["timestamp"] = timestamp
                last_reached_pin = key
        if pins[key] == 1:
            if rail_sections[key]["state"] == 0 and pins[key]["timestamp"] + 100 < timestamp:
                pins[key]["state"] = 0
                pins[key]["timestamp"] = timestamp
    if last_reached_pin != prev_pin:
        print(last_reached_pin)
    time.sleep(.1)


def main():
    startup()
    while True:
        continuous_tracking()


if __name__ == '__main__':
    main()
