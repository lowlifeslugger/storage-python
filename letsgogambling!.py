import random
import time

def gambling_game():
    # lets go gambling!
    while True:
        fun = random.randint(1, 10)
        boring = input("enter a number from 1-10 : ")

        try:
            boring = int(boring)

            if boring == fun:
                time.sleep(1)
                print(f"you won this round\n your choice {boring}, my choice {fun}")

                choiceo = input(
                    "wanna continue?\n type y to continue and anything else to exit : "
                )

                if choiceo == "y":
                    continue
                else:
                    break

            else:
                time.sleep(1)
                print(
                    f" loser loser loser!\n your choice {boring} - boring , "
                    f"my choice {fun} - fun , supperior "
                )

                choice = input(
                    "wanna continue?\n type y to continue and anything else to exit : "
                )

                if choice == "y":
                    continue
                else:
                    break

        except ValueError:
            time.sleep(4)
            print(
                f"{boring} look me in the eye and tell me\n "
                "thats a number , you idiot sandwhich"
            )
            continue
