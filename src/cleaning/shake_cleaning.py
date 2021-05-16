import pickle
import re


def clean_all_lines():
    # 800,077
    all_lines = []
    with open('../../data/shakespeare/alllines.txt') as plays:
        for i, line in enumerate(plays):
            if line.split()[0] == "Exeunt":
                continue

            line = line.strip()
            line = line[1:len(line) - 1]

            if len(line) == 0:
                continue

            # If starts with ACT, SCENE, or Enter remove
            first_word = line.split()[0]
            if first_word == 'ACT' or first_word == 'SCENE' or first_word == "Enter":
                continue

            # Pad punctuation
            line = pad_puncutation(line)
            line.rstrip()
            line = " ".join(line.split())
            all_lines.append(line)
    return all_lines


def clean_parallel_text():
    # 331817
    modern_lines_aligned = []
    original_lines_aligned = []
    with open('../../data/shakespeare/clean_modern.txt') as modern, open(
            '../../data/shakespeare/clean_original.txt') as original:
        word_counter = 0
        for modernLine, originalLine in zip(modern, original):
            # Strup newline
            modernLine = modernLine.rstrip()
            originalLine = originalLine.rstrip()
            modern_lines_aligned.append(modernLine)
            original_lines_aligned.append(originalLine)
    return modern_lines_aligned, original_lines_aligned


def pad_puncutation(s):
    s = re.sub('([.,!?()])', r' \1 ', s)
    s = re.sub('\s{2,}', ' ', s)
    return s


def write_to_file(modern, original, all_lines):
    with open('../../data/shakespeare/processed/all_proc.txt', 'w') as f:
        for item in all_lines:
            f.write("%s\n" % item)

    with open('proc_all', 'wb') as fp:
        pickle.dump(all_lines, fp)

    with open('../../data/shakespeare/processed/modern_proc.txt', 'w') as f:
        for item in modern:
            f.write("%s\n" % item)

    with open('proc_modern', 'wb') as fp:
        pickle.dump(modern, fp)

    with open('../../data/shakespeare/processed/original_proc.txt', 'w') as f:
        for item in original:
            f.write("%s\n" % item)

    with open('proc_original', 'wb') as fp:
        pickle.dump(original, fp)


def main():
    modern, original = clean_parallel_text()
    all_lines = clean_all_lines()
    write_to_file(modern, original, all_lines)


if __name__ == '__main__':
    main()