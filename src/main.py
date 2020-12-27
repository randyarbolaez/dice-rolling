from random import randint


def error_handling(prompt):
    while True:
        num = input(prompt)
        if num.isdigit():
            if int(num) > 101:
                print('Damn, what do you need so many dices for? I\'m not doing all that work :))')
                continue
            else:
                return int(num)
        else:
            print('Numbers only!!')

def get_all_number_of_dice():
    number_of_dice = error_handling('How many dice do you want? ')
    i = 0

    while i < number_of_dice:
        print('Dice number', i+1,':',randint(1,6))
        i+=1

def main():
    get_all_number_of_dice()


main()
