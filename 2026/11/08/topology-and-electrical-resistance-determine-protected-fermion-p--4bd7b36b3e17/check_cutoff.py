"""Exhaustive graph-structure check of minimal full-capture monitoring on small complete networks."""
from itertools import combinations

def comps(n,edges):
    p=list(range(n))
    def root(a):
        while p[a]!=a:
            p[a]=p[p[a]];a=p[a]
        return a
    for a,b in edges:p[root(a)]=root(b)
    return len({root(a) for a in range(n)})

def main():
    for n in range(2,7):
        edges=list(combinations(range(n),2));N=len(edges);best=N+1;ex=[]
        for bitset in range(1<<N):
            F={edges[j] for j in range(N) if bitset>>j&1}
            bar=set(edges)-F
            b1=len(bar)-n+comps(n,bar)
            dim=b1+comps(n,F)-1
            if dim==0:
                if len(F)<best:best=len(F);ex=[F]
                elif len(F)==best and len(ex)<2:ex.append(F)
        target=1 if n==2 else 2 if n==3 else N-n+1
        assert best==target,(n,best,target)
        print(f'n={n}; possible loss sets={1<<N}; minimum full-capture loss pairs={best}; verified witness count>={len(ex)}')
if __name__=='__main__':main()
