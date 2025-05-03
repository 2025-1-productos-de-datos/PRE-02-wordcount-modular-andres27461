# obtain a list of files in the input directory
import os

from ._internals.preprocess_lines import preprocess_lines
from ._internals.split_in_words import split_in_words
from ._internals.count_words import count_words

from ._internals.write_count_words import write_count_words


def main():

    ## read all lines
    all_lines = []
    input_file_list = os.listdir("data/input/")
    for filename in input_file_list:
        file_path = os.path.join("data/input", filename)
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            all_lines.extend(lines)

    all_lines = preprocess_lines(all_lines)
    words = split_in_words(all_lines)
    counter = count_words(words)
    write_count_words(counter)


if __name__ == "__main__":
    main()
