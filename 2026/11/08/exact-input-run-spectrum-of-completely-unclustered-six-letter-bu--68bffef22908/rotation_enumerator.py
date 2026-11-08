"""Independent census from primitive Lyndon necklaces and sorted rotations."""
from collections import Counter
from itertools import product

N = 6

def rotations(word):
    return [word[i:] + word[:i] for i in range(N)]


def is_primitive_lyndon(word):
    rr = rotations(word)
    return len(set(rr)) == N and word == min(rr)


def bwt_by_rotations(word):
    return tuple(rot[-1] for rot in sorted(rotations(word)))


def census():
    records = {}
    for t in range(1, N + 1):
        for word in product(range(t), repeat=N):
            if len(set(word)) != t or not is_primitive_lyndon(word):
                continue
            output = bwt_by_rotations(word)
            if any(output[i] == output[i + 1] for i in range(N - 1)):
                continue
            runs = sum(word[i] != word[(i + 1) % N] for i in range(N))
            key = (t, output)
            assert key not in records, 'Distinct necklaces must have distinct BWT images'
            records[key] = (word, runs)
    return records


def histogram():
    h = Counter()
    for (t, output), (word, runs) in census().items():
        h[t, runs] += 1
    return h


if __name__ == '__main__':
    print(sorted(histogram().items()))
