#!/usr/bin/env python3
"""Independent direct-subsequence and recursive-grammar checks for a binary-word census."""
from itertools import product
from collections import defaultdict


def is_subsequence(needle, haystack):
    pos = 0
    for symbol in needle:
        pos = haystack.find(symbol, pos)
        if pos < 0:
            return False
        pos += 1
    return True


def direct_shortest_absence(word):
    for length in range(1, len(word) + 2):
        missing = ["".join(v) for v in product("01", repeat=length)
                   if not is_subsequence("".join(v), word)]
        if missing:
            return length, missing
    raise AssertionError("No absent subsequence")


def greedy_grammar(word):
    if len(set(word)) == 1:
        return True, 0
    x = word[0]
    run = 0
    while run < len(word) and word[run] == x:
        run += 1
    tail = word[run + 1:]
    if not tail or (run == 1 and tail[0] != x):
        return False, 0
    yes, k = greedy_grammar(tail)
    return yes, k + 1


def count_expected(max_length):
    count = defaultdict(int)
    count[(1, 0)] = 2
    for n in range(2, max_length + 1):
        for k in range((n-1)//2+1):
            count[(n, k)] = (count[(n-1, k)]
                             + count[(n-2, k-1)]
                             + count[(n-3, k-1)])
    return count


def run():
    expected = count_expected(16)
    for n in range(1, 13):
        tally = defaultdict(int)
        for bits in product("01", repeat=n):
            w = "".join(bits)
            length, missing = direct_shortest_absence(w)
            allowed, k = greedy_grammar(w)
            assert allowed == (len(missing) == 1), (n, w, missing, allowed)
            if allowed:
                assert length == k+1, (n, w, length, k)
                tally[k] += 1
        for k in range((n-1)//2+1):
            assert tally[k] == expected[(n,k)], (n,k,tally[k],expected[(n,k)])
        print(f"n={n:2d} unique={sum(tally.values()):5d} by_k={dict(sorted(tally.items()))}")
    print("DIRECT_GRAMMAR_VERIFY_OK")

if __name__ == '__main__':
    run()
