"""
Author:         Brandon Ewanick
Date:           04/23/24
Assignment:     Project 02
Course:         CPSC 1050
Lab Section:    001

CODE DESCRIPTION: Let’s end the semester off strong! It’s time to be creative and create your own project- one that you can display to future employers. 
So, we are making it mandatory for you to create a personal project and you must use your imagination to generate a world to explore through code!
An RPG (Role Play Game) is a game in which players assume the roles of characters in a fictional setting.

"""
import random

#Define classes
class Character:
    def __init__(self, name, health, stamina):
        self.name = name
        self.health = health
        self.stamina = stamina
        self.inventory = {}
        self.trophy_case = {}
        self.kill_counter = 0

    #Implement movement
    def move(self):
        pass
    #Implement interaction
    def interact(self):
        pass
    #Implement combat
    def combat(self):
        pass
    #Implement player inventory  
    def add_to_inventory(self, item_name):
        if item_name in items:
            self.inventory[item_name] = items[item_name]
            print(f"{item_name} added to inventory.")


class Enemy(Character):
    def __init__(self, name, health, stamina, trophy):
        self.name = name
        self.health = health
        self.stamina = stamina
        self.trophy = trophy

enemies = {
    "Gotham Central Park": Enemy("Gang Member", 75, 10, "Gang Member Trophy"),
    "Wayne Enterprises": Enemy("Criminal", 85, 15, "Criminal Trophy"),
    "Ace Chemicals": Enemy("Joker's Henchman", 100, 20, "Joker's Henchman Trophy"),
    "Arkham Asylum": Enemy("Escaped Inmate", 90, 25, "Escaped Inmate Trophy")
}

class Item:
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect

items = {
    "Chug Jug": Item("Chug Jug", "health"),
    "Wintergreen Zyn": Item("Wintergreen Zyn", "stamina"),
    "Rage Spell": Item("Rage Spell", "damage")
}

class Quest:
    def __init__(self, name, description, objectives):
        self.name = name
        self.description = description
        self.objectives = objectives

quests = {
    "Gotham Central Park": Quest("Rescue the Hostages", "Save the hostages held by a gang in the park.", ["Defeat Gang Members", "Free Hostages"]),
    "Wayne Enterprises": Quest("Stop Corporate Sabotage", "Prevent a group of criminals from stealing valuable technology.", ["Capture Criminals", "Secure Technology"]),
    "Ace Chemicals": Quest("Confront the Joker", "Face off against the Joker and stop his latest scheme.", ["Defeat Joker's Henchmen", "Subdue the Joker"]),
    "Arkham Asylum": Quest("Contain the Riot", "Restore order in Arkham Asylum amidst a breakout attempt.", ["Subdue Escaped Inmates", "Restore Security"])
}

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Map:
    def __init__(self):
        self.locations = {}
    def add_location(self, x, y, location):
        self.locations[(x, y)] = location
    def get_location(self, x, y):
        return self.locations.get((x, y), None)

gotham_map = Map()

gotham_map.add_location(0, 0, Location("Gotham Central Park", "A serene park amidst the bustling city."))
gotham_map.add_location(0, 1, Location("Wayne Enterprises", "The towering skyscraper of Wayne Enterprises."))
gotham_map.add_location(1, 0, Location("Ace Chemicals", "The infamous chemical plant where the Joker was born."))
gotham_map.add_location(1, 1, Location("Arkham Asylum", "The high-security psychiatric hospital for Gotham's most dangerous criminals."))


def map_loader():
    print("Loading Gotham City Map...")

def print_map():
    for location in gotham_map.locations.values():
        print(f"{location.name}: {location.description}")

def accept_quest(player, location_name):
    quest = quests[location_name]
    print("You accepted the quest!")
    print("Quest:", quest.name)
    print("Description:", quest.description)
    print("Objectives:", ", ".join(quest.objectives))

    start_encounter(player, location_name)
    complete_quest(player, location_name)

def move_to_new_location(player):
    new_location = random.choice(list(gotham_map.locations.keys()))
    global player_location
    player_location = new_location

def explore_location(player, complete_quest=False):
    print("\nExploring current location...")
    current_location = gotham_map.get_location(player_location[0], player_location[1])
    print(f"You are at {current_location.name}: {current_location.description}")
    
    if current_location.name in quests:
        print("Quest available in this location:")
        print(quests[current_location.name].name)
        print(quests[current_location.name].description)
        print("1. Accept Quest")
        print("2. Ignore and continue exploring")
        choice = input("Enter your choice: ")
        if choice == "1":
            accept_quest(player, current_location.name)
        elif choice == "2":
            print("You ignore the quest and continue exploring.")
            move_to_new_location(player)
    else:
        print("No quests available in this location.")

    # Check if there's an encounter
    if current_location.name in enemies and choice == "1":
        if enemies[current_location.name].health > 0:
            start_encounter(player, current_location.name)
        else:
            move_to_new_location(player)

def start_encounter(player, location_name):
    if player.health <= 0:
        print("Game over. Batman has been defeated.")
        return  # Exit function if Batman is defeated

    enemy = enemies[location_name]

    if enemy.health <= 0:
        move_to_new_location(player)
        return

    print(f"\nYou encounter a {enemy.name}!")
    print(f"Enemy Stats: Health - {enemy.health}, Attack - {enemy.stamina}")
    print("1. Fight")
    print("2. Flee")
    choice = input("Enter your choice: ")
    if choice == "1":
        fight(player, enemy, location_name)
    elif choice == "2":
        print("You flee from the encounter.")
        global fled_from_encounter
        fled_from_encounter = True
        move_to_new_location(player)
    else:
        print("Invalid choice. You stand your ground.")
        fight(player, enemy, location_name)

transitioning_to_new_location = False
fled_from_encounter = False

def fight(player, enemy, location_name):
    global rage_spell_active, chug_jug_active, wintergreen_Zyn_active, obtained_items  # Access the global variables
    current_location = gotham_map.get_location(player_location[0], player_location[1])  # Retrieve current location

    # Check for active power-ups
    if rage_spell_active:
        print("You have double damage for this encounter!")

    while player.health > 0 and enemy.health > 0:
        # Player attacks
        player_attack = random.randint(5, 20)
        if rage_spell_active:
            player_attack *= 2
        enemy.health -= player_attack
        print(f"You hit the enemy for {player_attack} damage.")
        if enemy.health <= 0:
            print("Enemy defeated!")
            player.kill_counter += 1
            trophy_name = enemies[current_location.name].trophy
            print(f"The enemy dropped {trophy_name}.")
            player.add_to_inventory(trophy_name)
            # Roll for a dropped item
            drop_chance = random.random()  # Generate a random number between 0 and 1
            if drop_chance < 0.95:  # Adjust drop chance as needed
                drop_item = random.choice(list(items.keys()))  # Choose a random item to drop
                print(f"The enemy dropped {drop_item}.")
                # Assume the player automatically picks up the dropped item
                player.add_to_inventory(drop_item)
                use_item(player, drop_item)
            break
        # Enemy attacks
        enemy_attack = random.randint(5, 20)
        player.health -= enemy_attack
        print(f"The enemy hits you for {enemy_attack} damage.")
        if player.health <= 0:
            print("You have been defeated!")
            break

rage_spell_active = False
chug_jug_active = False
wintergreen_Zyn_active = False

obtained_items = {}


def use_item(player, item_name):
    if item_name in items:
        item = items[item_name]
        if item.effect == "health":
            player.health += 50  # Increase health by 50 (you can adjust the value as needed)
            print("Used Chug Jug. Health increased by 50.")
        elif item.effect == "stamina":
            player.stamina += 50  # Increase stamina by 50 (you can adjust the value as needed)
            print("Used Wintergreen Zyn. Stamina increased by 50.")
        elif item.effect == "damage":
            # Double the damage temporarily (you can implement a duration for effects if needed)
            print("Used Rage Spell. Damage doubled for this encounter.")
            double_damage_active = True
    else:
        print("Item not found.")

def complete_quest(player, location_name):
    print("Quest completed!")

    move_to_new_location(player)
    current_location = gotham_map.get_location(player_location[0], player_location[1])
    if current_location.name not in quests:
        explore_location(player)
    
def check_inventory(player):
    print("\nInventory: ")
    if player.inventory:
        for item_name in player.inventory:
            print(item_name)
    else:
        print("You have no items in your inventory.")

def check_trophies(player):
    if player.trophy_case:
        for trophy_name in player.trophy_case:
            print(trophy_name)
    else:
        print("You have no trophies in your inventory.")

def check_stats(player):
    print(f"Health: {player.health}")
    print(f"Stamina: {player.stamina}")
    print(f"Enemies defeated: {player.kill_counter}")

def save_game():
    print("Saving game...")

def load_game():
    print("Loading game...")

player_location = (0, 0)



#Main game loop
def main():
    print("Welcome to the Gotham Knight: Rise of the Dark Avenger!")
    map_loader()
    player = Character("Batman", 250, 100)
    game_over = False

    while player.health > 0:
        print("\n=== Gotham City Map ===")
        print_map()
        print("Current Location: ", player_location)
        print("1. Explore Location")
        print("2. Check inventory")
        print("3. Check trophy case")
        print("4. Check player stats")
        print("5. Save game")
        print("6. Load game")
        print("7. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            explore_location(player)
        elif choice == "2":
            check_inventory(player)
        elif choice == "3":
            check_trophies(player)
        elif choice == "4":
            check_stats(player)
        elif choice == "5":
            save_game()
        elif choice == "6":
            load_game()
        elif choice == "7":
            print("Exiting game. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
        
        if player.kill_counter == 4:
            print("Congratulations! You have defeated all the enimies and saved Gotham City! You have won!")
            break
        
    if not game_over and player.health <=0:
        print("Game over. Batman has been defeated")
        game_over = True

if __name__ == "__main__":
    main()