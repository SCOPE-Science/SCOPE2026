"""Direct deletion-set verification of a fixed-composition reconstruction graph.
Requires only Python 3 standard library. Run: python check_direct.py
"""
from itertools import combinations


def deck(word):
    return {word[:i] + word[i + 1:] for i in range(len(word))}


def syndrome(word, r):
    return sum(i for i, b in enumerate(word, 1) if b == '1') % (r + 1)


def clique(n, k):
    r = min(k, n - k)
    base = ['10' * j + '01' * (r - j) for j in range(r + 1)]
    if k <= n - k:
        return [x + '0' * (n - 2 * r) for x in base]
    return [''.join('1' if c == '0' else '0' for c in x)
            + '1' * (n - 2 * r) for x in base]


def check():
    pairs = 0
    for n in range(2, 11):
        for k in range(n + 1):
            r = min(k, n-k)
            words = [''.join('1' if i in inds else '0' for i in range(n))
                     for inds in combinations(range(n), k)]
            decks = {w: deck(w) for w in words}
            seen_edges = 0
            for a, b in combinations(words, 2):
                common = len(decks[a] & decks[b])
                assert common <= 2, (n,k,a,b,common)
                if common == 2:
                    seen_edges += 1
                    assert syndrome(a,r) != syndrome(b,r), (n,k,a,b)
                pairs += 1
            family = clique(n,k)
            assert len(family) == r+1 and len(set(family)) == r+1
            assert all(len(x) == n and x.count('1') == k for x in family)
            assert len({syndrome(x,r) for x in family}) == r+1
            for a,b in combinations(family,2):
                assert len(decks[a] & decks[b]) == 2, (n,k,a,b)
            print('n=%d k=%d |V|=%d |E|=%d clique=%d' %
                  (n,k,len(words),seen_edges,len(family)))
    # A five-cycle with ten independently evaluated deletion-ball intersections.
    cycle = ('01011001','10011001','10010101','10101010','01011010')
    assert all(len(x)==8 and x.count('1') == 4 for x in cycle)
    for i,j in combinations(range(5),2):
        common = len(deck(cycle[i]) & deck(cycle[j]))
        assert common == (2 if (j-i in (1,4)) else 0), (i,j,common)
    print('PASS: direct deletion-set census through n=10; %d pairs tested; induced C5 confirmed.' % pairs)

if __name__ == '__main__':
    check()
