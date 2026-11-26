"""Reproduce exact terminal entrance-shell formulas for synchronous OR on Q_d."""
from math import comb

def tau(x,d):
    n=1<<d
    mask=(1<<n)-1
    seen={}
    ys=[]
    cur=x
    while cur not in seen:
        seen[cur]=len(ys)
        ys.append(cur)
        nxt=0
        for v in range(n):
            if any((cur>>(v^(1<<i)))&1 for i in range(d)):
                nxt |= 1<<v
        cur=nxt
    return seen[cur]

def count(d):
    counts={}
    for s in range(1<<(1<<d)):
        t=tau(s,d)
        counts[t]=counts.get(t,0)+1
    return counts

def expected(d):
    N=1<<(d-1);H=1<<N
    u=N*((1<<d)-d-1)- N*comb(d,2)//2
    return 2*N*H-N*N, (2*u*(H-N)-u*u if d>=3 else None)

if __name__=='__main__':
    for d in range(2,5):
        obs=count(d);m,p=expected(d)
        assert obs.get(d-1,0)==m,(d,obs,m)
        if d>=3: assert obs.get(d-2,0)==p,(d,obs,p)
        assert sum(obs.values())==(1<<(1<<d))
        print('d',d,'shell_histogram',obs,'last',m,'penultimate',p)
