def main():
    decode("coding_qual_input.txt")

def decode(message_file):
    with open(message_file) as file:
        for line in file:
            print(line)

if __name__ == "__main__":
    main()