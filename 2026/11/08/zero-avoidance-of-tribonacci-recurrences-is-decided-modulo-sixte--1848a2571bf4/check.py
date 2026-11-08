#!/usr/bin/env python3
"""Exact finite certificate for the Tribonacci zero-avoidance theorem.
Run with Python 3; uses integer arithmetic only. The infinite lifting is proved in RESULT.md.
"""
from collections import Counter
from itertools import product


def step(v, mod):
    return (v[1], v[2], (v[0]+v[1]+v[2]) % mod)


def finite_mod16_certificate():
    m=16; seen=set(); summary=Counter(); vector_summary=Counter()
    for v in product(range(m), repeat=3):
        if v in seen:
            continue
        orb=[]; w=v
        while w not in seen:
            seen.add(w); orb.append(w); w=step(w,m)
        assert w == v, (w,v) # invertible recurrence, every state in a cycle
        primitive=any(x%2 for x in v)
        if not primitive:
            continue
        assert len(orb) in (16,32)
        zeros=[w for w in orb if w[0]==0]
        if zeros:
            # the nonstandard finite lemma: existence of a Hensel-liftable zero
            assert any(w[1]%4 != 0 for w in zeros), (v,zeros)
        kind='hit' if zeros else 'avoid'
        summary[(len(orb),kind)]+=1
        vector_summary[kind]+=len(orb)
    assert len(seen)==4096
    assert summary==Counter({(16,'avoid'):32,(32,'avoid'):24,(32,'hit'):72})
    assert vector_summary==Counter({'hit':2304,'avoid':1280})
    print('mod16 primitive orbit types (length, hits-zero): 16 avoid=32, 32 avoid=24, 32 hit=72')
    print('mod16 primitive vectors: avoid=1280, hit=2304, total=3584')
    print('all 72 zero-hitting primitive orbits have a zero state with next coordinate nonzero modulo 4')


def direct_counts(r):
    m=1<<r; seen=bytearray(m**3)
    total=0;primitive=0
    spectrum=Counter()
    for a in range(m):
      for b in range(m):
       for c in range(m):
        initial=(a,b,c); ix=(a*m+b)*m+c
        if seen[ix]:continue
        w=initial; cyc=0; avoid=True
        while not seen[(w[0]*m+w[1])*m+w[2]]:
            seen[(w[0]*m+w[1])*m+w[2]]=1
            if w[0]==0:avoid=False
            cyc+=1;w=step(w,m)
        assert w == initial
        if avoid:
            total+=cyc
            spectrum[cyc]+=1
            if a%2 or b%2 or c%2:
                primitive+=cyc
    return total,primitive,spectrum


def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]


def matrix_certificate():
    A=[[0,1,0],[0,0,1],[1,1,1]]
    T=A
    for _ in range(4):
        T=matmul(T,T)
    assert T == [[1705,2632,3136],[3136,4841,5768],[5768,8904,10609]]
    B=[[(T[i][j]-(i==j))//8 for j in range(3)] for i in range(3)]
    assert all((T[i][j]-(i==j))%8==0 for i in range(3) for j in range(3))
    b4=[[x%4 for x in row] for row in B]
    assert b4==[[1,1,0],[0,1,1],[1,1,2]]
    print('T^16 matrix, integrality of (T^16-I)/8, and its reduction modulo 4 checked')


def main():
    finite_mod16_certificate()
    matrix_certificate()
    for r in range(1,7):
        N,P,spec=direct_counts(r)
        expectedP={1:1,2:8,3:128}.get(r,1280*8**(r-4))
        expectedN={1:1,2:9}.get(r,(5*8**r-642)//14)
        assert P==expectedP and N==expectedN
        print(f'r={r}: zero-free={N}; primitive-zero-free={P}; cycle lengths={dict(sorted(spec.items()))}')
    print('all finite checks passed')

if __name__=='__main__':main()
