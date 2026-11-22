"""Independent exact checks for the generalized-theta tree Fourier theorem.
Only finite tests: arbitrary parameter theorems require the accompanying proof.
"""
import itertools
from math import comb,prod
from collections import Counter

def graph(lengths):
    edges=[]
    target=1
    next_v=2
    for length in lengths:
        prev=0
        for j in range(length):
            if j==length-1: end=target
            else: end=next_v; next_v+=1
            edges.append((prev,end)); prev=end
    return edges,next_v

def independent_tree_mask(edges,vertices,indices):
    parent=list(range(vertices))
    def find(x):
        while x!=parent[x]:
            parent[x]=parent[parent[x]];x=parent[x]
        return x
    for i in indices:
        a,b=edges[i]; ra,rb=find(a),find(b)
        if ra==rb:return None
        parent[ra]=rb
    if len({find(v) for v in range(vertices)})!=1:return None
    return sum(1<<i for i in indices)

def direct_transform(lengths):
    edges,v=graph(lengths);m=len(edges)
    assert v==m-len(lengths)+2
    indicator=[0]*(1<<m)
    for indices in itertools.combinations(range(m),v-1):
        mask=independent_tree_mask(edges,v,indices)
        if mask is not None: indicator[mask]=1
    count=sum(indicator)
    f=indicator[:]
    for j in range(m):
        jump=1<<j
        for p in range(0,len(f),2*jump):
            for t in range(jump):
                x,y=f[p+t],f[p+t+jump]
                f[p+t],f[p+t+jump]=x+y,x-y
    return f,count

def formula(freq,lengths):
    chunks=[];pos=0
    for ell in lengths:
        sub=(freq>>pos)&((1<<ell)-1)
        chunks.append(ell-2*sub.bit_count());pos+=ell
    z=sum(__import__('math').prod(chunks[:i]+chunks[i+1:]) for i in range(len(chunks)))
    return (-1 if freq.bit_count()%2 else 1)*z

def compressed_multiplicities(lengths):
    answer=Counter()
    for js in itertools.product(*(range(ell+1) for ell in lengths)):
        u=[ell-2*j for ell,j in zip(lengths,js)]
        e=sum(prod(u[:i]+u[i+1:]) for i in range(len(u)))
        sign=(-1)**(sum(js))
        answer[sign*e]+=prod(comb(ell,j) for ell,j in zip(lengths,js))
    return answer

def asserted_gap(lengths):
    k=len(lengths);s=sum(t%2==0 for t in lengths)
    if s==0:return 1 if k%2 else 2
    if s==1:return 1
    return 2**(s-1)

def claimed_invertible(lengths):
    k=len(lengths);odd=k-sum(t%2==0 for t in lengths)
    return odd==k-1 or (odd==k and k%2==1)

def run():
    test=[]
    for k in (3,4,5):
        for lengths in itertools.product((2,3,4),repeat=k):
            if sum(lengths)<=12:test.append(lengths)
    test.extend([(2,2,2,2,2,2),(3,3,3,3),(3,3,3,3,3),(2,2,2,2,3),(2,2,2,3,3),(2,2,3,3,3),(2,3,3,3,3),(2,2,2,2,2,3)])
    results=[]
    for lengths in test:
        f,count=direct_transform(lengths)
        for freq,actual in enumerate(f):
            expect=formula(freq,lengths)
            assert actual==expect,(lengths,freq,actual,expect)
        assert count==sum(prod(lengths[:i]+lengths[i+1:]) for i in range(len(lengths)))
        assert Counter(f)==compressed_multiplicities(lengths)
        assert sum(v*v for v in f)==len(f)*count
        rank=sum(v!=0 for v in f)
        assert (rank==len(f))==claimed_invertible(lengths),(lengths,rank)
        nonzero=min(abs(v) for v in f if v)
        assert nonzero==asserted_gap(lengths),(lengths,nonzero,asserted_gap(lengths))
        assert max(map(abs,f))==count
        results.append((lengths,len(f),rank,len(f)-rank,nonzero))
    for sample in [(2,2,2),(2,2,3),(2,3,3),(3,3,3),(2,2,2,2),(3,3,3,3),(2,2,3,3,3)]:
        print('SAMPLE',next((x for x in results if x[0]==sample),None))
    print('THETA_GENERALIZED_SPECTRUM_PASS',len(results),'cases; all exact FWHT entries; ranks and sharp gaps')
if __name__=='__main__':run()
