def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
        #     ['\"]Enter the item to add: ['\"]\)
            add_item = input("Enter the item to add: ")
            shopping_list.append(add_item)
            # Prompt for and add an item
            pass
        elif choice == '2':
            remove_item=input("Enter an Item to be removed: ")
            shopping_list.remove(remove_item)
            # Prompt for and remove an item
            pass
        elif choice == '3':
            if len(shopping_list)==0:
                print("There is no item to be displayed :(")
            else:
                print(shopping_list)
            # Display the shopping list
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
