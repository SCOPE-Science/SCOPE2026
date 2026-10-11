#!/usr/bin/env python3
from fractions import Fraction
from itertools import product, combinations
import heapq

def edges(n):
    return list(combinations(range(n),2))

def share(e,f):
    return len(set(e)&set(f))==1

def prufer_tree(seq,n):
    deg=[1]*n
    for x in seq:
        deg[x]+=1
    leaves=[i for i,d in enumerate(deg) if d==1]
    heapq.heapify(leaves)
    out=[]
    for x in seq:
        leaf=heapq.heappop(leaves)
        out.append(tuple(sorted((leaf,x))))
        deg[leaf]-=1
        deg[x]-=1
        if deg[x]==1:
            heapq.heappush(leaves,x)
    a=heapq.heappop(leaves); b=heapq.heappop(leaves)
    out.append(tuple(sorted((a,b))))
    return out

def covariance_formula(n):
    es=edges(n); m=len(es)
    C=[[Fraction(0) for _ in range(m)] for __ in range(m)]
    for i,e in enumerate(es):
        for j,f in enumerate(es):
            if i==j:
                C[i][j]=Fraction(2*(n-2),n*n)
            elif share(e,f):
                C[i][j]=Fraction(-1,n*n)
    return es,C

def precision_entry(n,root,e,f):
    Ae=share(root,e); Af=share(root,f)
    if e==f:
        return Fraction(n*(n+1 if Ae else n+2),n-1)
    sf=share(e,f)
    if Ae and Af:
        return Fraction(n*(n+1) if sf else n*n,2*(n-1))
    if Ae != Af:
        return Fraction(n*(n+2) if sf else n*(n+1),2*(n-1))
    return Fraction(n*(n+3) if sf else n*(n+2),2*(n-1))

def matmul(A,B):
    n=len(A); p=len(B); m=len(B[0])
    out=[[Fraction(0) for _ in range(m)] for __ in range(n)]
    for i in range(n):
        for k in range(p):
            if A[i][k]:
                a=A[i][k]
                for j in range(m):
                    if B[k][j]:
                        out[i][j]+=a*B[k][j]
    return out

def run():
    trees_enumerated=0
    one_edge_checks=0
    two_edge_checks=0
    covariance_checks=0
    product_entries=0
    partial_orbit_checks=0

    for n in range(3,8):
        es=edges(n); idx={e:i for i,e in enumerate(es)}
        single=[0]*len(es); pair=[[0]*len(es) for _ in es]
        total=n**(n-2)
        for seq in product(range(n),repeat=n-2):
            tr=prufer_tree(seq,n)
            ids=[idx[e] for e in tr]
            trees_enumerated+=1
            for i in ids:
                single[i]+=1
            for a,b in combinations(ids,2):
                pair[a][b]+=1; pair[b][a]+=1
        for i,e in enumerate(es):
            assert Fraction(single[i],total)==Fraction(2,n)
            one_edge_checks+=1
            for j in range(i+1,len(es)):
                f=es[j]
                expected=Fraction(3,n*n) if share(e,f) else Fraction(4,n*n)
                assert Fraction(pair[i][j],total)==expected
                two_edge_checks+=1
        _,C=covariance_formula(n)
        p=Fraction(2,n)
        for i,e in enumerate(es):
            assert C[i][i]==p*(1-p)
            covariance_checks+=1
            for j in range(i+1,len(es)):
                f=es[j]
                joint=Fraction(3,n*n) if share(e,f) else Fraction(4,n*n)
                assert C[i][j]==joint-p*p
                covariance_checks+=1

    for n in range(4,13):
        es,C=covariance_formula(n)
        root=es[0]; keep=list(range(1,len(es)))
        Cr=[[C[i][j] for j in keep] for i in keep]
        P=[[precision_entry(n,root,es[i],es[j]) for j in keep] for i in keep]
        M=matmul(Cr,P)
        for i in range(len(M)):
            for j in range(len(M)):
                assert M[i][j]==(1 if i==j else 0)
                product_entries+=1
        for ai,i in enumerate(keep):
            e=es[i]; de=P[ai][ai]
            for bj in range(ai+1,len(keep)):
                j=keep[bj]; f=es[j]; df=P[bj][bj]; pef=P[ai][bj]
                assert pef>0
                sq=Fraction(pef*pef,de*df)
                Ae=share(root,e); Af=share(root,f); sf=share(e,f)
                if Ae and Af and sf:
                    expected=Fraction(1,4)
                elif Ae and Af and not sf:
                    expected=Fraction(n*n,4*(n+1)*(n+1))
                elif Ae != Af and sf:
                    expected=Fraction(n+2,4*(n+1))
                elif Ae != Af and not sf:
                    expected=Fraction(n+1,4*(n+2))
                elif (not Ae) and (not Af) and sf:
                    expected=Fraction((n+3)*(n+3),4*(n+2)*(n+2))
                else:
                    expected=Fraction(1,4)
                assert sq==expected
                partial_orbit_checks+=1

    print("VERIFY_OK "
          f"trees_enumerated={trees_enumerated} "
          f"one_edge_checks={one_edge_checks} "
          f"two_edge_checks={two_edge_checks} "
          f"covariance_checks={covariance_checks} "
          f"product_entries={product_entries} "
          f"partial_orbit_checks={partial_orbit_checks}")

if __name__=="__main__":
    run()
