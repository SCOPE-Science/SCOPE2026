#!/usr/bin/env python3
"""Standalone exact checks for Kneser-graph coordinate control.

Uses only the Python standard library. Rational rank computations check the
unspecified real-field restrictions without floating-point decisions.
"""
from fractions import Fraction
from itertools import combinations
from math import comb, factorial
from random import Random


def rank_over_q(rows, cols):
    a = [[Fraction(v) for v in row] for row in rows]
    r=0
    for j in range(cols):
        pivot=next((i for i in range(r,len(a)) if a[i][j]),None)
        if pivot is None:
            continue
        a[r],a[pivot]=a[pivot],a[r]
        for i in range(r+1,len(a)):
            t=a[i][j]/a[r][j]
            if t:
                for c in range(j,cols):
                    a[i][c]-=t*a[r][c]
        r+=1
        if r==cols:
            break
    return r


def odd_unicyclic_components(n, edges):
    adj=[[] for _ in range(n)]
    for u,v in edges:
        adj[u].append(v)
        adj[v].append(u)
    seen=set()
    for origin in range(n):
        if origin in seen:
            continue
        seen.add(origin)
        stack=[origin]
        comp=[]
        while stack:
            v=stack.pop()
            comp.append(v)
            for w in adj[v]:
                if w not in seen:
                    seen.add(w)
                    stack.append(w)
        if sum(len(adj[v]) for v in comp)!=2*len(comp):
            return False
        colors={origin:0}
        stack=[origin]
        odd_cycle=False
        while stack:
            v=stack.pop()
            for w in adj[v]:
                if w not in colors:
                    colors[w]=1-colors[v]
                    stack.append(w)
                elif colors[w]==colors[v]:
                    odd_cycle=True
        if not odd_cycle:
            return False
    return True


def exceptional_6(n,edges):
    if n!=6:
        return False
    edge_set=set(edges)
    for part in combinations(range(6),3):
        a=set(part)
        b=set(range(6))-a
        exceptional_edges=set(combinations(sorted(a),2))|set(combinations(sorted(b),2))
        if edge_set==exceptional_edges:
            return True
    return False


def direct_pbh(n,controlled,uncontrolled):
    # The eigenspace ker(B) is observable precisely if B_U is injective.
    BU=[[int(v in edge) for edge in uncontrolled] for v in range(n)]
    first=rank_over_q(BU,len(uncontrolled))==len(uncontrolled)
    # Coordinate trace of B^T{x : sum x=0}; eliminate x[n-1].
    high=[]
    for edge in controlled:
        row=[0]*(n-1)
        for v in edge:
            if v==n-1:
                for i in range(n-1): row[i]-=1
            else:
                row[v]+=1
        high.append(row)
    second=rank_over_q(high,n-1)==n-1
    return first,second


def egf_counts(max_n):
    N=max_n
    t=[Fraction(0)]*(N+1)
    for k in range(1,N+1):
        t[k]=Fraction(k**(k-1),factorial(k))
    def product(a,b):
        c=[Fraction(0)]*(N+1)
        for i in range(N+1):
            for j in range(N-i+1):
                c[i+j]+=a[i]*b[j]
        return c
    cycle=[Fraction(0)]*(N+1)
    power=[Fraction(1)]+[Fraction(0)]*N
    for length in range(1,N+1):
        power=product(power,t)
        if length>=3 and length%2:
            for k in range(N+1):
                cycle[k]+=power[k]/(2*length)
    forest=[Fraction(0)]*(N+1)
    forest[0]=1
    for k in range(1,N+1):
        forest[k]=sum(j*cycle[j]*forest[k-j] for j in range(1,k+1))/k
    return [int(factorial(k)*forest[k]) for k in range(N+1)]


def check_spectra(n):
    edges=list(combinations(range(n),2))
    N=len(edges)
    k=comb(n-2,2)
    for i,e in enumerate(edges):
        for j,f in enumerate(edges):
            # adjacency of KG(n,2) from complete-graph unsigned incidence
            kneser=int(i!=j and set(e).isdisjoint(f))
            dot=len(set(e)&set(f))
            assert kneser==1+int(i==j)-dot
    assert (k-1)==(n-1)*(n-4)//2
    assert (k+n-3)==n*(n-3)//2


def verify(n, exhaustive=True, sample_size=1000):
    edges=list(combinations(range(n),2))
    N=len(edges)
    total=comb(N,n)
    if exhaustive:
        chosen=combinations(range(N),n)
    else:
        rng=Random(202601)
        chosen=(tuple(sorted(rng.sample(range(N),n))) for _ in range(sample_size))
    tested=first_ok=full_ok=exception_count=0
    for subset in chosen:
        ids=set(subset)
        U=[edges[j] for j in subset]
        S=[edges[j] for j in range(N) if j not in ids]
        predicted=odd_unicyclic_components(n,U) and not exceptional_6(n,U)
        first,second=direct_pbh(n,S,U)
        assert first==odd_unicyclic_components(n,U)
        assert (first and second)==predicted
        tested+=1
        first_ok+=first
        full_ok+=(first and second)
        exception_count+=(first and not second)
    print(f'n={n}: total_candidates={total} tested={tested} incidence_bases={first_ok} controllable={full_ok} exceptional={exception_count}')
    return full_ok


def main():
    for n in range(5,9):
        check_spectra(n)
    expected=egf_counts(9)
    print('Odd-unicyclic EGF counts n=5..9:',expected[5:10])
    assert verify(5)==expected[5]==162
    assert verify(6)==expected[6]-10==2520
    assert verify(7,exhaustive=False,sample_size=1000)>=0
    edges=list(combinations(range(7),2))
    counted=sum(odd_unicyclic_components(7,[edges[i] for i in ids])
                for ids in combinations(range(len(edges)),7))
    assert counted==expected[7]==45615
    print('n=7: exhaustive 116280 structural subsets; bases=45615')
    print('VERIFY_OK')

if __name__=='__main__':
    main()
