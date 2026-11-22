"""Exact finite checks for rectangular matched-defect bipartite closed-neighborhood complexes.

Standard library only. Run: python3 verify.py
This script corroborates examples; the unbounded theorem is proved separately.
"""
from itertools import permutations, combinations, product

def graph(m,k):
    n=2*m+k
    A=range(m); B=range(m,n)
    adj=[set() for _ in range(n)]
    for i in A:
        for j in B:
            if j==m+i: continue
            adj[i].add(j); adj[j].add(i)
    return adj

def closed_neighborhood_faces(adj):
    n=len(adj)
    S={0}
    for v in range(n):
        vs=sorted({v}|adj[v]); a=len(vs)
        for z in range(1,1<<a):
            mask=0
            for idx in range(a):
                if z>>idx & 1: mask|=1<<vs[idx]
            S.add(mask)
    return S

def hemispheres(adj,m):
    def union_neigh(centers):
        s={0}
        for v in centers:
            vs=sorted({v}|adj[v]); a=len(vs)
            for z in range(1,1<<a):
                mask=0
                for idx in range(a):
                    if z>>idx & 1: mask|=1<<vs[idx]
                s.add(mask)
        return s
    return union_neigh(range(m)),union_neigh(range(m,len(adj)))

def bitrank(vecs):
    piv={}
    for v in vecs:
        while v:
            p=v.bit_length()-1
            if p in piv: v^=piv[p]
            else:
                piv[p]=v
                break
    return len(piv)

def betti(faces):
    f={}
    for mask in faces:
        if mask:
            d=mask.bit_count()-1;f.setdefault(d,[]).append(mask)
    for d in f: f[d].sort()
    ranks={}
    for d in sorted(f):
        if d==0: ranks[d]=0;continue
        lo={v:i for i,v in enumerate(f[d-1])}
        cols=[]
        for mask in f[d]:
            v=0
            x=mask
            while x:
                b=x&-x;x-=b
                v ^=1<<lo[mask^b]
            cols.append(v)
        ranks[d]=bitrank(cols)
    return {d:len(f[d])-ranks.get(d,0)-ranks.get(d+1,0) for d in f}

def sign_of_perm(items):
    return -1 if sum(items[i]>items[j] for i in range(len(items)) for j in range(i+1,len(items)))%2 else 1

def signed_lefschetz(faces,perm):
    total=0
    for mask in faces:
        if mask==0:continue
        orig=[i for i in range(len(perm)) if mask>>i&1]
        dest=[perm[i] for i in orig]
        if set(dest)!=set(orig):continue
        sign=sign_of_perm(dest)
        total += (-1)**(len(orig)-1)*sign
    return total

def test(m,k):
    adj=graph(m,k);n=len(adj)
    x=closed_neighborhood_faces(adj)
    U,V=hemispheres(adj,m)
    assert x==U|V
    G={0}|{1<<i for i in range(n)}
    edges=0
    for a in range(m):
        for b in adj[a]:
            G.add((1<<a)|(1<<b));edges+=1
    assert U & V==G
    B=betti(x)
    rank=edges-n+1
    assert B.get(0)==1 and all((d==0 and v==1) or (d==2 and v==rank) or (v==0) for d,v in B.items()),(m,k,B,rank)
    assert B.get(2,0)==rank
    return x,rank

def check_char(m,k,faces):
    num=0
    for sigma in permutations(range(m)):
        for tau in permutations(range(k)):
            pp=[0]*(2*m+k)
            for i in range(m):pp[i]=sigma[i];pp[m+i]=m+sigma[i]
            for j in range(k):pp[2*m+j]=2*m+tau[j]
            f=sum(i==sigma[i] for i in range(m))
            e=sum(j==tau[j] for j in range(k))
            expected=f*f+f*e-3*f-e+1
            actual=signed_lefschetz(faces,pp)-1
            assert actual==expected,(m,k,sigma,tau,actual,expected)
            num+=1
    return num

if __name__=='__main__':
    runs=0; groupchecks=0
    for m in range(3,6):
        for k in range(1,4):
            X,rank=test(m,k)
            runs+=1
            if m<=4 and k<=3: groupchecks +=check_char(m,k,X)
            print('m=%d k=%d faces=%d beta2=%d' %(m,k,len(X)-1,rank))
    print('VERIFIED finite homology instances:',runs)
    print('VERIFIED automorphism traces:',groupchecks)
    print('ALL CHECKS PASSED')

# Endpoint controls for the missing-matching graph before an extra universal vertex is added.
for m in (4,5,6):
    old_faces=closed_neighborhood_faces(graph(m,0))
    old=betti(old_faces)
    expected={2:m*m-3*m+1}
    expected[m-2]=expected.get(m-2,0)+2
    assert all(old.get(d,0)==r for d,r in expected.items()),(m,old,expected)
    assert all(v==0 for d,v in old.items() if d not in ({0}|set(expected))),old
    print('balanced-control m=%d beta=%s' %(m,{d:v for d,v in old.items() if v and d}))
print('BALANCED ENDPOINT CHECKS PASSED')
