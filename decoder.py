def main():
    decode("coding_qual_input.txt")

def decode(message_file):
    with open(message_file, 'r') as file:
        lines = file.readlines()
    numbers = [int(line.split()[0]) for line in lines]
    words = [line.split()[1] for i, line in enumerate(lines) if i + 1 in numbers]
    decoded_message = ' '.join(words)
    return decoded_message

if __name__ == "__main__":
    main()