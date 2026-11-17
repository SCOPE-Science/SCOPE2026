#!/usr/bin/env python3
"""Independent run-count and periodic-configuration constructor for odd-cycle dumbbells."""
from itertools import product
from math import comb

def run_sum(length):
    return 2*sum(comb(length-2*j-1,2*j-1)
                 for j in range(1,length//4+1))

def stable_words(length):
    words=[]
    for word in product((0,1),repeat=length):
        if word[0]==word[-1]: continue
        run=1
        ok=True
        for i in range(1,length):
            if word[i]==word[i-1]:run+=1
            else:
                if run<2:ok=False;break
                run=1
        if run<2:ok=False
        if ok:words.append(word)
    return words

def graph(a,b,d):
    g=[[] for _ in range(a+b+d-1)]
    def add(i,j):g[i].append(j);g[j].append(i)
    for start,size in ((0,a),(a,b)):
        for i in range(size):add(start+i,start+(i+1)%size)
    connector=[0]+list(range(a+b,a+b+d-1))+[a]
    for i in range(d):add(connector[i],connector[i+1])
    return g,connector

def update(x,g):
    result=[]
    for i,ns in enumerate(g):
        s=sum(x[j] for j in ns)
        result.append(1 if 2*s>len(ns) else 0 if 2*s<len(ns) else x[i])
    return tuple(result)

def check(a,b,d):
    g,connector=graph(a,b,d)
    wa=stable_words(a-1);wb=stable_words(b-1)
    for u in wa:
        for v in wb:
            for h in (0,1):
                x=[h,*u,(h^ (d%2)),*v]+[0]*(d-1)
                for k,node in enumerate(connector[1:-1],1):x[node]=h^(k%2)
                x=tuple(x);y=update(x,g)
                assert update(y,g)==x
                assert {i for i in range(len(x)) if x[i]!=y[i]}==set(connector)
    print(f'{a},{b},{d} constructed_period_2_states={2*len(wa)*len(wb)}')

if __name__=='__main__':
    for length in range(2,19):
        empirical=len(stable_words(length))
        expected=run_sum(length)
        assert empirical==expected,(length,empirical,expected)
    # Rational generating function and six-residue Fibonacci correction.
    coefficients=[0]*101
    for L in range(4,101):
        coefficients[L]=2*coefficients[L-1]-coefficients[L-2]+coefficients[L-4]+(2 if L==4 else 0)
        assert coefficients[L]==run_sum(L)
    fib=[0,1]
    for i in range(2,101):fib.append(fib[-1]+fib[-2])
    q=(1,0,-1,-1,0,1)
    for L in range(2,101):assert coefficients[L]==fib[L-1]+q[L%6]
    for a,b,d in ((3,5,1),(5,5,1),(5,5,2),(5,5,7),
                  (5,7,3),(7,7,4),(7,9,2),(9,11,6)):
        check(a,b,d)
    print('PASS combinatorial_coefficients=99 constructive_cases=8')
