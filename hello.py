import random as rand

TRAIN_SPLIT = 0.9
CONTEXT_WINDOW_SIZE = 64

def main():
    file = open("dataset.txt", 'r')
    shakespear = file.read()
    spliceIndex = int(len(shakespear) * TRAIN_SPLIT)

    first = shakespear[:spliceIndex]
    last = shakespear[spliceIndex:]
    
    vocab = set(shakespear)
    
    randomized_vocab_vectors = {}
    
    for character in vocab:
        random_vec = []
        for vec_idx in range(63):
            random_vec.append(rand.uniform(-1.0, 1.0))
        randomized_vocab_vectors[character] = random_vec
    
    # for idx in range(len(shakespear)):
    #     print(shakespear[idx-31:idx+32])
    print(randomized_vocab_vectors)
    print(vocab)


if __name__ == "__main__":
    main()
