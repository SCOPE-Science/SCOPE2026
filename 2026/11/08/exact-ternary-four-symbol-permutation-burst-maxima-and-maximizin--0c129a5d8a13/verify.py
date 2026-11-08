"""Reproducibility checker for ternary four-position permutation spheres.
Pure Python 3 standard library, exact integer arithmetic.
"""
from itertools import product, permutations
from collections import Counter
from math import factorial, comb

Q=(0,1,2)
TYPES=('000','001','010','011','012')
REPS=((0,0,0),(0,0,1),(0,1,0),(0,1,1),(0,1,2))
EXPECTED={
 '000':(('000',0),('011',1),('011',1)),
 '001':(('000',3),('011',3),('011',9)),
 '010':(('001',1),('010',3),('012',6)),
 '011':(('001',3),('010',1),('012',6)),
 '012':(('001',9),('010',9),('012',6)),
}

def type_of(s):
    names={}
    return ''.join(str(names.setdefault(x,len(names))) for x in s)

def mult(v):
    c=Counter(v)
    # Use a single exact denominator (individual division need not be integral).
    den=1
    for z in c.values(): den*=factorial(z)
    return factorial(len(v))//den

def endpoint_changes(v):
    c=Counter(v)
    m=len(v)
    total=mult(v)
    def number_fixed(fixed):
        cc=c.copy()
        for a in fixed:
            cc[a]-=1
            if cc[a]<0:return 0
        den=1
        for z in cc.values():den*=factorial(z)
        return factorial(m-len(fixed))//den
    return total-number_fixed([v[0]])-number_fixed([v[-1]])+number_fixed([v[0],v[-1]])

T={v:endpoint_changes(v) for m in (2,3,4) for v in product(Q,repeat=m)}
for v,t in T.items():
    assert t==sum(w[0]!=v[0] and w[-1]!=v[-1] for w in set(permutations(v)))

for target,rep in zip(TYPES,REPS):
    b,c,d=rep
    pred=tuple((type_of((a,b,c)),T[(c,d)]+T[(b,c,d)]+T[(a,b,c,d)]) for a in Q)
    assert pred==EXPECTED[target],(target,pred)

STATES=list(product(Q,repeat=3))

def step(dp):
    new={}
    for s in STATES:
        b,c,d=s
        candidates=[]
        for a in Q:
            p=(a,b,c)
            v,num=dp[p]
            candidates.append((v+T[(c,d)]+T[(b,c,d)]+T[(a,b,c,d)],num))
        best=max(v for v,num in candidates)
        new[s]=(best,sum(num for v,num in candidates if v==best))
    return new

def predicted(n):
    if n%3==0:
        t=n//3
        return 8*n-18,6,(-11,-3,-3,-3,0),(t*(t+1),comb(t+1,2),t,t,1)
    if n%3==1:
        t=n//3
        return 8*n-20,3*(t+2)*(t+3),(-8,0,0,0,0),(2*t,t,1,1,comb(t+2,2))
    t=n//3
    return 8*n-19,6*(t+2),(-8,0,-3,-3,0),(2,1,comb(t+2,2),comb(t+2,2),t+1)

dp={s:(1+T[s[:2]]+T[s[1:]]+T[s],1) for s in STATES}
for n in range(4,301):
    dp=step(dp)
    maxval,maxcount,deltas,counts=predicted(n)
    assert max(v for v,c in dp.values())==maxval,n
    assert sum(c for v,c in dp.values() if v==maxval)==maxcount,n
    for s,(v,c) in dp.items():
        j=TYPES.index(type_of(s))
        assert (v,c)==(maxval+deltas[j],counts[j]),(n,s,v,c)
print('PASS recurrence and all five state classes through length 300')

# Exact symbolic polynomial check of the infinite induction, not extrapolation.
from fractions import Fraction as F

def plus(*polys):
    return tuple(sum(p[j] for p in polys) for j in range(3))

def shift_one(p):
    # p( t + 1 ) for p(t) = p0 + p1*t + p2*t*t.
    a,b,c=p
    return (a+b+c,b+2*c,c)

P1=[(0,2,0),(0,1,0),(1,0,0),(1,0,0),(1,F(3,2),F(1,2))]
P2=[(2,0,0),(1,0,0),(1,F(3,2),F(1,2)),(1,F(3,2),F(1,2)),(1,1,0)]
P0=[(0,1,1),(0,F(1,2),F(1,2)),(0,1,0),(0,1,0),(1,0,0)]
D1=(-8,0,0,0,0)
D2=(-8,0,-3,-3,0)
D0=(-11,-3,-3,-3,0)

for prevd,nextd,prevcounts,nextcounts,increase in (
    (D1,D2,P1,P2,9),
    (D2,D0,P2,[shift_one(p) for p in P0],9),
    (D0,D1,P0,P1,6),
):
    for j,target in enumerate(TYPES):
        candidates=[(prevd[TYPES.index(k)]+weight,TYPES.index(k))
                    for k,weight in EXPECTED[target]]
        best=max(x for x,_ in candidates)
        assert best==increase+nextd[j],(target,best)
        winning=plus(*(prevcounts[k] for x,k in candidates if x==best))
        assert winning==nextcounts[j],(target,winning,nextcounts[j])
print('PASS exact symbolic max-plus and tie-count induction')


# Independent direct channel enumeration (permutation output sets, no T formula).
WINDOWS={v:set(permutations(v)) for v in product(Q,repeat=4)}
for n in range(4,11):
    best=-1
    num=0
    for x in product(Q,repeat=n):
        sphere={x}
        for i in range(n-3):
            for p in WINDOWS[x[i:i+4]]:
                sphere.add(x[:i]+p+x[i+4:])
        b=len(sphere)
        by_span=1+sum(T[x[i:i+m]] for m in (2,3,4) for i in range(n-m+1))
        assert b==by_span,(n,x,b,by_span)
        if b>best:best=b;num=1
        elif b==best:num+=1
    target_best,target_count,*_=predicted(n)
    assert (best,num)==(target_best,target_count),(n,best,num)
    print('PASS direct n=%d: max=%d, maximizers=%d, words=%d'%(n,best,num,3**n))
print('VERIFY_OK')
