import random


def main():

    print("""Hi welcome to Ryushi! 
You're a Yautja and have successfully planted a bomb in a hive containing a Queen.
The enraged Queen sends forth her Warriors to snuff you out. Eventually, you stumble
upon a Rhynth and must travel across the harsh Ryushi desert to get to your ship.
Make haste, because the Queen's brood are hot on your trail!""")

    done = False

    miles_traveled = 00
    thirst_level = 0
    rhynth_tiredness = 0
    warriors_miles = -20
    canteen = 3

    while not done:
        print()
        print("A. Drink from your canteen")
        print("B. Moderate speed")
        print("C. Ahead full speed.")
        print("D. Stop for the night.")
        print("E. Status check.")
        print("Q. Quit.")
        print()
        val = input("What is your choice? ")
        print()

        if val.upper() == "Q":
            print("""The battle was hard fought, but you give up and set off a bomb taking
you and the warriors out.""")
            break

        elif val.upper() == "D":
            rhynth_tiredness = 0
            print("The camel is happy")
            warriors_miles += random.randrange(7, 15)

        elif val.upper() == "E":
            print("Miles traveled: " + str(miles_traveled))
            print("Drinks in canteen: " + str(canteen))
            print("The warriors are " + str((miles_traveled - warriors_miles)) + " behind you")

        elif val.upper() == "C":
            miles_traveled += random.randrange(10, 20)
            thirst_level += 1
            rhynth_tiredness += random.randrange(1, 4)
            warriors_miles += random.randrange(7, 15)
            print("Miles traveled: " + str(miles_traveled))
            if random.randrange(21) == 0:
                print("You found an oasis.")
                thirst_level = 0
                rhynth_tiredness = 0

        elif val.upper() == "B":
            miles_traveled += random.randrange(5, 13)
            print("Miles traveled: " + str(miles_traveled))
            thirst_level += 1
            rhynth_tiredness += 1
            warriors_miles += random.randrange(7, 15)
            if random.randrange(21) == 0:
                print("You found an oasis.")
                thirst_level = 0
                rhynth_tiredness = 0

        elif val.upper() == "A":
            if canteen <= 0:
                print("No drinks left!")

            else:
                thirst_level = 0
                canteen -= 1
                print("Ah, that was refreshing!")

        if thirst_level > 6:
            print("You have died of thirst!")
            print()
            break

        elif thirst_level > 4:
            print("You are thirsty!")

        if rhynth_tiredness > 8:
            print("Your rhynth is dead.")
            print()
            break

        elif rhynth_tiredness > 5:
            print("Your rhynth is getting tired.")

        if warriors_miles >= miles_traveled:
            print("You have been captured and will become part of the Queen's brood. You lose!")
            break

        elif miles_traveled - warriors_miles <= 15:
            print("The warriors are nearby!")

        if miles_traveled >= 200:
            print("You safely arrived at your ship and watched as the planet Ryushi is liquidated. You Win!")
            break


main()
