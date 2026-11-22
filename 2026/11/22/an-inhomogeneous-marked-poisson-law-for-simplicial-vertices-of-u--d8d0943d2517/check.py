#!/usr/bin/env python3
"""Exact finite checks for simplicial-interval probabilities and structural rule.
Only standard Python is needed. Analytic point-process proof is in RESULT.md.
"""
from fractions import Fraction as Q
from itertools import permutations
from math import factorial
from collections import Counter


def simp_by_marks(intervals, target):
    a,b=intervals[target]; left=[]; right=[]
    for i,(c,d) in enumerate(intervals):
        if i==target:continue
        if a<c<b:left.append(c)
        if a<d<b:right.append(d)
    return not left or not right or max(left)<min(right)


def simp_by_graph(intervals, target):
    a,b=intervals[target]
    neighbors=[]
    for j,(c,d) in enumerate(intervals):
        if target!=j and max(a,c)<min(b,d):neighbors.append(j)
    for i in range(len(neighbors)):
        c,d=intervals[neighbors[i]]
        for k in neighbors[i+1:]:
            e,f=intervals[k]
            if max(c,e)>min(d,f):return False
    return True


def matchings(seq):
    if not seq:
        yield ()
    else:
        first=seq[0]
        for k in range(1,len(seq)):
            for rest in matchings(seq[1:k]+seq[k+1:]):
                yield ((first,seq[k]),)+rest


def multiply(a,b):
    out=[Q(0)]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b):out[i+j]+=v*w
    return out


def exact_formula(n,a,b):
    # h=g(a). g(t)=a^2+(1-b)^2+2t-2t^2
    h=1-((1-a)**2-(1-b)**2)
    polynomial=[a*a+(1-b)**2,Q(2),Q(-2)]
    power=[Q(1)]
    for _ in range(n-2):power=multiply(power,polynomial)
    integrand=multiply([Q(2),Q(-2)],power)
    integral=sum(v*(b**(j+1)-a**(j+1))/Q(j+1) for j,v in enumerate(integrand))
    return h**(n-1)+(n-1)*integral


def exact_order_probability(n,a,b):
    # Sum over all exact orderings of the other labelled endpoints in
    # (<a),(a,b),(>b); each ordering has probability a^l (b-a)^m (1-b)^r/(l!m!r!).
    labels=tuple(range(2*(n-1)))
    factorials=[factorial(i) for i in range(len(labels)+1)]
    result=Q(0)
    for perm in permutations(labels):
        for l in range(len(labels)+1):
            for m in range(len(labels)-l+1):
                r=len(labels)-l-m
                numerator=a**l*(b-a)**m*(1-b)**r
                if not numerator:continue
                weight=numerator/Q(factorials[l]*factorials[m]*factorials[r])
                positions={perm[k]: (k-l if l<=k<l+m else -1 if k<l else m) for k in range(len(labels))}
                inside=[(positions[2*j],positions[2*j+1]) for j in range(n-1)]
                # Within middle region positions 0..m-1; left/right of I -1 or m.
                marks=[]
                for u,v in inside:
                    if 0<=u<m and (v<0 or v>=m):
                        marks.append((u,'R' if v<0 else 'L'))
                    if 0<=v<m and (u<0 or u>=m):
                        marks.append((v,'R' if u<0 else 'L'))
                    if 0<=u<m and 0<=v<m:
                        lo,hi=sorted((u,v));marks.extend([(lo,'L'),(hi,'R')])
                marks.sort()
                types=[q for _,q in marks]
                if 'R' not in types or 'L' not in types or max(i for i,s in enumerate(types) if s=='L')<min(i for i,s in enumerate(types) if s=='R'):
                    result+=weight
    return result


def main():
    checks=0
    distribution={}
    for n in range(1,7):
        c=Counter()
        no_left=0; no_right=0; no_both=0
        for m in matchings(tuple(range(2*n))):
            val=0
            for j in range(n):
                a,b=m[j]
                ls=any(a<x<b for q,(x,y) in enumerate(m) if q!=j)
                rs=any(a<y<b for q,(x,y) in enumerate(m) if q!=j)
                no_left+=not ls; no_right+=not rs; no_both+=(not ls and not rs)
                got=simp_by_marks(m,j)
                want=simp_by_graph(m,j)
                assert got==want,(n,m,j,got,want)
                checks+=1
                val+=got
            c[val]+=1
        denominator=sum(c.values())
        harmonic=sum((Q(1,2*j+1) for j in range(n)),Q(0))
        assert Q(no_left,denominator)==harmonic,(n,no_left,denominator)
        assert Q(no_right,denominator)==harmonic,(n,no_right,denominator)
        assert Q(no_both,denominator)==1,(n,no_both,denominator)
        checks+=3
        distribution[n]=dict(sorted(c.items()))
    assert distribution[1]=={1:1}
    assert distribution[2]=={2:3}
    assert distribution[3]=={2:4,3:11}
    assert distribution[4]=={2:22,3:36,4:47}
    checks+=4
    pairs=[(Q(1,5),Q(3,5)),(Q(1,4),Q(3,4)),(Q(1,9),Q(2,9))]
    for n in [2,3,4]:
        for a,b in pairs:
            lhs=exact_formula(n,a,b)
            rhs=exact_order_probability(n,a,b)
            assert lhs==rhs,(n,a,b,lhs,rhs)
            checks+=1
    print('PASS:',checks,'exact structural/order checks')
    print('small-n distributions:',distribution)
    print('exact conditional formula vs exhaustive endpoint orders: 9 cases')

if __name__=='__main__':main()
