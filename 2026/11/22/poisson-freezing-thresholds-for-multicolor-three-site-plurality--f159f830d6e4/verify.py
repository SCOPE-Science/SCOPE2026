#!/usr/bin/env python3
"""Independent small-instance tests of cyclic plurality with incumbent tie."""
from itertools import product

def step(a):
    n = len(a)
    return tuple(a[(i-1)%n] if a[(i-1)%n] == a[(i+1)%n] != a[i] else a[i] for i in range(n))

def flip(a):
    b=step(a)
    return tuple(int(a[i]!=b[i]) for i in range(len(a)))

def block(a,i,t):
    return int(all(a[(i-t-1+j)%len(a)] == a[(i-t-1+j+2)%len(a)]
                   and a[(i-t-1+j)%len(a)] != a[(i-t+j)%len(a)]
                   for j in range(2*t+1)))

def exact_stop(a):
    cur=a
    for t in range(len(a)+2):
        nxt=step(cur)
        if nxt==cur: return t
        cur=nxt
    return None

def verify():
    results=[]
    for q in (2,3,4):
        for n in range(3,9):
            cnt=[0]*(n+1); two=0
            for a in product(range(q),repeat=n):
                cur=a
                for t in range(min(n,4)):
                    e=flip(cur)
                    assert all(e[i] == block(a,i,t) for i in range(n)),(q,n,a,t)
                    b=step(cur)
                    ee=flip(b)
                    assert all(ee[i] == e[(i-1)%n]*e[i]*e[(i+1)%n] for i in range(n)),(q,n,a,t)
                    cur=b
                t=exact_stop(a)
                if t is None:
                    assert n%2==0 and all(a[i]==a[(i+2)%n] and a[i]!=a[(i+1)%n] for i in range(n)),(q,n,a)
                    two+=1
                else:
                    cnt[t]+=1
            assert sum(cnt)+two==q**n
            assert two==(q*(q-1) if n%2==0 else 0)
            sharp=max(i for i,x in enumerate(cnt) if x)
            predicted=(n-1)//2 if n%2 else (n-2)//2
            assert sharp==predicted,(q,n,sharp,predicted)
            results.append((q,n,q**n,two,sharp))
    print('PASS: all q=2,3,4, n=3..8: local erosion, finite bound, only alternating 2-cycles')
    print('Columns q n total two_cycle_states sharp_fixation_time')
    for r in results: print(*r)
    # Check absolute local identity on all length-7 words over alphabet q=5.
    for a in product(range(5), repeat=7):
        a1=step(a)
        e=flip(a)
        f=flip(a1)
        assert all(f[i]==e[(i-1)%7]*e[i]*e[(i+1)%7] for i in range(7))
    print('PASS: one-step erosion identity on all 5^7 = 78125 length-seven words')

if __name__=='__main__':verify()
