import os
import pygame
import time
pygame.init()

def integer_to_vietnamese_numeral(n, region="north", activate_tts=False):
    if not isinstance(n, int):
        raise TypeError("Not an integer")
    if n < 0:
        raise TypeError("Not a positive integer")

    vnnum = {'0': 'không', '1': 'một', '2': 'hai', '3': 'ba', '4': 'bốn', '5': 'năm', '6': 'sáu', '7': 'bảy',
             '8': 'tám', '9': 'chín'}
    vnaunit = {0: '', 1: 'nghìn', 2: 'triệu', 3: 'tỷ'}

    def speak(num):
        if num in ['000', '00', '0']:
            lst.append('')
        elif num[1] is "0":
            if num[2] is '0':
                lst.append(vnnum[num[0]] + " trăm")
            else:
                lst.append(vnnum[num[0]] + " trăm linh " + vnnum[num[2]])
        elif num[1] is '1':
            if num[2] is '5':
                lst.append(vnnum[num[0]] + " trăm mười lăm")
            elif num[2] is '0':
                lst.append(vnnum[num[0]] + " trăm mười")
            else:
                lst.append(vnnum[num[0]] + " trăm mười " + vnnum[num[2]])
        elif num[2] is '1':
            lst.append(vnnum[num[0]] + " trăm " + vnnum[num[1]] + " mươi mốt")
        elif num[2] is '0':
            lst.append(vnnum[num[0]] + " trăm " + vnnum[num[1]] + " mươi")
        elif num[2] is '5':
            lst.append(vnnum[num[0]] + " trăm " + vnnum[num[1]] + " mươi lăm")
        else:
            lst.append(vnnum[num[0]] + " trăm " + vnnum[num[1]] + " mươi " + vnnum[num[2]])

    n = str(n)

    lst = []
    new_n = n[(len(str(n)) % 3):]
    k = n[:(len(str(n)) % 3)]

    if len(k) == 1:
        lst.append(vnnum[k])

    if len(k) == 2:
        if k[0] is '1':
            if k[1] is '5':
                lst.append('mười lăm')
            elif k[1] is "0":
                lst.append('mười')
            else:
                lst.append('mười ' + vnnum[k[1]])
        elif k[1] is '5':
            lst.append(vnnum[k[0]] + ' mươi lăm')
        elif k[1] is '0':
            lst.append(vnnum[k[0]] + ' mươi')
        elif k[1] is '1':
            lst.append(vnnum[k[0]] + " mươi mốt")
        else:
            lst.append(vnnum[k[0]] + ' mươi ' + vnnum[k[1]])

    for m in [new_n[i: i + 3] for i in range(0, len(new_n) - 1, 3)]:
        speak(m)

    lst_dao = lst[::-1]

    for pos in range(0, len(lst_dao)):
        if len(lst_dao[pos]) == 0:
            pass
        else:
            lst_dao[pos] = lst_dao[pos] + " " + vnaunit[lst_dao.index(lst_dao[pos])]

    result = " ".join(lst_dao[::-1]).replace("  ", " ").strip()

    if not isinstance(region, str) and not region is None:
        raise TypeError('Argument "region" is not a string')

    if not region is None and not region in ['north', 'south']:
        raise ValueError('Argument "region" has not a correct value')
    elif region is 'north':
        pass
    else:
        result = result.replace("nghìn", "ngàn").replace("linh", "lẻ")


    words = {}

    # if not isinstance(activate_tts, bool) and activate_tts is not None:
    #     raise TypeError('Argument "activate_tts" is not a boolean')
    # else activate_tts is False or activate_tts is None:
    #     pass

    if activate_tts is True:
        for word in result.split(' '):
            if not word in words:
                words[word] = pygame.mixer.Sound(os.path.join('/home/hdkhai/Devel/tien_khai/sounds/vie/north/' , '%s.ogg' %word))
            words[word].play()
        time.sleep(0.5)
    return result

# print(integer_to_vietnamese_numeral(10))
# print(integer_to_vietnamese_numeral(101, region='north'))
# print(integer_to_vietnamese_numeral(100, region='south', activate_tts=True))
print(integer_to_vietnamese_numeral(54648, region='north', activate_tts=True))
