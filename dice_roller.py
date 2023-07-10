import random


def roller(result):

    # A roll of 'd6' will assume '1d6' was intended
    if result[:rolledDice.index("d")] <= str(1):
        num = 1
    else:
        num = result[:rolledDice.index("d")]

# num and die are rolledDice before and after the 'd'.
# die has +1 to pass over the 'd'.
# Result is as long as the user defines.
    if "+" in rolledDice:
        die = result[rolledDice.index("d") + 1:rolledDice.index("+")]
        bonus = result[rolledDice.index("+") + 1:]
    elif "-" in rolledDice:
        die = result[rolledDice.index("d") + 1:rolledDice.index("-")]
        bonus = int(result[rolledDice.index("-") + 1:]) * - \
            1  # converts to negative
    else:
        die = result[rolledDice.index("d") + 1:]
        bonus = 0

# Some ints for later
    rollList = []
    dieTotal = 0

# Display user INPUT.  It avoids displaying +- 0.
    print("Roll:    ", end="")
    print(str(num) + "d" + str(die), end="")
    if int(bonus) != 0:
        if '+' in rolledDice:
            print("+", end="")
        print(str(bonus), end="")
    print()

# Generate list of random numbers, with bonus/penalty applied.
    for i in range(0, int(num)):
        rollList.append(int(random.randint(1, int(die))))

# Show raw RESULTS
    print("Results: " + str(rollList), end="")
    if int(bonus) != 0:
        print(" + [" + str(bonus) + "]", end="")
    print()

# Add the list TOTAL
    for x in rollList:
        dieTotal += x
    print("Total:   [" + str(int(dieTotal) + int(bonus)) + "]")
    print()
# some spacing, yay!


# The meat of it.
print("Nick's Dice Roller!")
print()
print("Enter any combination you like, as long as it's shortform.")
print("Examples of valid rolls: 6, d6, 1d6, 8+5, 38d12-4, ''")

# BEST LOOP EVER HAAAAHAHAHAHAHA I AM A GENIUS
while True:

    # Error handling, because my god those were a pain in my fucking ass.
    try:
        rolledDice = input("Enter a die value: ")

# if input is single unit, it's either a number or invalid, so add a d.
        if len(rolledDice) == 1:
            rolledDice = 'd' + rolledDice

# Or, simply force invalid into exception.
        else:
            input == ""

# Run the function
        roller(rolledDice)
    except ValueError:
        print("You have entered an invalid roll, have a random one instead.")
# This random roller exists because it helped me test my stuff, and is a
# a fun issue catcher.
        rolledDice = (str(str(random.randint(1, 6))
                          + "d"
                          + str(random.choice(
                            ['4', '6', '8', '10', '12', '20'])))
                      + random.choice(["+", "-"])
                      + str(random.randint(0, 5)))
        roller(rolledDice)


"""
############################## TO DO ################################
#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #

20s
Make it so that rolling [X]d[Y=20]+[Z] will roll (d20+[Z]), [X] times.

Non-negatives
Usually, damage numbers can't go below 1.

Functional
This is getting messy. Learn to use functions in better ways.

Include this Regex for roll recognition:
(?:(\d+)?([Dd]+))?(?:(\d+))([-+]?)(\d*)
"""
