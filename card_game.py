import random

cards = ['Черви_6', 'Черви_7', 'Черви_8', 'Черви_9', 'Черви_10', 'Черви_Валет', 'Черви_Дама', 'Черви_Король',
         'Черви_Туз',
         'Буби_6', 'Буби_7', 'Буби_8', 'Буби_9', 'Буби_10', 'Буби_Валет', 'Буби_Дама', 'Буби_Король', 'Буби_Туз',
         'Крести_6', 'Крести_7', 'Крести_8', 'Крести_9', 'Крести_10', 'Крести_Валет', 'Крести_Дама', 'Крести_Король',
         'Крести_Туз',
         'Вини_6', 'Вини_7', 'Вини_8', 'Вини_9', 'Вини_10', 'Вини_Валет', 'Вини_Дама', 'Вини_Король', 'Вини_Туз']


def card_del():
    for i in range(6):
        cards.remove(card_player[i])
        cards.remove(card_pc[i])


card_player = random.sample(cards, 6)
card_pc = random.sample(cards, 6)
print(f'Ваша карта: {card_player}')
if card_player == card_pc:
    print('Ошибка!')
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

for i in range(6):
    if random_mast == card_player[i][0:5]:  # Проверка для червей
        meaning_card_player += dict_card[card_player[i]] + 1000
    elif random_mast == card_player[i][0:4]:
        meaning_card_player += dict_card[card_player[i]] + 1000
    elif random_mast == card_player[i][0:6]:
        meaning_card_player += dict_card[card_player[i]] + 1000
    else:
        meaning_card_player += dict_card[card_player[i]]

    if random_mast == card_pc[i][0:5]:  # Проверка для червей
        meaning_card_pc += dict_card[card_pc[i]] + 1000
    elif random_mast == card_pc[i][0:4]:
        meaning_card_pc += dict_card[card_pc[i]] + 1000
    elif random_mast == card_pc[i][0:6]:
        meaning_card_pc += dict_card[card_pc[i]] + 1000
    else:
        meaning_card_pc += dict_card[card_pc[i]]

if meaning_card_player > meaning_card_pc:
    print('Пользователь победил')
elif meaning_card_player == meaning_card_pc:
    print('Одинаковые значения карт == недопустимо')
else:
    print('Пользователь проиграл')
