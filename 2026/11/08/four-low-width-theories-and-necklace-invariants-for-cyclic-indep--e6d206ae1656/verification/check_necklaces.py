#!/usr/bin/env python3
"""Independent arithmetic/structural checks of cyclic clone digraphs.
Runs no external services and does not assume finite tests prove an infinite theorem.
"""
from itertools import product
from math import gcd, factorial
from collections import Counter

def mkgraph(word):
    layers=[i for i,m in enumerate(word) for _ in range(m)]
    v=len(layers); L=len(word)
    edge=[[int((layers[b]-layers[a])%L==1) for b in range(v)] for a in range(v)]
    return layers,edge

def rot_min(w):
    return min(w[i:]+w[:i] for i in range(len(w)))

def phi(n):
    return sum(gcd(i,n)==1 for i in range(1,n+1))

def necklace_count(L,k):
    return sum(phi(d)*k**(L//d) for d in range(1,L+1) if L%d==0)//L

def minimal_size_poly(L,k):
    # Burnside by enumerating rotation-fixed colored cycles, averaging over C_L.
    c=Counter()
    for shift in range(L):
        for w in product(range(1,k+1),repeat=L):
            if all(w[i]==w[(i+shift)%L] for i in range(L)):
                c[sum(w)]+=1
    assert all(x%L==0 for x in c.values())
    return {i:v//L for i,v in c.items()}

def tests():
    cnt=0
    for L in range(3,8):
        for k in range(1,5):
            representatives={rot_min(w) for w in product(range(1,k+1),repeat=L)}
            assert len(representatives)==necklace_count(L,k)
            if k<=3 and L<=5:
                counts=Counter(sum(w) for w in representatives)
                assert counts==minimal_size_poly(L,k)
            cnt+=1
    graph_cnt=0
    triple_cnt=0
    walk_cnt=0
    for L in range(3,7):
        for word in product(range(1,4),repeat=L):
            if sum(word)>12:continue
            layers,E=mkgraph(word)
            n=len(layers)
            # Three-variable out-neighbor equality defines exactly the clone class.
            for i in range(n):
                for j in range(n):
                    same=(all(E[i][z]==E[j][z] for z in range(n)))
                    assert same==(layers[i]==layers[j])
                    triple_cnt+=1
            # True directed closed walks must have lengths divisible by cycle length.
            # Test possible lengths up to 2L by Boolean matrix powers.
            M=[[int(i==j) for j in range(n)] for i in range(n)]
            for t in range(1,2*L+1):
                M=[[int(any(M[a][b] and E[b][c] for b in range(n))) for c in range(n)] for a in range(n)]
                observed=any(M[i][i] for i in range(n))
                assert observed==(t%L==0)
                walk_cnt+=1
            graph_cnt+=1
    print('Burnside necklace formulas and minimum-order coefficient checks: {} parameter pairs PASS'.format(cnt))
    print('Directed blow-up graph instances: {}'.format(graph_cnt))
    print('Three-variable clone-predicate pair checks: {}'.format(triple_cnt))
    print('Directed closed-walk length checks: {}'.format(walk_cnt))
    print('all structural and enumeration checks PASS')
if __name__=='__main__':tests()
