#!/usr/bin/env python3
"""Exact finite-size witnesses for the triangular-graph actuator criterion."""
from itertools import combinations
from collections import Counter
from fractions import Fraction
from math import comb, factorial

PRIME=1000003

def rank_mod(rows,p=PRIME):
    a=[list(map(lambda x:x%p,row)) for row in rows]
    n=len(a); m=len(a[0]) if n else 0
    pivot_row=0
    for j in range(m):
        pivot=next((i for i in range(pivot_row,n) if a[i][j]),None)
        if pivot is None: continue
        a[pivot_row],a[pivot]=a[pivot],a[pivot_row]
        inv=pow(a[pivot_row][j],-1,p)
        for k in range(j,m):a[pivot_row][k]=a[pivot_row][k]*inv%p
        for i in range(pivot_row+1,n):
            t=a[i][j]
            if t:
                for k in range(j,m):a[i][k]=(a[i][k]-t*a[pivot_row][k])%p
        pivot_row+=1
        if pivot_row==n:break
    return pivot_row

def odd_unicyclic(n,edges):
    adj=[[] for _ in range(n)]
    for a,b in edges:adj[a].append(b);adj[b].append(a)
    seen=set()
    for start in range(n):
        if start in seen: continue
        queue=[start];seen.add(start);col={start:0};half_edges=0;odd=False
        for v in queue:
            half_edges+=len(adj[v])
            for w in adj[v]:
                if w not in seen:
                    seen.add(w);queue.append(w);col[w]=1-col[v]
                elif col[w]==col[v]:odd=True
        if half_edges//2 != len(queue) or not odd:return False
    return True

def e2_observed(n,unselected):
    # A vector in ker(B) is invisible on the selected coordinates
    # iff the columns of B_unselected are linearly dependent.
    return rank_mod([[int(i in edge) for edge in unselected]
                     for i in range(n)])==len(unselected)

def e1_observed(n,selected):
    # Parametrize the zero-sum vectors by v_i (i<n-1), v_last=-sum v_i.
    rows=[[int(i in edge)-int(n-1 in edge) for i in range(n-1)]
          for edge in selected]
    return rank_mod(rows)==n-1

def predicted(n,selected,unselected):
    if n==3: return len(selected)==2
    if n==4:
        degrees=sorted(sum(v in edge for edge in selected) for v in range(n))
        return degrees==[0,2,2,2] or degrees==[1,1,1,3]
    if not odd_unicyclic(n,unselected):return False
    if n==6 and sorted(sum(v in edge for edge in unselected)
                        for v in range(n))==[2]*6:
        # An odd-unicyclic 2-regular simple graph on six vertices is 2K3.
        return False
    return True

def check_incidence_identity(n):
    edges=list(combinations(range(n),2));N=len(edges)
    B=[[int(i in edge) for edge in edges] for i in range(n)]
    for i in range(n):
        for j in range(n):
            assert sum(B[i][k]*B[j][k] for k in range(N)) == ((n-2) if i==j else 0)+1
    for i,e in enumerate(edges):
        for j,f in enumerate(edges):
            A = int(i!=j and bool(set(e)&set(f)))
            assert sum(B[k][i]*B[k][j] for k in range(n))-2*int(i==j)==A

def check_order(n):
    E=list(combinations(range(n),2));N=len(E)
    k=max(n-1,N-n);hist=Counter();all_count=0
    for selected in combinations(E,k):
        selected=set(selected);unselected=[e for e in E if e not in selected]
        actual=e2_observed(n,unselected) and e1_observed(n,selected)
        want=predicted(n,selected,unselected)
        assert actual==want, (n,selected,actual,want)
        hist[actual]+=1; all_count+=1
    assert all_count==comb(N,k)
    expected={3:3,4:8,5:162,6:2520,7:45615}
    assert hist[True]==expected[n],(n,hist)
    print('n=',n,'subsets=',all_count,'controllable=',hist[True],'noncontrollable=',hist[False])

def check_egf():
    L=9
    rooted=[Fraction(0)]+[Fraction(i**(i-1),factorial(i)) for i in range(1,L+1)]
    def mul(a,b):
        return [sum(a[k]*b[i-k] for k in range(i+1)) for i in range(L+1)]
    U=[Fraction(0) for _ in range(L+1)]
    power=[Fraction(1)]+[Fraction(0) for _ in range(L)]
    for ell in range(1,L+1):
        power=mul(power,rooted)
        if ell>=3 and ell%2:
            U=[u+p/Fraction(2*ell) for u,p in zip(U,power)]
    expo=[Fraction(1)]+[Fraction(0) for _ in range(L)]
    for n in range(1,L+1):
        expo[n]=sum(k*U[k]*expo[n-k] for k in range(1,n+1))/n
    counts={n:factorial(n)*expo[n] - (10 if n==6 else 0)
            for n in range(5,L+1)}
    assert [counts[n] for n in (5,6,7,8)]==[162,2520,45615,937440]
    print('labelled counts:',', '.join(f'{n}:{int(v)}' for n,v in counts.items()))

if __name__=='__main__':
    for n in range(3,10):check_incidence_identity(n)
    for n in range(3,8):check_order(n)
    check_egf()
    print('all finite checks PASS; this is not a proof of the infinite statement')
