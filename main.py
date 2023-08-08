def calculate_average_speed(units):
    speeds = [unit[1] for unit in units]
    return sum(speeds) / len(speeds)

def calculate_race_averages(unit_speeds):
    average_speeds = {}
    for race, units in unit_speeds.items():
        overall_average_speed = calculate_average_speed(units)
        average_speeds[race] = {
            "overall": overall_average_speed
        }

        if race == "Zerg":
            on_creep_units = [(unit[0], unit[1]) for unit in units if unit[2] == "on creep"]
            off_creep_units = [(unit[0], unit[1]) for unit in units if unit[2] == "off creep"]
            on_creep_average_speed = calculate_average_speed(on_creep_units)
            off_creep_average_speed = calculate_average_speed(off_creep_units)
            average_speeds[race]["on_creep"] = on_creep_average_speed
            average_speeds[race]["off_creep"] = off_creep_average_speed

    return average_speeds

def display_race_averages(average_speeds, selected_race):
    speeds = average_speeds[selected_race]
    print(f"{selected_race.capitalize()} Average Speed:")
    if isinstance(speeds['overall'], float):
        print(f"Overall: {speeds['overall']}")
    else:
        print("Invalid overall speed value.")
    if "on_creep" in speeds:
        if isinstance(speeds['on_creep'], float):
            print(f"On Creep: {speeds['on_creep']}")
        else:
            print("Invalid on_creep speed value.")
        if isinstance(speeds['off_creep'], float):
            print(f"Off Creep: {speeds['off_creep']}")
        else:
            print("Invalid off_creep speed value.")
    print()


def main():
    unit_speeds = {
        "Protoss": [
            ("High Templar", 2.62, "off creep"),
            ("Carrier", 2.62, "off creep"),
            ("Mothership", 2.62, "off creep"),
            ("Observer", 2.62, "off creep"),
            ("Void RayA S", 2.62, "off creep"),
            ("Void RayA", 2.89, "off creep"),
            ("Colossus", 3.15, "off creep"),
            ("Disruptor", 3.15, "off creep"),
            ("Immortal", 3.15, "off creep"),
            ("Sentry", 3.15, "off creep"),
            ("Zealot", 3.15, "off creep"),
            ("Tempest", 3.15, "off creep"),
            ("Adept", 3.5, "off creep"),
            ("Void Ray", 3.85, "off creep"),
            ("Archon", 3.94, "off creep"),
            ("Dark Templar", 3.94, "off creep"),
            ("ObserverS", 3.94, "off creep"),
            ("Probe", 3.94, "off creep"),
            ("Stalker", 4.13, "off creep"),
            ("Warp Prism", 4.13, "off creep"),
            ("Void RayS", 4.65, "off creep"),
            ("ZealotS", 4.72, "off creep"),
            ("Warp PrismS", 5.36, "off creep"),
            ("Shade (Adept)", 5.6, "off creep"),
            ("Oracle", 5.6, "off creep"),
            ("Phoenix", 5.95, "off creep"),
            ("Purification Nova (Disruptor)", 5.95, "off creep"),
            ("ZealotSA", 10.4, "off creep"),
            ("Interceptor", 10.5, "off creep"),
        ],
            "Terran": [
                ("Battlecruiser", 2.62, "off creep"),
                ("Thor", 2.62, "off creep"),
                ("Hellbat", 3.15, "on creep"),
                ("Marauder", 3.15, "on creep"),
                ("Marine", 3.15, "on creep"),
                ("Siege Tank", 3.15, "on creep"),
                ("Viking (Assault Mode)", 3.15, "on creep"),
                ("Medivac", 3.5, "off creep"),
                ("Banshee", 3.85, "off creep"),
                ("Viking (Fighter Mode)", 3.85, "off creep"),
                ("Ghost", 3.94, "off creep"),
                ("MULE", 3.94, "off creep"),
                ("SCV", 3.94, "off creep"),
                ("Widow Mine", 3.94, "off creep"),
                ("MedivacS", 4.13, "off creep"),
                ("Raven", 4.13, "off creep"),
                ("Cyclone", 4.72, "on creep"),
                ("Liberator", 4.72, "on creep"),
                ("MarauderA", 4.72, "on creep"),
                ("MarineA", 4.72, "on creep"),
                ("BansheeS", 5.25, "off creep"),
                ("Reaper", 5.25, "off creep"),
                ("MedivacA", 5.94, "off creep"),
                ("Hellion", 5.95, "off creep")
            ],
            "Zerg": [
                    ("Overlord", 0.902, "off creep"),
                    ("Queen", 1.31, "on creep"),
                    ("Spine Crawler", 1.4, "on creep"),
                    ("Spore Crawler", 1.4, "on creep"),
                    ("Brood Lord", 1.97, "off creep"),
                    ("RoachB", 1.97, "on creep"),
                    ("Overseer", 2.62, "off creep"),
                    ("Locust", 2.62, "on creep"),
                    ("OverlordS", 2.62, "off creep"),
                    ("InfestorB", 2.8, "on creep"),
                    ("Changeling (Undisguised)", 3.15, "on creep"),
                    ("Hydralisk", 3.15, "on creep"),
                    ("Infestor", 3.15, "on creep"),
                    ("Roach", 3.15, "on creep"),
                    ("Swarm Host", 3.15, "on creep"),
                    ("Baneling", 3.5, "on creep"),
                    ("Ravager", 3.85, "on creep"),
                    ("Drone", 3.94, "off creep"),
                    ("HydraliskS", 3.94, "on creep"),
                    ("Viper", 4.13, "off creep"),
                    ("BanelingS", 4.13, "on creep"),
                    ("Lurker", 4.13, "on creep"),
                    ("Ultralisk", 4.13, "on creep"),
                    ("Zergling", 4.13, "on creep"),
                    ("RoachS", 4.2, "on creep"),
                    ("LurkerS", 4.55, "on creep"),
                    ("OverseerS", 4.72, "off creep"),
                    ("Corruptor", 4.73, "off creep"),
                    ("UltraliskS", 4.95, "on creep"),
                    ("Broodling", 5.37, "on creep"),
                    ("Mutalisk", 5.6, "off creep"),
                    ("ZerglingS", 6.57, "on creep")
        ]
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