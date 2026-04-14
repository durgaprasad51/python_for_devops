import os

command = "uptime"
command = "date"


def check_cpu(command):# defining a function
    print(os.system(command))

check_cpu("df -h") # calling a function

def check_date(command): # defining a function
    return os.system(command)    # return can be writtena in place of print()

check_date("date")    # calling a function

def check_mem(command): # defining a function
    return os.system(command)    # return can be writtena in place of print()

check_mem("free")


"""
To make this above code more shorter

import os

def run_command(command):# defining a function
    return os.system(command)

run_command("date")
run_command("dh -h")
run_command("free")
run_command("uptime")
"""


# datetime module

import datetime

def show_date():  # defined a function
    return datetime.datetime.today()

today = show_date()         # calling the function
print(today)