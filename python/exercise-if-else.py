#!/usr/bin/env python3.6
user = { 'admin': True, 'active': True, 'name': 'Kevin' }
#user['active'] = False
#user['admin'] = False

if user['admin'] and user['active']:
    print(f"{user['name']} is ADMIN and ACTIVE")
elif user['active']:
    print(f"{user['name']} is ACTIVE")
elif user['admin']:
    print(f"{user['name']} is ADMIN")
else:
    print(f"{user['name']}")
