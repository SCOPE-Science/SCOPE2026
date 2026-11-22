#!/usr/bin/env python3
"""Exact finite checks for graph-indexed coincidence variables in two-parameter partitions.
Pure Python 3 standard library. Finite checks supplement (not replace) the proof.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import factorial

CHECKS=0

def check(expr, note=''):
    global CHECKS
    CHECKS += 1
    if not expr:
        raise AssertionError(f'check {CHECKS}: {note}')

def partitions(n):
    def extend(blocks, i):
        if i==n:
            yield tuple(tuple(b) for b in blocks)
            return
        for j in range(len(blocks)):
            b=[x[:] for x in blocks]; b[j].append(i)
            yield from extend(b,i+1)
        yield from extend([*[b[:] for b in blocks], [i]],i+1)
    return list(extend([],0))

def rising(v,n,step=1):
    out=F(1)
    for j in range(n): out*=v+step*j
    return out

def partition_weight(blocks,a,t):
    # Pitman two-parameter exchangeable partition probability function.
    k=len(blocks); n=sum(map(len,blocks))
    out=rising(t+a,k-1,a)/rising(t+1,n-1)
    for b in blocks:out*=rising(1-a,len(b)-1)
    return out

def co(blocks,u,v):
    return any(u in b and v in b for b in blocks)

def check_model(a,t):
    D=(t+1)*(t+2); D4=D*(t+3)
    p=(1-a)/(t+1)
    p_inc=(1-a)*(2-a)/D
    p_dis=(1-a)*((2-a)*(3-a)+(t+a)*(1-a))/D4
    check(p_inc-p_dis==(1-a)*(t+a)/D4, 'pair-type gap')
    check(p_inc>p_dis, 'strict pair-type gap')
    p111=p_inc; psingle=(1-a)*(t+a)/D
    p000=(t+a)*(t+2*a)/D
    check(p111+3*psingle+p000==1, 'triangle mass')
    check(p111+psingle==p, 'triangle edge marginal')
    limit=(t+3-a)/(1-a)
    nmax=limit.numerator//limit.denominator
    check(nmax>=3, 'finite horizon at least three')
    for n in range(1,7):
        ps=partitions(n)
        probs=[partition_weight(b,a,t) for b in ps]
        check(sum(probs)==1, 'partition normalization')
        check(all(v>=0 for v in probs), 'partition nonnegativity')
        if n>=3:
            pattern={s:F(0) for s in product((0,1),repeat=3)}
            for b,w in zip(ps,probs):
                pattern[tuple(int(co(b,u,v)) for u,v in ((0,1),(0,2),(1,2)))]+=w
            for s,val in pattern.items():
                expected=p111 if sum(s)==3 else psingle if sum(s)==1 else p000 if sum(s)==0 else F(0)
                check(val==expected, 'triangle pattern exact')
        if n>=4:
            pin=sum(w for b,w in zip(ps,probs) if co(b,0,1) and co(b,0,2))
            pdi=sum(w for b,w in zip(ps,probs) if co(b,0,1) and co(b,2,3))
            check(pin==p_inc, 'incident pair exact')
            check(pdi==p_dis, 'disjoint pair exact')
    for N in range(3,nmax+3):
        wN=p111
        w1=N*psingle
        w0=(t+a)*(t+3-a-N*(1-a))/D
        check(w0+w1+wN==1, 'extension weights normalized')
        if N<=nmax:
            check(min(w0,w1,wN)>=0, 'extension nonnegativity')
            # The first-three marginal induced by the support {K=0,1,N}.
            check(wN==p111, 'all-one marginal')
            check(w1/N==psingle, 'singleton marginal')
            check(w0+w1*F(N-3,N)==p000, 'all-zero marginal')
        else:check(w0<0, 'sharp impossibility obstruction')

PARAMETERS=[(F(0),F(1,4)),(F(0),F(1)),(F(0),F(2)),(F(0),F(5)),
            (F(1,4),F(-1,8)),(F(1,4),F(1)),(F(1,2),F(-1,4)),
            (F(1,2),F(1)),(F(1,2),F(3)),(F(3,4),F(1,2)),
            (F(3,4),F(4))]
for alpha,theta in PARAMETERS:check_model(alpha,theta)

# Every simple graph with <=5 vertices: incidence-pair types either uniform
# or mixed; the uniform-pair-type graphs are exactly stars, triangles, matchings.
for n in range(2,6):
    edges=list(combinations(range(n),2))
    for mask in range(1,1<<len(edges)):
        selected=[e for j,e in enumerate(edges) if mask>>j&1]
        degrees=[sum(i in e for e in selected) for i in range(n)]
        star=len(selected)<=1 or max(degrees)==len(selected)
        triangle=len(selected)==3 and sorted(d for d in degrees if d>0)==[2,2,2]
        matching=max(degrees)==1
        overlaptypes={len(set(e)&set(f)) for e,f in combinations(selected,2)}
        uniform=len(overlaptypes)<=1
        check(uniform==(star or matching or triangle),'graph type classification')
print('PASS:',CHECKS,'exact checks; all findings above require the separate symbolic proof')
