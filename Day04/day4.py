
def main():
    # file_name = "input_sample.txt"
    file_name = "input.txt"
    file = open(file_name)
    lines = file.readlines()
    total = 0
    for line in lines:
        game_name, list_of_numbers = line.split(":")
        winning_numbers_str, your_numbers_str = list_of_numbers.split("|")
        game_name.strip()
        winning_numbers = [int(number.strip()) for number in winning_numbers_str.strip().split()]
        your_numbers = [int(number.strip()) for number in your_numbers_str.strip().split()]
        number_of_your_numbers_that_win = len([number for number in your_numbers if number in winning_numbers])
        if number_of_your_numbers_that_win > 0:
            total += pow(2,number_of_your_numbers_that_win - 1)
    print(f"TOTAL POINTS: {total}")

if __name__=="__main__":
    main()