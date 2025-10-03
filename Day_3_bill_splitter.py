"""
 Challenge: Simple Bill Splitter

Write a Python script that helps split a bill evenly between friends.

Your program should:
1. Ask how many people are in the group.
2. Ask for each person's name.
3. Ask for the total bill amount.
4. Calculate each person's share of the bill.
5. Display how much each person owes in a clean, readable format.
"""

import textwrap

# Function that takes peoples names and number 

num_people = int(input('how many people are eating? '))

def data(num :int) -> list:
    names = []
    if num < 2: 
        name = input('what is your name? ')
        names.append(name)
        return names 
    else: 
        for i in range(num): 
            person = input(f'what is the name of {i+1} ')
            names.append(person)
        return names
    

people = data(num_people)

bill_total = int(input('what is the total bill? '))

def even_splitter(bill: int, names: list) -> list:
    if len(names) < 2:
        owe = bill
        return owe
    else:
        owe = bill / len(names)
        return owe
    
bill = even_splitter(bill_total, people)


# match each person to their owe
my_bill = {}
for i in range(len(people)):
    my_bill[people[i]] = bill


# display bill info
print("\nYour Total Bill\n")
print("*" * 50)
#print each key value on it's own line
for key, value in  my_bill.items():
    print(textwrap.dedent(f'{key}  {value}'))
print("*" * 50)
