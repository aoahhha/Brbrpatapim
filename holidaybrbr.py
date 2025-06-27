import random

class HolidayCharacter:
    def __init__(self):
        self.relevant_months = []
        self.character_name = "Holiday Character"
        self.actions = {}

    def is_character_relevant(self, month):
        return month in self.relevant_months

    def action(self, action_name):
        return self.actions.get(action_name.lower(), f"{self.character_name} undefined action")

    def interact(self):
        print(f"You meet {self.character_name}")


class Santa(HolidayCharacter):
    def __init__(self):
        super().__init__()
        self.character_name = "Santa Claus"
        self.naughty_list = []
        self.nice_list = []
        self.relevant_months = [12]
        self.actions = {
        "deliver gifts": "Ho ho ho! Delivering presents to you",
        "eat cookies": "Mmmm love these cookies",
        "ride sleigh": "Love riding my new sleigh",
        "gifting present": "Here, take this little one"
    }

    def check(self, name):
        if name.lower() in [n.lower() for n in self.naughty_list]:
            return f"{name} is on the Naughty List!🎅🔥"
        elif name.lower() in [n.lower() for n in self.nice_list]:
            return f"{name} is on the Nice List!🎁✨"
        else:
            return f"{name} is not on any list... yet.🕵️‍♂️"

    def interact(self):
        name = input("What's your name? ")
        behavior = input("Were you nice or naughty this year? ").strip().lower()
        if behavior == "nice":
            self.nice_list.append(name)
        elif behavior == "naughty":
            self.naughty_list.append(name)
        print(self.check(name))
        print(self.action("deliver gifts"))


class JasonVoorhees(HolidayCharacter):
    def __init__(self):
        super().__init__()
        self.character_name = "Jason Voorhees"
        self.victims = []
        self.present = ["Blood Splatter Coffee Mug", "Glow-in-the-DarkJason Voorhees mask", "candy", "mini liquor bottles"]
        self.relevant_months = [10]

        self.actions = {
            "stalk": "Chh... chhh... chha, ha, ha ,ha",
            "appear": "Jason suddenly appears from the darkness!",
            "chase": "Running after victim with machete",
            "give present": "Giving present to my friend"
    }

    def add_victim(self, name):
        self.victims.append(name)
        return f"{name} has been added to Jason's victim list!"

    def check_present(self, present):
        if present.lower() in [p.lower() for p in self.present]:
            return f"Jason clenches his fists and presents a {present}🎁"
        return "Jason stares blankly... then offers an ominous thumbs-up 👍"

    def interact(self):
        name = input("Who dares to approach me!? ")
        print(self.add_victim(name))
        print(self.action("appear"))
        gift = random.choice(self.present)
        print(self.check_present(gift))




class StPatrick(HolidayCharacter):
    def __init__(self):
        super().__init__()
        self.character_name = "Saint Patrick"
        self.relevant_months = [3]
        self.irish_blessings = [
            "May your pockets be heavy and your heart be light",
            "May good luck be with you every day",
            "Slainte!"
        ]
        self.shamrocks = 0

        self.actions = {
            "banish snakes": "All snakes are fleeing Ireland!",
            "tell": "Using this shamrock ☘️ to explain the Holy Trinity",
            "rainbow": "Looking for a big pot of Gold!",
            "bless": self.bless
    }

    def bless(self):
        return random.choice(self.irish_blessings)

    def add_shamrock(self):
        self.shamrocks += 1
        return f"Snakes banished: {self.shamrocks}"

    def interact(self):
        print(self.action("tell"))
        print(self.add_shamrock())
        print("Blessing: " + self.bless())



class EasterBunny(HolidayCharacter):
    def __init__(self):
        super().__init__()
        self.character_name = "Easter Bunny"
        self.relevant_months = [4]
        self.eggs_hidden = 0
        self.carrots_eaten = 0
        self.basket = ["Chocolate eggs", "Jelly beans",
                       "Marshmallow", "Colorful stickers"]

        self.actions = {
            "hide eggs": "Hiding eggs in the garden!",
            "hop": "hop, hop, hop",
            "crunch carrot": "Crunching carrots! Mmmm xD",
            "deliver basket": "Leaving an Easter basket by your doorstep"
    }

    def hide_eggs(self, count):
        self.eggs_hidden += count
        return f"Hidden {count} eggs! Total hidden: {self.eggs_hidden}"

    def eat_carrot(self):
        self.carrots_eaten += 1
        return f"Nom nom! Carrots eaten today: {self.carrots_eaten}"

    def check_basket(self):
        return f"Basket contains {', '.join(self.basket)}"

    def interact(self):
        print(self.action("hop"))
        print(self.hide_eggs(random.randint(1, 5)))
        print(self.eat_carrot())
        print(self.check_basket())

def holiday_game():
    characters = [Santa(), JasonVoorhees(), StPatrick(), EasterBunny()]

    while True:
        print("\nWelcome to the Holiday World! Choose a character to interact with:")
        for i, char in enumerate(characters):
            print(f"{i + 1}. {char.character_name}")
        print("5. Start again")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice (1-6): ")) - 1
        except ValueError:
            print("Invalid input. Please enter a number: ")
            continue

        if 0 <= choice < len(characters):
            character = characters[choice]
            print(f"\nYou selected {character.character_name}!\n")
            character.interact()
        elif choice == 4:
            print("Restarting game...")
            continue
        elif choice == 5:
            print("Bye!")
            break
        else:
            print("Please choose a number between 1 and 6.")


if __name__ == "__main__":
    holiday_game()

