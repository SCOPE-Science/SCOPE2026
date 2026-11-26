"""Literal ternary enumeration of two scattered 012 embeddings; no dependencies."""
from itertools import product
from math import comb

def count_and_type(word):
    zeros = 0
    pairs = 0
    triples = 0
    positive_two_positions = []
    for ch in word:
        if ch == 0:
            zeros += 1
        elif ch == 1:
            pairs += zeros
        else:
            if pairs:
                positive_two_positions.append(pairs)
            triples += pairs
    return triples, tuple(positive_two_positions)

def predicted(n):
    if n == 0:
        return 0
    return ((5*n-29)*2**n)//4 + n*n+4*n+7

def main():
    for n in range(12):
        total = 0
        cases = {(2,):0,(1,1):0}
        for w in product(range(3),repeat=n):
            c,t = count_and_type(w)
            if c == 2:
                total += 1
                assert t in cases,(n,w,t)
                cases[t] += 1
        expect = predicted(n)
        assert total == expect,(n,total,expect)
        print(f"n={n} total={total} class_2={cases[(2,)]} class_1_1={cases[(1,1)]}")
    print('DIRECT_OK')
if __name__ == '__main__': main()
