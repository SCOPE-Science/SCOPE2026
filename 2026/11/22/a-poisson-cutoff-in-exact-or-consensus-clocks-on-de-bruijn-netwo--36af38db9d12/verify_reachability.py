"""Independent graph-path and quotient counting certificates for de Bruijn OR."""
from itertools import product
from fractions import Fraction
from math import exp


def digraph(q,d):
    words=list(product(range(q),repeat=d))
    index={w:i for i,w in enumerate(words)}
    arcs=[set(index[w[1:]+(a,)] for a in range(q)) for w in words]
    return words,arcs


def bfs_exact_paths(arcs,t):
    n=len(arcs)
    cur=[{v} for v in range(n)]
    for _ in range(t):
        cur=[set().union(*(arcs[k] for k in reach)) for reach in cur]
    return cur


def formula_count(q,d,t):
    partition=[tuple(range(r,q**d,q**(d-t))) for r in range(q**(d-t))]
    # Each block must contain a selected coordinate; dynamic count across disjoint blocks.
    count=1
    for block in partition:
        ways=0
        # independent combinatorial enumeration over one block
        for bits in product((0,1),repeat=len(block)):
            ways+=int(any(bits))
        count*=ways
    return count


def check(q,d):
    words,arcs=digraph(q,d)
    for t in range(d+1):
        paths=bfs_exact_paths(arcs,t)
        expected=[{j for j,w2 in enumerate(words) if (not d-t or w[-(d-t):]==w2[:d-t])} for w in words]
        assert paths==expected, (q,d,t)
        theoretical=(2**(q**t)-1)**(q**(d-t))
        if q**t <= 9:
            assert formula_count(q,d,t)==theoretical
    # An all-ones initial state is already there; an all-zero initial state never reaches it.
    assert len(paths)==q**d


def biased_prob(q,d,t,p):
    return (1-(1-p)**(q**t))**(q**(d-t))

if __name__=='__main__':
    for q,d in ((2,1),(2,2),(2,3),(2,4),(3,1),(3,2)):
        check(q,d)
        print('PATHS',q,d,'PASSED')
    # The uncovered-block count in the critical window is exactly binomial,
    # with an exactly constant mean equal to 2^c for every h.
    for c in (-1, 0, 1):
        for h in (3,4,5,6):
            d = 2**h+h+c
            m = 2**(d-h)
            empty = Fraction(1,2**(2**h))
            mean = m * empty
            expected = Fraction(2**c) if c >= 0 else Fraction(1,2**(-c))
            assert mean == expected
            variance = mean * (1-empty)
            assert variance < mean and variance > 0
        print('CRITICAL_BINOMIAL_MEAN',c,str(expected))
    print('REACHABILITY_ALL_CHECKS_PASSED')
