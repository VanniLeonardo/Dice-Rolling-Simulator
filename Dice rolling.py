import random
import numpy as np
import decimal
mod = 1000000007
dp = np.zeros((55, 55))
faces = 6


def game_start():
    while True:
        roll = input("Would you like to roll a dice? (Yes/No): ")
        if roll.lower() == "Yes".lower():
            ask_before_roll_dice()
            break
        elif roll.lower() == "No".lower():
            print("Oh :(")
            break
        else:
            print("Please enter a valid option (Yes/No)")
        
def ask_before_roll_dice():
    global dice_count 
    try:
      dice_count = int(input("How many dices would you like to roll?: "))
      if dice_count == 0:
        print("You can't roll 0 dices")
        ask_before_roll_dice()
      target_sum_ask_function()
    except ValueError:
      print("Please provide an integer")
      ask_before_roll_dice()

def target_sum_ask_function():
    target_sum_ask = input("Do you have a target sum in mind (Yes/No)? ")
    if target_sum_ask.lower() == "Yes".lower():
          target_sum_yes()
    elif target_sum_ask.lower() == "No".lower():
        roll_dice()
    else:
        print("Please provide a valid input (Yes/No)")   
        target_sum_ask_function()   

def target_sum_yes():
    try:
        target_sum = int(input("What is your target sum?: "))
        if target_sum == 0:
            print("The sum can never be 0, please enter a valid sum")
            target_sum_yes()
        else:
            prob = probability_of_sum(dice_count, target_sum)
            print(f"The probability of rolling {dice_count} dices with a sum of {target_sum} is {prob:.10%} ({ways_to_get_k} in {total_ways})")
            roll_again()
    except ValueError:
        print("Please provide an integer")
        target_sum_yes()
    return


def NoofWays(faces, dice_count, target_sum):
    dp = [[0] * (target_sum + 1) for _ in range(dice_count + 1)]
    dp[0][0] = 1

    for i in range(1, dice_count + 1):
        for j in range(1, target_sum + 1):
            for k in range(1, faces + 1):
                if k <= j:
                    dp[i][j] += dp[i - 1][j - k]

    return dp[dice_count][target_sum]

def probability_of_sum(dice_count, target_sum):
        global ways_to_get_k
        global total_ways
        ways_to_get_k = NoofWays(faces, dice_count, target_sum)
        total_ways = faces**dice_count
        prob = ways_to_get_k / total_ways
        ways_to_get_k = format(decimal.Decimal(ways_to_get_k), '.1e')
        total_ways = format(decimal.Decimal(total_ways), '.1e')
        for i in range(55):
            for j in range(55):
                dp[i][j] = -1
        if target_sum > faces * dice_count or target_sum < dice_count:
            print(f"The sum must be between {dice_count} and {faces * dice_count}")
        
        return prob

def roll_dice():
    dice_sum = 0
    for i in range(dice_count):
        dice_result = random.randint(1, faces)
        dice_sum += dice_result
        print(f"Dice number {i + 1} rolled {dice_result}")
    print(f"The dice sum was {dice_sum}")
    print(f"The dice average was {dice_sum / dice_count}")
    global prob
    prob = probability_of_sum(dice_count, dice_sum)
    print(f"The probability of rolling {dice_count} dices with a sum of {dice_sum} was {prob:.10%} ({ways_to_get_k} in {total_ways})")
    roll_again()

def roll_again():
    while True:
        roll = input("Roll again? (Yes/No): ")
        if roll.lower() == "Yes".lower():
            ask_before_roll_dice()
            break
        elif roll.lower() == "No".lower():
            print("Oh :(")
            break
        else:
            print("Please provide a valid input (Yes/No)")
            roll_again()
            break

game_start()
