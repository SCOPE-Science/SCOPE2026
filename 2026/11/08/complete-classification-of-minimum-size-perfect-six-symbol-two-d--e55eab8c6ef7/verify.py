#!/usr/bin/env python3
"""Independent exhaustive test for the six-symbol length-four two-deletion classification."""
from itertools import permutations

Q = 6

def descendant_mask(word):
    pairs = {(word[i], word[j]) for i in range(4) for j in range(i + 1, 4)}
    return sum(1 << (Q * a + b) for a, b in pairs)

def generate():
    options = []
    for a in range(Q):
        choices = []
        for b in range(Q):
            for c in range(Q):
                if len({a, b, c}) == 3:
                    w = (a, b, c, a)
                    m = descendant_mask(w)
                    assert m.bit_count() == 6
                    choices.append((w, m))
        assert len(choices) == 20
        options.append(choices)
    all_solutions = set()
    def extend(a, words, covered):
        if a == Q:
            assert covered.bit_count() == 36
            all_solutions.add(tuple(words))
            return
        for w, m in options[a]:
            if (covered & m) == 0:
                extend(a + 1, words + [w], covered | m)
    extend(0, [], 0)
    return all_solutions

def relabel(code, pi):
    renamed = [(pi[w[0]], pi[w[1]], pi[w[2]], pi[w[3]]) for w in code]
    return tuple(sorted(renamed))

def reversed_code(code):
    return tuple(sorted(w[::-1] for w in code))

def main():
    for word in __import__('itertools').product(range(Q), repeat=4):
        mask = descendant_mask(word)
        loops = sum(bool(mask & (1 << (Q*a+a))) for a in range(Q))
        if mask.bit_count() == 6 and loops:
            assert word[0] == word[3] and len(set(word[:3])) == 3
    codes = generate()
    assert len(codes) == 240, len(codes)
    reference = ((0,2,3,0),(1,3,2,1),(2,4,5,2),(3,5,4,3),(4,0,1,4),(5,1,0,5))
    assert reference in codes
    symmetries = list(permutations(range(Q)))
    orbit1 = {relabel(reference,p) for p in symmetries}
    assert len(orbit1) == 120 and orbit1 <= codes
    reverse = reversed_code(reference)
    assert reverse in codes and reverse not in orbit1
    orbit2 = {relabel(reverse,p) for p in symmetries}
    assert len(orbit2) == 120
    assert not (orbit1 & orbit2)
    assert orbit1 | orbit2 == codes
    assert all(sum(descendant_mask(w).bit_count() for w in c) == 36 for c in codes)
    print('PASS: 240 labeled perfect codes; 2 alphabet-relabeling orbits of 120 each; reversal exchanges orbits')

if __name__ == '__main__':
    main()
