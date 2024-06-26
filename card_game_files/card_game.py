# Код ошибки: 1 - Одинаковые карты
# Код ошибки: 2 - Не смогли удалить полученые карты из списка карт
# Код ошибки: 3 - Не засчитана победа
# Код ошибки: 4 - Элемент не найден в списке
import random
from card_game_files.cards_colod import cards, dict_card

card_player = random.sample(cards, 6)
card_pc = random.sample(cards, 6)
cards = ['Черви_6', 'Черви_7', 'Черви_8', 'Черви_9', 'Черви_10', 'Черви_Валет', 'Черви_Дама', 'Черви_Король',
         'Черви_Туз',
         'Буби_6', 'Буби_7', 'Буби_8', 'Буби_9', 'Буби_10', 'Буби_Валет', 'Буби_Дама', 'Буби_Король', 'Буби_Туз',
         'Крести_6', 'Крести_7', 'Крести_8', 'Крести_9', 'Крести_10', 'Крести_Валет', 'Крести_Дама', 'Крести_Король',
         'Крести_Туз',
         'Вини_6', 'Вини_7', 'Вини_8', 'Вини_9', 'Вини_10', 'Вини_Валет', 'Вини_Дама', 'Вини_Король', 'Вини_Туз']
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


def error():
    if card_player == card_pc:
        print('Техническая ошибка!  Перезапустите игру! Код ошибки: 1')
    while len(cards) > 24:
        try:
            for card in card_player:
                cards.remove(card)

            for card in card_pc:
                cards.remove(card)
        except ValueError:
            print(f'Техническая ошибка! Перезапустите игру! Код ошибки: 2')


def error_card():
    # Проверка на ошибки в колодах
    if len(set(card_player)) < 6 or len(set(card_pc)) < 6:
        print('Техническая ошибка!  Перезапустите игру! Код ошибки: 1')


def find_index(lst, value):
    try:
        index = lst.index(value)
        return index
    except ValueError:
        print('Техническая ошибка! Код ошибки: 4')


def del_card():
    card_player.remove(choice_player)
    card_pc.remove(choice_pc)
    index_player = cards.index(choice_player)
    index_pc = cards.index(choice_pc)
    try:
        cards.pop(index_player)
        cards.pop(index_pc)
    except:
        cards.remove(choice_player)
        cards.remove(choice_pc)
    finally:
        del cards[index_player]
        del cards[index_pc]
error()
choice_pc = random.choice(card_pc)
while len(card_player) > 0 and len(card_pc) > 0:
    try:
        error_card()
        print(f'Раунд: {round_number}')
        round_number += 1
        print(f'В колоде осталось {len(cards)} карт.')
        print('Ваши карты: ', card_player)
        choice_player = input('Введите карту которой хотите сходить: ')
        while choice_player not in card_player:
            print('У вас нет такой карты!')
            choice_player = input('Введите карту которой хотите сходить: ')
        for card in card_pc:
            choice_pc = random.choice(card_pc)
            if choice_pc[0] == choice_player[0] or random_mast[0] == choice_pc[0]:
                break
        error_card()
        if choice_pc[0] == choice_player[0] or random_mast[0] == choice_pc[0]:
            meaning_card_player = dict_card[choice_player]
            meaning_card_pc = dict_card[choice_pc]
            if random_mast[0] == choice_player[0]:
                meaning_card_player += dict_card[choice_player] + 1000

            if random_mast[0] == choice_pc[0]:
                meaning_card_pc += dict_card[choice_pc] + 1000

            print(f'Игрок ходит картой {choice_player}, а компьютер {choice_pc}:')
            if meaning_card_player > meaning_card_pc:
                print('Игрок выйграл этот раунд.')
                win_player += 1
                del_card()
            elif meaning_card_player == meaning_card_pc:
                print('Одинаковые значения карт == недопустимо.')
                continue

            elif meaning_card_player < meaning_card_pc:
                print('Компьютер выйграл этот раунд.')
                win_pc += 1
                del_card()

            else:
                print('Техническая ошибка! Перезапустите игру! Код ошибки: 3')
                del_card()
            if len(cards) > 0:
                if len(card_player) < 6:
                    card_player.extend(random.sample(cards, 6 - len(card_player)))
                if len(card_pc) < 6:
                    card_pc.extend(random.sample(cards, 6 - len(card_pc)))
                error_card()
                error()
        elif choice_pc[0] != choice_player[0] and random_mast[0] != choice_pc[0]:
            for card in card_pc:
                choice_pc = random.choice(card_pc)
                if choice_pc[0] == choice_player[0] or random_mast[0] == choice_pc[0]:
                    error_card()
                    break
            else:
                card_pc.append(choice_player)
                print('Компютер берёт карты')
                card_player.remove(choice_player)
                card_pc.remove(choice_pc)
                error_card()
            continue
        else:
            card_pc.append(choice_player)
            print('Компютер берёт карты')
            card_player.remove(choice_player)
            card_pc.remove(choice_pc)
            error_card()
    except:
        if len(card_player) < 6:
            card_player.extend(random.sample(cards, 6 - len(card_player)))
        if len(card_pc) < 6:
            card_pc.extend(random.sample(cards, 6 - len(card_pc)))

if win_player > win_pc:
    print(f'Поздравляем! Игрок победил компьютер со счетом {win_player}:{win_pc}')
elif win_player < win_pc:
    print(f'Компьютер победил! Результат {win_player}:{win_pc}')
else:
    print('Ничья!')

# TODO добавить коректировки
# TODO добавить try обработчик ошибок
# TODO разобраться с проблемой в конце игры
