import string
import json

def countWords_1(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
        lines = [line.strip().lower().translate(str.maketrans("", "", string.punctuation)) for line in lines if line != '\n']

    w_counts = {}
    for line in lines:
        words = line.split()
        for w in words:
            if w == '':
                continue
            w_counts[w] = w_counts.get(w, 0) + 1

    with open(output_file, 'w') as json_file:
        json.dump(w_counts, json_file)

# countWords_1('E:/Code/VScode/Python/62fit3ss1_assignment2_2101140046/sample.txt', 'sample_out_1.json')