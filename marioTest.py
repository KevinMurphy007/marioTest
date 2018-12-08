import os
from mario_lib import *

my_dir = os.path.dirname(os.path.realpath(__file__))

bodies_file = my_dir + '/' + 'bodies.csv'
char_file = my_dir + '/' + 'characters.csv'

read_and_combine(bodies_file, char_file)
best_speed = best_speed(bodies_file, char_file)
best_accel = best_acceleration(bodies_file, char_file)

print(best_speed)
print(best_accel)
