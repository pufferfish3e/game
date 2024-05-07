import random

plot = 0 
turn_times = []

def ask_for_input():
    print("Whats the move general?")
    command = input()
    command_determiner(command)

def turn(): 
    global turn_times
    print("=" *40)
    print(len(turn_times))
    for items in range(0, len(turn_times)):
        print(items)
        if turn_times[items][1] > 0:
             turn_times[items][1] = turn_times[items][1] - 1
        print(turn_times)
    ask_for_input()

def delay(delay_time, functinon_name):
    global turn_times
    print("activated")
    turn_times.append([functinon_name, delay_time])
    print(turn_times)


def command_determiner(input_command):
    if input_command.split(" ")[0] == "fight":
        turn()
    else:
        print(input_command.split(" "))
        exit

delay(5, "hi")
ask_for_input()
