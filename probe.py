import random

cards = ['Черви_6', 'Черви_7', 'Черви_8', 'Черви_9', 'Черви_10', 'Черви_Валет', 'Черви_Дама', 'Черви_Король',
         'Черви_Туз',
         'Буби_6', 'Буби_7', 'Буби_8', 'Буби_9', 'Буби_10', 'Буби_Валет', 'Буби_Дама', 'Буби_Король', 'Буби_Туз',
         'Крести_6', 'Крести_7', 'Крести_8', 'Крести_9', 'Крести_10', 'Крести_Валет', 'Крести_Дама', 'Крести_Король',
         'Крести_Туз',
         'Вини_6', 'Вини_7', 'Вини_8', 'Вини_9', 'Вини_10', 'Вини_Валет', 'Вини_Дама', 'Вини_Король', 'Вини_Туз']

card_player = random.sample(cards, 6)
card_pc = random.sample(cards, 6)
choice_player = input('Введите карту которой хотите сходить: ')

choice_pc = random.choice(card_pc)


index_player = cards.index(choice_player)
index_pc = cards.index(choice_pc)
cards.pop(index_player)
cards.pop(index_pc)
print(len(cards))