#!/usr/bin/env python3
"""Independent exhaustive state-graph check of time-to-periodicity counts."""
from collections import Counter,deque

def image(s,n,kind):
    out=0
    for i in range(2*n):
        if kind=='mobius':
            nb=((i-1)%(2*n),(i+1)%(2*n),(i+n)%(2*n))
        else:
            k=i%n; off=0 if i<n else n
            nb=(off+(k-1)%n,off+(k+1)%n,i+n if i<n else i-n)
        b=sum((s>>j)&1 for j in nb)&1
        out|=b<<i
    return out

def exp_cum(n,kind,t):
    h=n&-n
    if n%3: return 2**(2*n)
    if n%2:
        d=4*min(t,1) if kind=='mobius' else 2*min(t,2)
    else:
        d=2*min(t,2*h) if kind=='mobius' else 4*min(t,h)
    return 2**(2*n-4*h+d)

def check():
    comps=0
    for n in range(3,9):
      for kind in ('mobius','prism'):
        sz=1<<(2*n)
        dest=[image(i,n,kind) for i in range(sz)]
        indeg=[0]*sz
        for j in dest: indeg[j]+=1
        q=deque(i for i in range(sz) if not indeg[i]); order=[]
        while q:
            i=q.popleft();order.append(i);k=dest[i];indeg[k]-=1
            if indeg[k]==0:q.append(k)
        entry=[0]*sz
        for i in reversed(order):entry[i]=entry[dest[i]]+1
        count=Counter(entry)
        for t in range(max(count)+2):
            actual=sum(c for entry_t,c in count.items() if entry_t<=t)
            expected=exp_cum(n,kind,t)
            assert actual==expected,(n,kind,t,actual,expected)
            comps+=1
        print(n,kind,'all_states',sz,'entry_hist',dict(sorted(count.items())))
    print('CHECK_STATES_OK',comps,'cumulative comparisons; 2*(4^3+..+4^8) configurations')
if __name__=='__main__': check()
