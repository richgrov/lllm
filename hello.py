def main():
    file = open("dataset.txt", 'r')
    shakespear = file.read()
    spliceIndex = int(len(shakespear) * 0.9)

    first = shakespear[:spliceIndex]
    last = shakespear[spliceIndex:]

    vocab = set(shakespear)
    for idx in range(len(shakespear)):
        print(shakespear[idx-31:idx+32])
    print(vocab)


if __name__ == "__main__":
    main()
