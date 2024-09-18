task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_limit = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time_limit == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
    case "low":
        if time_limit=="no":
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
