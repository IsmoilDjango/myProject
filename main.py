# numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18]
# numbers_kv = []
# for i in numbers:
#     if i % 2 == 0:
#         numbers_kv.append(i**2)
# print(numbers_kv)
# eng_katta = max(numbers_kv)
# eng_kichik = min(numbers_kv)
# print(f"Eng katta qiymat: {eng_katta}, \nEng kichik qiymat: {eng_kichik}")

# fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
# fruits_len = []
#
# for i in fruits:
#     if len(i)<5:
#         fruits_len.append(i)
# print(fruits_len)

# numbers = [10, 5, 20, 15, 30]
# a = 12
# numbers1 = []
# for i in numbers:
#     if i>a:
#         numbers1.append(i)
# print(numbers1)

# class BankHisobi:
#     def __init__(self, ism, balans=0):
#         self.ism = ism
#         self.__balans = balans
#
#     def balansni_korish(self):
#         return f"{self.ism} hisobidagi balans: {self.__balans} so'm"
#     def depozit(self, summa):
#         self.__balans += summa
#         return f"{summa} so'm qo'shildi. Yangi balans: {self.__balans} so'm"
#
#     def yechib_olish(self, summa):
#         if summa > self.__balans:
#             return "Balans yetarli emas"
#         self.__balans -= summa
#         return f"{summa} so'm yechildi. Qolgan balans: {self.__balans} so'm"
#
# hisob = BankHisobi("Ismoil", 5000)
# print(hisob.balansni_korish())  # Natija: Ismoil hisobidagi balans: 5000 so'm
# print(hisob.depozit(2000))       # Natija: 2000 so'm qo'shildi. Yangi balans: 7000 so'm
# print(hisob.yechib_olish(3000))  # Natija: 3000 so'm yechildi. Qolgan balans: 4000 so'm



# Inkapsulyatsiya (Encapsulation)
# class BankHisobi:
#     def __init__(self, balans):
#         self.__balans = balans  # Yashirin atribut
#
#     def balansni_korish(self):
#         return self.__balans
#
#     def depozit(self, summa):
#         self.__balans += summa
#         return self.__balans
#
# hisob = BankHisobi(1000)
# print(hisob.balansni_korish())  # Natija: 1000
# hisob.depozit(500)
# print(hisob.balansni_korish())  # Natija: 1500

# Yashirin atributga to‘g‘ridan-to‘g‘ri kirish xato bo‘ladi:
# print(hisob.__balans)  # AttributeError


# 3.2. Meros olish (Inheritance)
# Meros olish bir klassdan boshqa klassga metod va atributlarni meros qilib olish imkonini beradi.
# class Hayvon:
#     def __init__(self, nom):
#         self.nom = nom
#
#     def tovush(self):
#         return "Tovush yo'q"
#
# class It(Hayvon):  # Meros olish
#     def tovush(self):
#         return "Vov-vov"
#
# class Mushuk(Hayvon):  # Meros olish
#     def tovush(self):
#         return "Miyov-miyov"
#
# it = It("Alabay")
# mushuk = Mushuk("Persian")
# print(it.tovush())     # Natija: Vov-vov
# print(mushuk.tovush()) # Natija: Miyov-miyov

# Polimorfizm (Polymorphism)
# Polimorfizm bir xil nomli metodlar turli obyektlar uchun har xil ishlashiga imkon beradi.

# class Hayvon:
#     def tovush(self):
#         pass
# class It(Hayvon):
#     def tovush(self):
#         return "Vov-vov"
# class Mushuk(Hayvon):
#     def tovush(self):
#         return "Miyov-miyov"
# def tovushni_eshit(hayvon):
#     print(hayvon.tovush())
#
# it = It()
# mushuk = Mushuk()
# tovushni_eshit(it)      # Natija: Vov-vov
# tovushni_eshit(mushuk)  # Natija: Miyov-miyov


# Abstraksiya (Abstraction)

# Abstraksiya yordamida faqat muhim ma'lumotlarni ko‘rsatib, ortiqcha detallar yashiriladi. Python'da abstraksiya uchun abc moduli ishlatiladi.
#
# from abc import ABC, abstractmethod
#
# class Hayvon(ABC):
#     @abstractmethod
#     def tovush(self):
#         pass
#
# class It(Hayvon):
#     def tovush(self):
#         return "Vov-vov"
#
# class Mushuk(Hayvon):
#     def tovush(self):
#         return "Miyov-miyov"
#
# it = It()
# print(it.tovush())  # Natija: Vov-vov
#
# mushuk = Mushuk()
# print(mushuk.tovush())  # Natija: Miyov-miyov


# OOP kodni modulga bo‘lish va boshqarishni soddalashtiradi.
# Klasslar obyektlar uchun andoza bo‘lib xizmat qiladi.
# Meros olish, polimorfizm, inkapsulyatsiya va abstraksiya OOPning asosiy elementlari.
# OOP yirik va murakkab dasturlarni tuzishda juda qulay.



# numbers = [5,10,15,20,25]
# nums_or = []
# nums = []
# for i in numbers:
#     nums_or.append(i/2)
# print(nums_or)
#
# for j in range(len(nums_or)):
#     if j == 0:
#         nums.append(nums_or[j]+nums_or[j+1])
#     elif j != 0 and j != len(nums_or)-1:
#         nums.append(nums_or[j-1]+nums_or[j+1])
#     elif j == len(nums_or)-1:
#         nums.append(nums_or[j]+nums_or[j-1])
#     else:
#         print("List bo'sh!")
# print(len(nums_or))
# print(nums)

# nums = [1,2,3]
# nums_sub = []
# for i in range(len(nums)):
#     for j in range(i+1, len(nums) + 1):
#         if j - i >= 2:
#             nums_sub.append(nums[i:j])
#
# nums_sub.sort(key=len)
# print(nums_sub)

# data = [[3, 5, 8], [10, 'a', 15], [4, -1, 6], ['x', 9, 0]]
# # list ichidagi eonlar yig'indisini topish
# s = 0
# def summa():
#     for i in data:
#         for j in i:
#             if type(j) == int:
#                 global s
#                 s +=j
# summa()
# print(s)
#
# # teskarisni topsh
# reverse_data = []
# def reverse():
#     for i in data:
#         reversed_i = list(reversed(i))
#         reverse_data.append(reversed_i)
#
# reverse()
# print(reverse_data)
#
# # eng kattasini topish
# max_data = []
# def maximum():
#     for i in data:
#         for j in i:
#             if type(j) == int:
#                 max_data.append(j)
# maximum()
# print(max(max_data))

# # ixchamlashgan dastur kodi
# data = [[3, 5, 8], [10, 'a', 15], [4, -1, 6], ['x', 9, 0]]
#
# def summa(data):
#     return sum(j for i in data for j in i if isinstance(j, int))
# print(summa(data))
#
# def reverse(data):
#     return [list(reversed(i)) for i in data]
# print(reverse(data))
#
# def maximum(data):
#     return max(j for i in data for j in i if isinstance(j, int))
# print(maximum(data))

# mahsulot = ['olma', 'anor', 'apelsin']
# # lists methods
# add = input("Qo'shadigan mahsulot nomini kiriting:")
#
# if add in mahsulot:
#     print(f"{add} ni qo'sha olmaysiz. Chunki, u mahsulot ro'yhatida bor")
# else:
#     mahsulot.append(add)
#     print(f"{add} ro'yhatga qo'shildi:\n {mahsulot}")
#
# remove = input("Olib tahslanadigan mahsulot nomini kiriting:")
# if remove not in mahsulot:
#     print(f"{remove} ro'yhatda yo'q")
# else:
#     mahsulot.remove(remove)
#     print(f"{remove} olib tashlandi.\nQolgan mahsulotlar: {mahsulot}")
#
# index = input("Indexsini topish kerak bo'lgan mahsulotni kiriting:")
# if index in mahsulot:
#     print(f"Mahsulotning ro'yhatdagi indexsi: {mahsulot.index(index)}")
# else:
#     print("Ushbu mahsulot ro'yhatda yo'q")



# talabalarni baholash
# dict = {"ismoil":90, "laylo":87}


























