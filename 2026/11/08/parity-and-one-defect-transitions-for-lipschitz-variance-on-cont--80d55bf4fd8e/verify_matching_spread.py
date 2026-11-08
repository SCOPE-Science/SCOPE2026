#!/usr/bin/env python3
"""Exact reproducibility checks for matched contractions of an equilateral metric."""
from fractions import Fraction
from itertools import product


def states(k, p, q):
    local=((0,0),(q,q),(0,p),(p,0),(q-p,q),(q,q-p))
    for seq in product(range(6), repeat=k):
        if not any(s in (0,2,3) for s in seq) or not any(s in (1,4,5) for s in seq):
            continue
        xs=tuple(x for s in seq for x in local[s])
        yield xs


def value(xs):
    n=len(xs)
    return n*sum(x*x for x in xs)-sum(xs)**2


def formula(k,p,q):
    if k%2==0:
        return k*k*q*q
    base=(k*k-1)*q*q
    # one mixed: a=(k-1)/2 full upper, sum (k-1)q + p, sumsq (k-1)q^2 + p^2
    mixed=(2*k)*((k-1)*q*q+p*p)-((k-1)*q+p)**2
    return max(base,mixed)


def winner_shapes(k,p,q):
    n=2*k; val=formula(k,p,q)
    pure=(k*k*q*q if k%2==0 else (k*k-1)*q*q)
    sh=set()
    for st in product(range(6),repeat=k):
        if sum(x in (2,3,4,5) for x in st)>1:continue
        xs=tuple(x for s in st for x in ((0,0),(q,q),(0,p),(p,0),(q-p,q),(q,q-p))[s])
        if value(xs)==val:sh.add(xs)
    return sh


def prufer_to_tree(seq,n):
    deg=[1]*n
    for v in seq:deg[v]+=1
    edges=[]
    for v in seq:
        u=next(i for i in range(n) if deg[i]==1)
        edges.append((u,v));deg[u]-=1;deg[v]-=1
    u,v=[i for i in range(n) if deg[i]==1]
    edges.append((u,v))
    return edges


def tight_tree_vertices(k,p,q):
    n=2*k; found=set()
    for seq in product(range(n),repeat=n-2):
        ed=prufer_to_tree(seq,n)
        aa=[[] for _ in range(n)]
        for j,(u,v) in enumerate(ed):
            length = p if u//2==v//2 else q
            aa[u].append((v,j,length,1));aa[v].append((u,j,length,-1))
        for mask in range(1<<(n-1)):
            zz=[None]*n;zz[0]=0;stack=[0]
            while stack:
                x=stack.pop()
                for y,j,l,sgn in aa[x]:
                    if zz[y] is None:
                        zz[y]=zz[x]+sgn*l*(1 if (mask>>j)&1 else -1)
                        stack.append(y)
            if all(abs(zz[i]-zz[j]) <= (p if i//2==j//2 else q) for i in range(n) for j in range(i+1,n)):
                mn=min(zz)
                found.add(tuple(x-mn for x in zz))
    return found


def main():
    checked=0
    for k in range(2,7):
        ls=[(1,4),(1,2),(3,4),(9,10)]
        if k%2:
            t=Fraction(2*(k-1),2*k-1)
            ls.extend([(t.numerator,t.denominator)])
        for p,q in ls:
            prof=list(states(k,p,q))
            mx=max(map(value,prof))
            predicted=formula(k,p,q)
            assert mx==predicted,(k,p,q,mx,predicted)
            got={xs for xs in prof if value(xs)==mx}
            want=winner_shapes(k,p,q)
            assert got==want,(k,p,q,len(got),len(want),got-want)
            checked+=1
    print('MATCHED_METRIC_EXACT_VERTEX_PROFILES_AND_ALL_OPTIMIZERS_OK',checked)
    for k,p,q in [(2,1,2),(3,1,3),(3,4,5),(3,9,10)]:
        v=tight_tree_vertices(k,p,q)
        target=set(states(k,p,q))
        assert v==target,(k,p,q,len(v),len(target),v-target,target-v)
        print('INDEPENDENT_TIGHT_SPANNING_TREE_ENUMERATION_OK',k,p,q,len(v))
    for k in range(2,25):
        if k%2==0:continue
        t=Fraction(2*(k-1),2*k-1)
        assert formula(k,t.numerator,t.denominator)==(k*k-1)*t.denominator*t.denominator
        assert formula(k,t.numerator-1,t.denominator)==(k*k-1)*t.denominator*t.denominator
        assert formula(k,t.numerator+1,t.denominator)>(k*k-1)*t.denominator*t.denominator
    print('EXACT_THRESHOLD_PHASE_CHECKS_OK 11')
    print('ALL_MATCHED_EQUILATERAL_SPREAD_CHECKS_OK')
if __name__=='__main__':main()
