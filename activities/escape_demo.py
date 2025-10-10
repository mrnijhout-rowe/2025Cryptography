# The rooms dictionary
rooms = {
    "classroom": {
        "description": "A dusty classroom with old desks.",
        "items": ["key"],
        "exits": {"north": "hallway"}
    },
    "hallway": {
        "description": "A dim hallway. You see an exit door!",
        "items": ["flashlight"],
        "exits": {"south": "classroom", "east": "library"}
    },
    "library": {
        "description": "A musty, dusty library.",
        "items": ["book"],
        "exits": {"west": "hallway"}
    }
}

# The items dictionary
items = {
    "key": {
        "name": "Old Key",
        "description": "A brass key with '207' engraved on it"
    },
    "flashlight": {
        "name": "Flashlight",
        "description": "A heavy-duty flashlight"
    }
}

# Game state
game_state = {
    "current_room": "classroom",
    "inventory": []
}

# Functions
def display_room(room_name):
    """Show the current room"""
    room = rooms[room_name]
    print(f"\n{room['description']}")
    if room["items"]:
        print(f"You can see: {', '.join(room['items'])}")
    print(f"Exits: {', '.join(room['exits'].keys())}")

def take_item(item_name):
    """Take an item from the current room"""
    current_room = game_state["current_room"]
    if item_name in rooms[current_room]["items"]:
        rooms[current_room]["items"].remove(item_name)
        game_state["inventory"].append(item_name)
        print(f"You picked up the {item_name}.")
    else:
        print("That's not here.")

def go(direction):
    """Move to another room"""
    current_room = game_state["current_room"]
    if direction in rooms[current_room]["exits"]:
        game_state["current_room"] = rooms[current_room]["exits"][direction]
        print(f"You go {direction}.")
    else:
        print("You can't go that way.")

# Main game loop
print("=== ESCAPE ROOM DEMO ===")
print("Commands: 'take [item]', 'go [direction]', 'inventory', 'quit'")

while True:
    display_room(game_state["current_room"])
    
    command = input("\nWhat do you do? > ").lower().split()
    
    if len(command) == 0:
        continue
    
    if command[0] == "quit":
        print("Thanks for playing!")
        break
    elif command[0] == "take" and len(command) > 1:
        take_item(command[1])
    elif command[0] == "go" and len(command) > 1:
        go(command[1])
    elif command[0] == "inventory":
        print(f"You're carrying: {game_state['inventory']}")
    else:
        print("I don't understand that command.")