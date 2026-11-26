"""Independent support-transition proof checker; run: python3 verify_support.py."""
from itertools import product
from collections import Counter

SETS = tuple(frozenset(i for i in range(3) if mask & (1<<i)) for mask in range(1,8))
Q0 = (frozenset({0}),frozenset({0}))
Q3 = (frozenset({0,1,2}),frozenset({0,1,2}))
Q4A = (frozenset({0,1}),frozenset({0,2}))
Q4B = (frozenset({0,2}),frozenset({0,1}))
REC = (Q0, Q3, Q4A, Q4B)


def update_one(x, has_neighbour_one):
    if x == 1:return 2
    if x == 2:return 0
    return 1 if has_neighbour_one else 0


def next_support(pair):
    a,b=pair
    return (frozenset(update_one(x,1 in b) for x in a),
            frozenset(update_one(x,1 in a) for x in b))


def classify(pair):
    t=0
    while pair not in REC:
        pair=next_support(pair)
        t+=1
        assert t <= 4
    return (t,1 if pair == Q0 else (3 if pair == Q3 else 4))


def weight(n,k):
    return (0,1,2**n-2,3**n-3*2**n+3)[k]


def main():
    # Check that the support recurrent components are precisely those declared.
    assert next_support(Q0)==Q0
    assert next_support(Q3)==Q3
    assert next_support(Q4A)==Q4B
    assert next_support(Q4B)==Q4A
    c=Counter((classify((a,b)),len(a),len(b)) for a,b in product(SETS,repeat=2))
    assert sum(c.values()) == 49
    # Non-numerical identities for all m,n: 49 support types partition
    # the three-state assignments by exact nonempty support cardinality.
    for m in range(1,31):
        for n in range(1,31):
            cnt=Counter()
            for (t,p),a,b in c:
                cnt[t,p] += c[((t,p),a,b)]*weight(m,a)*weight(n,b)
            assert sum(cnt.values()) == 3**(m+n)
            u=2**m-2;U=2**n-2
            v=3**m-3*2**m+3;V=3**n-3*2**n+3
            assert sum(vv for (tt,p),vv in cnt.items() if p==3)==v*V
            assert sum(vv for (tt,p),vv in cnt.items() if p==4)==6*u*U+3*u*V+3*v*U
            assert cnt[0,4] == 2*u*U
            assert cnt[4,1] == 2*u+2*U+v+V
    print('SUPPORT_OK', 'support_pairs',49,'parameter_pairs',900)
    for t in range(5):
        for p in (1,3,4):
            terms=sorted((a,b,v) for ((tt,pp),a,b),v in c.items() if (tt,pp)==(t,p))
            if terms:print((t,p),terms)

if __name__=='__main__':main()
