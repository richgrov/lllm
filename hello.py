import random as rand
import jax.numpy as jnp
from jax import grad, jit, vmap

def predict(params, inputs):
    for W, b in params:
        outputs = jnp.dot(inputs, W) + b
        inputs = jnp.tanh(outputs)  # inputs to the next layer
    return outputs                # no activation on last layer

def loss(params, inputs, targets):
    preds = predict(params, inputs)
    return jnp.sum((preds - targets)**2)

def main():
    file = open("dataset.txt", 'r')
    shakespear = file.read()
    spliceIndex = int(len(shakespear) * 0.9)

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

    grad_loss = jit(grad(loss))  # compiled gradient evaluation function
    perex_grads = jit(vmap(grad_loss, in_axes=(None, 0, 0)))  # fast per-example grads

    print(grad_loss)
    print(perex_grads)

if __name__ == "__main__":
    main()
