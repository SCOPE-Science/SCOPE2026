from itertools import combinations,product
from collections import Counter,defaultdict
from math import comb

def graph_adj(n,edges):
    A=[0]*n
    for u,v in edges:
        A[u]|=1<<v;A[v]|=1<<u
    return A

def connected(A):
    seen=1;front=1
    while front:
        new=0
        for i in range(len(A)):
            if (front>>i)&1:new|=A[i]
        new &=~seen
        if not new:break
        seen|=new;front=new
    return seen==(1<<len(A))-1

def D2(A):
    n=len(A); result=[]
    for u in range(n):
        for v in range(u+1,n):
            if A[u]>>v&1:continue
            cm=A[u]&A[v]
            if cm: result.append(cm)
    return result

def tmv(A,sel):
    return all(cm & ~sel for cm in D2(A))

def blow(A,sizes):
    offsets=[0]
    for x in sizes:offsets.append(offsets[-1]+x)
    B=[]
    for v in range(len(A)):
        for i in range(sizes[v]):
            z=0
            for w in range(len(A)):
                if w==v or A[v]>>w&1:
                    z|=((1<<sizes[w])-1)<<offsets[w]
            z &=~(1<<(offsets[v]+i))
            B.append(z)
    return B,offsets

def check(A,sizes,with_betti=False):
    B,o=blow(A,sizes); n=len(A);N=len(B)
    basetmv={s for s in range(1<<n) if tmv(A,s)}
    fc=Counter();ff=Counter(); sets=[]
    for s in range(1<<N):
        F=sum((1<<i) for i in range(n) if ((s>>o[i])&((1<<sizes[i])-1))==(1<<sizes[i])-1)
        expected=F in basetmv
        actual=tmv(B,s)
        assert expected==actual,(A,sizes,s,F)
        if actual:
            fc[s.bit_count()]+=1;sets.append(s)
    setset=set(sets)
    for s in sets:
        if all((s|(1<<i)) not in setset for i in range(N) if not (s>>i&1)):
            ff[s.bit_count()]+=1
    predc=Counter();predf=Counter()
    for F in basetmv:
        poly=[1]
        for i,m in enumerate(sizes):
            factor=[0]*(m+1)
            if F>>i&1: factor[m]=1
            else:
                for k in range(m):factor[k]=comb(m,k)
            nxt=[0]*(len(poly)+len(factor)-1)
            for a,x in enumerate(poly):
                for b,y in enumerate(factor):nxt[a+b]+=x*y
            poly=nxt
        for i,c in enumerate(poly):predc[i]+=c
        if not any(((F>>i)&1)==0 and (F|1<<i) in basetmv for i in range(n)):
            z=sum((sizes[i] if not (F>>i&1) else 1) for i in range(n));
            num=1
            for i in range(n):
                if not (F>>i&1):num*=sizes[i]
            predf[sum(sizes)-n+F.bit_count()]+=num
    assert fc==predc,(fc,predc)
    assert ff==predf,(ff,predf)
    if with_betti:
        # sparse vector-rank simplicial chain boundary over F2
        dims={}
        for s in sets:
            if s==0:continue
            dims.setdefault(s.bit_count()-1,[]).append(s)
        maxd=max(dims)
        ranks={}
        for d in range(1,maxd+1):
            prev={s:i for i,s in enumerate(dims.get(d-1,[]))}
            pivot={}
            for s in dims.get(d,[]):
                val=0;z=s
                while z:
                    bit=z&-z;z-=bit
                    val ^= (1<<prev[s^bit])
                while val:
                    p=val.bit_length()-1
                    if p not in pivot: pivot[p]=val;break
                    val^=pivot[p]
            ranks[d]=len(pivot)
        b={d:len(faces)-ranks.get(d,0)-ranks.get(d+1,0) for d,faces in dims.items()}
        b[0]=b.get(0,0)-1
        assert all(x>=0 for x in b.values())
        return N,len(sets),fc,ff,{d:x for d,x in b.items() if x}
    return N,len(sets),fc,ff

def all_dists(A):
    n=len(A); ds=[]
    for u in range(n):
        d=[-1]*n;d[u]=0;front=1<<u;depth=0
        while front:
            nxt=0
            for v in range(n):
                if front>>v&1:nxt |= A[v]
            nxt &= sum(1<<v for v in range(n) if d[v]<0)
            depth+=1
            for v in range(n):
                if nxt>>v&1:d[v]=depth
            front=nxt
        ds.append(d)
    return ds

def direct_shortest_visibility(A,sel,ds):
    n=len(A)
    for u in range(n):
        for v in range(u+1,n):
            if ds[u][v]==1:continue
            visited=1<<u; front=1<<u;dist=0
            allowed=((1<<n)-1)&~sel | (1<<u) | (1<<v)
            while front and not (visited>>v&1):
                z=0
                for k in range(n):
                    if front>>k&1:z|=A[k]
                front=z&allowed&~visited
                visited |=front;dist+=1
            if not (visited>>v&1) or dist!=ds[u][v]:return False
    return True

def direct_profiles():
    profiles=[(cycle(4),(2,)*4),(cycle(5),(2,)*5),(cycle(4),(3,)*4),
              (graph_adj(4,[(0,1),(1,2),(2,3)]),(2,)*4)]
    checked=0
    for A,sz in profiles:
        B,_=blow(A,sz);ds=all_dists(B)
        for s in range(1<<len(B)):
            assert direct_shortest_visibility(B,s,ds)==tmv(B,s),(A,sz,s)
            checked+=1
    return checked

def cycle(n):return graph_adj(n,[(i,(i+1)%n) for i in range(n)])

def main():
    profiles=0; tested=0; facets=0; examples=[]
    for n in range(2,6):
      for bits in range(1<<(n*(n-1)//2)):
        pairs=list(combinations(range(n),2))
        A=graph_adj(n,[p for j,p in enumerate(pairs) if bits>>j&1])
        if not connected(A):continue
        # equal and nonuniform blowup; max order 10
        sizeslist=[(2,)*n,tuple(2+(i==0) for i in range(n))] if n<=4 else [(2,)*n]
        for sizes in sizeslist:
          if sum(sizes)>10:continue
          res=check(A,sizes)
          profiles+=1;tested+=2**res[0];facets+=sum(res[3].values())
    for n,m in [(3,2),(4,2),(4,3),(5,2),(6,2),(7,2)]:
        N,ct,fc,ff,betti=check(cycle(n),(m,)*n,True)
        expect={} if n==3 else ({4*m-3:1} if n==4 else {n*(m-1)-1:1})
        assert betti==expect,(n,m,betti,expect)
        examples.append((n,m,N,ct,sum(ff.values()),betti))
    print('VERIFY_OK direct_geodesic_subsets',direct_profiles(),'profiles',profiles,'tested_subsets',tested,'facets',facets,'cycle_profiles',examples)
if __name__=='__main__':main()
