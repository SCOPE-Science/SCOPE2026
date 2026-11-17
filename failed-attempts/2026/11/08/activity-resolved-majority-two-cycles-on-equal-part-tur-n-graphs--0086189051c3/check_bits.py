#!/usr/bin/env python3
"""Exhaustive labelled binary configurations of balanced complete multipartite graphs.

For each test, independently apply the simultaneous neighbor-majority rule twice.
"""
from collections import Counter
from math import comb, factorial

def predicted(r,q):
    h=comb(q,q//2) if q%2==0 else 0
    fixed=2+h**r
    out={}
    for a in range(1,r//2+1):
        if r%2 and a==(r-1)//2:
            out[2*a*q]=r*comb(r-1,a)*(2**q-2)
        else:
            out[2*a*q]=factorial(r)//(factorial(a)**2*factorial(r-2*a))*h**(r-2*a)
    return fixed,{k:v for k,v in out.items() if v}

def update(x,r,q):
    total=x.bit_count(); y=0;mask=(1<<q)-1; deg=(r-1)*q
    for i in range(r):
        old=(x>>(i*q))&mask
        s=old.bit_count()
        if 2*(total-s)>deg: new=mask
        elif 2*(total-s)<deg:new=0
        else:new=old
        y|=new<<(i*q)
    return y

cases=[]
for r in range(2,8):
    for q in range(2,10):
        if r*q>18: continue
        fixed=0; activities=Counter()
        for x in range(1<<(r*q)):
            y=update(x,r,q)
            if x==y: fixed+=1
            elif update(y,r,q)==x: activities[(x^y).bit_count()]+=1
        expected=predicted(r,q)
        assert (fixed,dict(activities))==expected,(r,q,fixed,dict(activities),expected)
        cases.append((r,q,fixed,sum(activities.values()),dict(sorted(activities.items()))))
print('method=direct_bit_configuration', 'case_count='+str(len(cases)))
for row in cases:print(*row)
print('DIRECT_ALL_PASS')
