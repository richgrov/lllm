def main():
    file = open("dataset.txt", 'r')
    vocab = set(file.read())
    print(vocab)


if __name__ == "__main__":
    main()
