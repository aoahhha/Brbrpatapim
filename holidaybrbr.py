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






