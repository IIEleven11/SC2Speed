def calculate_average_speed(units):
    speeds = [unit[1] for unit in units]
    return sum(speeds) / len(speeds)


def calculate_race_averages(unit_speeds):
    average_speeds = {}
    for race, units in unit_speeds.items():
        overall_average_speed = calculate_average_speed(units)
        average_speeds[race] = {"overall": overall_average_speed}
    return average_speeds


def display_race_averages(average_speeds, selected_race):
    speeds = average_speeds[selected_race]
    print(f"{selected_race.capitalize()} Average Speed:")
    if isinstance(speeds["overall"], float):
        print(f"Overall: {speeds['overall']}")
    else:
        print("Invalid overall speed value.")
    if "on_creep" in speeds:
        if isinstance(speeds["on_creep"], float):
            print(f"On Creep: {speeds['on_creep']}")
        else:
            print("Invalid on_creep speed value.")
        if isinstance(speeds["off_creep"], float):
            print(f"Off Creep: {speeds['off_creep']}")
        else:
            print("Invalid off_creep speed value.")
    print()


def main():
    unit_speeds = {
        "Protoss": [
            ("Probe", 3.94),
            ("Zealot", 4.725 + 5.67),
            ("Sentry", 3.15),
            ("Stalker", 4.13),
            ("Adept", 3.5),
            ("High Templar", 2.62),
            ("Dark Templar", 3.94),
            ("Archon", 3.94),
            ("Observer", 2.63 + 1.31),
            ("Warp Prism", 5.36),
            ("Immortal", 3.15),
            ("Colossus", 3.15),
            ("Disruptor", 3.15),
            ("Phoenix", 5.95),
            ("Void Ray", 3.85 + 0.798),
            ("Oracle", 5.6),
            ("Tempest", 3.15),
            ("Carrier", 2.62),
            ("Interceptor", 10.5),
            ("Mothership", 2.62),
        ],
        "Terran": [
            ("SCV", 3.94),
            ("MULE", 3.94),
            ("Marine", 3.15 + 1.57),
            ("Marauder", 3.15 + 1.57),
            ("Reaper", 5.25),
            ("Ghost", 3.94),
            ("Hellion", 5.95),
            ("Hellbat", 3.15),
            ("Widow Mine", 3.94),
            ("Siege Tank tm", 3.15),
            ("Cyclone", 4.72),
            ("Thor", 2.62),
            ("Viking fm", 3.85),
            ("Viking am", 3.15),
            ("Medivac", 3.5 + 2.44),
            ("Liberator fm", 4.72),
            ("Banshee", 3.85 + 1.4),
            ("Raven", 4.13),
            ("Battlecruiser", 2.62),
        ],
        "Zerg": [
            ("Larva", 0.79),
            ("Drone", 3.94),
            ("Queen", 1.31),
            ("Zergling", 4.13 + 2.45),
            ("Baneling", 3.5 + 0.63),
            ("Roach", 3.15 + 1.05),
            ("Ravager", 3.85),
            ("Hydralisk", 3.15 + 0.79),
            ("Lurker", 4.13 + 0.413),
            ("Infestor", 3.15),
            ("Swarm Host", 3.15),
            ("Locust", 2.62),
            ("Ultralisk", 4.13 + 0.82),
            ("Overlord", 0.902 + 1.728),
            ("Overseer", 2.62 + 2.1),
            ("Changeling", 3.15),
            ("Mutalisk", 5.6),
            ("Corruptor", 4.725),
            ("Viper", 4.13),
            ("Brood Lord", 1.97),
            ("Broodling", 5.37),
        ],
    }
    print("Welcome to the Starcraft 2 Unit Speed Calculator!")
    average_speeds = calculate_race_averages(unit_speeds)

    while True:
        print("Please choose a race to see the average unit speeds:")
        print("Press the number 1 for Zerg")
        print("Press the number 2 for Terran")
        print("Press the number 3 for Protoss")
        print("Press the number 4 for All")
        print("Press the number 5 to  Exit")

        race_choice = input("Enter the number of your choice: ")

        if race_choice == "1":
            race = "Zerg"
        elif race_choice == "2":
            race = "Terran"
        elif race_choice == "3":
            race = "Protoss"
        elif race_choice == "5":
            print("Ok fuck you too then")
            return
        elif race_choice == "4":
            for race in average_speeds:
                display_race_averages(average_speeds, race)
            return
        else:
            print("Invalid choice. Please try again.")
            return

        if race in average_speeds:
            display_race_averages(average_speeds, race)
        else:
            print("No data available for the selected race.")


if __name__ == "__main__":
    main()
