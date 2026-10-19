"""Project Two starter for the student's text-based adventure game."""

# Student: Alan Sutton


def show_instructions():
    """Display the game objective and available commands."""
    print("Mario's Mushroom Kingdom Adventure")
    print("Collect all 6 items before entering Bowser's Castle to win!")
    print("Move commands: go north, go south, go east, go west")
    print("Collect an item: get <item name>")
    print("-" * 40)


def show_status(current_room, inventory, rooms):
    """Display the player's current game status."""
    print("You are in the " + current_room)
    print("Inventory:", inventory)

    if "item" in rooms[current_room]:
        print("You see a " + rooms[current_room]["item"])

    print("-" * 40)


def main():
       """Run the game until Mario wins or loses against Bowser."""
    # Room connections and items match the Project One storyboard.
    rooms = {
        "Peach's Castle": {
            "north": "Lava Castle Gate",
            "west": "Toad House",
            "east": "Underground Cavern"
        },
        "Toad House": {
            "east": "Peach's Castle",
            "item": "1-Up Mushroom"
        },
        "Lava Castle Gate": {
            "north": "Bowser's Castle",
            "south": "Peach's Castle",
            "item": "Super Star"
        },
        "Underground Cavern": {
            "west": "Peach's Castle",
            "south": "Ghost House",
            "item": "Super Mushroom"
        },
        "Ghost House": {
            "north": "Underground Cavern",
            "south": "Koopa Beach",
            "item": "Super Leaf"
        },
        "Koopa Beach": {
            "north": "Ghost House",
            "south": "Coin Heaven",
            "item": "Fire Flower"
        },
        "Coin Heaven": {
            "north": "Koopa Beach",
            "item": "Coin"
        },
        "Bowser's Castle": {
            "south": "Lava Castle Gate"
        }
    }

    current_room = "Peach's Castle"
    inventory = []
    total_items = 6

    show_instructions()

    # Keep accepting commands until Mario reaches Bowser's Castle.
    while True:
        show_status(current_room, inventory, rooms)
        command = input("Enter your move: ").strip()
        lower_command = command.lower()

        if lower_command.startswith("go "):
            direction = lower_command[3:].strip()

            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
                print("You moved to the " + current_room + ".")
            else:
                print("You can't go that way!")

        elif lower_command.startswith("get "):
            requested_item = command[4:].strip()

            if ("item" in rooms[current_room] and
                    requested_item.lower() == rooms[current_room]["item"].lower()):
                item = rooms[current_room].pop("item")
                inventory.append(item)
                print(item + " retrieved!")
            else:
                print("You can't get that item here!")

        else:
            print("Invalid command! Use 'go <direction>' or 'get <item name>'.")

        # Bowser's room ends the game, with a win or a loss.
        if current_room == "Bowser's Castle":
            if len(inventory) == total_items:
                print("Congratulations! Mario collected all 6 items and defeated Bowser!")
                print("You win!")
            else:
                print("Bowser defeated Mario! GAME OVER!")
                print("You needed all 6 items before facing Bowser.")

            print("Thanks for playing Mario's Mushroom Kingdom Adventure!")
            input("Press Enter to close the game...")
            break

if __name__ == "__main__":
    main()
