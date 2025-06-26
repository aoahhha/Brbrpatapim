class HolidayCharacter:
    def __init__(self):
        self.relevant_months = []
        self.character_name = "Holiday Character"
    def is_character_relevant(self, month):
        return month in self.relevant_months


class Santa(HolidayCharacter):
    def __init__(self):
        super().__init__()
        self.character_name = "Santa Claus"
        self.naughty_list = []
        self.nice_list = []
        self.relevant_months = [12]

    def action(self, action_name):
        action = {"deliver gifts": "Ho ho ho! Delivering presents to you",
                  "eat cookies": "Mmmm love these cookies",
                  "ride sleigh": "Love riding my new sleigh",
                  "gifting present": "Here, take this little one"
                  }
        return action.get(action_name.lower(), "Santa is revising gift quota")

    def check(self, name):
        if name.lower() in [n.lower() for n in self.naughty_list]:
            return f"{name} is on the Naughty List!🎅🔥"
        elif name.lower() in [n.lower() for n in self.nice_list]:
            return f"{name} is on the Nice List!🎁✨"
        else:
            return f"{name} is not on any list... yet.🕵️‍♂️"






