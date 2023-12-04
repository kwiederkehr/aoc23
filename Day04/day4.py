from collections import namedtuple, OrderedDict
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


CardInfo = namedtuple("GameInfo", ["winning_numbers", "your_numbers", "card_count"])


def part2():
    all_my_scratchcards = OrderedDict()

    # file_name = "input_sample.txt"
    file_name = "input.txt"
    file = open(file_name)
    lines = file.readlines()
    for line in lines:
        game_name, list_of_numbers = line.split(":")
        winning_numbers_str, your_numbers_str = list_of_numbers.split("|")
        game_name = int(game_name.strip("Card "))
        winning_numbers = [int(number.strip()) for number in winning_numbers_str.strip().split()]
        your_numbers = [int(number.strip()) for number in your_numbers_str.strip().split()]
        all_my_scratchcards[game_name] = CardInfo(winning_numbers=winning_numbers, your_numbers=your_numbers, card_count=1)

    # it's an ordered dict, so it executes in order
    for card_name, card_info in all_my_scratchcards.items():
        number_of_your_numbers_that_win = len([number for number in card_info.your_numbers if number in card_info.winning_numbers])
        if number_of_your_numbers_that_win > 0:
            for i in range(1,number_of_your_numbers_that_win+1):
                card_to_update = all_my_scratchcards[card_name+i]
                updated_card = CardInfo(winning_numbers=card_to_update.winning_numbers, your_numbers=card_to_update.your_numbers, card_count=card_to_update.card_count + card_info.card_count)
                all_my_scratchcards[card_name+i] = updated_card

    total_cards = sum([card_info.card_count for card_info in all_my_scratchcards.values()])
    print(f"THE TOTAL CARDS: {total_cards}")


if __name__=="__main__":
    main()
    part2()
