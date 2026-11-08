"""Direct graph dynamics, independent of linear algebra, n=2..6, F_2.
Runs without third-party dependencies: python verify_labelled.py
"""
from collections import Counter

def neighbor_list(n):
    ne=[[] for _ in range(2*n)]
    for side in range(2):
        for j in range(n):
            v=side*n+j
            ne[v].append((1-side)*n+j)
            if j>0:ne[v].append(side*n+j-1)
            if j+1<n:ne[v].append(side*n+j+1)
    return ne

def tick(x,ne):
    z=0
    for v,adj in enumerate(ne):
        if sum((x>>j)&1 for j in adj)%2:z|=1<<v
    return z

def params(n):
    if (n+1)%3:return 0
    k=n+1; v=0
    while k%2==0:k//=2; v+=1
    return 2**(v+1)

def main():
    total=0
    for n in range(2,7):
        ne=neighbor_list(n); obs=Counter()
        for x in range(1<<(2*n)):
            seen={};y=x
            while y not in seen:
                if len(seen)>=(1<<(2*n))+1: raise AssertionError('cycle not found')
                seen[y]=len(seen);y=tick(y,ne)
            t=seen[y];period=len(seen)-t
            obs[t]+=1;total+=1
        m=params(n)
        theory=Counter({0:2**(2*n-2*m)})
        for t in range(1,m+1):theory[t]=2**(2*n-2*m)*(2**(2*t)-2**(2*(t-1)))
        assert obs==theory,(n,obs,theory)
        print('n=',n,'state_count=',1<<(2*n),'entry_histogram=',dict(sorted(obs.items())))
    print('PASS direct orbits over',total,'labelled initial configurations')
if __name__=='__main__':main()
