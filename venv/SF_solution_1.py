import numpy as np

min = 1
max = 101

number = np.random.randint(min, max)
print(f"Try to guess! (My number is {number})")
counter = 0

def num_guesser_func(number, min=1, max=101):
    global counter
    def num_approver_func():
        procent = 0
        global counter
        while procent<100:
            counter+=1
            procent = round(100 / (20-counter))
            print(f"I'm {procent}% sure")

    while True:
        counter+=1
        new_number = np.random.randint(min, max)
        if new_number>number:
            max = new_number
        elif new_number<number:
            min = new_number
        else:
            num_approver_func()
            print(f"In {counter} attempts I guessed the number is {new_number}")
            break

    return new_number

num_guesser_func(number)