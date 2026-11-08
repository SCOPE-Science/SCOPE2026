#!/usr/bin/env python3
"""Independent color-phase enumeration, exact mass spectrum, and symbolic 9-state transfer check."""
import json
from collections import Counter
from itertools import product
from math import comb
import sympy as sp

def fib(t):
    a,b=0,1
    for _ in range(t):a,b=b,a+b
    return a

def word_mass(n):
    positive=Counter()
    valid=0
    for colors in product(range(3),repeat=n):
        h2=colors.count(2)
        if h2==0:continue
        starts=[n]
        caps=[h2]
        for i,b in enumerate(colors):
            a,c=colors[(i-1)%n],colors[(i+1)%n]
            neighbors=[int(a==j)+int(c==j) for j in range(3)]
            if b==0:lo=3; cap=neighbors[2]
            elif b==1:cap=1+neighbors[0];lo=3-cap
            else:cap=neighbors[1];lo=neighbors[2]
            if not cap:break
            starts.append(lo); caps.append(cap)
        else:
            valid+=1
            local=Counter({0:1})
            for base,cap in zip(starts,caps):
                nxt=Counter()
                for degree,mult in local.items():
                    for shift in range(cap):nxt[degree+base+shift]+=mult
                local=nxt
            for m,num in local.items():positive[m]+=3*num
    negative=Counter({7*n-1-m:num for m,num in positive.items()})
    total=positive+negative
    return positive,negative,total,valid

def symbolic_transfer():
    y,t,l=sp.symbols('y t l')
    edges=[(a,b) for a in range(3) for b in range(3)]
    mat=sp.zeros(9)
    for i,(a,b) in enumerate(edges):
        for j,(bb,c) in enumerate(edges):
            if b!=bb:continue
            q= (int(a==2)+int(c==2)) if b==0 else (1+int(a==0)+int(c==0) if b==1 else int(a==1)+int(c==1))
            mat[i,j]=q*(y if b==2 else 1)
    det=sp.factor((sp.eye(9)-t*mat).det())
    proposed=1-t-2*y*t**2-(y**2+4*y)*t**3-2*y*y*t**4-y*y*t**5+y*y*t**6
    assert sp.expand(det-proposed)==0
    d1=sp.factor(det.subs(y,1))
    assert sp.expand(d1-(1-3*t+t*t)*(1+t+t*t)**2)==0
    derivative=sp.cancel(-sp.diff(det,y).subs(y,1)/d1)
    decomp=-2+(1-t)/(2*(1-3*t+t*t))+(t+3)/(2*(1+t+t*t))
    assert sp.factor(derivative-decomp)==0
    # Counting admissible rim phase words: binary-support transfer.
    support=sp.zeros(9)
    for i,(a,b) in enumerate(edges):
        for j,(bb,c) in enumerate(edges):
            if b!=bb:continue
            q=(int(a==2)+int(c==2)) if b==0 else (1+int(a==0)+int(c==0) if b==1 else int(a==1)+int(c==1))
            support[i,j]=int(q>0)
    chi=sp.factor(support.charpoly().as_expr())
    assert str(chi)=='lambda**4*(lambda**2 + lambda + 1)*(lambda**3 - 2*lambda**2 - 1)'
    return str(sp.expand(det)),str(sp.factor(d1)),str(sp.factor(derivative)),str(chi)

if __name__=='__main__':
    det,d1,der,chi=symbolic_transfer()
    cases=[]
    for n in range(3,13):
        pos,neg,total,valid=word_mass(n)
        p=3*n*(fib(2*n+1)+{0:3,1:-2,2:-1}[n%3])
        eps=n%2
        assert sum(total.values())==p,(n,sum(total.values()),p)
        assert min(pos)==2*n+eps and max(pos)==3*n-1
        assert sorted(pos)==list(range(2*n+eps,3*n))
        assert min(neg)==4*n and max(neg)==5*n-1-eps
        assert sorted(neg)==list(range(4*n,5*n-eps))
        assert pos[2*n+eps]==(6 if n%2==0 else 12*n)
        assert neg[5*n-1-eps]==pos[2*n+eps]
        assert sum(pos.values())*2==p
        assert pos[3*n-1]==3*valid
        aa=[3,2,4]
        for k in range(3,n+1):aa.append(2*aa[k-1]+aa[k-3])
        assert valid==aa[n]+(1 if n%3==0 else -2)
        cases.append({'n':n,'period_three':p,'lower_endpoint':pos[2*n+eps], 'positive_upper_endpoint':pos[3*n-1], 'support':[[2*n+eps,3*n-1],[4*n,5*n-1-eps]], 'valid_hub_phase_words':valid})
    print(json.dumps({'status':'PASS','method':'phase-color polynomial enumeration and independent symbolic transfer determinant','det_I_minus_tM':det,'factor_at_y1':d1,'log_derivative':der,'support_transfer_characteristic':chi,'cases':cases},sort_keys=True,separators=(',',':')))
