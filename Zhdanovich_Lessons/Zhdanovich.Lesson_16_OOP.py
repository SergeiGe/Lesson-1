
# Описать два метода в классе,
# один принимает в себя либо строку, либо число.
# Если я передаю строку, то смотрим:
# если произведение количества гласных и согласных букв меньше или равно длине слова,
# то выводить все гласные, иначе согласные;
# если передаю число, то вывести произведение суммы чётных цифр на длину числа.
# В первом методе запрещено использовать функцию len.
# Длину строки или числа искать во втором методе.



class Str_Chislo:
    def __init__(self, string):
        self.string = string
        # print(self.string)

    def get_str_chislo(self):
        if type(self.string) == str:
            self.glas = 0
            self.soglas = 0
            self.gl = []
            self.sogl = []

            for i in self.string:
                if i.lower() in 'аоиыеёэуюяaeiou':
                    self.glas += 1
                    self.gl.append(i)
                elif i.isalpha():
                    self.soglas += 1
                    self.sogl.append(i)

            if self.glas * self.soglas <= dlina_stroki():
                print('Все гласные:', self.gl)
            else:
                print('Все согласные:', self.sogl)

        elif type(self.string) == int:
            self.sum_chet = 0

            for i in str(self.string):
                if int(i)%2 == 0:
                    self.sum_chet += int(i)
                    print("Произведение суммы четных чисел на длину числа равно: ",self.sum_chet * dlina_stroki())


    def dlina_stroki(self):
        self.dlina = len(self.string)
        print(self.dlina)

# my_Str_Num = Str_Chislo('Тестовая строка')
my_Str_Num = Str_Chislo(123)

























