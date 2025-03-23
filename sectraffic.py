import requests
import os
import platform
from time import sleep as s
from time import time as t
from pystyle import Colors, Colorate
from colorama import Fore, init
init()

#ЗАХОДИ НА НАШ КАНАЛ!!! (tg: @DecryptageTeam)

#Задаем переменные для уодобного переключения цвета
BLUE = Fore.LIGHTBLUE_EX
RED = Fore.LIGHTRED_EX
RESET = Fore.RESET

def d10m():
    url = 'https://speedtest.selectel.ru/10MB'
    name = platform.system()
    
    #Вычисление времени и запрос
    start = t()
    response = requests.get(url)
    end = t()
    fullTime = end - start
    
    #Итог по времени выполнения
    print(f' [~] Время выполнение кода - {fullTime:.0f} sec\n')
    
    #Конечный вопрос в функции
    endF = input(' [?] Хотите вернуться обратно? (y/n): ')
    if endF == 'y' or 'н':
        print(' [!] Возвращаем вас обратно...')
        s(2) 
        os.system('cls' if name == 'Windows' else 'clear')
        main()
            
    elif endF == 'n' or 'т':
        print(' [!] Выходим...')
        s(2)
    
    else:
        print(' [!] Неправильная опция! Возвращаем вас обратно...')
        s(2)
        
        os.system('cls' if name == 'Windows' else 'clear')
        main()
            
def d100m():
    url = 'https://speedtest.selectel.ru/100MB'
    name = platform.system()
    
    #Вычисление времени и запрос
    start = t()
    response = requests.get(url)
    end = t()
    fullTime = end - start
    
    #Итог по времени выполнения
    print(f' [~] Время выполнение кода - {fullTime:.0f} sec\n')
    
    #Конечный вопрос в функции
    endF = input(' [?] Хотите вернуться обратно? (y/n): ')
    if endF == 'y' or 'н':
        print(' [!] Возвращаем вас обратно...')
        s(2) 
        
        os.system('cls' if name == 'Windows' else 'clear')
        main()
            
    elif endF == 'n' or 'т':
        print(' [!] Выходим...')
        s(2)
    
    else:
        print(' [!] Неправильная опция! Возвращаем вас обратно...')
        s(2)
        
        os.system('cls' if name == 'Windows' else 'clear')
        main()
def d1g():
    url = 'https://speedtest.selectel.ru/1GB'
    name = platform.system()
    
    #Вычисление времени и запрос
    start = t()
    response = requests.get(url)
    end = t()
    fullTime = end - start
    
    #Итог по времени выполнения
    print(f' [~] Время выполнение кода - {fullTime:.0f} sec\n')
    
    #Конечный вопрос в функции
    endF = input(' [?] Хотите вернуться обратно? (y/n): ')
    if endF == 'y' or 'н':
        print(' [!] Возвращаем вас обратно...')
        s(2) 
        os.system('cls' if name == 'Windows' else 'clear')
        main()
            
    elif endF == 'n' or 'т':
        print(' [!] Выходим...')
        s(2)
    
    else:
        print(' [!] Неправильная опция! Возвращаем вас обратно...')
        s(2)
        
        os.system('cls' if name == 'Windows' else 'clear')
        main()

def d10g():
    url = 'https://speedtest.selectel.ru/10GB'
    name = platform.system()
    
    #Вычисление времени и запрос
    start = t()
    response = requests.get(url)
    end = t()
    fullTime = end - start
    
    #Итог по времени выполнения
    print(f' [~] Время выполнение кода - {fullTime:.0f} sec\n')
    
    #Конечный вопрос в функции
    endF = input(' [?] Хотите вернуться обратно? (y/n): ')
    if endF == 'y' or 'н':
        print(' [!] Возвращаем вас обратно...')
        s(2) 
        
        os.system('cls' if name == 'Windows' else 'clear')
        main()
            
    elif endF == 'n' or 'т':
        print(' [!] Выходим...')
        s(2)
    
    else:
        print(' [!] Неправильная опция! Возвращаем вас обратно...')
        s(2)
        
        os.system('cls' if name == 'Windows' else 'clear')
        main()

def main():
    banner = '''
 _______ _______ _______ _______  ______ _______ _______ _______ _____ _______
 |______ |______ |          |    |_____/ |_____| |______ |______   |   |      
 ______| |______ |_____     |    |    \_ |     | |       |       __|__ |_____ 
 
 [1] Downloading 10MB
 [2] Downloading 100MB
 [3] Downloading 1GB
 [4] Downloading 10GB'''
    print(Colorate.Vertical(Colors.red_to_purple, banner, 2))
    results = input(f'\n{BLUE} [!] Введите опцию -> ')

    if results == '1':
        d10m()

    elif results == '2':
        d100m()
    
    elif results == '3':
        d1g()

    elif results == '4':
        d10g()

    else:
        print(f'{RED} [-] Ошибка! Перезапуск...')
        s(2)
        os.system('cls')
        main()
        
main()
