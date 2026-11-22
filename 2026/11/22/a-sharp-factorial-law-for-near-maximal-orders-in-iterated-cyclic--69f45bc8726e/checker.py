"""Standalone exact order-distribution checker for iterated regular wreath powers."""
from itertools import product
from collections import Counter
from fractions import Fraction
from math import gcd

def distribution(p,h):
    F = [Fraction(1) for j in range(h+1)]
    for n in range(1,h+1):
        old = F
        F=[]
        for j in range(h+1):
            x=old[j]
            y=old[j-1] if j>0 else Fraction(0)
            F.append((x**p+(p-1)*y)/p)
    return [F[j]-(F[j-1] if j else Fraction(0)) for j in range(h+1)]

def all_perms(p,h):
    group=[(0,)]
    d=1
    for level in range(1,h+1):
        result=[]
        for components in product(group,repeat=p):
            for shift in range(p):
                result.append(tuple(((b+shift)%p)*d+components[b][i] for b in range(p) for i in range(d)))
        group=result
        d*=p
    return group

def exponent(perm):
    n=len(perm);seen=[False]*n; power=0
    for i in range(n):
        if seen[i]:continue
        j=i; ln=0
        while not seen[j]:
            seen[j]=True; ln+=1;j=perm[j]
        power=max(power,ln)
    return power

def run():
    for p,h in [(2,1),(2,2),(2,3),(2,4),(3,1),(3,2),(5,1),(5,2)]:
        group=all_perms(p,h)
        count=Counter()
        for g in group:
            order=exponent(g)
            j=0
            while order>1:
                assert order%p==0
                order//=p;j+=1
            count[j]+=1
        pred=distribution(p,h)
        assert all(Fraction(count[j],len(group))==pred[j] for j in range(h+1)),(p,h,count,pred)
        print(f'p={p} h={h} group={len(group)} exact order-power counts='+repr([count[j] for j in range(h+1)]))
        assert Fraction(count[h],len(group))==Fraction(p-1,p)**h
    # Independent floating-point recurrence sanity checks for the fixed-defect tails.
    from math import expm1, log1p, factorial
    for p in [2, 3, 5]:
        alpha=(p-1)/p
        H=500
        R=3
        tail=[[0.0]*(R+1) for _ in range(H+1)]
        for h in range(H+1):
            for r in range(R+1):
                if h<=r:
                    tail[h][r]=1.0
                elif r==0:
                    tail[h][r]=alpha**h
                else:
                    x=tail[h-1][r-1]
                    bp=(-expm1(p*log1p(-x))/p) if x<1 else 1/p
                    tail[h][r]=alpha*tail[h-1][r]+bp
        ratios=[tail[H][r]/(alpha**(H-r)*H**r/factorial(r)) for r in range(R+1)]
        assert all(.95<z<1.01 for z in ratios), (p, ratios)
        print(f'p={p} h=500 fixed-defect asymptotic tail ratios=' + repr([round(z,6) for z in ratios]))
    print('ALL_EXACT_CHECKS_PASSED')
if __name__=='__main__':run()
