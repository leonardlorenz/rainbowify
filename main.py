#!/bin/python

import sys
import os
import subprocess
import math

def help():
    print('Synopsis:')
    print('./main.py <input image> <fuzz factor> <colour to replace> <output path>')

def add_zeroes(colour):
    if len(colour) < 2:
        colour = str(0) + colour
    return colour

def rgb_to_colour(r, g, b):
    red = hex(r)[2:]
    green = hex(g)[2:]
    blue = hex(b)[2:]

    red = add_zeroes(red)
    green = add_zeroes(green)
    blue = add_zeroes(blue)

    return_str = '#' + red + green + blue
    return return_str

def calc_colour(i):
    i = i * 0.1
    brightness = 1
    red = brightness * (math.sin(i + 2) + 1) * 128;
    green = brightness * (math.sin(i + 4) + 1) * 128;
    blue = brightness * (math.sin(i + 6) + 1) * 128;
    #print(str(red) + ' ' + str(green) + ' ' + str(blue))
    return rgb_to_colour(int(red), int(green), int(blue))

def main():
    if len(sys.argv) > 2:
        input_image = sys.argv[1]
        fuzz_factor = 50000
        colour_to_replace = 'white'
        output_path = ''

        if sys.argv[2]:
            fuzz_factor = sys.argv[2]
        if sys.argv[3]:
            colour_to_replace = sys.argv[3]
        if len(sys.argv) > 4:
            output_path = sys.argv[4].split('.')[0] + "-converted." + input_image.split('.')[1]
        else:
            output_path = input_image.split('.')[0] + "-converted." + input_image.split('.')[1]

        if output_path is '':
            print('No output path specified. Exitting.')
            help()

        for i in range(0, 60):

            output_colour = calc_colour(i)
            print(output_colour)

            convert_path = os.popen('which convert').read().strip('\n')
            print(convert_path)

            final_output_path = output_path.split('.')[0] + '-' + str(i) + '.' + output_path.split('.')[1]

            subprocess.call([convert_path, input_image, '-fill', output_colour, '-fuzz', fuzz_factor, '-opaque', colour_to_replace, final_output_path])
    else:
        help()

if __name__ == "__main__":
        main()
