# -*- coding: UTF-8 -*-
from datetime import datetime
import re
def create_name_invite(name_invite):
    pos_fin = len(name_invite)
    pos_ini = pos_fin - 4
    part1 = name_invite[0:4]
    part2 = name_invite[pos_ini: pos_fin]
    return part1 + ' ' + part2
    #print '%s %s' % (part1, part2)

def send_invite(name_ready):
    print 'Enviado convite para %s' % (name_ready)

def process_invite(name_invite):
    name_ready = create_name_invite(name_invite)
    send_invite(name_ready)

def add_names(names):
    print 'Type a name:'
    name = raw_input()
    names.append(name)

def remove_name(names):
    print 'what would you like to remove?'
    name = raw_input()
    names.remove(name)

def calc_age():
    print 'Type year of birth:'
    year_of_birth = raw_input()
    now = datetime.now()
    age = now.year - int(year_of_birth)
    print 'You are %s years old' % age

def print_names(names):
    print 'List of names:'
    for name in names:
        print name

def alter_name(names):
    print 'What name would you like to change?'
    name_to_change = raw_input()
    if(name_to_change in names):
        pos = names.index(name_to_change)
        print 'Type new name:'
        new_name = raw_input()
        names[pos] = new_name

def search_name(names):
    print 'Type a name for search:'
    name_to_search = raw_input()
    if(name_to_search in names):
        print '%s exists on list' % (name_to_search)
    else:
        print '%s does not exist on list' % (name_to_search)

def search_regex(names):
    print 'Type a name for search with regex:'
    regex = raw_input()
    all_names = ''.join(names)
    result = re.findall(regex, all_names)
    print(result)

def menu():
    names = []
    choice = ''
    while(choice != '0'):
        print '\nType \n1 to add\n2 to list\n3 to remove_name', '\
         \n4 to change\n5 to search\n6 to regex \n0 to finish\n '

        choice = raw_input()

        if(choice == '1'):
            add_names(names)
        if(choice == '2'):
            print_names(names)
        if(choice == '3'):
            remove_name(names)
        if(choice == '4'):
            alter_name(names)
        if(choice == '5'):
            search_name(names)
        if(choice=='6'):
            search_regex(names)


menu()
