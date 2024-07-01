# In this kata we want to convert a string into an integer. The strings simply represent the numbers in words.
#
# Examples:
#
# "one" => 1
# "twenty" => 20
# "two hundred forty-six" => 246
# "seven hundred eighty-three thousand nine hundred and nineteen" => 783919
# Additional Notes:
#
# The minimum number is "zero" (inclusively)
# The maximum number, which must be supported is 1 million (inclusively)
# The "and" in e.g. "one hundred and twenty-four" is optional, in some cases it's present and in others it's not
# All tested numbers are valid, you don't need to validate them

units_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
              'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

teens_dict = {'eleven': 11, 'twelve': 12,
              'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17,
              'eighteen': 18, 'nineteen': 19}

tens_dict = {'ten': 10, 'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50,
             'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90}

hundreds_dict = {'thousand': 1000, 'hundred': 100}


def parse_int(my_string):

    def prep_word(string_to_parse):
        # split string
        no_hyphens = string_to_parse.replace('-', ' ')
        remove_and = no_hyphens.replace(' and ', ' ')
        word_list = remove_and.split()
        return word_list

    def parse_words(word_list, multiplier, current_count):
        current_count = current_count
        # Handle hundreds
        if 'hundred' in word_list:
            current_count += units_dict[word_list[0]] * 100 * multiplier
            if word_list[-1] == 'hundred':  # multiple of one hundred
                return current_count

        # # Handle if no 'hundred' in word list, but with multiple of ten or a teen
        if word_list[-1] in tens_dict:  # multiple of ten
            current_count += tens_dict[word_list[-1]] * multiplier
        elif word_list[-1] in teens_dict:  # teen
            current_count += teens_dict[word_list[-1]] * multiplier
            return current_count

        # Handle units
        if word_list[-1] in units_dict:
            current_count += units_dict[word_list[-1]] * multiplier
        # Check if second last word is a multiple of ten
        if len(word_list) > 1 and word_list[-2] in tens_dict:
            current_count += tens_dict[word_list[-2]] * multiplier

        return current_count

    words = prep_word(my_string)
    print(words)

    num_counter = 0
    thousands = None

    # Handle 1000000
    if 'million' in words:
        return 1000000

    # Handle 0:
    if 'zero' in words:
        return 0

    # Handle all other cases
    # Split words into batches of 3 positions (ie 0 to 999)
    if 'thousand' in words:
        thousand_index_position = words.index('thousand')
        print(f"thousand index: {thousand_index_position}")
        thousands = words[0: thousand_index_position]
        units_tens_hundreds = words[thousand_index_position + 1:]
        print(thousands, units_tens_hundreds)
    else:
        units_tens_hundreds = words
        print(units_tens_hundreds)

    if units_tens_hundreds:
        num_counter = parse_words(units_tens_hundreds, 1, num_counter)
    if thousands:
        num_counter = parse_words(thousands, 1000, num_counter)

    return num_counter


print(parse_int('one'))
print(parse_int('twenty'))
print(parse_int('thirty-two'))
print(parse_int('two hundred and sixty three thousand four hundred and forty-six'))
print(parse_int('two thousand'))
print(parse_int('nineteen'))

# Tests
# test.assert_equals(parse_int('one'), 1)
# test.assert_equals(parse_int('twenty'), 20)
# test.assert_equals(parse_int('two hundred forty-six'), 246)
