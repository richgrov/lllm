import random as rand
from data import Data

CONTEXT_WINDOW_SIZE = 64

def main():
    thing = Data("dataset.txt")
    this = thing.getRandomContextWindow(CONTEXT_WINDOW_SIZE)
    that = thing.randomVecsInVocab(CONTEXT_WINDOW_SIZE)
    # for i in range(len(this)):
    #     print(len(this[i][0]))
    print(len(this[0]))
    print(that)
    # randomized_vocab_vectors = {}
    
    # for character in vocab:
    #     random_vec = []
    #     for vec_idx in range(63):
    #         random_vec.append(rand.uniform(-1.0, 1.0))
    #     randomized_vocab_vectors[character] = random_vec
    
    # for idx in range(len(shakespear)):
    #     print(shakespear[idx-31:idx+32])
    # print(randomized_vocab_vectors)
    # print(vocab)


if __name__ == "__main__":
    main()
