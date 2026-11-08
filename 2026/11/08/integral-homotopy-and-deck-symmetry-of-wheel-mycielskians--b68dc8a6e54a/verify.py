#!/usr/bin/env python3
"""Exact finite-field checks of wheel double-cover independence complexes.

Run with Python 3 standard library: python verify.py
All assertions operate on independently constructed face sets.
"""
from collections import defaultdict
from math import comb

def wheel_graph(n):
    N=n+1; edges=set()
    for i in range(n):
        a,b=i,(i+1)%n
        edges.add(tuple(sorted((a,b))))
        edges.add((i,n))
    return N,edges

def double_cover(N,edges):
    return 2*N, {tuple(sorted((2*u+s,2*v+1-s))) for u,v in edges for s in (0,1)}

def mycielskian(N,edges,l):
    # l+1 copies of G; copy l preserves original edges,
    # adjacent layers are crossed over original G-edges, and apex at layer 0.
    V=(l+1)*N+1
    F=set()
    for u,v in edges:
        F.add(tuple(sorted((l*N+u,l*N+v))))
        for layer in range(l):
            F.add(tuple(sorted((layer*N+u,(layer+1)*N+v))))
            F.add(tuple(sorted((layer*N+v,(layer+1)*N+u))))
    w=V-1
    for v in range(N):F.add((v,w))
    return V,F

def independent_faces(N,edges):
    adj=[0]*N
    for a,b in edges:
        assert a!=b
        adj[a]|=1<<b;adj[b]|=1<<a
    faces=[[] for _ in range(N+1)]
    def dfs(available, chosen, count):
        if not available:
            faces[count].append(chosen)
            return
        low=available & -available
        v=low.bit_length()-1
        dfs(available^low,chosen,count)
        dfs((available^low)&~adj[v],chosen|low,count+1)
    dfs((1<<N)-1,0,0)
    return faces

def rank_gf2(columns):
    piv={}
    for col in columns:
        v=col
        while v:
            i=v.bit_length()-1
            if i in piv:v^=piv[i]
            else:
                piv[i]=v
                break
    return len(piv)

def reduced_betti(faces):
    ranks=[0]*(len(faces)+1)
    # ranks[k] : C_k -> C_(k-1), C_-1 = F2,
    # corresponds to faces with k+1 vertices. Empty face not used.
    for k in range(1,len(faces)):
        if not faces[k]:continue
        if k==1:
            ranks[k]=1
            continue
        idx={face:i for i,face in enumerate(faces[k-1])}
        columns=[]
        for face in faces[k]:
            x=0;v=face
            while v:
                bit=v&-v;v^=bit
                x^=1<<idx[face^bit]
            columns.append(x)
        ranks[k]=rank_gf2(columns)
    return {k-1:len(faces[k])-ranks[k]-ranks[k+1]
            for k in range(1,len(faces)) if faces[k] and len(faces[k])-ranks[k]-ranks[k+1]}

def cycle_parameters(n):
    t,r=divmod(n,3)
    if r==0:return 2,t-1
    if r==1:return 1,t-1
    return 1,t

def double_cover_parameters(n):
    if n%2:
        return cycle_parameters(2*n)
    count,degree=cycle_parameters(n)
    return count*count,2*degree+1

def model_betti(n,l):
    countA,a=cycle_parameters(n)
    countZ,d=double_cover_parameters(n)
    out=defaultdict(int)
    k,r=divmod(l,3)
    if r==2:
        j=k+1
        for t in range(j+1):out[2*j-1+t*(d-1)]+=comb(j,t)*countZ**t
    elif r==1:
        for t in range(k+1):
            m=comb(k,t)*countZ**t
            out[2*k+1+t*(d-1)]+=m
            out[a+2*k+1+t*(d-1)]+=countA*m
    else:
        for t in range(k+1):
            m=comb(k,t)*countZ**t
            out[2*k+t*(d-1)]+=2*m
            out[a+2*k+t*(d-1)]+=countA*m
    return dict(out)

def main():
    results=[]
    for n in range(5,10):
        N,E=wheel_graph(n)
        V,DE=double_cover(N,E)
        faces=independent_faces(V,DE)
        got=reduced_betti(faces)
        z,d=double_cover_parameters(n)
        expected={1:1}
        expected[d]=expected.get(d,0)+z
        assert got==expected,(n,got,expected)
        results.append((n,sum(map(len,faces)),got))
    # Independently check the general coned-cover splitting for every simple
    # labeled graph with one through four vertices (including isolated nodes).
    cone_cases=0
    for h in range(1,5):
        possible=[(i,j) for i in range(h) for j in range(i+1,h)]
        for mask in range(1<<len(possible)):
            hedges={edge for j,edge in enumerate(possible) if mask>>j&1}
            # The rim double cover and the coned double cover are built separately.
            bN,bE=double_cover(h,hedges)
            base=reduced_betti(independent_faces(bN,bE))
            coneN=h+1
            coneE=hedges|{(i,h) for i in range(h)}
            cN,cE=double_cover(coneN,coneE)
            got=reduced_betti(independent_faces(cN,cE))
            expected=dict(base)
            expected[1]=expected.get(1,0)+1
            assert got==expected,(h,mask,got,expected)
            cone_cases+=1
    # Explicit small Mycielskian cases, independently enumerated.
    for n,l in [(5,0),(5,1),(5,2),(5,3),(6,0),(6,1)]:
        N,E=wheel_graph(n)
        V,ME=mycielskian(N,E,l)
        faces=independent_faces(V,ME)
        got=reduced_betti(faces)
        expected=model_betti(n,l)
        assert got==expected,(n,l,got,expected)
        results.append((f'mu_{l}(W_{n})',sum(map(len,faces)),got))
    for row in results:print(*row)
    print(f'ALL_VERIFY_OK wheel_covers=5 coned_graphs={cone_cases} mycielskians=6')
if __name__=='__main__':main()
