#!/usr/bin/env python3
"""Finite reproducibility checks for dyadic block-palindrome widths."""
from functools import lru_cache


def period_doubling(n):
    return ''.join(str((((i+1) & -(i+1)).bit_length()-1) & 1)
                   for i in range(n))


def morphism(x):
    return ''.join('01' if a == '0' else '00' for a in x)


def greedy(word):
    """Return (left block lengths, center) by direct shortest-border comparison."""
    lo, hi = 0, len(word)
    lengths = []
    while hi > lo:
        t = 1
        while 2*t <= hi-lo and word[lo:lo+t] != word[hi-t:hi]:
            t += 1
        if 2*t > hi-lo:
            return lengths, word[lo:hi]
        lengths.append(t)
        lo += t
        hi -= t
    return lengths, ''


def width(result):
    lengths, center = result
    return 2*len(lengths) + int(bool(center))


def optimum_by_dp(word):
    """Independent complete search over every nonoverlapping border."""
    n = len(word)
    @lru_cache(None)
    def best(lo, hi):
        if lo == hi:
            return 0
        ans = 1
        for t in range(1, (hi-lo)//2+1):
            if word[lo:lo+t] == word[hi-t:hi]:
                ans = max(ans, 2+best(lo+t, hi-t))
        return ans
    return best(0, n)


def predicted_even_lengths(n):
    """Valuation-driven border sequence, independent of substring matching."""
    h = n // 2
    ans = [1]
    for j in range(1, h//2):
        even = 2*j
        v = (even & -even).bit_length()-1
        ans.extend((1, 1) if v % 2 == 0 else (2,))
    return ans


def check():
    exact = []
    shortest_border_comparisons = 0
    for k in range(14):
        n = 1 << k
        s = period_doubling(n)
        assert (morphism(period_doubling(n//2)) == s) if k else True
        actual = greedy(s)
        m = k//2
        want = (2*(4**m)+1)//3
        assert width(actual) == want, (k, width(actual), want)
        assert actual[1] == ('0' if k == 0 else '01' if k == 1 else '10' if k % 2 == 0 else '0001')
        if k%2 == 0 and k>0:
            expected = predicted_even_lengths(n)
            assert actual[0] == expected, (k,actual[0],expected)
            assert sum(expected) == n//2-1
            assert len(expected) == (n-1)//3
            assert all(s[n-1-a]=='0' for a in [sum(expected[:i]) for i in range(len(expected)+1)])
        if k%2 == 1:
            parent = greedy(period_doubling(n//2))
            assert actual[0] == [2*z for z in parent[0]]
            assert actual[1] == morphism(parent[1])
        for t in actual[0]:
            shortest_border_comparisons += t
        exact.append((k,n,want))
    # Direct optimization, not invoking the greedy theorem, on the first eight levels.
    for k in range(9):
        s = period_doubling(1 << k)
        assert optimum_by_dp(s) == width(greedy(s))
    # Generic shortest-border theorem spot checks, all binary words to length ten.
    checked_binary = 0
    for n in range(1, 11):
        for x in range(1 << n):
            s = format(x, '0%db'%n)
            assert width(greedy(s)) == optimum_by_dp(s)
            checked_binary += 1
    print('VERIFY_OK dyadic_levels=%d max_prefix=%d full_optimum_levels=%d all_binary_words=%d border_steps=%d' %
          (len(exact), 1 << 13, 9, checked_binary, shortest_border_comparisons))
    for k,n,w in exact:
        print('k=%d length=%d maximal_block_palindrome_width=%d' % (k,n,w))


if __name__ == '__main__':
    check()
