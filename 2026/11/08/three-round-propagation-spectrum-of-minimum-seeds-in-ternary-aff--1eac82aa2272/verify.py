"""Standalone verification of three-round propagation in ternary affine STS.

Run: python3 verify.py
Requires Python standard library only. Compares the formula with direct
finite-space propagation, and independently reproduces the profile table.
"""
from itertools import combinations
from math import comb

T1 = {(1, 0), (0, 2)}
T2 = {(1, 0), (0, 2), (2, 1), (4, 0)}
T3 = T2 | {(1, 3), (0, 5), (3, 2), (2, 4), (1, 6), (0, 8)}

EXPECTED = {
 ((1,0),(1,0)): {(0,2)},
 ((1,0),(0,2)): {(1,0),(2,1)},
 ((1,0),(2,1)): {(0,2),(2,1),(1,3)},
 ((1,0),(4,0)): {(1,3),(0,5)},
 ((0,2),(0,2)): {(2,1),(4,0)},
 ((0,2),(2,1)): {(0,2),(1,0),(1,3),(2,1),(3,2)},
 ((0,2),(4,0)): {(0,2),(1,3),(2,4)},
 ((2,1),(2,1)): {(0,2),(0,5),(1,0),(1,3),(2,1),(2,4),(3,2),(4,0)},
 ((2,1),(4,0)): {(0,5),(1,3),(1,6),(2,1),(2,4),(3,2)},
 ((4,0),(4,0)): {(0,8),(1,6),(2,4),(3,2)},
}


def vectors_of_type(n, a, b):
    for I in combinations(range(n), a):
        left = tuple(j for j in range(n) if j not in I)
        for J in combinations(left, b):
            z = [0]*n
            for i in I: z[i] = 1
            for j in J: z[j] = 2
            yield tuple(z)


def type_of(x):
    return x.count(1), x.count(2)


def vector_pair_sum(x,y):
    return tuple((-a-b)%3 for a,b in zip(x,y))


def verify_profile_table():
    n=8
    names = [(1,0),(0,2),(2,1),(4,0)]
    seen = set()
    for i, a in enumerate(names):
        x = (1,)*a[0] + (2,)*a[1] + (0,)*(n-sum(a))
        for b in names[i:]:
            types = set()
            for y in vectors_of_type(n, *b):
                if y != x: types.add(type_of(vector_pair_sum(x,y)))
            assert types == EXPECTED[(a,b)], (a,b,types)
            seen |= types
    assert seen == T3, seen
    print('EIGHT_COORDINATE_PAIR_TABLE_OK',len(EXPECTED),'entries',len(T3),'output types')


def count_formula(n, r):
    if r == 0: return n
    if r == 1: return n+comb(n,2)
    if r == 2: return n+comb(n,2)+3*comb(n,3)+comb(n,4)
    if r == 3:
        return n+comb(n,2)+3*comb(n,3)+5*comb(n,4)+11*comb(n,5)+15*comb(n,6)+7*comb(n,7)+comb(n,8)
    raise ValueError


def direct_rounds(d):
    zero=(0,)*d
    S={zero}|{tuple(int(i==j) for i in range(d)) for j in range(d)}
    n=d+1
    for t in range(4):
        assert len(S) == count_formula(n,t), (d,t,len(S),count_formula(n,t))
        if t == 3: break
        X=list(S)
        new=set(S)
        for i,p in enumerate(X):
            for q in X[:i]:
                new.add(vector_pair_sum(p,q))
        S=new
    assert (len(S)==3**d)==(d<=4)
    return len(S)


def verify_combinatorial_profile_counts():
    for n in range(2,25):
        for r, types in [(1,T1),(2,T2),(3,T3)]:
            count = sum(comb(n,a)*comb(n-a,b) for a,b in types if a+b<=n)
            assert count == count_formula(n,r), (n,r,count)
    print('ALL_DIMENSION_MULTINOMIAL_COUNT_IDENTITIES_OK', '2..24')


if __name__ == '__main__':
    verify_profile_table()
    verify_combinatorial_profile_counts()
    for d in range(1,10):
        print('DIRECT_GEOMETRY_OK dimension',d,'round3_count',direct_rounds(d))
    print('VERIFY_OK')
