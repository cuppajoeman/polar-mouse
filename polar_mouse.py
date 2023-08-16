import math
from screeninfo import get_monitors

# assuming one monitor
main_monitor = get_monitors()[0]

screen_width, screen_height = main_monitor.x, main_monitor.y

aim_angle = 0

rotation_sensitivity = 0.005
y_axis_controls_length = True
aim_length_scale = 1
length_sensitivity = 0.0009

aim_length_x = screen_width / 2
aim_length_y = screen_height / 2
origin = (screen_width / 2, screen_height / 2)

max_distance = math.sqrt(aim_length_x ** 2 + aim_length_y ** 2)

def clamp(input, min, max):
    if (input < min):
        return min
    elif (input > max):
        return max
    return input

def translate(origin, point):
    print(origin, point)
    return tuple(map(sum,zip(origin, point)))

def get_new_polar_mouse_position(delta_x, delta_y):
    global aim_length_scale
    global aim_angle

    if y_axis_controls_length:
        aim_length_scale = clamp(aim_length_scale + delta_y * length_sensitivity, 0, 1)

    aim_angle += delta_x * rotation_sensitivity

    x_pos = aim_length_scale * aim_length_x * math.cos(aim_angle)
    y_pos = aim_length_scale * aim_length_y * math.sin(aim_angle)

    # return clamp(x_pos + origin[0], -screen_width/2, screen_width/2), clamp(y_pos + origin[1], -screen_height/2, screen_height/2)
    return x_pos + origin[0], y_pos + origin[1]