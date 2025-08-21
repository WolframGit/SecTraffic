import requests, webbrowser, platform, os
from datetime import datetime as dt
from time import sleep as s
from time import time as t
from pystyle import Colors, Colorate
from colorama import Fore, init
init()

#Задаем переменные для уодобного переключения цвета
BLUE = Fore.LIGHTBLUE_EX
RED = Fore.LIGHTRED_EX
RESET = Fore.RESET

def target(ram):
    try:
        date_time = dt.now()
        url = f'https://speedtest.selectel.ru/{ram}'
        print(f' [!] Target activated! - ({date_time.hour}:{date_time.minute}:{date_time.second})')
    
        #Вычисление времени и запрос
        start = t()
        response = requests.get(url)
        end = t()
        fullTime = end - start
    
        #Итог по времени выполнения
        print(f' [~] Время выполнение кода - {fullTime:.0f} sec\n')
        returner()
    except KeyboardInterrupt:
        print(' [!] EXIT!!!')
        exit

def returner():
    #Конечный вопрос в функции
    endF = input(' [?] Хотите вернуться обратно? (y/n): ')
    
    if endF in ('y', 'н'):
        print(' [!] Возвращаем вас обратно...')
        s(2) 
        os.system('cls' if name == 'Windows' else 'clear')
        main()
            
    elif endF in ('n', 'т'):
        print(' [!] Выходим...')
        s(2)
        exit()
    
    else:
        print(' [!] Неправильная опция! Возвращаем вас обратно...')
        s(2)
        
        os.system('cls' if name == 'Windows' else 'clear')
        main()

def main():
    
    banner = r'''
 _______ _______ _______ _______  ______ _______ _______ _______ _____ _______
 |______ |______ |          |    |_____/ |_____| |______ |______   |   |      
 ______| |______ |_____     |    |    \_ |     | |       |       __|__ |_____ 
 
 [1] Downloading 10MB
 [2] Downloading 100MB
 [3] Downloading 1GB
 [4] Downloading 10GB'''
    print(Colorate.Vertical(Colors.red_to_purple, banner, 2))
    option = ['-', '10MB', '100MB', '1GB', '10GB']
    int_option = [1, 2, 3, 4]
    results = int(input(f'\n{BLUE} [!] Введите опцию -> '))

    if results in int_option:
        target(option[results])
        
global name
name = platform.system()

if __name__ == '__main__':
    main()

