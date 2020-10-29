import re

# This function takes in a line of text and returns
# a list of words in the line.


def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


def main():
    """ Read in lines from a file """

    # Open the file for reading, and store a pointer to it in the new
    # variable "file"
    my_file = open("dictionary.txt")

    # Create an empty list to store our names

    dictionary_list = []

    # Loop through each line in the file like a list
    for line in my_file:
        # Remove any line feed, carriage returns or spaces at the end of the line
        line = line.strip()

        # Add the name to the list

        dictionary_list.append(line)

    my_file.close()

    print("---Linear Search ---")

    text_file = open("AliceInWonderLand200.txt")

    line_tracker = 0

    for line in text_file:

        line_tracker += 1

        alice_list = split_line(line)

        for word in alice_list:
            # Start at the beginning of the list
            current_list_position = 0

            # Loop until you reach the end of the list, or the value at the
            # current position is equal to the key
            while current_list_position < len(dictionary_list) and dictionary_list[current_list_position] != word.upper():
                # Advance to the next item in the list
                current_list_position += 1

            if current_list_position == len(dictionary_list):

                print("Line " + str(line_tracker) + " possible misspelled word: " + word)

    text_file.close()

    print("---Binary Search ---")

    text_file = open("AliceInWonderLand200.txt")

    line_tracker = 0

    for line in text_file:

        line_tracker += 1

        alice_list = split_line(line)

        for word in alice_list:

            lower_bound = 0
            upper_bound = len(dictionary_list) - 1
            found = False

            # Loop until we find the item, or our upper/lower bounds meet
            while lower_bound <= upper_bound and not found:

                # Find the middle position
                middle_pos = (lower_bound + upper_bound) // 2

                # Figure out if we:
                # move up the lower bound, or
                # move down the upper bound, or
                # we found what we are looking for
                if dictionary_list[middle_pos] < word.upper():
                    lower_bound = middle_pos + 1
                elif dictionary_list[middle_pos] > word.upper():
                    upper_bound = middle_pos - 1
                else:
                    found = True
            if not found:
                print("Line " + str(line_tracker) + " possible misspelled word: " + word)

    text_file.close()


main()
