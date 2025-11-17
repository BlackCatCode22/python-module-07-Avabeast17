from animal import Animal


class Lion(Animal):
    numOfLions = 0
    list_of_lion_names = []
    lion_sound = "roar"

    def __init__(self, name="aName", animal_id="anID",
                 birth_date="2009-01-01", color="a_color",
                 sex="a_sex", weight="a_weight",
                 originating_zoo="a_zoo", date_arrival="2009-01-01"):

        Lion.numOfLions += 1

        super().__init__("Lion", name, animal_id,
                         birth_date, color, sex,
                         weight, originating_zoo, date_arrival)

    def make_sound(self):
        return self.lion_sound

    def get_lion_name(self):
        return Lion.list_of_lion_names.pop(0)
