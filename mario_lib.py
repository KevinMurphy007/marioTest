import os
import csv
carbody_dict = dict()
character_dict = dict()
body_accel_list=[]
body_speed_list=[]
char_speed_list=[]
char_accel_list=[]


def read_and_combine(bodies_file, char_file):
    """
    read from the bodies file and the char file
    (CSV) and then iterate thru both of them (nested)
    and to print out all the combinations
    """
    with open(bodies_file) as body_file:
        reader = csv.reader(body_file)
        next(reader)
        for row in reader:
            body = row[0].strip()
            type = row[1].strip()
            speed = row[2]
            Acceleration = row[3]
            weight = row[4]
            handling = row[5]
            traction = row[6]
            Mini_turbo = row[7]
            carbody_dict[body] = (type, speed, Acceleration, weight, handling, traction, Mini_turbo)

    with open(char_file) as character_file:
        reader1 = csv.reader(character_file)
        next(reader1)
        for row in reader1:
            char = row[0].strip()
            speed = row[1]
            Acceleration = row[2]
            weight = row[3]
            handling = row[4]
            traction = row[5]
            Mini_turbo = row[6]
            character_dict[char] = (speed, Acceleration, weight, handling, traction, Mini_turbo)

def best_speed(bodies_file, char_file):
    """
    read from bodies and char files
    iterate thru them all and get the speed
    sum the speed for the character and the body
    print out the character/body combo that has the highest
    speed.  And print out the highest (total) speed.
    """
    for car in carbody_dict:
        num = carbody_dict[car]
        speed = carbody_dict[car][1]
        body_speed_list.append(speed)

        for character in character_dict:
            num1 = character_dict[character]
            speed = character_dict[character][1]
            char_speed_list.append(speed)

#Best Speed Body
    best_speed_body = body_speed_list[0]
    counter = 0
    while counter < len(body_speed_list):
        if body_speed_list[counter] >= best_speed_body:
            best_speed_body = body_speed_list[counter]
        counter = counter + 1

#Best Speed Character
    best_speed_char = char_speed_list[0]
    counter = 0
    while counter < len(char_speed_list):
        if char_speed_list[counter] >= best_speed_char:
            best_speed_char = char_speed_list[counter]
        counter = counter + 1

# Best Overall speed
    best_speed = float(best_speed_body) + float(best_speed_char)

    return best_speed

def best_acceleration(bodies_file, char_file):
    for car in carbody_dict:
        num = carbody_dict[car]
        acceleration = carbody_dict[car][2]
        body_accel_list.append(acceleration)

    for character in character_dict:
        num1 = character_dict[character]
        acceleration = character_dict[character][2]
        char_accel_list.append(acceleration)

    #Best Acceleration Body
        best_accel_body = body_accel_list[0]
        counter = 0
        while counter < len(body_accel_list):
            if body_accel_list[counter] >= best_accel_body:
                best_accel_body = body_accel_list[counter]
            counter = counter + 1

    #Best Acceleration Character
        best_accel_char = char_accel_list[0]
        counter = 0
        while counter < len(char_accel_list):
            if char_accel_list[counter] >= best_accel_char:
                best_accel_char = char_accel_list[counter]
            counter = counter + 1

    #Best Overall Acceleration
        best_accel = float(best_accel_body) + float(best_accel_char)
        return best_accel



# TODO refactor and consider if there's a better way than passing in the
# filename each time
