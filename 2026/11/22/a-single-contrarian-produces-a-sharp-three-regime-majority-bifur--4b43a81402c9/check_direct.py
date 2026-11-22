"""Exhaustive bit-level cross-check for a marked minority site on K_{a,b}.
Public scientific verification only. Python >=3.9.
"""
from collections import Counter
from math import comb


def count_formula(a,b):
    assert a>=1 and b>=1
    tb = comb(b,b//2) if b%2==0 else 0
    ta = comb(a,a//2) if a%2==0 else 0
    total = 1 << (a+b)
    if a==1:
        return {(0,4):4,(1,4):total-4}
    if a==2:
        r0=(1<<b)+tb
        return {(0,1):r0,(1,1):total-2*r0,(2,1):r0}
    r0=4+ta*tb
    r2=ta*( (1<<b)-2-tb )+tb*((1<<a)-2-ta)
    osc=((1<<a)-ta)*((1<<b)-tb)//2
    return {'r0':r0,'r1':total-r0-r2,'r2':r2,'osc':osc,'fixed':2+ta*tb,'two_cycle':1}


def update(a,b,mask):
    n=a+b
    c=mask&1
    sa=((mask & ((1<<a)-1)).bit_count())
    sb=((mask>>a).bit_count())
    new=0
    # a-th vertex 0 is the only contrarian
    if 2*sb>b:
        marked=0; conform=1
    elif 2*sb<b:
        marked=1; conform=0
    else:
        marked=c; conform=None
    new|=marked
    for i in range(1,a):
        bit=(mask>>i)&1
        new|=(bit if conform is None else conform)<<i
    if 2*sa>a: other=1
    elif 2*sa<a: other=0
    else: other=None
    for i in range(a,n):
        bit=(mask>>i)&1
        new|=(bit if other is None else other)<<i
    return new


def initial_time(a,b,state):
    seen={};path=[];cur=state
    while cur not in seen:
        seen[cur]=len(path);path.append(cur)
        cur=update(a,b,cur)
        assert len(path)<=5, ('unexpected long orbit',a,b,state,path)
    return seen[cur],len(path)-seen[cur],tuple(path[seen[cur]:])


def test():
    checked=0
    for a in range(1,9):
        for b in range(1,9):
            sample=Counter();recurrent=set();periodic_attractors=set()
            for s in range(1<<(a+b)):
                t,p,cycle=initial_time(a,b,s)
                sample[t,p]+=1
                if t==0: recurrent.add(s)
                if p>1: periodic_attractors.add(tuple(sorted(cycle)))
                checked+=1
            expected=count_formula(a,b)
            if a<=2:
                for (t,p),cnt in expected.items():
                    assert sample[t,p]==cnt,(a,b,t,p,sample,expected)
                assert set(sample)<=set(expected),(a,b,sample,expected)
                assert len(periodic_attractors)==(1 if a==1 else 0)
            else:
                assert sum(cnt for (t,p),cnt in sample.items() if t==0)==expected['r0'],(a,b,sample,expected)
                assert sum(cnt for (t,p),cnt in sample.items() if t==1)==expected['r1'],(a,b,sample,expected)
                assert sum(cnt for (t,p),cnt in sample.items() if t==2)==expected['r2'],(a,b,sample,expected)
                assert sum(cnt for (t,p),cnt in sample.items() if p==2)==expected['osc'],(a,b,sample,expected)
                assert set(p for t,p in sample)<={1,2}
                assert len(periodic_attractors)==1
                assert sum(1 for s in recurrent if update(a,b,s)==s)==expected['fixed']
    print(f'DIRECT PASS: {checked} labelled initial states, 64 parameter pairs, all periods/depths/basin sizes')

if __name__=='__main__':test()
