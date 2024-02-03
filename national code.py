import os
import time

try:
    run = 1
    while run:
        codes = {
            '001':'Tehran','002':'Tehran','003':'Tehran','004':'Tehran','005':'Tehran','006':'Tehran','007':'Tehran','008':'Tehran',
            '092':'Mashhad','093':'Mashhad','094':'Mashhad',
            '127':'Esfehan','128':'Esfehan','129':'Esfehan',
            '456':'Semnan','361':'Zahedan','362':'Zahedan',
            '228':'Shiraz','229':'Shiraz','230':'Shiraz',
            '136':'Tabriz','137':'Tabriz','138':'Tabriz',
            '338':'Bandar Abbas','339':'Bandar Abbas',
            '461':'Shahre Kord','462':'Shahre Kord',
            '406':'Khoram Abad','407':'Khoram Abad',
            '324':'Kermanshah','325':'Kermanshah',
            '422':'Boyerahmad','423':'Boyerahmad',
            '372':'Sanandaj','373':'Sanandaj',
            '274':'Orumieh','275':'Orumieh',
            '211':'Gorgaan','212':'Gorgaan',
            '386':'Hamedan','387':'Hamedan',
            '431':'Ghazvin','432':'Ghazvin',
            '067':'Bojnurd','068':'Bojnurd',
            '064':'Birjand','065':'Birjand',
            '349':'Bushehr','350':'Bushehr',
            '145':'Ardebil','146':'Ardebil',
            '427':'Zanjaan','428':'Zanjaan',
            '174':'Ahvaaz','175':'Ahvaaz',
            '298':'Kerman','299':'Kerman',
            '052':'Araak','053':'Araak',
            '208':'Saari','209':'Saari',
            '258':'Rasht','259':'Rasht',
            '031':'Karaj','032':'Karaj',
            '449':'Ilaam','450':'Ilaam',
            '442':'Yazd','443':'Yazd',
            '037':'Ghom','038':'Ghom'}

        def check(code):
            if len(code) != 10:
                print('It should be a 10 digit number!')
                return True
            x = 0
            for i in range(2,11):
                x += i * int(code[10-i])
            x %= 11
            if x < 2:
                if x != int(code[-1]):
                    print('Code is not valid!')
                    return True
                return False
            else:
                x = 11 - x
                if x != int(code[-1]):
                    print('Code is not valid!')
                    return True
                return False

        nc = input('Your 10 digit national code number: ')
        while check(nc):
            nc = input('Your 10 digit national code number: ')
        city = codes[nc[:3]]
        if os.path.exists('info.txt'):
            save = 1
            with open('info.txt','r') as info:
                lines = info.read().split('\n')
                for line in lines:
                    name,family,national_code = line.split(',')
                    if national_code == nc:
                        save = 0
                        print(f'Your information already exist.\nNational code: {national_code}\nFirst name: {name}\nLast name: {family}\nCity: {city}')
            if save:
                first_name = input('Your first name: ')
                last_name = input('Your last name: ')
                with open('info.txt','a') as info:
                    info.write(f'\n{first_name},{last_name},{nc}')
                print(f'Information saved!\nNational code: {nc}\nFirst name: {first_name}\nLast name: {last_name}\nCity: {city}')
        else:
            first_name = input('Your first name: ')
            last_name = input('Your last name: ')
            with open('info.txt','w') as info:
                info.write(f'{first_name},{last_name},{nc}')
            print(f'Information saved!\nNational code: {nc}\nFirst name: {first_name}\nLast name: {last_name}\nCity: {city}')
        run = input('Continue? (y/n): ')
        if run == 'y':
            run = 1
        elif run == 'n':
            run = 0
            print('Have a good day!')
            time.sleep(3)
        while run != 0 and run != 1:
            print('y means yes and n means no!')
            run = input('Continue? (y/n): ')
        if run == 'y':
            run = 1
        elif run == 'n':
            run = 0
            print('Have a good day!')
            time.sleep(3)
except:
    print("There is a problem here! Probably you didn't insert a number as the national code")