from animal import Animal



class Hyena(Animal):
    numOfHyenas = 0
    list_of_hyena_names = []
    hyena_sound = "laugh"

    def __init__(self, name="aName", animal_id="anID",
                 birth_date="2009-01-01", color="a_color",
                 sex="a_sex", weight="a_weight",
                 originating_zoo="a_zoo", date_arrival="2009-01-01"):

        # increment static hyena counter
        Hyena.numOfHyenas += 1

        super().__init__("Hyena", name, animal_id,
                         birth_date, color, sex,
                         weight, originating_zoo, date_arrival)

    def make_sound(self):
        return self.hyena_sound

    def get_hyena_name(self):
        return Hyena.list_of_hyena_names.pop(0)
