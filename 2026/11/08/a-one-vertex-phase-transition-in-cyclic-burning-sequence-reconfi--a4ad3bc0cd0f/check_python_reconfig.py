"""Independent Python set-based construction of strict burning-schedule slide graphs.
Brute-forces ordered source tuples for 2<=k<=4, both square and one-short cycles.
"""
from collections import deque
from itertools import product
from math import factorial

def stats(k,deficit):
    n=k*k-deficit
    balls=[ [{(x+d)%n for d in range(-(k-i-1),k-i)} for x in range(n)]
           for i in range(k)]
    def legal(s):
        if any(min((s[i]-s[j])%n,(s[j]-s[i])%n)<j-i
                for i in range(k) for j in range(i+1,k)):
            return False
        return len(set().union(*(balls[i][s[i]] for i in range(k))))==n
    states={s for s in product(range(n),repeat=k) if legal(s)}
    adj={s:set() for s in states}
    for s in states:
        for i in range(k):
            for step in (-1,1):
                t=list(s); t[i]=(t[i]+step)%n; t=tuple(t)
                if t in states: adj[s].add(t)
    unseen=set(states); sizes=[]
    while unseen:
        u=unseen.pop(); q=deque([u]);size=1
        while q:
            v=q.popleft()
            for w in adj[v] & unseen:
                unseen.remove(w);q.append(w);size+=1
        sizes.append(size)
    sizes.sort()
    expected=n*(factorial(k-1) if deficit==0 else factorial(k))
    assert len(states)==expected
    if deficit==0:
        assert len(sizes)==expected and sizes==[1]*expected
        assert all(not vals for vals in adj.values())
    else:
        assert len(sizes)==factorial(k-1)
        assert sizes==[n*k]*factorial(k-1)
        assert all(len(vals)==2 for vals in adj.values())
    return n,len(states),sum(map(len,adj.values()))//2,len(sizes),sizes[0]

if __name__=='__main__':
    for k in range(2,5):
        for d in (0,1):
            print(k,d,stats(k,d))
    print('PASS independent Python graph census')
