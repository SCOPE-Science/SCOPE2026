#!/usr/bin/env python3
"""Independent finite exhaustive checks of four-factor certificate and pair counts.
Scientific verification: direct factor occurrences versus four-factor hit test.
Python 3 standard library only; zero-based internal bit positions.
"""
from itertools import combinations


def make_word(a, b, t):
    return '0' * a + '1' * b if t == 1 else ('0' * a + '1' * b) * t


def witness_mask(word, factor):
    length = len(factor)
    mask = 0
    for i in range(len(word) - length + 1):
        if word[i:i + length] == factor:
            mask |= ((1 << length) - 1) << i
    return mask


def all_factor_masks(word):
    factors = {word[i:j] for i in range(len(word)) for j in range(i+1, len(word)+1)}
    return [witness_mask(word, x) for x in factors]


def certificate_masks(word, a, b):
    return [witness_mask(word, x) for x in ('0'*a, '1'*b, '01', '10')]


def exact_pair_count(a,b,t):
    if a == 1:
        return (t - 1)*(b*t+1)
    if b == 1:
        return (t - 1)*(a*t+1)
    return 2*t*(t-1)


def run():
    subset_checks = 0
    parameter_checks = 0
    pair_checks = 0
    for a in range(1, 6):
        for b in range(1, 6):
            for t in range(2, 8):
                w = make_word(a,b,t)
                cm = certificate_masks(w,a,b)
                n = len(w)
                pairs = sum(all(((1 << i)|(1 << j))&m for m in cm)
                            for i,j in combinations(range(n),2))
                assert pairs == exact_pair_count(a,b,t), (a,b,t,pairs)
                pair_checks += 1
                if n <= 15:
                    fm = all_factor_masks(w)
                    for mask in range(1<<n):
                        predicted = all(mask&m for m in cm)
                        actual = all(mask&m for m in fm)
                        assert predicted == actual, (a,b,t,mask,predicted,actual)
                        subset_checks += 1
                    parameter_checks += 1
    print('PASS: full-factor equivalence checked for',subset_checks,'position subsets across',parameter_checks,'parameter triples.')
    print('PASS: pair counts checked for',pair_checks,'parameter triples, a,b in [1,5], t in [2,7].')

if __name__ == '__main__':
    run()
