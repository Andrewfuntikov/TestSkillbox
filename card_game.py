import random

cards = ['Черви_6', 'Черви_7', 'Черви_8', 'Черви_9', 'Черви_10', 'Черви_Валет', 'Черви_Дама', 'Черви_Король',
         'Черви_Туз',
         'Буби_6', 'Буби_7', 'Буби_8', 'Буби_9', 'Буби_10', 'Буби_Валет', 'Буби_Дама', 'Буби_Король', 'Буби_Туз',
         'Крести_6', 'Крести_7', 'Крести_8', 'Крести_9', 'Крести_10', 'Крести_Валет', 'Крести_Дама', 'Крести_Король',
         'Крести_Туз',
         'Вини_6', 'Вини_7', 'Вини_8', 'Вини_9', 'Вини_10', 'Вини_Валет', 'Вини_Дама', 'Вини_Король', 'Вини_Туз']

card_player = random.sample(cards, 6)
card_pc = random.sample(cards, 6)


def error():
    if card_player == card_pc:
        print('Техническая ошибка! \n Перезапустите игру!\n Код ошибки: 1')


dict_card = {'Черви_6': 100,
             'Черви_7': 110,
             'Черви_8': 120,
             'Черви_9': 130,
             'Черви_10': 140,
             'Черви_Валет': 150,
             'Черви_Дама': 160,
             'Черви_Король': 170,
             'Черви_Туз': 180,
             'Буби_6': 100,
             'Буби_7': 110,
             'Буби_8': 120,
             'Буби_9': 130,
             'Буби_10': 140,
             'Буби_Валет': 150,
             'Буби_Дама': 160,
             'Буби_Король': 170,
             'Буби_Туз': 180,
             'Крести_6': 100,
             'Крести_7': 110,
             'Крести_8': 120,
             'Крести_9': 130,
             'Крести_10': 140,
             'Крести_Валет': 150,
             'Крести_Дама': 160,
             'Крести_Король': 170,
             'Крести_Туз': 180,
             'Вини_6': 100,
             'Вини_7': 110,
             'Вини_8': 120,
             'Вини_9': 130,
             'Вини_10': 140,
             'Вини_Валет': 150,
             'Вини_Дама': 160,
             'Вини_Король': 170,
             'Вини_Туз': 180}

mast = ['Черви', 'Буби', 'Крести', 'Вини']
random_mast = random.choice(mast)
print(f'Козырная масть: {random_mast}')

meaning_card_player = 0
meaning_card_pc = 0
win_pc = 0
win_player = 0
round_number = 1

while len(card_player) > 0 and len(card_pc) > 0:
    try:
        error()
        print(f'Раунд: {round_number}')
        round_number += 1
        print(f'В колоде осталось {len(cards)} карт.')  # Печатаем количество карт в колоде
        print('Ваши карты: ', card_player)
        choice_player = input('Введите карту которой хотите сходить: ')
        while choice_player not in card_player:  # Проверка на ввод карты, которой нет у игрока
            print('У вас нет такой карты!')
            choice_player = input('Введите карту которой хотите сходить: ')
        choice_pc = random.choice(card_pc)
        card_player.remove(choice_player)  # Удаление карты игрока из списка
        card_pc.remove(choice_pc)  # Удаление карты компьютера из списка
        cards.remove(choice_player)  # Удаление карты из колоды
        cards.remove(choice_pc)  # Удаление карты из колоды
        if random_mast == choice_player[0:5]:  # Проверка для червей
            meaning_card_player += dict_card[choice_player] + 1000
        elif random_mast == choice_player[0:4]:
            meaning_card_player += dict_card[choice_player] + 1000
        elif random_mast == choice_player[0:6]:
            meaning_card_player += dict_card[choice_player] + 1000
        else:
            meaning_card_player += dict_card[choice_player]

        if random_mast == choice_pc[0:5]:  # Проверка для червей
            meaning_card_pc += dict_card[choice_pc] + 1000
        elif random_mast == choice_pc[0:4]:
            meaning_card_pc += dict_card[choice_pc] + 1000
        elif random_mast == choice_pc[0:6]:
            meaning_card_pc += dict_card[choice_pc] + 1000
        else:
            meaning_card_pc += dict_card[choice_pc]

        print(f'Игрок ходит картой {choice_player}, а компьютер {choice_pc}:')

        if meaning_card_player > meaning_card_pc:
            print('Пользователь выйграл этот раунд.')
            win_player += 1
        elif meaning_card_player == meaning_card_pc:
            print('Одинаковые значения карт == недопустимо.')
        elif meaning_card_player > meaning_card_pc:
            print('Компьютер выйграл этот раунд.')
            win_pc += 1
        else:
            ('Пользователь проиграл.')
            win_pc += 1

        # Пополнение карт до 6
        if len(card_player) < 6:
            card_player.extend(random.sample(cards, 6 - len(card_player)))
        if len(card_pc) < 6:
            card_pc.extend(random.sample(cards, 6 - len(card_pc)))
    except:
        continue
        # Пополнение карт до 6
        if len(card_player) < 6:
            card_player.extend(random.sample(cards, 6 - len(card_player)))
        if len(card_pc) < 6:
            card_pc.extend(random.sample(cards, 6 - len(card_pc)))

if win_pc > win_player:
    print('Увы.... \n Компьютер выйграл.')
else:
    print('Вы выйграли поздравляю!')

# TODO добавить удаление карт из списка до цикла
# TODO добавить коректировки
# TODO добавить try обработчик ошибок
# TODO разобраться с проблемой в конце игры
# TODO Откоректировать текст
# TODO откоректирвоать error()
# TODO спрыгнуть с крыши