"""Exhaustive checker for 4-mer reverse-complement overlap greedy."""
from functools import lru_cache
from itertools import product, combinations
from collections import Counter

def reverse_complement(word):
    return ''.join('1' if c == '0' else '0' for c in word[::-1])

def representative(word):
    return min(word, reverse_complement(word))

def normalize(words):
    candidates = sorted(set(map(representative, words)))
    return tuple(s for s in candidates if not any(
        s != t and (s in t or reverse_complement(s) in t) for t in candidates))

def overlap(a, b):
    return next((k for k in range(min(len(a), len(b)) - 1, 0, -1)
                 if a.endswith(b[:k])), 0)

REPS = tuple(sorted({representative(''.join(t)) for t in product('01', repeat=4)}))
assert len(REPS) == 10

@lru_cache(None)
def maximum_greedy_length(state):
    if len(state) == 1:
        return len(state[0])
    best_overlap = -1
    choices = set()
    for i, j in combinations(range(len(state)), 2):
        for left, right in ((state[i], state[j]), (state[j], state[i])):
            for a in (left, reverse_complement(left)):
                for b in (right, reverse_complement(right)):
                    k = overlap(a, b)
                    if k > best_overlap:
                        best_overlap, choices = k, set()
                    if k == best_overlap:
                        remaining = (state[t] for t in range(len(state)) if t not in (i, j))
                        choices.add(normalize((*remaining, a + b[k:])))
    return max(maximum_greedy_length(choice) for choice in choices)

def full_mask(s):
    mask = 0
    for i in range(len(s) - 3):
        mask |= 1 << REPS.index(representative(s[i:i+4]))
    return mask

def run():
    # An explicit 13-symbol word covers all ten classes, so longer
    # candidates cannot improve the minimum for any nonempty subset.
    witness = '0010100001100'
    assert len(witness) == 13 and full_mask(witness) == 1023
    exact_opt = [100] * 1024
    for n in range(4, 14):
        for letters in product('01', repeat=n):
            covered = full_mask(''.join(letters))
            required = covered
            while True:
                exact_opt[required] = min(exact_opt[required], n)
                if required == 0:
                    break
                required = (required - 1) & covered

    extremes, joint = [], Counter()
    for mask in range(1, 1024):
        state = normalize(REPS[i] for i in range(10) if mask & (1 << i))
        worst = maximum_greedy_length(state)
        optimum = exact_opt[mask]
        assert optimum <= 13
        joint[(optimum, worst)] += 1
        if 3 * worst > 4 * optimum:
            raise AssertionError((mask, optimum, worst))
        if 3 * worst == 4 * optimum:
            extremes.append(mask)
    assert extremes == [131, 159, 183, 215, 407, 663]
    assert sum(joint.values()) == 1023
    assert joint[(6,8)] == 1 and joint[(9,12)] == 5
    print('representatives:', ' '.join(REPS))
    print('instances:', sum(joint.values()))
    print('sharp ratio: 4/3')
    print('equality masks:', *extremes)
    print('full-set optimum/worst:', exact_opt[1023], maximum_greedy_length(REPS))
    print('distinct greedy search states:', maximum_greedy_length.cache_info().currsize)
    print('joint histogram:', sorted(joint.items()))

if __name__ == '__main__':
    run()
