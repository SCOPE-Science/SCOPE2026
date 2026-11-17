"""Independent direct-state enumeration of Rule 54 on labelled rings."""
from collections import Counter

def step(s,n):
    t=0
    for i in range(n):
        bits = 4*((s>>((i-1)%n))&1)+2*((s>>i)&1)+((s>>((i+1)%n))&1)
        t |= ((54>>bits)&1)<<i
    return t

def orbits(n):
    visited=set();hist=Counter()
    for state in range(1<<n):
        if state in visited:continue
        path=[];where={};s=state
        while s not in visited and s not in where:
            where[s]=len(path);path.append(s);s=step(s,n)
        if s in where:hist[len(path)-where[s]]+=1
        visited.update(path)
    return dict(sorted(hist.items()))

if __name__=='__main__':
    for n in range(3,12):print(f'n={n} orbit_periods={orbits(n)}')
    n=11
    witnesses=['00001001111','00001111001']
    for w in witnesses:
        x=int(w,2)
        seq=[]
        for i in range(11):
            seq.append(x);x=step(x,n)
        assert x==int(w,2) and len(set(seq))==11
        print(f'11-site witness={w} exact_temporal_period=11')
