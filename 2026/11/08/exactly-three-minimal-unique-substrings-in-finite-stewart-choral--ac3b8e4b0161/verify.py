#!/usr/bin/env python3
"""Standalone exact checks for finite Stewart-choral minimal-unique factors.

The finite replay tests the symbolic theorem; it is not a replacement for
its all-index induction and repeated-interval argument.
"""

def morph(word):
    return ''.join('001' if c == '0' else '011' for c in word)


def longest_other_prefixes(word):
    """For each suffix, longest common prefix with any different suffix."""
    n = len(word)
    sa = list(range(n))
    rank = [int(c) for c in word]
    tmp = [0] * n
    shift = 1
    while True:
        sa.sort(key=lambda i: (rank[i], rank[i+shift] if i+shift<n else -1))
        tmp[sa[0]] = 0
        for j in range(1, n):
            a, b = sa[j-1], sa[j]
            pa = (rank[a], rank[a+shift] if a+shift<n else -1)
            pb = (rank[b], rank[b+shift] if b+shift<n else -1)
            tmp[b] = tmp[a] + int(pa != pb)
        rank, tmp = tmp, rank
        if rank[sa[-1]] == n-1:
            break
        shift <<= 1
    lcp = [0] * n
    h = 0
    for i in range(n):
        j = rank[i]
        if j == 0:
            h = 0
            continue
        predecessor = sa[j-1]
        while i+h<n and predecessor+h<n and word[i+h] == word[predecessor+h]:
            h += 1
        lcp[j] = h
        if h:
            h -= 1
    best = [0] * n
    for j, i in enumerate(sa):
        best[i] = max(lcp[j], lcp[j+1] if j+1<n else 0)
    return best


def mus_suffix_array(word):
    ml = longest_other_prefixes(word)
    n = len(word)
    return [(i, ml[i]+1) for i in range(n-1)
            if ml[i] < n-i and ml[i+1] >= ml[i]]


def mus_brute(word):
    results = []
    for i in range(len(word)):
        for length in range(1, len(word)-i+1):
            u = word[i:i+length]
            count = sum(word[j:j+length] == u
                        for j in range(len(word)-length+1))
            if count != 1:
                continue
            if length == 1:
                results.append((i, length))
                break
            prefix = u[:-1]
            suffix = u[1:]
            pcount = sum(word[j:j+length-1] == prefix
                         for j in range(len(word)-length+2))
            scount = sum(word[j:j+length-1] == suffix
                         for j in range(len(word)-length+2))
            if pcount > 1 and scount > 1:
                results.append((i, length))
            break
    return results


def expected(m):
    a = (11*m+3)//6
    d = (5*m-1)//2
    return [(m-1, (m+3)//2), (a-1, 2*m//3+1),
            (d, m//3+1)]


def run():
    word = '0'
    previous = None
    for k in range(1, 10):
        word = morph(word)
        if k == 1:
            continue
        m = 3 ** (k-1)
        c = (m-1)//2
        C = (3*m-1)//2
        a = (11*m+3)//6
        b = (m+3)//6
        d = (5*m-1)//2
        n = len(word)
        assert n == 3*m
        assert word[:m] == word[m:2*m]
        assert sum(x != y for x,y in zip(word[:m], word[2*m:])) == 1
        assert word[c] != word[2*m+c]
        assert word[:C] == word[m:m+C]
        assert word[a:a+m-1] == word[b:b+m-1]
        assert word[d+1:n] == word[c+1:m]
        assert word[:c+1] == word[m:m+c+1]
        assert [i for i in range(n-c) if word[i:i+c+1] == word[:c+1]] == [0,m]
        observed = mus_suffix_array(word)
        assert observed == expected(m), (k, observed, expected(m))
        if k <= 4:
            assert mus_brute(word) == observed
        u1 = word[a-1:d+1]
        u2 = word[d:a+m]
        if previous is not None:
            assert u1 == morph(previous[0])[1:-1]
            assert u2 == morph(previous[1])[1:-1]
        previous = (u1, u2)
        print(f'k={k} length={n} MUSs={observed}')
    print('STEWART_CHORAL_MUS_VERIFY_OK')


if __name__ == '__main__':
    run()
