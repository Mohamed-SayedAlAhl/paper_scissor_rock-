import random
pc=random.choice(["paper","scissor","rock"]).lower()
player=input("Choose paper , scissor or rock : ").lower()
if player=="paper" and pc=="scissor":
    print(f"you lose. I chose {pc}")
elif player=="scissor" and pc=="rock":
    print(f"you lose. I chose {pc}")
elif player=="rock" and pc=="paper":
    print(f"you lose.I chose {pc}")
elif player==pc:
    print("tie")
else:
    print(f"you win.I chose {pc}")