#!/usr/bin/env python3
"""Independent direct state-transition and functional-graph test for Rule 170."""
from itertools import permutations
from collections import Counter
from math import factorial


def update(x,n,order):
    for i in order:
        old=(x>>((i+1)%n))&1
        x=(x&~(1<<i))|(old<<i)
    return x


def period_of_state(x,n,order):
    v=x;seen={};path=[]
    while v not in seen:
        seen[v]=len(path);path.append(v)
        v=update(v,n,order)
    return seen[v],len(path)-seen[v]


def mobius(n):
    if n==1:return 1
    ans=1
    for p in range(2,n+1):
        if n%p:continue
        if all(p%q for q in range(2,int(p**0.5)+1)):
            if n%(p*p)==0:return 0
            ans=-ans
    return ans


def aperiod(p):
    return sum(mobius(p//d)*2**d for d in range(1,p+1) if p%d==0)


def main():
    for n in range(3,8):
        phase=Counter();found=0
        for order in permutations(range(n)):
            t=[order.index(i) for i in range(n)]
            k=sum(t[(i-1)%n]<t[i] for i in range(n))
            count=Counter()
            for x in range(1<<n):
                pre,period=period_of_state(x,n,order)
                assert pre in (0,1)
                count[(pre,period)]+=1
            assert sum(v for (a,p),v in count.items() if a==0)==1<<k
            assert sum(v for (a,p),v in count.items() if a==1)==(1<<n)-(1<<k)
            for p in range(1,n):
                v=sum(count[(a,p)] for a in (0,1))
                predicted=(1<<(n-k))*aperiod(p) if k%p==0 else 0
                assert v==predicted,(n,order,k,p,v,predicted)
                assert count[(0,p)]==(aperiod(p) if k%p==0 else 0)
            phase[k]+=1;found+=1
        print('n',n,'orders_checked',found,'cyclic_ascent_range',min(phase),max(phase))
        assert found==factorial(n)
    print('BRUTE_FUNCTIONAL_GRAPH_OK')

if __name__=='__main__':main()
