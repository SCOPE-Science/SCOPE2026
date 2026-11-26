#!/usr/bin/env python3
"""Exact exhaustive certificate for the five-vertex percolation-vaccination theorem.
Run with Python 3 (standard library only)."""
from itertools import combinations, permutations
from math import comb

A = ((0,1),(1,3),(1,4),(2,3),(2,4),(3,4))
B = ((0,2),(0,3),(0,4),(1,2),(1,3),(1,4),(2,4))

def trim(a):
    a=list(a)
    while len(a)>1 and a[-1]==0:a.pop()
    return tuple(a)

def add(a,b):
    return trim([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
                 for i in range(max(len(a),len(b)))])

def minus(a,b):return add(a,[-v for v in b])

def mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return trim(out)

def times(a,n):return trim([n*x for x in a])

def canonical(n, edges):
    e={tuple(sorted(x)) for x in edges}
    return min(tuple((min(order[i],order[j]),max(order[i],order[j])) in e
                     for i in range(n) for j in range(i+1,n))
               for order in permutations(range(n)))

def connected(n, edges):
    seen={0}
    while True:
        nxt=seen | {b for a,b in edges if a in seen} | {a for a,b in edges if b in seen}
        if nxt==seen:return len(seen)==n
        seen=nxt

def comps(n, edges):
    roots=list(range(n))
    def root(k):
        while roots[k]!=k:k=roots[k]
        return k
    for a,b in edges:roots[root(a)]=root(b)
    sizes={}
    for u in range(n):
        z=root(u);sizes[z]=sizes.get(z,0)+1
    return sum(x*x for x in sizes.values())

def risk_num(n,edges,removed):
    # (n-1) times expected final epidemic size, integer polynomial in p.
    E=[(a,b) for a,b in edges if a!=removed and b!=removed]
    nodes=[i for i in range(n) if i!=removed]
    ix={v:i for i,v in enumerate(nodes)}
    E=[(ix[a],ix[b]) for a,b in E]
    m=len(E);P=[0]*(m+1)
    for mask in range(1<<m):
        sub=[E[j] for j in range(m) if mask>>j & 1]
        k=len(sub);c=comps(n-1,sub)
        for j in range(k,m+1):
            P[j]+=c*(-1)**(j-k)*comb(m-k,j-k)
    return trim(P)

def conn_risk_num(n,edges,removed):
    # Independent pair-connectivity evaluation (not component-size summation).
    E=[(a,b) for a,b in edges if a!=removed and b!=removed]
    nodes=[i for i in range(n) if i!=removed]
    N=len(nodes);m=len(E);P=[0]*(m+1)
    for mask in range(1<<m):
        sub=[E[j] for j in range(m) if mask>>j&1]
        # Number of ordered connected distinct pairs plus N diagonal terms.
        reach=0
        for a in nodes:
            seen={a}
            while True:
                nxt=seen | {v for u,v in sub if u in seen} | {u for u,v in sub if v in seen}
                if nxt==seen:break
                seen=nxt
            reach+=len(seen)
        k=mask.bit_count()
        for j in range(k,m+1):P[j]+=reach*(-1)**(j-k)*comb(m-k,j-k)
    return trim(P)

def bernstein_positive(a):
    # For t=p/(1-p)>=0: (1+t)^d a(t/(1+t)) has these coefficients.
    d=len(a)-1
    vals=[sum(a[k]*comb(d-k,j-k) for k in range(j+1)) for j in range(d+1)]
    return all(x>=0 for x in vals)

def all_graph_classes(n):
    pairs=list(combinations(range(n),2));reps={}
    for mask in range(1<<len(pairs)):
        E=tuple(pairs[k] for k in range(len(pairs)) if mask>>k&1)
        if connected(n,E):reps.setdefault(canonical(n,E),E)
    return reps

def assert_polynomial(a,b,description):
    assert trim(a)==trim(b),(description,a,b)

def exceptional_checks(E,kind):
    P=[risk_num(5,E,i) for i in range(5)]
    p=(0,1); q=(-1,1)
    if kind=='A':
        # 4(R3-R1)=2p^2(4p-1), 4(R3-R2)=2p(p-1)(2p²+4p+1)
        assert_polynomial(minus(P[3],P[1]),times(mul(mul(p,p),(-1,4)),2),'A switch')
        assert_polynomial(P[4],P[3],'A exchange symmetry')
        assert_polynomial(minus(P[3],P[2]),times(mul(mul(p,q),(1,4,2)),2),'A dominates vertex2')
        assert_polynomial(minus(P[3],P[0]),times(mul(mul(p,q),(2,8,7,-7)),2),'A dominates vertex0')
        # Since 2+8p+7p²(1-p)>0, R3<R0 throughout (0,1).
    else:
        # 4(R2-R0)=2p²(1-p)(4p-1).
        assert_polynomial(minus(P[2],P[0]),times(mul(mul(mul(p,p),(1,-1)),(-1,4)),2),'B switch')
        assert_polynomial(P[4],P[2],'B exchange symmetry')
        assert_polynomial(P[1],P[0],'B other exchange symmetry')
        assert_polynomial(minus(P[3],P[2]),times(mul(mul(p,(1,-2,1)),(1,6,7)),2),'B dominates vertex3')
    for i in range(5):
        assert_polynomial(P[i],conn_risk_num(5,E,i),'pair check '+kind+str(i))


def main():
    totals={};exceptions=[];bern_checks=0;independent_checks=0
    for n,expected in [(2,1),(3,2),(4,6),(5,21)]:
        reps=all_graph_classes(n)
        assert len(reps)==expected,('graph class count',n,len(reps))
        totals[n]=len(reps)
        for can,E in reps.items():
            pol=[risk_num(n,E,i) for i in range(n)]
            # Independent pair-based formula for every representative and vertex.
            for i in range(n):
                assert_polynomial(pol[i],conn_risk_num(n,E,i),'independent evaluator')
                independent_checks+=1
            good=[w for w in range(n) if all(bernstein_positive(minus(pol[j],pol[w]))
                                             for j in range(n))]
            if good:
                w=good[0]
                for j in range(n):
                    assert bernstein_positive(minus(pol[j],pol[w]))
                    bern_checks+=1
            else: exceptions.append((n,can))
    expected={canonical(5,A),canonical(5,B)}
    assert len(exceptions)==2,exceptions
    assert {c for n,c in exceptions}==expected,exceptions
    exceptional_checks(A,'A');exceptional_checks(B,'B')
    print('PASS: connected unlabeled graph counts:',totals)
    print('PASS: exactly two crossover classes, both on five vertices')
    print('PASS: 1/4 threshold and all competing vertex inequalities in both classes')
    print('PASS: nonnegative transformed-polynomial coefficient certificates:',bern_checks)
    print('PASS: independent component/pair evaluations:',independent_checks+10)
if __name__=='__main__':main()
