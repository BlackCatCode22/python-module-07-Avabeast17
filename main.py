from animal import Animal
from hyena import Hyena
from lion import Lion
from datetime import date


list_of_hyenas = []
list_of_lions = []
list_of_tigers = []
list_of_bears = []

current_date = date.today()
current_year = current_date.year


def calc_birth_date(the_season, the_years):
    year_of_birthday = int(current_year) - int(the_years)
    the_birth_day = ""

    if the_season == "spring":
        the_birth_day = f"{year_of_birthday}-03-21"
    elif the_season == "summer":
        the_birth_day = f"{year_of_birthday}-06-21"
    elif the_season == "fall":
        the_birth_day = f"{year_of_birthday}-09-21"
    elif the_season == "winter":
        the_birth_day = f"{year_of_birthday}-12-21"
    else:

        the_birth_day = f"{year_of_birthday}-06-21"

    return the_birth_day


def load_names():

    with open("animalNames.txt") as f:
        current = None
        for line in f:
            line = line.strip()
            if not line:
                continue

            low = line.lower()
            if low.startswith("hyena names"):
                current = "hyena"
            elif low.startswith("lion names"):
                current = "lion"
            else:
                if current == "hyena":
                    Hyena.list_of_hyena_names.extend(
                        [n.strip() for n in line.split(",") if n.strip()]
                    )
                elif current == "lion":
                    Lion.list_of_lion_names.extend(
                        [n.strip() for n in line.split(",") if n.strip()]
                    )


def process_one_line(one_line):
    groups_of_words = one_line.strip().split(",")
    single_words = groups_of_words[0].strip().split(" ")
    age_in_years = single_words[0]
    a_sex = single_words[3]
    a_species = single_words[4]

    single_words = groups_of_words[1].strip().split(" ")
    season = single_words[-1]

    color = groups_of_words[2].strip()
    weight = groups_of_words[3].strip()
    origin_01 = groups_of_words[4].strip()
    origin_02 = groups_of_words[5].strip()

    from_zoo = origin_01 + ", " + origin_02
    birth_day = calc_birth_date(season, age_in_years)

    if "hyena" in a_species.lower():
        my_hyena = Hyena("aName", "anID", birth_day,
                         color, a_sex, weight, from_zoo, current_date)

        my_hyena.name = my_hyena.get_hyena_name()
        my_hyena.animal_id = "Hy" + str(Hyena.numOfHyenas).zfill(2)
        list_of_hyenas.append(my_hyena)

    if "lion" in a_species.lower():
        my_lion = Lion("aName", "anID", birth_day,
                       color, a_sex, weight, from_zoo, current_date)

        my_lion.name = my_lion.get_lion_name()
        my_lion.animal_id = "Li" + str(Lion.numOfLions).zfill(2)
        list_of_lions.append(my_lion)


def main():
    load_names()

    file_path = "arrivingAnimals.txt"
    with open(file_path, "r") as file:
        for line in file:
            process_one_line(line)

    print(f"\n\nNumber of animals created: {Animal.numOfAnimals}")
    print(f"\nNumber of hyenas created: {Hyena.numOfHyenas}")
    print(f"\nNumber of lions created: {Lion.numOfLions}\n")

    print("Zookeeper's Challenge Zoo Population\n")

    print("Hyena Habitat:\n")
    for hyena in list_of_hyenas:
        print(hyena.animal_id + "; " + hyena.name +
              "; birthdate: " + str(hyena.birth_date) + "; " +
              hyena.color + "; " + hyena.sex + "; " + hyena.weight +
              "; " + hyena.originating_zoo + "; arrived: " +
              str(hyena.date_arrival))

    print("\nLion Habitat:\n")
    for lion in list_of_lions:
        print(lion.animal_id + "; " + lion.name +
              "; birthdate: " + str(lion.birth_date) + "; " +
              lion.color + "; " + lion.sex + "; " + lion.weight +
              "; " + lion.originating_zoo + "; arrived: " +
              str(lion.date_arrival))


if __name__ == "__main__":
    main()
