"""Reproducible direct-graph checks for induced-forest sets of cycle clique blowups."""
from collections import Counter
from itertools import product
from math import comb, ceil

def acyclic(mask, edges, nv):
    parent=list(range(nv))
    def find(v):
        while parent[v]!=v:
            v=parent[v]
        return v
    for u,v in edges:
        if (mask>>u)&(mask>>v)&1:
            x,y=find(u),find(v)
            if x==y: return False
            parent[x]=y
    return True

def direct(n,m):
    nv=n*m
    edges=[(i,j) for i in range(nv) for j in range(i+1,nv)
           if i//m==j//m or (i//m-j//m)%n in (1,n-1)]
    valid=[]
    for mask in range(1<<nv):
        if acyclic(mask,edges,nv):valid.append(mask)
    validset=set(valid)
    f=Counter(); g=Counter()
    for mask in valid:
        k=mask.bit_count();f[k]+=1
        if all((mask>>v)&1 or mask|(1<<v) not in validset for v in range(nv)):
            g[k]+=1
    return f,g,len(valid),len(g)

def formula(n,m):
    a=comb(m,2)
    weights={0:{0:1},1:{1:m},2:{2:a}}
    f=Counter();g=Counter()
    for w in product((0,1,2),repeat=n):
        if any((w[i]==2 and w[(i+1)%n]!=0) or (w[i]!=0 and w[(i+1)%n]==2) for i in range(n)):
            continue
        if set(w)=={1}:continue
        k=w.count(1)+2*w.count(2)
        count=m**w.count(1)*a**w.count(2)
        f[k]+=count
        if (0 in w and w.count(0)==1 and w.count(1)==n-1) or (2 in w and all(
                ((w[(i-1)%n]==0 and w[(i+1)%n]==0) if v==2 else
                 (w[(i-1)%n]==1 or w[(i+1)%n]==1) if v==1 else
                 (w[(i-1)%n]==2 or w[(i+1)%n]==2))
                for i,v in enumerate(w))):
            g[k]+=count
    return f,g

if __name__=='__main__':
    tested=0; masks=0;maximal=0
    for n,m in [(4,2),(5,2),(6,2),(7,2),(8,2),(4,3),(5,3),(4,4)]:
        d,e,t,_=direct(n,m)
        f,g=formula(n,m)
        assert f==d,(n,m,'forest',f,d)
        assert g==e,(n,m,'facet',g,e)
        print('GRAPH_OK',n,m,'sets',t,'facets',sum(e.values()),'facet_sizes',sorted(e))
        tested+=1;masks+=1<<(n*m);maximal+=sum(e.values())
    for n in range(4,12):
        _,g=formula(n,2)
        low = min(n-1,2*ceil(n/3))
        high = n if n%2==0 else n-1
        assert min(g)==low and max(g)==high,(n,g)
        assert (len(g)==1)==(n in (5,7)),(n,g)
    print('VERIFY_OK direct_graph_profiles',tested,'candidate_masks',masks,'facets',maximal,'cyclic_counts_and_purity=PASS')

def gap_formula(n,m):
    """Independently enumerate cyclic gap compositions with a marked doubled fiber."""
    a=comb(m,2)
    out=Counter({n-1: n*m**(n-1)})
    def gaps(k,r,typ,ones):
        if k==0:
            if r==0:
                yield typ,ones
            return
        for j in range(1,r+1):
            if j==3: continue
            if j>=4: yield from gaps(k-1,r-j,typ+(j,),ones+j-2)
            elif j in (1,2): yield from gaps(k-1,r-j,typ+(j,),ones)
    for k in range(1,n//2+1):
        tmp=Counter()
        for typ,ones in gaps(k,n-k,(),0):
            tmp[2*k+ones]+=m**ones * a**k
        for size,count in tmp.items():
            assert (n*count)%k == 0
            out[size]+=n*count//k
    return out

if __name__=='__main__':
    checked=0
    for n in range(4,12):
        for m in range(2,5):
            _,g=formula(n,m)
            c=gap_formula(n,m)
            assert g==c, (n,m,g,c)
            checked+=1
    print('GAP_FORMULA_OK profiles',checked)
