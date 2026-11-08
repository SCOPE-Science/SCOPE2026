"""Reproducible exact small-case checks for signed CountSketch on weighted unicyclic incidence matrices."""
from fractions import Fraction
from itertools import product
from math import comb
import random


def falling(s, k):
    if k > s:
        return 0
    result=1
    for j in range(k):result*=s-j
    return result


def predicted(n, ell, s, weights):
    assert len(weights)==n
    equal_pairs=sum(weights[i]==weights[j] for i in range(ell) for j in range(i+1,ell))
    eligible=Fraction(ell*(n-ell)+comb(ell,2),1)-Fraction(equal_pairs,2)
    return (Fraction(falling(s,n),s**n)+eligible*Fraction(falling(s,n-1),s**n))


def edges(n, ell):
    assert 3<=ell<=n
    ans=[(i,(i+1)%ell) for i in range(ell)]
    ans.extend((0,ell) if i==ell else (i-1,i) for i in range(ell,n))
    return ans


def rank_integer(mat):
    # Integer-exact elimination using fractions, finite small instances only.
    mat=[[Fraction(x) for x in row] for row in mat]
    if not mat:return 0
    h=len(mat);w=len(mat[0]);r=0
    for j in range(w):
        pivot=next((i for i in range(r,h) if mat[i][j]!=0),None)
        if pivot is None:continue
        mat[r],mat[pivot]=mat[pivot],mat[r]
        v=mat[r][j];mat[r]=[x/v for x in mat[r]]
        for i in range(r+1,h):
            t=mat[i][j]
            if t:mat[i]=[u-t*v for u,v in zip(mat[i],mat[r])]
        r+=1
        if r==h:break
    return r


def survival_count(n, ell, s, weights):
    # Use weights as positive edge ROW SCALES, so no square roots appear.
    E=edges(n,ell)
    B=[]
    for (u,v),w in zip(E,weights):
        row=[0]*(n-1)
        if u>0:row[u-1]-=w
        if v>0:row[v-1]+=w
        B.append(row)
    ok=0
    for buckets in product(range(s),repeat=n):
        for signs in product((-1,1),repeat=n):
            SB=[[0]*(n-1) for _ in range(s)]
            for i,row in enumerate(B):
                t=SB[buckets[i]]
                for j,v in enumerate(row):t[j]+=signs[i]*v
            ok+=rank_integer(SB)==n-1
    return Fraction(ok,(2*s)**n)


def run():
    trials=0
    for n in [3,4]:
        for ell in range(3,n+1):
            for s in [n-1,n,n+1]:
                for ww in ([1]*n,list(range(1,n+1)),[1]*ell+[2]*(n-ell)):
                    got=survival_count(n,ell,s,ww)
                    want=predicted(n,ell,s,ww)
                    assert got==want,(n,ell,s,ww,got,want)
                    trials+=1
    for n in range(3,50):
        lengths=range(3,n+1)
        f=lambda ell:Fraction(ell*(n-ell)+comb(ell,2),1)-Fraction(comb(ell,2),2)
        mx=max(f(ell) for ell in lengths)
        opt=[ell for ell in lengths if f(ell)==mx]
        x=Fraction(4*n-1,6)
        alt=[ell for ell in lengths if abs(Fraction(ell)-x)==min(abs(Fraction(t)-x) for t in lengths)]
        assert opt==alt,(n,opt,alt)
        # Generic distinct cycle weights: n-1 and n are maximizers, except n=3.
        fg=lambda ell:ell*(n-ell)+comb(ell,2)
        optg=[ell for ell in lengths if fg(ell)==max(fg(t) for t in lengths)]
        assert optg==[n-1,n] if n>=4 else optg==[3],(n,optg)
        trials+=2
    rng=random.Random(73021)
    sampled=0
    for n, ell in [(5,3),(5,4),(5,5),(6,3),(6,4),(6,6)]:
        for s in [n-1,n,n+1]:
            for weights in [[1]*n,list(range(1,n+1)),[1,2,1,2,1,2][:n]]:
                E=edges(n,ell)
                B=[]
                for (u,v),w in zip(E,weights):
                    row=[0]*(n-1)
                    if u>0:row[u-1]-=w
                    if v>0:row[v-1]+=w
                    B.append(row)
                for _ in range(70):
                    buckets=[rng.randrange(s) for _ in range(n)]
                    signs=[rng.choice((-1,1)) for _ in range(n)]
                    SB=[[0]*(n-1) for _ in range(s)]
                    for i,row in enumerate(B):
                        for j,v in enumerate(row): SB[buckets[i]][j]+=signs[i]*v
                    observed=(rank_integer(SB)==n-1)
                    groups={}
                    for i,b in enumerate(buckets):groups.setdefault(b,[]).append(i)
                    dup=n-len(groups)
                    if dup==0:expected=True
                    elif dup>=2:expected=False
                    else:
                        pair=next(g for g in groups.values() if len(g)==2)
                        i,j=pair
                        ci=(Fraction(1,weights[i]) if i<ell else Fraction(0))
                        cj=(Fraction(1,weights[j]) if j<ell else Fraction(0))
                        # Orientation chosen consistently for the cycle here.
                        expected=(ci*signs[j] != cj*signs[i])
                    assert observed==expected,(n,ell,s,weights,buckets,signs)
                    sampled+=1
    print('VERIFIED_EXACT exhaustive scenarios:',trials-94,'; exact finite extremum comparisons:',94, '; independent structural trials:',sampled)
    print('n=6, ell=4, s=5, equal:',predicted(6,4,5,[1]*6))
    print('n=6, ell=6, s=5, equal:',predicted(6,6,5,[1]*6))
    print('n=6, ell=4, s=5, distinct:',predicted(6,4,5,[1,2,3,4,1,1]))

if __name__=='__main__':run()
