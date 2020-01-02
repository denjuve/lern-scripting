#!/usr/bin/env python3.6
count = 0
while count <= 10:
    if count == 0:
        count += 1
        continue
    elif count % 2 == 0:
        print(f"we're counting even  numbers: {count}")
        count += 1
        continue
    else:
        print(f"we're counting odd numbers: {count}")
        count += 1
        continue
