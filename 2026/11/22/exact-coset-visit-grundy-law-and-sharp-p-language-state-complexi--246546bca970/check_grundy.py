#!/usr/bin/env python3
"""Direct recursion and independent prefix-coset enumeration for subgroup word games."""
from itertools import product, permutations
from collections import Counter
from math import comb

def cyclic(n):
    return list(range(n)), lambda x,y:(x+y)%n, 0

def symmetric3():
    group=list(permutations(range(3)))
    return group,lambda x,y:tuple(x[y[k]] for k in range(3)),tuple(range(3))

def test(label,G,mul,identity,H,maxlen):
    H=set(H)
    key=lambda a: a
    # Direct definition: compute all suffix products independently of the coset formula.
    memo={():0}
    q=len(G); h=len(H)
    for n in range(1,maxlen+1):
        hist=Counter()
        for w in product(G,repeat=n):
            options=[]
            for j in range(n):
                s=identity
                for v in w[j:]: s=mul(s,v)
                if s in H: options.append(memo[w[:j]])
            k=0
            while k in options: k+=1
            memo[w]=k
            hist[k]+=1
            # Independently compare the coset-visit formula.
            prefixes=[identity]
            for g in w: prefixes.append(mul(prefixes[-1],g))
            last=prefixes[-1]
            coset=set(mul(last,t) for t in H)
            expected=sum(int(v in coset) for v in prefixes[:-1])
            assert k==expected,(label,w,k,expected)
        expected_hist={k:comb(n,k)*h**k*(q-h)**(n-k) for k in range(n+1)}
        expected_hist={k:v for k,v in expected_hist.items() if v}
        assert dict(hist)==expected_hist,(label,n,hist,expected_hist)
        print(label,'n=',n,'counts=',dict(sorted(hist.items())))
    print('PASS',label)

if __name__=='__main__':
    G,mul,e=cyclic(4); test('Z4 / {0,2}',G,mul,e,{0,2},7)
    G,mul,e=cyclic(3); test('Z3 / identity',G,mul,e,{0},7)
    G,mul,e=symmetric3()
    t=(1,0,2)
    # This subgroup is NOT normal in S3.
    test('S3 / nonnormal order-2',G,mul,e,{e,t},5)
