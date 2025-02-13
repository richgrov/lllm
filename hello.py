def main():
    file = open("dataset.txt", 'r')
    text = file.read()
    spliceIndex = int(len(text) * 0.9)

    first = text[:spliceIndex]
    last = text[spliceIndex:]

    vocab = set(text)


if __name__ == "__main__":
    main()
