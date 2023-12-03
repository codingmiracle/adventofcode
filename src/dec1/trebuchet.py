
def get_calibration_value(string: str) -> int:
    keywords = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
                "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
    first_digit = 0
    last_digit = 0
    min_first = len(string)
    max_last = -1
    for word in keywords:
        index = string.find(word)
        if index < min_first and index != -1:
            first_digit = keywords.get(word)
            min_first = index
        index = string.rfind(word)
        if index > max_last and index != -1:
            last_digit = keywords.get(word)
            max_last = index

    return int(str(first_digit) + str(last_digit))


def part1(input: str) -> int:
    lines = [token for token in input.split("\n")]
    calibration_sum = 0
    for line in lines:
        nums = [char for char in line if char.isdigit()]
        if len(nums) == 0:
            continue
        elif len(nums) == 1:
            calibration_value = int(str(nums[0]) + str(nums[0]))
        else:
            calibration_value = int(str(nums[0]) + str(nums[len(nums) - 1]))
        calibration_sum += calibration_value
    return calibration_sum


def part2(input: str) -> int:
    lines = [token for token in input.split("\n")]
    calibration_sum = 0
    for line in lines:
        print(get_calibration_value(line))
        calibration_sum += get_calibration_value(line)
    return calibration_sum


if __name__ == '__main__':
    inputfile = open('input.txt')
    print(part2(inputfile.read()))
