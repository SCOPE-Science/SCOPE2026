#!/usr/bin/env python3
"""Reproduce finite checks for the monochromatic complement-factor census.

Uses elementary brute-force deletion masks as one representation and polynomial
bounded-composition convolution as a separate representation. Python >= 3.9.
"""
from itertools import product, combinations
from collections import defaultdict
from math import comb


def gap_vector(word, distinguished=0):
    gaps = [0]
    for x in word:
        if x == distinguished:
            gaps[-1] += 1
        else:
            gaps.append(0)
    return tuple(gaps)


def spectrum_formula(gaps):
    coefficients = [1]
    for length in gaps:
        new = [0] * (len(coefficients) + length)
        for i, p in enumerate(coefficients):
            for j in range(length + 1):
                new[i+j] += p
        coefficients = new
    return tuple(coefficients)


def spectrum_mask(word, distinguished=0):
    a_positions = tuple(i for i, x in enumerate(word) if x == distinguished)
    result = []
    for k in range(len(a_positions)+1):
        survivors = set()
        for deleted in combinations(a_positions, k):
            deleted = set(deleted)
            survivors.add(tuple(x for i, x in enumerate(word) if i not in deleted))
        result.append(len(survivors))
    return tuple(result)


def predicted_max(m, b):
    r = b+1
    s, h = divmod(m, r)
    return spectrum_formula((s,) * (r-h) + (s+1,)*h)


def check_family(alphabet_size, max_length):
    seen_words = seen_profiles = seen_masks = 0
    groups = defaultdict(list)
    for n in range(max_length+1):
        groups.clear()
        for word in product(range(alphabet_size), repeat=n):
            m = word.count(0)
            b = n-m
            gap = gap_vector(word)
            predicted = spectrum_formula(gap)
            observed = spectrum_mask(word)
            assert observed == predicted, ('mask/poly discrepancy', word, observed, predicted)
            groups[(m,b)].append((word,observed,gap))
            seen_words += 1
            seen_profiles += len(predicted)
            seen_masks += 2**m
        for (m,b), entries in groups.items():
            r = b+1
            s,h = divmod(m,r)
            top = predicted_max(m,b)
            assert all(all(x <= y for x,y in zip(profile,top)) for _,profile,_ in entries)
            winners = [v for v in entries if v[1] == top]
            predicted_winner_count = comb(r,h)*(alphabet_size-1)**b
            assert len(winners) == predicted_winner_count, (alphabet_size,n,m,b,len(winners),predicted_winner_count)
            assert all(all(gap_i in (s,s+1) for gap_i in g) for _,_,g in winners)
            denom = comb(m+b,b)
            assert len(entries) == denom * (alphabet_size-1)**b
            for k in range(m+1):
                observed_sum = sum(profile[k] for _,profile,_ in entries)
                formula_sum = comb(r+k-1,k)*comb(r+m-k-1,m-k)*(alphabet_size-1)**b
                assert observed_sum == formula_sum, (alphabet_size,n,m,k,observed_sum,formula_sum)
    return seen_words,seen_profiles,seen_masks


def check_smoothing(max_gap=16):
    checks = 0
    for a in range(max_gap+1):
        for b in range(max_gap+1):
            if a>=b+2:
                before=spectrum_formula((a,b))
                after=spectrum_formula((a-1,b+1))
                difference=tuple(x-y for x,y in zip(after,before))
                assert difference == tuple(int(b+1<=k<=a-1) for k in range(a+b+1))
                checks+=1
    return checks

if __name__ == '__main__':
    print('Smoothing identities:',check_smoothing())
    for q, nmax in ((2,11),(3,8),(4,7)):
        nwords, nprof, masks = check_family(q,nmax)
        print(f'q={q}, lengths=0..{nmax}: {nwords} words, {nprof} spectrum entries, {masks} deletion embeddings checked; exact maxima, maximizer counts, conditional means passed')
    print('All tests passed.')
