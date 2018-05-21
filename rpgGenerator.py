import math
import random

dict_test = {"Name": "Zara", "Age": 7, "Class": "First"}
dict_stats = {"strength": 0, "constitution": 0, "dexterity": 0, "intelligence": 0, "health": 0, "defense": 0, "charisma": 0, "luck": 0}
element = ["fire", "ice", "wind", "lightning", "earth", "dark", "holy", "poison"]
char_class = ["knight", "mage", "red-mage", "barbarian", "rogue", "thief", "shop keeper", "squire", "teacher", "monk", "deckhand", "demon prince", "dancer", "pirate"]
char_race = ["dwarf", "elf", "giant", "gnome", "goblin", "orcs", "turtle", "serpent", "sphinx", "human", "lizard", "fae", "gnoll", "vampire", "werewolf", "mermaid", "dryad", "seer", "hunter", "ghost", "drake", "demon", "angel", "cyclops", "shade", "possessed", "skelton", "zombie", "dragon", "shapeshifter"]
gold = 0
alignment = "neutral"
dict_rollout = ["warrior", "mage", "thief"]


def generate_character():
    for sta in dict_stats:
        dict_stats[sta] = random.randrange(1, 10)
    print(dict_stats)
    actual_class = char_class[random.randrange(0, len(char_class))]
    actual_race = char_race[random.randrange(0, len(char_race))]
    actual_element = element[random.randrange(0, len(element))]
    print(actual_class)
    print(actual_race)
    print(actual_element)


def generate_rollout(type, dict_stats_local):
    """
    Generate stats, than sort the stats in priority and apply them to a variety of character types
    :param type: String value of the type
    :param dict_stats_local: dictionary of character values to write to
    :return: Compiled dictionary of character values
    """
    stats = generate_stats(72, 8, 9)
    # Sort array
    stats.sort()
    # Reverse highest to lowest
    stats.reverse()
    # Pop the first element off the array depending on type
    if type == "warrior":
        print("Warrior")
        dict_stats_local["strength"] = stats.pop(0)
        dict_stats_local["health"] = stats.pop(0)
        dict_stats_local["defense"] = stats.pop(0)
        dict_stats_local["constitution"] = stats.pop(0)
        dict_stats_local["dexterity"] = stats.pop(0)
        dict_stats_local["charisma"] = stats.pop(0)
        dict_stats_local["intelligence"] = stats.pop(0)
        dict_stats_local["luck"] = stats.pop(0)
    if type == "mage":
        print("Mage")
        dict_stats_local["intelligence"] = stats.pop(0)
        dict_stats_local["constitution"] = stats.pop(0)
        dict_stats_local["dexterity"] = stats.pop(0)
        dict_stats_local["luck"] = stats.pop(0)
        dict_stats_local["defense"] = stats.pop(0)
        dict_stats_local["charisma"] = stats.pop(0)
        dict_stats_local["strength"] = stats.pop(0)
        dict_stats_local["health"] = stats.pop(0)
    if type == "theif":
        print("Theif")
        dict_stats_local["luck"] = stats.pop(0)
        dict_stats_local["charisma"] = stats.pop(0)
        dict_stats_local["dexterity"] = stats.pop(0)
        dict_stats_local["intelligence"] = stats.pop(0)
        dict_stats_local["constitution"] = stats.pop(0)
        dict_stats_local["strength"] = stats.pop(0)
        dict_stats_local["health"] = stats.pop(0)
        dict_stats_local["defense"] = stats.pop(0)
    print(dict_stats_local)


def generate_stats(total_stat_points, num_stats, max_value):
    """
    Generates a set of stats based on max threshold and number of stats
    :param total_stat_points: The max amount of points to spread across all stats
    :param num_stats: The number of values
    :param max_value: The top end value a stat can be set to
    :return:
    """
    stats = []
    counter = 0
    points_left = total_stat_points
    while counter < num_stats:
        if points_left > max_value:
            temp = random.randrange(1, max_value + 1)
            points_left -= temp
            stats.append(temp)
        elif points_left <= max_value:
            temp = random.randrange(1, points_left)
            points_left -= temp
            stats.append(temp)
        counter += 1
    return stats


def generate_gold(max_gold, gift):
    """
    Generates the starting gold for the character
    :param max_gold: The top end threshold of gold that can be gained
    :param gift: Influence the value by passing in a range from 0.01 + 1
    :return: Generated gold value
    """
    rand = random.randrange(1, 50)
    percentages = []
    for num in range(1, rand + 1):
        percentages.append(random.uniform(.02, .08))
        if rand > 10:
            percentages.append(random.uniform(.05, .24))
            if rand > 20:
                percentages.append(random.uniform(.25, .49))
                if rand > 30:
                    percentages.append(random.uniform(.50, .79))
                    if rand > 40:
                        percentages.append(random.uniform(.80, .94))
                        if rand > 48:
                            percentages.append(random.uniform(.95, 1))
        percentages.append(.02)
    return int((percentages[random.randrange(0, len(percentages) - 1)]+gift)*max_gold + random.randrange(1, 99))





if __name__ == '__main__':
    print("You are starting your journey with " + str(generate_gold(100000, 0.8)) + " pieces of gold!")
    generate_rollout("warrior", dict_stats)
    actual_class = char_class[random.randrange(0, len(char_class))]
    actual_race = char_race[random.randrange(0, len(char_race))]
    actual_element = element[random.randrange(0, len(element))]
    print(actual_class)
    print(actual_race)
    print(actual_element)
    generate_rollout("mage", dict_stats)
    actual_class = char_class[random.randrange(0, len(char_class))]
    actual_race = char_race[random.randrange(0, len(char_race))]
    actual_element = element[random.randrange(0, len(element))]
    print(actual_class)
    print(actual_race)
    print(actual_element)
    generate_rollout("theif", dict_stats)
    actual_class = char_class[random.randrange(0, len(char_class))]
    actual_race = char_race[random.randrange(0, len(char_race))]
    actual_element = element[random.randrange(0, len(element))]
    print(actual_class)
    print(actual_race)
    print(actual_element)