from first import first_and_last_number_from_string_as_2_digit_number, convert_any_spelled_numbers_into_numbers


def test_1a():
    test_cases = [
        (27, "hello27"),
        (12, "12"),
        (12, "1s2d"),
        (12, "1asdf2"),
        (12,"aaa1b2dddd"),
        (13, "123"),
        (77, "a7dadsfasdga"),
        (77, "7"),
        (77, "77"),
        (77, "asfasdfasgd7a"),
        (77, "a7b"),
        (77,"787"),
        (77, "7897"),
        (12, "1abc2"),
        (38, "pqr3stu8vwx"),
        (15, "a1b2c3d4e5f"),
        (77, "treb7uchet"),
        (29, "two1nine"),
        (83, "eightwothree"),
        (13, "abcone2threexyz"),
        (24, "xtwone3four"),
        (42, "4nineeightseven2"),
        (14, "zoneight234"),
        (76, "7pqrstsixteen"),
        (79, "sevenine")
    ]
    for test_case in test_cases:
        print(f"now testing {test_case}")
        assert test_case[0] == first_and_last_number_from_string_as_2_digit_number(test_case[1]), test_case

def test_1b():
    test_cases = [
        # ("1", "one"),
        ("22two", "2two"),
        ("2tw", "2tw"),
        ("22", "22"),
        ("2two2", "two2"),
        ("thirty3three", "thirtythree"),
        ("2two19nine","two1nine"),
        ("8wo3", "eightwothree"),
        ("abc123xyz", "abcone2threexyz"),
        ("x2ne34","xtwone3four"),
        ("49872","4nineeightseven2"),
        ("z1ight234","zoneight234"),
        ("7pqrst6teen","7pqrstsixteen"),
    ]
    for test_case in test_cases:
        print(f"in test case {test_case}")
        actual_return = convert_any_spelled_numbers_into_numbers(test_case[1])
        assert test_case[0] == actual_return, f"{test_case}, {actual_return}"


if __name__=="__main__":
    test_1a()
    # test_1b()