#!/usr/bin/env python3.6

def _user_attribs():
    user = { 'admin': True, 'active': True, 'name': 'Kevin' }
    user['name'] = input("Enter user name ") or "Default"
    #user = { 'admin': True, 'active': True, 'name': 'Pedro' }
    #user = { 'admin': True, 'active': True, 'name': 'Gomes' }
    #user['active'] = False
    #user['admin'] = False
    
    #userlist = ['Kevin', 'Pedro', 'Gomes']
    #for MYUSER in userlist:
    #    user = { 'admin': True, 'active': True, 'name': MYUSER }
    
    #    print(f"{user['name']}")
    #    user['active'] = False
    #    user['admin'] = False
    
    if user['admin'] and user['active']:
        print(f"{user['name']} is ADMIN and ACTIVE")
    elif user['active']:
        print(f"{user['name']} is ACTIVE")
    elif user['admin']:
        print(f"{user['name']} is ADMIN")
    else:
        print(f"{user['name']}")
    a = print(f"{user['name']}")
    return a

_user_attribs()
print(f"{a}")
