colors = ["red", "blue", "green"]


def line_to_cube_color_max(line: str) -> tuple[str, dict[str, int]]:
    game_number, all_reaches = line.split(":")
    reaches = all_reaches.split(";")
    maxes = {color: 0 for color in colors}
    for one_reach in reaches:
        all_colors = one_reach.split(",")
        for one_color in all_colors:
            amount, color_name = one_color.strip().split(" ")
            assert color_name in colors, "Invalid color name"
            maxes[color_name] = int(amount) if int(amount) > maxes[color_name] else maxes[color_name]

    return game_number, maxes


def read_file(file_name: str) -> dict[str, dict[str, int]]:
    file = open(file_name)
    lines = file.readlines()

    games_and_maxes = {}

    for line in lines:
        game_name, maxes = line_to_cube_color_max(line)
        games_and_maxes[game_name] = maxes

    return games_and_maxes


def get_possible_game_names(games_to_maxes: dict[str, dict[str, int]], bag_actually_contained: dict[str, int]) -> list[str]:
    possible_games = []
    print(games_to_maxes)
    for game_name, colors_to_maxes in games_to_maxes.items():
        enough_of_each_color = [color_amount <= bag_actually_contained[color_name] for color_name, color_amount in colors_to_maxes.items()]
        if all(enough_of_each_color):
            possible_games.append(game_name)

    return possible_games


def sum_game_ids(game_names: list[str]) -> int:
    total = 0
    for game_name in game_names:
        game_id = int(game_name.strip("Game "))
        total += game_id

    return total


def get_powers(games_to_maxes: dict[str, dict[str, int]]) -> list[int]:
    powers = []
    for maxes in games_to_maxes.values():
        power = 1
        for color_max in maxes.values():
            power *= color_max

        powers.append(power)

    return powers


def main():
    print("I can do this!")
    games_to_maxes = read_file("input1.txt")

    bag_actually_contained = {"red":12 , "blue": 14, "green": 13}
    possible_games = get_possible_game_names(games_to_maxes, bag_actually_contained)
    print(f"ALL THE POSSIBLE GAMES {possible_games}")

    total_sum = sum_game_ids(possible_games)

    print(f"THE TOTAL SUM: {total_sum}")

    powers = get_powers(games_to_maxes)
    total_power_sum = 0
    for power in powers:
        total_power_sum += power

    print(f"THE TOTAL POWERS: {total_power_sum}")


if __name__=="__main__":
    main()