import time
import threading

import requests

url = 'http://192.168.0.100:5000/rest/items'

speed_url = "http://192.168.0.180/motor?params="

last_reached_pin = "11"

pins = {
    "11": {"state": 0, "next_pin": 26, "speed": 550, "sleep": .5},
    "26": {"state": 0, "next_pin": 24, "speed": 1000, "sleep": 0},
    "24": {"state": 0, "next_pin": 23, "speed": 1000, "sleep": 0},
    "23": {"state": 0, "next_pin": 34, "speed": 1000, "sleep": 0},
    "34": {"state": 0, "next_pin": 33, "speed": 1000, "sleep": 0},
    "33": {"state": 0, "next_pin": 31, "speed": 1000, "sleep": 0},
    "31": {"state": 0, "next_pin": 32, "speed": 700, "sleep": 0},
    "32": {"state": 0, "next_pin": 21, "speed": 600, "sleep": 0},
    "21": {"state": 0, "next_pin": 27, "speed": 1000, "sleep": 0},
    "27": {"state": 0, "next_pin": 25, "speed": 600, "sleep": 0},
    "25": {"state": 0, "next_pin": 13, "speed": 800, "sleep": 0},
    "13": {"state": 0, "next_pin": 12, "speed": 600, "sleep": .1},
    "12": {"state": 0, "next_pin": 11, "speed": 1000, "sleep": 0},
    "35": {"state": 0, "next_pin": 33, "speed": 1000, "sleep": 0},
    "22": {"state": 0, "next_pin": 35, "speed": 1000, "sleep": 0}
}


def continuous_tracking():
    while True:
        tracking()


def startup():
    requests.get(url=speed_url + "600")
    global last_reached_pin
    start_point_found = False
    while not start_point_found:
        resp = requests.get(url=url)
        data = resp.json()
        rail_sections = data["track"]["rail_sections"]
        for key in pins:
            pins[key]["state"] = rail_sections[key]["state"]
            if pins[key]["state"] == 0:
                last_reached_pin = key
                start_point_found = True
        time.sleep(.1)


def tracking():
    global last_reached_pin
    next_pin = str(pins[last_reached_pin]["next_pin"])
    resp = requests.get(url=url)
    data = resp.json()
    req_pin_state = data["track"]["rail_sections"][next_pin]["state"]
    if req_pin_state == 0:
        print(next_pin)
        last_reached_pin = next_pin
        time.sleep(pins[next_pin]["sleep"])
        requests.get(url=speed_url + str(pins[next_pin]["speed"]))

    next_next_pin = str(pins[next_pin]["next_pin"])
    req_next_pin_state = data["track"]["rail_sections"][next_next_pin]["state"]
    if req_next_pin_state == 0:
        print("NEXT_NEXT_PIN!")
        print(next_next_pin)
        last_reached_pin = next_next_pin
        requests.get(url=speed_url + str(pins[next_next_pin]["speed"]))

    # timestamp = int(time.time() * 1000)
    # for key in pins:
    #     if pins[key]["state"] == 0:
    #         if rail_sections[key]["state"] == 1 and pins[key]["timestamp"] + 100 < timestamp:
    #             pins[key]["state"] = 1
    #             pins[key]["timestamp"] = timestamp
    #             last_reached_pin = key
    #     if pins[key] == 1:
    #         if rail_sections[key]["state"] == 0 and pins[key]["timestamp"] + 100 < timestamp:
    #             pins[key]["state"] = 0
    #             pins[key]["timestamp"] = timestamp
    # if last_reached_pin != prev_pin:
    #     print(last_reached_pin)

    time.sleep(.1)


def main():
    startup()
    train_tracking_thread = threading.Thread(target=continuous_tracking, daemon=True, name="trainTrackingThread")
    train_tracking_thread.start()
    # continuous_tracking()
    while True:
        time.sleep(1)
        #print("main is running")
        #print("current threads: ")
        #print(threading.enumerate())


if __name__ == '__main__':
    main()
