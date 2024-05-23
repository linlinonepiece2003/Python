import string
import json

def countWords_2(inputF, outputF):
    with open(inputF, 'r') as file:
        lines = file.readlines()
        lines = [line.strip().lower().translate(str.maketrans("", "", string.punctuation)) for line in lines if line != '\n']

    Wcounts = {}
    all_Wcount = 0
    for line in lines:
        words = line.split()
        for w in words:
            if w == '':
                continue
            Wcounts[w] = Wcounts.get(w, 0) + 1
            all_Wcount += 1

    for w in Wcounts:
        if w == '':
            continue
        Wcounts[w] = round((Wcounts[w] / all_Wcount) * 100, 2)

    sorted_Wcounts = dict(sorted(Wcounts.items(), key=lambda item: item[1], reverse=True))

    with open(outputF, 'w') as json_file:
        json.dump(sorted_Wcounts, json_file)


# countWords_2('E:/Code/VScode/Python/62fit3ss1_assignment2_2101140046/sample.txt', 'sample_out_2.json')       