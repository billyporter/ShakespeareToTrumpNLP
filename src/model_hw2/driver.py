import sys
import transformer
import math
import os
import random


def read_parallel(file1, file2):
    with open('data/temp_combine.txt',
              'w') as f, open(file1) as source, open(file2) as target:
        for line1, line2 in zip(source, target):
            line1 = line1.strip().replace('\t', ' ')
            line2 = line2.replace('\t', ' ')
            combined_line = f'{line1}\t{line2}'
            f.write(combined_line)


def split_data(combined, train, dev):

    lines = []
    with open(combined) as f:
        lines = f.readlines()
        line_count = len(lines)

    random.shuffle(lines)
    print(line_count)
    train_count = line_count - (11054 * 0.2)

    with open(combined) as f, open(train, 'w') as f_train, open(dev,
                                                                'w') as f_dev:
        for i, line in enumerate(lines):
            if i < train_count:
                f_train.write(line)
            else:
                f_dev.write(line)
    return


def main():
    shake_modern = 'data/truth/modern_proc.txt'
    shake_original = 'data/truth/original_proc.txt'

    target_file = shake_original
    source_file = shake_modern
    test_file = 'data/truth/trump.txt'
    gen_file = 'data/s_to_t/shake_fake_1'
    model = 'saved_models/model_TS_1'
    os.system('rm -f data/s_to_t/*')
    os.system('rm -f data/t_to_s/*')
    os.system('rm -f saved_models/*')
    combined = 'data/temp_combine.txt'
    train_data = 'data/temp_train.txt'
    dev_data = 'data/temp_dev.txt'

    iter_num = 1
    while (True):
        print(f'---------{iter_num} iteration---------')

        # Create temporary joint file
        read_parallel(source_file, target_file)
        split_data(combined, train_data, dev_data)

        # Train transformer
        train_args = f'--train {train_data} --dev {dev_data} --save {model}'.split(
        )
        transformer.main(train_args)

        # Translate
        test_args = f'--load {model} --outfile {gen_file} {test_file}'.split()
        transformer.main(test_args)

        # Increase iteration, set new files
        iter_num += 1
        source_file = gen_file
        if iter_num % 2 == 0:
            target_file = 'data/truth/all_proc.txt'
            test_file = 'data/truth/trump.txt'
            gen_file = f'data/s_to_t/shake_fake_{math.ceil((iter_num + 1)/ 2)}'
            model = f'saved_models/model_TS_{math.ceil((iter_num + 1) / 2)}'
        else:
            target_file = 'data/truth/trump.txt'
            test_file = 'data/truth/all_proc.txt'
            gen_file = f'data/t_to_s/trump_fake_{math.ceil((iter_num + 1) / 2)}'
            model = f'saved_models/model_ST_{math.ceil((iter_num + 1) / 2)}'


if __name__ == '__main__':
    main()
