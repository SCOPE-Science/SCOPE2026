#!/usr/bin/env python3
"""Exact rational elimination for majority 2-cycles in a nearly-crown graph.
All algebra is integer; no external solver is required.
"""
from itertools import product
from math import gcd, comb, factorial

LEVELS=('L','M','P','H')

def map_level(la,lb):
    def one(old, mate, lev):
        if lev=='L': return 0
        if lev=='H': return 1
        if lev=='M': return old if mate==0 else 0
        if lev=='P': return 1 if mate==0 else old
        raise ValueError(lev)
    result=[]
    for i in range(4):
        a,b=i//2,i%2
        result.append(2*one(a,b,lb)+one(b,a,la))
    return tuple(result),int(lb in 'PH'),int(la in 'PH')

# Inequalities in variables (t00, t01, t10, t11, q): sum coeff * variable <= bound.
# The defining equality t00+t01+t10+t11=2q is eliminated exactly by t11=2q-t00-t01-t10.
def to4(coeff, bound):
    c=coeff[3]
    return (coeff[0]-c, coeff[1]-c, coeff[2]-c, coeff[4]+2*c),bound

def normalize(row):
    coeff,b=row
    g=0
    for z in (*coeff,b):g=gcd(g,abs(z))
    if g>1:coeff=tuple(z//g for z in coeff); b//=g
    return coeff,b

def simplify(rows):
    unique={}
    for row in rows:
        a,b=normalize(row)
        if not any(a):
            if b<0:return None
            continue
        if a not in unique or b<unique[a]: unique[a]=b
    return [(a,b) for a,b in unique.items()]

def feasible_exact(rows):
    rows=simplify(rows)
    if rows is None:return False
    nvar=4
    for _ in range(nvar):
        # Favor least pair explosion.
        choice=min(range(nvar),key=lambda j: sum(r[0][j]>0 for r in rows)*sum(r[0][j]<0 for r in rows))
        pos=[r for r in rows if r[0][choice]>0]
        neg=[r for r in rows if r[0][choice]<0]
        zero=[r for r in rows if r[0][choice]==0]
        after=[]
        for (ap,bp) in pos:
            for (an,bn) in neg:
                pn=ap[choice];nn=-an[choice]
                new_a=tuple((nn*ap[k]+pn*an[k]) for k in range(nvar) if k!=choice)
                after.append((new_a,nn*bp+pn*bn))
        after.extend((tuple(a[k] for k in range(nvar) if k!=choice),b) for a,b in zero)
        rows=simplify(after)
        if rows is None:return False
        nvar-=1
    return True

def level_rows(lev, coeff, off=0):
    # S=(coeff dot vars)+off, vs q; values are integers.
    c=list(coeff); c[4]-=1
    if lev=='L':return [(tuple(c),-1-off)]
    if lev=='M':return [(tuple(c),-off),(tuple(-z for z in c),off)]
    if lev=='P':return [(tuple(c),1-off),(tuple(-z for z in c),-1+off)]
    if lev=='H':return [(tuple(-z for z in c),-2+off)]
    raise ValueError(lev)

def make_rows(la,lb,la1,lb1,mask,x,y,T,X1,Y1):
    ac=(0,0,1,1,0);bc=(0,1,0,1,0)
    a1=tuple(int(T[j]>=2) for j in range(4))+(0,)
    b1=tuple(int(T[j]%2==1) for j in range(4))+(0,)
    pre=[((0,0,0,0,-1),-1)]
    for j in range(4):
        c=tuple(1 if z==j else 0 for z in range(4))+(0,)
        if mask>>j&1:pre.append((tuple(-z for z in c),-1))
        else:pre.extend(((c,0),(tuple(-z for z in c),0)))
    pre.extend(level_rows(la,ac,x))
    pre.extend(level_rows(lb,bc,y))
    pre.extend(level_rows(la1,a1,X1))
    pre.extend(level_rows(lb1,b1,Y1))
    return [to4(*r) for r in pre]

def class_solutions():
    tested=0;good=[]
    for la,lb,la1,lb1 in product(LEVELS,repeat=4):
        T,X1,Y1=map_level(la,lb)
        T2,X2,Y2=map_level(la1,lb1)
        for x,y in product((0,1),repeat=2):
            if (X2,Y2)!=(x,y): continue
            for mask in range(1,16):
                members=tuple(j for j in range(4) if mask>>j&1)
                if any(T2[T[j]]!=j for j in members):continue
                if all(T[j]==j for j in members) and (X1,Y1)==(x,y):continue
                tested+=1
                rows=make_rows(la,lb,la1,lb1,mask,x,y,T,X1,Y1)
                if feasible_exact(rows):good.append((la,lb,la1,lb1,x,y,members,rows))
    return tested,good

EXPECTED={(0,1,0,1),(0,1,1,),(0,1,1,2),(0,1,1,3),(1,0,0,2),(1,0,1,2),(1,0,2,),(1,0,2,3)}

def check():
    tested,good=class_solutions()
    assert tested==296,(tested,len(good))
    assert len(good)==8,len(good)
    seen={(x,y,*members) for la,lb,la1,lb1,x,y,members,rows in good}
    assert seen==EXPECTED,(seen,EXPECTED)
    # For two-population profiles, prove t_j=q, not only support.
    q_splits=0
    for la,lb,la1,lb1,x,y,members,rows in good:
        if len(members)==2:
            j=members[0]
            a=[0]*5;a[j]=1;a[4]=-1
            for sign in (-1,1):
                # sign=1: t_j-q>=1; sign=-1: t_j-q<=-1
                c=tuple(sign*v for v in a)
                if sign==1:c=tuple(-v for v in c)
                # simpler direct below
                if sign==1: # q-t_j <=-1 (t_j>=q+1)
                    bad=(tuple(-v for v in a),-1)
                else: # t_j-q <=-1 (t_j<=q-1)
                    bad=(tuple(a),-1)
                assert not feasible_exact(rows+[to4(*bad)]), (members,sign)
                q_splits+=1
    print('exact rational Fourier-Motzkin: candidate regime/support systems =',tested)
    print('infeasible systems =',tested-len(good))
    print('feasible systems =',len(good))
    print('exact equal-half exclusions =',q_splits)
    for la,lb,la1,lb1,x,y,members,_ in good:
        print('category',la,lb,'->',la1,lb1,'unmatched',x,y,'types',members,
              'counts', '2q' if len(members)==1 else 'q,q')
    print('P(n=2q+1, k=2q) primitive 2-cycles = 3*C(2q,q)+1, for all q>=1.')
if __name__=='__main__':check()
