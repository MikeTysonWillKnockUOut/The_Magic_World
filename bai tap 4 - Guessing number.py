import random
num_win = 0
num_lose = 0
money = 100
while True:
    print('Computer thinks a number from 1 to 100')
    print('Each game cost five bucks')
    comp_number = random.randint(1,100)
    money -= 5
    level = int(input('choose level [1,2,3]?'))
    #1: easy, 2: medium , 3: hard
    times = 10 if level == 1 else 5 if level == 2 else 3

    for time in range(times):
        your_num = int(input("Enter your guessing number #" + str(time + 1) + ": "))
        if your_num == comp_number:
            num_win += 1
            #your prize if you win
            if level == 1:
                 money += 5
            elif level == 2:
                 money +=10
            else:
                money += 15
            print('You are Genius!!!')
            break
        else:
            if your_num < comp_number:
                print ('too low!')
            else:
                print('too high!')
        if time + 1 >= times:
            num_lose += 1
            money -= 5
            print('------------------')
            print(f'Game over!, the number was: {comp_number}')
            break
    print('---------------------------------------------')
    print(f'You won {num_win} times')
    print(f'You Lose {num_lose} times')
    print(f'Your current money is {money}')
    if money == 0:
      print("Runs out of money")
      break
    cont= input('Dare to you to play [y/n]: ')
    if cont == 'n' or cont == 'N':
        break