def fix_words(word):
    return word.lower().replace(' ', '-')

def process_csv(input_file, output_file):           # Put all my files through here one at a time
    with open(input_file, 'r') as infile:
        lines = infile.readlines()

    modified_lines = []
    for line in lines:
        words = line.strip().split(',')
        modified_words = [fix_words(word) for word in words]
        modified_line = ','.join(modified_words)
        modified_lines.append(modified_line)

    with open(output_file, 'w') as outfile:
        outfile.write('\n'.join(modified_lines))

if __name__ == "__main__":
    input_csv_file = "verb_list.csv"    # Replace with the name of your input CSV file
    output_csv_file = "verb_list_output.csv"  # Replace with the name of your output CSV file

    process_csv(input_csv_file, output_csv_file)
