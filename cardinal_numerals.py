# import pygame
# pygame.init()

def integer_to_vietnamese_numeral(s, region='north', activate_tts = False):

    # Waypoint 2: Support Vietnamese Southern Numerals
    if region == None: region = 'north'
    if not isinstance(region, str): raise TypeError("Argument region is not a string")
    if region != 'south' and region != 'north' : raise ValueError("Argument region has not a correct value")
    if region == 'south':
        if 'nghìn' in s : s = s.replace('nghìn', 'ngàn')
        if 'linh' in s : s = s.replace('linh', 'lẻ')
        print(s)
    else: print(s)


# integer_to_vietnamese_numeral(ss, region='')
# print(file_name_map("bốn"))
