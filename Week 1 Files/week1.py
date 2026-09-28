# Simple 3-Day Budget Tracker

# Task 1: Setup
name = input("Enter your name: ")
total_spent = 0

# Task 2: Loop through 3 days
for day in range(1, 4):
    spent = float(input("Enter money spent today ($): "))
    total_spent = total_spent + spent

    if spent > 20:
        print("Over your $20 budget today!")
    else:
        print("Great! Under budget today.")

# Task 3: Final summary
print("Total money spent over 3 days: $" + str(total_spent))

if total_spent <= 60:
    print(f"Congratulations {name}, You stayed under your $60 total budget!")
else:
    print(f"Uh oh! {name}, You went over your $60 total budget!")
