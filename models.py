# -*- coding: UTF-8 -*-



class Profile(object):
    """Class for profiles"""
    def __init__(self, name, phone, company):
        self.name = name
        self.phone = phone
        self.company = company
        self.__likes = 0

    def print_profile(self):
        print 'Name: %s, Phone: %s, Cia: %s' % (self.name, self.phone, self.company)

    def count_likes(self):
        self.__likes+=1

    def get_likes(self):
        return self.__likes

    @classmethod
    def gen_from_csv(classe, name_file):
        file = open(name_file,'r')
        profiles = []
        for line in file:
            values = line.split(',')
            profiles.append(classe(*values))
        file.close()
        return profiles

class Profile_Vip(Profile):
    """Class for vip profiles"""
    def __init__(self, name, phone, company, nickname=''):
        super(Profile_Vip, self).__init__(name, phone, company)
        self.nickname = nickname

    def get_credit(self):
        return super(Profile_Vip, self).get_likes() * 10.0

class Date(object):
    """Formating a Date"""
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def print_date(self):
        print '%s/%s/%s' % (self.day, self.month, self.year)

class Person(object):
    """Create persons """
    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height

    def calc_imc(self):
        imc = self.weight/(self.height **2)
        print 'Imc de %s: %s' % (self.name,imc)

"""class Conta(object):

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo


    def calcular_imposto(self):
        self.saldo = self.saldo * 0.10
        return self.saldo


class ContaCorrente(Conta):

    def __init__(self, titular, saldo, bonus):
        super(ContaCorrente, self).__init__(titular, saldo)
        self.bonus = bonus;

    def calcular_imposto(self):
        return super(ContaCorrente, self).calcular_imposto() + self.bonus

#cc = ContaCorrente('xxx', 2000, 50);
#print cc.calcular_imposto()
"""
