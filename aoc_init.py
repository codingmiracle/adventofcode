import os
import sys

import requests
from datetime import date

root_dir = "C:\\Users\\dagra\\Software\\Python\\adventofcode2023\\src"
cookies = {
    "session": "53616c7465645f5ff3b6d4939cc8afb428cab761f644a767f14a6003c030c5e90953fb1196e1364a2d86535bb300d32955ff2c114820b63a2080d5ba9d8d7e05"} # env


def init_day(day: int):
    daily_dir = os.path.join(root_dir, f"dec{day}")
    try:
        os.mkdir(daily_dir)
    finally:
        request = requests.get(f"https://adventofcode.com/2023/day/{day}/input", cookies=cookies)
        inputfile = open(os.path.join(daily_dir, "input.txt"), "w")
        inputfile.write(request.text)
        inputfile.close()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1].startswith("--day") or sys.argv[1].startswith("-d"):
            try:
                init_day(int(sys.argv[2]))
            except IndexError:
                print(f"No day to initialize given after {sys.argv[1]}. try --day [number] or -d [number]")
    else:
        print(
            "No specific day given. Trying to initialize with system date."
            "For a specific day try --day [number] or -d [number]")
        if date.today().month != 12:
            raise Exception("it is not December. For a specific day try --day [number] or -d [number]")
        else:
            init_day(date.today().day)
