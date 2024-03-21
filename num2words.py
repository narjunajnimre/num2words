# A Python program to convert numbers into words with certain limitations.

# Dictionary for basic number words
num_to_word = {
    # This dictionary maps individual numbers to their word equivalents for quick lookup.
    # It includes numbers from 0 to 19, and multiples of ten up to ninety.
    0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
    5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
    10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
    14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
    18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty',
    40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy',
    80: 'eighty', 90: 'ninety'
}

# Suffixes for larger numbers
large_number_suffixes = [
    # This list contains tuples of numerical values and their corresponding suffixes.
    # It covers larger numbers from thousands up to decillions.
    (10**3, 'thousand'), (10**6, 'million'), (10**9, 'billion'),
    (10**12, 'trillion'), (10**15, 'quadrillion'), (10**18, 'quintillion'),
    (10**21, 'sextillion'), (10**24, 'septillion'), (10**27, 'octillion'),
    (10**30, 'nonillion'), (10**33, 'decillion')
]

# Function to translate numbers to words
def translate_number_to_words(number):
    # This function is the core of the program, converting a numerical value into its word form.
    if number < 20:
        # Numbers less than 20 are directly mapped from the dictionary.
        return num_to_word[number]
    elif number < 100:
        # For numbers between 20 and 99, the tens and ones places are processed.
        if number % 10 == 0:
            # If the number is a multiple of ten, it's directly mapped from the dictionary.
            return num_to_word[number]
        else:
            # Otherwise, the tens and ones places are combined with a hyphen.
            return num_to_word[number // 10 * 10] + '-' + num_to_word[number % 10]
    elif number < 1000:
        # For numbers between 100 and 999, the hundreds place is processed.
        hundreds_digit = number // 100
        remainder = number % 100
        if remainder:
            # If there's a remainder, 'hundred' is followed by 'and' and the remainder in words.
            return num_to_word[hundreds_digit] + ' hundred and ' + translate_number_to_words(remainder)
        return num_to_word[hundreds_digit] + ' hundred'
    else:
        # For numbers 1000 and above, the function iterates over the large_number_suffixes.
        formatted_number = ''
        for value, name in reversed(large_number_suffixes):
            if number >= value:
                # The number is divided into the large number part and the remainder.
                num = number // value
                remainder = number % value
                if remainder or (name == 'thousand' and number % 1000 != 0):
                    # The large number part is converted to words and appended with its suffix.
                    formatted_number += translate_number_to_words(num) + ' ' + name
                    if remainder and remainder < 100:
                        # If the remainder is less than 100, 'and' is added.
                        formatted_number += ' and '
                    elif remainder:
                        # If there's a remainder greater than 100, a comma is added.
                        formatted_number += ', '
                    number %= value
                else:
                    # If there's no remainder, only the large number part is converted to words.
                    formatted_number += translate_number_to_words(num) + ' ' + name
                    number %= value
                    break
        if number > 0:
            # Any remaining number is converted to words and appended.
            formatted_number += translate_number_to_words(number)
        return formatted_number.strip(', ')

# Main program
if __name__ == '__main__':
    while True:
        # The program runs in a loop, prompting the user for input.
        user_input = input("Enter a number or '~' to exit: ")
        if user_input == '~':
            # If the user enters '~', the program exits.
            break
        elif user_input.isdigit() and len(user_input) <= 36:
            # If the input is a digit and within the 36-digit limit, it's converted to an integer.
            number = int(user_input)
            # The number is then passed to the function and the result is printed.
            print(translate_number_to_words(number))
        elif len(user_input) > 36:
            # If the input exceeds the 36-digit limit, an error message is displayed.
            print("Error: The number is too long. Please enter a number with up to 36 digits.")
        else:
            # If the input is invalid, an error message is displayed.
            print("Please enter a valid number.")