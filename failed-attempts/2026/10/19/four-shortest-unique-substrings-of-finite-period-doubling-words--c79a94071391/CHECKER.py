#!/usr/bin/env python3
"""Direct finite factor-frequency checks for the period-doubling SUS theorem.
Scientific verification only; general validity rests on the written induction.
"""
from collections import defaultdict

def mu(word):
    return ''.join('01' if c == '0' else '00' for c in word)

def unique_starts(word, length):
    groups = defaultdict(list)
    for start in range(len(word) - length + 1):
        groups[word[start:start+length]].append(start)
    return sorted(indices[0] for indices in groups.values() if len(indices) == 1)

def occurrences(word, factor):
    return [i for i in range(len(word)-len(factor)+1)
            if word[i:i+len(factor)] == factor]

def main():
    word = '0'
    for n in range(1, 14):
        word = mu(word)
        if n < 3:
            continue
        target = (1 << (n-2)) + 1
        unit = 1 << (n-3)
        expected = [a*unit-1 for a in (2, 3, 4, 6)]
        assert unique_starts(word, target-1) == [], (n,'shorter')
        actual = unique_starts(word, target)
        assert actual == expected, (n,'length',actual,expected)
        q = 1 << (n-2)
        suffix = word[-q:]
        assert occurrences(word,suffix) == [0,2*q,3*q], (n,'suffix')
        print(f'n={n} length={len(word)} shortest={target} unique_count={len(actual)} starts={actual} suffix_count=3')
    print('All direct factor-frequency checks passed for n=3..13.')

if __name__ == '__main__':
    main()
