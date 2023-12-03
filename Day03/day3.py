from collections import namedtuple

Coordinate = namedtuple("Coordinate", ["row", "col"])
NumberWithCoordinates = namedtuple("NumberWithCoordinates", ["value", "row", "col_start", "col_end"])


def get_symbols(lines: list[str]) -> set[Coordinate]:
    coordinates = set()
    row = 0
    for line in lines:
        line = line.strip()
        col = 0
        for char in line:
            if not char.isdigit() and not char == ".":
                coordinates.add(new_coord := Coordinate(row=row, col=col))
            col += 1
        row += 1
    return coordinates


def get_asterisks(lines: list[str]) -> set[Coordinate]:
    coordinates = set()
    row = 0
    for line in lines:
        line = line.strip()
        col = 0
        for char in line:
            if char == "*":
                coordinates.add(new_coord := Coordinate(row=row, col=col))
            col += 1
        row += 1
    return coordinates


def get_numbers(lines: list[str]) -> set[NumberWithCoordinates]:
    numbers_with_coordinates = set()
    for row, line in enumerate(lines):
        num_as_str = ""
        first_col_for_num_as_str = None
        for col, char in enumerate(line):
            if char.isdigit():
                if num_as_str == "":
                    first_col_for_num_as_str = col

                num_as_str += char

                if col + 1 == len(line) or not line[col + 1].isdigit():
                    numbers_with_coordinates.add(
                        NumberWithCoordinates(value=int(num_as_str), row=row, col_start=first_col_for_num_as_str,
                                              col_end=col))
                    first_col_for_num_as_str = None
                    num_as_str = ""

    return numbers_with_coordinates


def get_surrounding_coordinates(number: NumberWithCoordinates) -> set[Coordinate]:
    coords_to_check = set()
    # the row before
    for i in range(number.col_start - 1, number.col_end + 2):  # range is exclusive so need to add 2
        coords_to_check.add(Coordinate(row=number.row - 1, col=i))

    # the row
    coords_to_check.add(Coordinate(row=number.row, col=number.col_start - 1))
    coords_to_check.add(Coordinate(row=number.row, col=number.col_end + 1))

    # the row after
    for i in range(number.col_start - 1, number.col_end + 2):  # range is exclusive so need to add 2
        coords_to_check.add(Coordinate(row=number.row + 1, col=i))

    return coords_to_check


def has_symbol_near_coords(number: NumberWithCoordinates, symbols: set[Coordinate]) -> bool:
    coords_to_check = get_surrounding_coordinates(number)

    return any([coord in symbols for coord in coords_to_check])


def get_numbers_near_symbols(numbers: set[NumberWithCoordinates], symbols: set[Coordinate]) -> list[int]:
    # for each number, check if it has symbols in relevant coords
    numbers_near_symbols = []
    for number in numbers:
        if has_symbol_near_coords(number, symbols):
            numbers_near_symbols.append(number.value)
    return numbers_near_symbols


def is_adjacent_to(number: NumberWithCoordinates, coord: Coordinate):
    # they're adjacent if the coord is surrounding to the number
    surrounding_coordinates = get_surrounding_coordinates(number)
    return coord in surrounding_coordinates


def get_adjacent_numbers(coord: Coordinate, numbers: set[NumberWithCoordinates]) -> list[int]:
    adjacent_numbers = []
    for number in numbers:
        if is_adjacent_to(number, coord):
            adjacent_numbers.append(number.value)
    return adjacent_numbers


def get_gear_ratios(asterisks: set[Coordinate], numbers: set[NumberWithCoordinates]) -> list[int]:
    gear_ratios = []
    for asterisk in asterisks:
        adjacent_numbers = get_adjacent_numbers(asterisk, numbers)
        if len(adjacent_numbers) == 2:
            gear_ratios.append(adjacent_numbers[0] * adjacent_numbers[1])

    return gear_ratios


def main():
    print("hello world")

    # file_name = "day3_sample.txt"
    file_name = "day3_input.txt"
    file = open(file_name)
    lines = file.readlines()

    all_symbols: set[Coordinate] = get_symbols(lines)
    all_numbers: set[NumberWithCoordinates] = get_numbers(lines)
    numbers_near_symbols: list[int] = get_numbers_near_symbols(all_numbers, all_symbols)

    total = sum(numbers_near_symbols)
    print(f"THE TOTAL {total}")

    asterisks = get_asterisks(lines)
    gear_ratios = get_gear_ratios(asterisks, all_numbers)
    print(f"TOTAL GEAR RATIOS {sum(gear_ratios)}")


if __name__ == "__main__":
    main()
