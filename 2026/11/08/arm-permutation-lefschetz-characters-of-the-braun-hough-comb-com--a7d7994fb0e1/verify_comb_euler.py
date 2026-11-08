#!/usr/bin/env python3
"""Reproduce signed simplicial Lefschetz traces of arm-permuting comb complexes.
All computations use exact integer arithmetic and finite exhaustive enumeration.
"""
from itertools import permutations
from collections import Counter
from functools import lru_cache

def graph(n,m):
    assert n>=0 and m>=1
    V=[('a',0,0),('b',0,0)]+[('z',k,0) for k in range(1,n+1)]+[('p',k,j) for j in range(m) for k in range(1,n+2)]
    ix={v:i for i,v in enumerate(V)}
    adj=[0]*len(V)
    def edge(x,y):
        i,j=ix[x],ix[y]
        assert i!=j
        adj[i]|=1<<j;adj[j]|=1<<i
    for j in range(m):
        edge(('a',0,0),('p',1,j));edge(('b',0,0),('p',n+1,j))
        for k in range(1,n+1):
            edge(('p',k,j),('p',k+1,j))
            edge(('z',k,0),('p',k,j));edge(('z',k,0),('p',k+1,j))
    return V,adj

def expected(n,m,perm):
    cycles=0; unseen=set(range(m))
    while unseen:
        cycles+=1;i=next(iter(unseen))
        while i in unseen:
            unseen.remove(i);i=perm[i]
    E=[1,-2,1]
    for k in range(3,n+1):E.append(E[k-3]-E[k-2]-E[k-1])
    return E[n] if cycles%2==0 else (0 if n%2 else (-1)**(n//2))

def independent_faces(adj):
    out=[];full=(1<<len(adj))-1
    def rec(left,chosen):
        if not left:
            out.append(chosen);return
        b=left&-left;i=b.bit_length()-1
        rec(left^b,chosen)
        rec(left &~(b|adj[i]),chosen|b)
    rec(full,0)
    return out

def action(V,perm):
    ix={v:i for i,v in enumerate(V)}
    p=[]
    for v in V:
        if v[0]=='p':v=('p',v[1],perm[v[2]])
        p.append(ix[v])
    return p

def signed_simplex_lefschetz(faces,p):
    total=-1 # augmented empty simplex contributes (-1)^(-1)=-1
    for face in faces:
        if not face:continue
        a=[i for i in range(len(p)) if face & (1<<i)]
        transformed=[p[i] for i in a]
        if set(transformed)!=set(a):continue
        inversions=sum(transformed[i]>transformed[j] for i in range(len(a)) for j in range(i+1,len(a)))
        total+=(-1)**(len(a)-1+inversions)
    return total

def transfer_check():
    T=[[0,-1,-1,1],[1,0,-1,0],[1,-1,0,0],[1,0,0,0]]
    v=[1,0,0,0]
    sequence={}
    for power in range(31):
        if power>=2:sequence[power-2]=-v[0]
        v=[sum(v[i]*T[i][j] for i in range(4)) for j in range(4)]
    assert [sequence[k] for k in range(7)]==[1,-2,1,2,-5,4,3]
    for n in range(3,29):assert sequence[n]==sequence[n-3]-sequence[n-2]-sequence[n-1],(n,sequence[n])
    return sequence

def main():
    seq=transfer_check()
    total_classes=0;total_faces=0;detailed=[]
    for n,m in [(0,2),(1,2),(2,2),(3,2),(4,2),(5,2),
                (0,3),(1,3),(2,3),(3,3),(4,3),
                (0,4),(1,4),(2,4),(3,4),
                (0,5),(1,5),(2,5)]:
        V,adj=graph(n,m)
        faces=independent_faces(adj)
        for pp in permutations(range(m)):
            actual=signed_simplex_lefschetz(faces,action(V,pp))
            want=expected(n,m,pp)
            assert actual==want,(n,m,pp,actual,want)
            total_classes+=1
        if n==2:
            for pp in permutations(range(m)):
                inv=sum(pp[i]>pp[j] for i in range(m) for j in range(i+1,m))
                sign=(-1)**inv
                actual=signed_simplex_lefschetz(faces,action(V,pp))
                assert actual==(-1)**m*sign
        total_faces+=len(faces)
        detailed.append(f'n={n} m={m} vertices={len(V)} independent_sets={len(faces)} permutations={1 if m==1 else __import__("math").factorial(m)}')
    print('EXACT_TRANSFER_VALUES_0_TO_11',','.join(str(seq[k]) for k in range(12)))
    print('GRAPH_FAMILY_TESTS',len(detailed))
    print('PERMUTATION_CHARACTER_CHECKS',total_classes)
    print('ENUMERATED_INDEPENDENT_SETS',total_faces)
    print('\n'.join(detailed))
    print('ALL_COMB_EQUIVARIANT_EULER_CHECKS_PASS')
if __name__=='__main__':main()
