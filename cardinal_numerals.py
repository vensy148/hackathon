import pygame
pygame.init()

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

    # Waypoint 3: Say Vietnamese Numeral
    file_name_map = {
        "một" : "mot1",
        "hai" : "hai",
        "ba" : "ba",
        "bốn" : "bon",
        "năm" : "nam",
        "sáu" : "sau",
        "bảy" : "bay",
        "tám" : "tam",
        "chín" : "chin",
        "không" : "khong",
        "mốt" : "mot2",
        "lăm" : "lam",
        "mươi" : "muoi1",
        "mười" : "muoi2",
        "ngàn" : "ngan",
        "nghìn" : "nghin",
        "trăm" : "tram",
        "triệu" : "trieu",
        "tỷ" : "ty",
        "lẻ" : "le",
        "linh" : "linh"
    }

    if region == "north":
        if activate_tts == None: activate_tts = False
        if not isinstance(activate_tts, bool): raise TypeError("Argument activate_tts is not a boolean")
        if activate_tts == True:
            for word in s.split(" "):
                file_location = "./sounds/vie/north/" + file_name_map[word] + ".ogg"
                print(file_location)
                pygame.mixer.Sound(file_location).play(maxtime = 1000)
                pygame.time.delay(600)

# ss = "bốn trăm linh năm"
# integer_to_vietnamese_numeral(ss,'south', True)
# integer_to_vietnamese_numeral(ss, region='')
# print(file_name_map("bốn"))
