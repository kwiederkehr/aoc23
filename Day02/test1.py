from part1 import line_to_cube_color_max

test_cases = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
]


def test_parse_line():
    test_cases = [
        ("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", ("Game 1", {"blue": 6, "red": 4, "green": 2})),
        ("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", ("Game 2", {"blue": 4, "red": 1, "green": 3})),
        ("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red", ("Game 3", {"blue": 6, "red": 20, "green": 13})),
        ("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red", ("Game 4", {"blue": 15, "red": 14, "green": 3})),
        ("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green", ("Game 5", {"blue": 2, "red": 6, "green": 3})),
    ]

    for test_case in test_cases:
        actual_result = line_to_cube_color_max(test_case[0])
        assert actual_result == test_case[1], test_case[0]


    print("All tests passed")


if __name__ == "__main__":
    test_parse_line()
