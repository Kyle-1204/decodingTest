def main():
    decode("coding_qual_input.txt")

def decode(message_file):
    with open(message_file) as file:
        data = []
        for line in file:
            line = line.split()
            data.append(line)
    sorted_list = sorted(data, key=lambda entry: int(entry[0]))
    count = 0
    inc = 1
    words = []
    while (count < len(sorted_list)):
        words.append(sorted_list[count][1])
        inc = inc + 1
        count = count + inc
    decoded_message = ' '.join(words)
    return decoded_message

if __name__ == "__main__":
    main()