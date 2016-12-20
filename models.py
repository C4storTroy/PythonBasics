# -*- coding: UTF-8 -*-

class Profile(object):
    """Class for user profiles"""
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
