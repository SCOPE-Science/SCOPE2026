#!/usr/bin/env python3
"""Independent finite checks for open packings in circular ladder graphs."""
from itertools import combinations
from math import comb

def prism_neighborhoods(n):
    assert n>=3
    out=[]
    for layer in (0,1):
        for i in range(n):
            out.append(frozenset({layer*n+(i-1)%n,layer*n+(i+1)%n,(1-layer)*n+i}))
    return out

def common_neighbor_graph(n):
    adj=prism_neighborhoods(n)
    return [sum(1<<v for v in range(2*n) if v!=u and adj[u]&adj[v]) for u in range(2*n)]

def predicted_graph(n):
    # for odd n: one C_(2n)^2; even n: two C_n^2
    C=[0]*(2*n)
    if n%2:
        order=[(k%n) + (k%2)*n for k in range(2*n)]
        for k in range(2*n):
            for d in (-2,-1,1,2):
                C[order[k]] |= 1<<order[(k+d)%(2*n)]
    else:
        for parity in (0,1):
            order=[i + n*((i+parity)%2) for i in range(n)]
            for k in range(n):
                for d in (-2,-1,1,2):
                    C[order[k]] |= 1<<order[(k+d)%n]
    return C

def polynomial_cycle_square(m):
    return [ (m*comb(m-2*k,k))//(m-2*k) for k in range(m//3+1)]

def expected_poly(n):
    if n%2: return polynomial_cycle_square(2*n)
    a=polynomial_cycle_square(n)
    p=[0]*(2*len(a)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(a):p[i+j]+=x*y
    return p

def exhaustive_packing_polynomial(n):
    N=prism_neighborhoods(n)
    neighbits=[sum(1<<u for u in Nv) for Nv in N]
    # independent ground truth: for each subset, accumulate distinct neighborhoods, rejecting duplicates
    counts=[0]*(2*n+1)
    for mask in range(1<<(2*n)):
        used=0; valid=True
        for i in range(2*n):
            if mask>>i & 1:
                if used & neighbits[i]: valid=False; break
                used |= neighbits[i]
        if valid: counts[mask.bit_count()]+=1
    while counts and not counts[-1]:counts.pop()
    return counts

def packed_count(m):
    a=m//3; r=m-3*a
    if r==0:return 3
    if r==1:return m
    return m*(a+1)//2

def main():
    total=0
    for n in range(3,11):
        actual=common_neighbor_graph(n)
        predicted=predicted_graph(n)
        assert actual==predicted, (n,'conflict structure')
        got=exhaustive_packing_polynomial(n)
        want=expected_poly(n)
        assert got==want,(n,got,want)
        rho=2*(n//3) if n%2==0 else (2*n)//3
        cnt=packed_count(n)**2 if n%2==0 else packed_count(2*n)
        assert len(got)-1==rho and got[-1]==cnt
        total+=1<<(2*n)
        print(f'n={n} vertex_subsets={1<<(2*n)} rho={rho} maxima={cnt} poly={got}')
    print(f'OK: {total} vertex subsets independently tested, conflict graph isomorphism n=3..10')
    for n in range(11,81):
        assert common_neighbor_graph(n)==predicted_graph(n), (n,'large-n conflict structure')
    print('OK: original-neighborhood conflict graph agrees with parity decomposition n=11..80')
    # Verify explicit cardinality divisibility and cyclic coloring constructions up to n=300
    for n in range(3,301):
        m=n if n%2==0 else 2*n
        chi=3 if n%3==0 else 4
        assert m in (3,4) or m>=6
        # four color word: block lengths 3 and 4; if divisible by3 use blocks of 3
        if chi==3: word=[0,1,2]*(m//3)
        else:
            # m>=4 not divisible by 3: represent as 3a+4b, b=1 for 1 mod3, b=2 for 2 mod3
            b=1 if m%3==1 else 2
            a=(m-4*b)//3
            assert a>=0
            word=[0,1,2]*a+[0,1,2,3]*b
        assert len(word)==m
        for k in range(m):
            for d in (1,2):assert word[k]!=word[(k+d)%m],(n,k,d)
        alpha=2*(n//3) if n%2==0 else (2*n)//3
        expected_perfect= n%3==0 or n in (4,8)
        assert (alpha*chi==2*n)==expected_perfect,(n,alpha,chi)
    print('OK: explicit cyclic colorings and perfect-class-size criterion n=3..300')

if __name__=='__main__': main()
