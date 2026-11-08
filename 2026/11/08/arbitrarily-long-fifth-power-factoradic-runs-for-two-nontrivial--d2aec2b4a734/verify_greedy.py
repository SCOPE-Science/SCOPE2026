#!/usr/bin/env python3
"""Second verification using greedy factorial-place expansion, independently of verify.py."""
from math import factorial

CYCLES = {(1,), (34,), (35,), (308,), (309,), (1058,), (1059,), (2114,3401)}
U = (1,34,35,308,309,1058,1059,2114,3401)

def F(n):
    if n==0:return 0
    k=1
    while factorial(k+1)<=n:
        k+=1
    total=0
    for j in range(k,0,-1):
        a, n=divmod(n,factorial(j))
        assert a<=j
        total+=a*a*a*a*a
    assert n==0
    return total

def cyc(n):
    seen={}
    path=[]
    while n not in seen:
        seen[n]=len(path)
        path.append(n)
        n=F(n)
    c=path[seen[n]:]
    c=tuple(c)
    return min(c[i:]+c[:i] for i in range(len(c)))

if __name__=='__main__':
    actual={cyc(i) for i in range(1,40320)}
    assert actual==CYCLES,(actual,CYCLES)
    for offset,p in ((1373,34),(75004,1058)):
        assert all(cyc(offset+u)==(p,) for u in U)
    print('independent_greedy_check=PASS')
    print('checked_initial_states=40319')
