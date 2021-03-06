from __future__ import print_function
import random
def food_id(food):
    ''' Returns catorrization of food
    
    Food is a string
    returns a string of categories
    '''
    
    fruits = ['apple', 'banana', 'orange']
    citrus = ['orange']
    starchy = ['banana', 'potato']
    
    
    # Check the category and report
    if food in fruits:
        if food in citrus:
            return 'Citrus, Fruit'
        else:
            return 'NOT Citrus, Fruit'
    else: 
        if food in starchy:
            return 'Starchy, NOT Fruit'
        else: 
            return 'NOT Starchy, NOT Fruit'
def food_id_test():
    ''' Unit test for food_id
    returns True if good, returns False if not good
    '''
    works = True
    if food_id('orange') != 'Citrus, Fruit':
        works = False
        print('orange bug in food_id()')
    if food_id('banana') != 'NOT Citrus, Fruit':
        works = False
        print('banana bug in food_id()')    
            
    if works:
        print('food_id passed all tests')
    return work

def guess_once():
    secret = random.randint(1,4)
    print('I have a number between 1 and 4.')
    guess= int(raw_input('Guess: '))
    if guess > secret:
        print('Too high, My number is', secret,'.',sep=' ')
    if guess < secret:
        print('Too low, my number is', secret)
    if guess == secret:
        print('Right on')