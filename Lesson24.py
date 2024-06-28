# # 1․ Գրել ծրագիր, որը․
# #    - կգեներացնի պատահական 10 մարդու տվյալներ, որոնք կպարունակեն հետևյալ ինֆորմացիան՝
# #      -- անունը,
# #      -- ազգանունը,
# #      -- ծննդյան տարին, ամիսը, ամսաթիվը,
# #      -- երկիրը,
# #      -- քաղաքը,
# #      -- մազերի գույնը,
# #      -- աշխատանքի տեսակը (մասնագիտությունը),
# #      տվյալները կարող են լինել հայերեն։
# from faker import Faker
# fake = Faker(locale='hy_AM')
# for i in range(11):
#     print(fake.first_name(), fake.last_name_female(),
#           fake.date_of_birth(), fake.address(), fake.color_name(), fake.job(), sep='\n')
# 3․ Գրել դեկորատոր ֆունկցիա, որը կփոփոխի
# հետևյալ ֆունկցիան այնպես, որ. - այն կաշխատի միայն ժամը 10։00 - ից 19։00 ընկած ժամանակահատվածում աշխատեցնելիս, - եթե
# նշված ժամանակահատվածից դուրս ենք կանչում ֆունկցիան, պետք է տպի ("Sorry, it's too late .", - եթե ճիշտ ժամի  կանչած ֆունկցիան, պետք է տպի
# #  նաև) ֆունկցիան կանչելու ժամանակը՝ տարին, ամիսը, օրը, ժամը, րոպեն, ֆունկցիան՝
# import time
#
#
# def decorator(func):
#     def inner(y):
#         if time.strptime('10:00', '%H:%M') <= time.localtime() <= time.strptime('19:00', '%H:%M'):
#             func(y)
#         else:
#             print("Sorry, it's too late .")
#
#     return inner
#
#
# @decorator
# def f(text):
#     print(f'Welcome {text}!')
#
#
# f('Team')
# 2․ Գրել ծրագիր, որը․
#    - հետևյալ dict_1-ից կստանա նոր dict_2 այնպես, որ dict_2-ի key-երը լինեն dict_1-ի value-ները,
#      իսկ value-ները՝ dict_1-ի value-ների երկարությունները,
#    օրինակ՝ dict_1 = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'},
#    պետք է ստացվի՝ dict_2 = {'red': 3, 'green': 5, 'black': 5, 'white': 5}:
# dict_1 = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# dict_2 = {}
# for k, v in dict_1.items():
#     dict_2[v] = len(v)
# print(dict_2)
# 3. Գրել ֆունկցիա, որը․
#    - կֆիլտրի տրված dictionary-ի value-ները, թողնելով միայն կենտ թվերը,
#    - կվերադարձնի ստացված dictionary-ն,
#    օրինակ՝ {'a': [1, 8, 3, 7, 2], 'b': [12, 4, 8, 4], 'c': [9, 9, 2, 8, 5]},
#    պետք է ստացվի՝ {'a': [1, 3, 7], 'b': [], 'c': [9, 9, 5]}:
# dict_1 = {'a': [1, 8, 3, 7, 2], 'b': [12, 4, 8, 4], 'c': [9, 9, 2, 8, 5]}
# dict_2 = {}
# for k, v in dict_1.items():
#     l_1 = []
#     for _ in v:
#         if _ % 2 == 1:
#             l_1.append(_)
#     dict_2[k] = l_1
# print(dict_2)
# 1․ Գրել հետևյալ ծրագիրը․
#    - բացել jupyter notebook-ը,
#    - գեներացնել list, որը կպարունակի 1-ից 1_000_000 միջակայքում գտնվող կենտ թվերը,
#    - պահել գեներացված list-ը համապատասխան ֆորմատով համակարգչի մեջ data անունով,
#    - բացել pycharm-ը,
#    - pycharm-ում կարդալ data ֆայլը,
#    - կարդացած list-ում կթողնի միայն 3-ի բաժանվող թվերը,
#    - կտպի ստացված list-ի արժեքների միջին թվաբանականը։
# import pickle
# with open('Untitled.ipynb', 'rb') as file:
#     odd_numbers = pickle.load(file)
# divisi_by_three = [i for i in odd_numbers if i % 3 == 0]
# print(sum(divisi_by_three) / len(divisi_by_three))
# Ex1
# import string
#
#
# def get_avr_length_of_words(text):
#     f = map(lambda x: len(x), map(lambda x: x.strip(string.punctuation), text.split(',')))
#     return sum(list(f)) / len(list(f))
#
#
# print(get_avr_length_of_words('Hello worldd!!!'))
# Ex 2
# def rec_pow(k):
#     if not k:
#         return 1
#     return rec_pow(k - 1) * k
#
#
# def rec_answer(array):
#     answer = []
#     for i in array:
#         answer.append()
#
#
# print(rec_answer([1, 5, 4, 2]))
# Ex 3
import string

# nums = [1, 5, 2, 8, 5, 6, 5, 2, 9, 6]
# l_1 = []
# for i in range(1, len(nums) + 1):
#     if i not in nums:
#         l_1.append(i)
#
# print(l_1)
# 1․ Գրել ֆունկցիա, որը․
#    - որպես արգումենտ կընդունի շրջանագծի շառավիղը (r) և սեկտորի անկյունը (alpha) ռադիաններով արտահայտված,
#    - կհաշվի և կտպի համապատասխան շառավղով և անկյունով սեկտորի մակերեսը,
#    - բանաձևը՝ S = (pi * r ** 2) * alpha / 360, բանաձևի մեջ alpha-ն արտահայտված է աստիճաններով։
# import math
#
#
# def circle_sector(r, alpha):
#     return (math.pi * r ** 2) * math.radians(alpha) / 360
#
#
# print(circle_sector(45, 5))

# 3․ Գրել ֆունկցիա, որը․ - տրված բառերի list - ը կֆիլտրի այնպես, որ կթողի միայն ամենաերկար
# բառերը (այսինքն՝ կգտնի ամենաերկար բառի երկարությունը և լիստում կթողնի միայն այդ երկարության բառերը),
# օրինակ՝ input = ["aba", "aa", "z", "ad", "vcd", "aba"]
# output = ["aba", "vcd", "aba"],
# input = ["aba", "aa", "z", "advc", "vcd", "aba"]
# output = ["advc"],
# from functools import reduce
#
# input_1 = ["aba", "aa", "z", "ad", "vcd", "aba"]
# long_verb = reduce(lambda x, y: x if len(x) > len(y) else y, input_1)
# h = filter(lambda h: len(h) == len(long_verb), input_1)
# print(list(h))
# import timeit
#
#
# def f(n):
#     product = 1
#     for i in range(1, n + 1):
#         product *= i
#     return product
#
#
# execution = timeit.timeit('f(100)', globals=globals(), number=100000)
# print(execution)
# class Person:
#     hands = 2
#     legs = 2
#
#     def __init__(self, name, username, age):
#         self.name = name
#         self.username = username
#         self.age = age
#
#     def run(self, m):
#         print(f'{self.name} run {m}, metr')
#
#     def __str__(self):
#         return f'{self.name} {self.username}'
#
#
# p1 = Person('Vazgen', 'Asryan', '21')
# p2 = Person('Gexam', 'Bazinyan', '10')
# print(p1.name)
# print(p1.__dict__)
# p1.run(10)
# print(p1)
# print(p2)


# class Triangle:
#     def __init__(self, a, b, c):
#         self.A = a
#         self.B = b
#         self.C = c
#         if self.A + self.C > self.B and self.A + self.B > self.C and self.C + self.B > self.A:
#             print('Valid triangle')
#         else:
#             print('Error not find triangle!')
#
#     def __str__(self):
#         return f'Triangle is a = {self.A}, b = {self.B}, c = {self.C}, P = {self.A + self.B + self.C}, S = {(self.A * self.B / 2)}'
#
#     def triangle(self, a, b, c):
#         if self.A == self.B == self.C:
#             return f'triangle is equal'
#         else:
#             return 'Not equal'
#
#     def squer_triangle(self, a, b, c):
#         if self.A ** 2 + self.B ** 2 == self.C ** 2:
#             return 'triangle is squertriangle'
#         else:
#             return 'not squertriangle'
