#!/usr/bin/env python3.6

def gather_info():
    height = float(input("enter your height (inches or meters) "))
    weight = float(input("enter your weight (pounds or kilograms) "))
    system = input("Imperial or metric units? ").lower().strip()
    print(f"height={height}, weight={weight}, system={system} ")
    return (height, weight, system)

def calculate_bmi(weight, height, system='metric'):  
#positional arguments (weight, height, system) can be mapped in function call
#system='metric' - assigning default value to the variable

    """
    return the body mass index (BMI) for the
    given weight, height, and mesurement system.
    """

    if system == 'metric':
        print(f"system == {system} ")
        bmi = (weight / (height ** 2))
        return bmi
    else:
        print(f"system == {system} ")
        bmi = 703 * (weight / (height ** 2))
        return bmi

while True:
#    height, weight, system = gather_info() 
    he, we, sys = gather_info() 
#rename vars and change mappings!!!!!!!!!!!!!!!!!
    if sys.startswith('i'):
        bmi = calculate_bmi(system=sys, height=he, weight=we)
        print(f"your BMI is {bmi} ")
        break
    elif sys.startswith('m'):
        bmi = calculate_bmi(weight=we, height=he) #system is passed because we define metric as default value
        print(f"your BMI is {bmi} ")
        break
    else:
        print("Enter correct mesurement system (imperial or metric (default)) ")
#        break

