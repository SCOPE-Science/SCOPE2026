#!/usr/bin/env python3
"""Exact finite checks for higher independence complexes of generalized friendship graphs.
The construction enumerates induced components directly, then computes simplicial
boundary ranks and signed Lefschetz numbers for graph automorphisms.
"""
from math import comb


def graph_faces(k,s,r):
    n=1+k*s
    edges={(0,j) for j in range(1,n)}
    for h in range(k):
        block=range(1+s*h,1+s*(h+1))
        edges|={(i,j) for i in block for j in block if i<j}
    faces=set()
    for mask in range(1<<n):
        unseen={i for i in range(n) if (mask>>i)&1}
        good=True
        while unseen:
            vertex=unseen.pop();stack=[vertex];size=0
            while stack:
                u=stack.pop();size+=1
                for v in tuple(unseen):
                    if (min(u,v),max(u,v)) in edges:
                        unseen.remove(v);stack.append(v)
            if size>r:good=False;break
        if good:faces.add(mask)
    return faces,n


def rank_mod2(columns):
    piv={}
    for c in columns:
        while c:
            p=c.bit_length()-1
            if p in piv:c^=piv[p]
            else:piv[p]=c;break
    return len(piv)


def reduced_betti(faces,n):
    faces_by_size=[[f for f in faces if f.bit_count()==j] for j in range(n+1)]
    ranks=[]
    for sz in range(1,n+1):
        ids={f:i for i,f in enumerate(faces_by_size[sz-1])}
        cols=[]
        for f in faces_by_size[sz]:
            c=0
            for v in range(n):
                if f>>v&1:c^=1<<ids[f^(1<<v)]
            cols.append(c)
        ranks.append(rank_mod2(cols))
    return [len(faces_by_size[d+1])-ranks[d]-(ranks[d+1] if d+1<n else 0) for d in range(n)]


def char_wedge_augmentation(perm,q):
    n=len(perm);seen=set();p=[1]
    for i in range(n):
        if i in seen:continue
        x=i;length=0
        while x not in seen:seen.add(x);length+=1;x=perm[x]
        other=[0]*(len(p)+length)
        for j,a in enumerate(p):
            other[j]+=a;other[j+length]+=(-1)**(length+1)*a
        p=other
    value=0
    for i in range(q+1):value=p[i]-value
    return value


def auto(k,s,kind):
    n=1+k*s;p=list(range(n))
    if kind=='leafswap' and s>=2:p[1],p[2]=p[2],p[1]
    elif kind=='blockswap' and k>=2:
        for i in range(s):p[1+i],p[1+s+i]=1+s+i,1+i
    elif kind=='withinall' and s>=2:
        for h in range(k):p[1+h*s],p[2+h*s]=2+h*s,1+h*s
    return p


def high_character(k,s,r,g):
    # trace on tensor of k exterior-power augmentation modules, accounting
    # for the degree-r Koszul sign when whole simplex blocks are swapped.
    blockperm=[(g[1+i*s]-1)//s for i in range(k)]
    seen=set();out=1
    for h in range(k):
        if h in seen:continue
        cycle=[];x=h
        while x not in seen:
            seen.add(x);cycle.append(x);x=blockperm[x]
        length=len(cycle)
        charmap=[]
        for j in range(s):
            v=1+s*h+j
            for _ in range(length):v=g[v]
            assert (v-1)//s==h
            charmap.append((v-1)%s)
        out*=((-1)**(r*(length-1)))*char_wedge_augmentation(charmap,r)
    return out


def lefschetz(faces,n,p):
    ans=-1
    for f in faces:
        if f==0:continue
        v=[j for j in range(n) if f>>j&1];w=[p[j] for j in v]
        if set(v)!=set(w):continue
        inv=sum(w[i]>w[j] for i in range(len(w)) for j in range(i+1,len(w)))
        ans+=(-1)**(len(v)-1+inv)
    return ans


def run():
    ncases=0; ncharacters=0; nmod2=0
    for k in range(2,5):
        for s in range(2,5):
            if 1+k*s>11:continue
            for r in range(1,2+k*s):
                fs,n=graph_faces(k,s,r);ncases+=1
                bt=reduced_betti(fs,n);nmod2+=1
                want=[0]*n
                m=k*s
                if r==1:
                    want[0]=1
                    want[k-1]=(s-1)**k
                elif 2<=r<=m:
                    want[r-1]=comb(m-1,r-1)
                    if r<s:want[k*r-1]=comb(s-1,r)**k
                assert bt==want,(k,s,r,bt,want)
                for kind in ('identity','leafswap','blockswap','withinall'):
                    p=auto(k,s,kind)
                    got=lefschetz(fs,n,p)
                    bottom=0;top=0
                    if r==1:
                        bottom=1
                        top=high_character(k,s,1,p)
                        predicted=bottom+(-1)**(k-1)*top
                    elif 2<=r<=m:
                        leafperm=[p[i]-1 for i in range(1,n)]
                        bottom=char_wedge_augmentation(leafperm,r-1)
                        if r<s:top=high_character(k,s,r,p)
                        predicted=(-1)**(r-1)*bottom+((-1)**(k*r-1)*top if r<s else 0)
                    else:predicted=0
                    assert got==predicted,(k,s,r,kind,got,predicted)
                    ncharacters+=1
    print(f'ALL_VERIFY_OK parameters={ncases} mod2_homology={nmod2} equivariant_lefschetz_checks={ncharacters}')

if __name__=='__main__':run()
