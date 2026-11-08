"""Exhaustive bounded-state verification of the two-cycle mass theorem; stdlib only."""
from itertools import product
from collections import Counter

def adj_from_mask(n, mask):
    adj=[[] for _ in range(n)]
    t=0
    for i in range(n):
        for j in range(i+1,n):
            if mask >> t & 1:
                adj[i].append(j);adj[j].append(i)
            t+=1
    return adj

def connected(adj):
    seen={0}; stack=[0]
    while stack:
        for j in adj[stack.pop()]:
            if j not in seen: seen.add(j);stack.append(j)
    return len(seen)==len(adj)

def update(x, adj,deg):
    f=[int(x[v]>=deg[v]) for v in range(len(x))]
    return tuple(x[v]-deg[v]*f[v]+sum(f[w] for w in adj[v]) for v in range(len(x)))

def predicted(adj,deg):
    n=len(adj); E=sum(deg)//2; out=Counter();maxcut=0; ordered_max=0
    for mask in range(1<<n):
        cross=[sum(((mask>>v)&1)!=((mask>>w)&1) for w in adj[v]) for v in range(n)]
        if not all(cross):continue
        cut=sum(cross)//2
        if cut>maxcut:maxcut=cut;ordered_max=0
        if cut==maxcut:ordered_max+=1
        L=2*E-cut
        coeff=[1]
        for c in cross:
            new=[0]*(len(coeff)+c-1)
            for i,a in enumerate(coeff):
                for k in range(c):new[i+k]+=a
            coeff=new
        for i,a in enumerate(coeff):out[L+i]+=a
    assert min(out)==2*E-maxcut
    assert max(out)==2*E+maxcut-n
    assert out[min(out)]==out[max(out)]==ordered_max
    assert all(out[k]>0 for k in range(min(out),max(out)+1))
    return out

def main():
    graphs=0;states=0;cycles=0
    for n in range(2,6):
        for mask in range(1<<(n*(n-1)//2)):
            adj=adj_from_mask(n,mask)
            if not connected(adj):continue
            deg=[len(a) for a in adj]
            want=predicted(adj,deg)
            got=Counter()
            for x in product(*(range(2*d) for d in deg)):
                states+=1
                y=update(x,adj,deg)
                z=update(y,adj,deg)
                if z==x and y!=x:
                    got[sum(x)]+=1;cycles+=1
            assert want==got,(n,mask,want,got)
            graphs+=1
    print(f'EXHAUSTIVE_OK graphs={graphs} bounded_states={states} primitive_two_states={cycles}')
if __name__=='__main__':main()
