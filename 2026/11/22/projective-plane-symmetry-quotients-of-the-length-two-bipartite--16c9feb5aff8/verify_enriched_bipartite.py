#!/usr/bin/env python3
"""Independent finite checks for the length-two enriched nerve of a complete bipartite graph.
All sequences are ordered nondegenerate simplices. The quotient uses orbit-normalized
ordered simplices, not an unordered or flag Vietoris-Rips complex.
"""
from itertools import product
from collections import defaultdict
from sympy import Matrix
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

def d(a,b,x,y):
    if x==y:return 0
    return 1 if ((x<a)!=(y<a)) else 2

def cells(a,b):
    n=a+b
    C=[[(x,) for x in range(n)],[],[]]
    for x,y in product(range(n), repeat=2):
        if x!=y and d(a,b,x,y)<=2:C[1].append((x,y))
    for x,y,z in product(range(n), repeat=3):
        if x!=y and y!=z and d(a,b,x,y)+d(a,b,y,z)<=2:C[2].append((x,y,z))
    return C

def canon(t,a,swap=False):
    def sidecanonical(seq):
        buckets=[{},{}]; out=[]
        for x in seq:
            side=0 if x<a else 1
            xkey=x if side==0 else x-a
            if xkey not in buckets[side]:buckets[side][xkey]=len(buckets[side])
            out.append((side,buckets[side][xkey]))
        return tuple(out)
    p=sidecanonical(t)
    if swap:
        return min(p,tuple((1-s,i) for s,i in p))
    return p

def quotient_cells(a,b,mode):
    C=cells(a,b)
    if mode=='none':return C,lambda t:t
    f=lambda t:canon(t,a,mode=='full')
    return [sorted({f(t) for t in D}) for D in C],f

def boundary(a,b,mode,source,target,key):
    R={t:i for i,t in enumerate(target)}
    M=[[0 for _ in source] for _ in target]
    # Each chosen orbit representative is sufficient as the action commutes with faces.
    raw=cells(a,b)
    inv={k:next(t for t in raw[len(k)-1] if key(t)==k) for k in source}
    for j,orb in enumerate(source):
        t=inv[orb]
        for i in range(len(t)):
            f=t[:i]+t[i+1:]
            if len(f)>1 and any(f[z]==f[z+1] for z in range(len(f)-1)):continue
            k=key(f)
            M[R[k]][j]+=(-1)**i
    return Matrix(M)

def rank_modp(A,p):
    B=[[int(A[i,j])%p for j in range(A.cols)] for i in range(A.rows)]
    r=0
    for c in range(A.cols):
        piv=next((i for i in range(r,A.rows) if B[i][c]%p),None)
        if piv is None:continue
        B[r],B[piv]=B[piv],B[r]
        z=pow(B[r][c],-1,p)
        for j in range(c,A.cols):B[r][j]=B[r][j]*z%p
        for i in range(r+1,A.rows):
            z=B[i][c]
            if z:
                for j in range(c,A.cols):B[i][j]=(B[i][j]-z*B[r][j])%p
        r+=1
        if r==A.rows:break
    return r

def check(a,b,mode):
    if mode=='full' and a!=b:return
    C,key=quotient_cells(a,b,mode)
    B1=boundary(a,b,mode,C[1],C[0],key)
    B2=boundary(a,b,mode,C[2],C[1],key)
    assert B1*B2==Matrix.zeros(len(C[0]),len(C[2]))
    r1=rank_modp(B1,101);r2=rank_modp(B2,101)
    h0=len(C[0])-r1;h1=len(C[1])-r1-r2;h2=len(C[2])-r2
    if mode=='none':
        assert [h0,h1,h2]==[1,0,a*b*(a+b)-(a+b-1)**2]
    elif mode=='parts':assert [h0,h1,h2]==[1,0,1]
    else:assert [h0,h1,h2]==[1,0,0]
    # mod two catches quotient torsion: RP2 acquires one H1 and H2 class.
    r12=rank_modp(B1,2);r22=rank_modp(B2,2)
    hm2=[len(C[0])-r12,len(C[1])-r12-r22,len(C[2])-r22]
    assert hm2==([1,1,1] if mode=='full' else [h0,h1,h2])
    print((a,b),mode,'cells',tuple(map(len,C)),'H_Q',(h0,h1,h2),'H_F2',tuple(hm2))

if __name__=='__main__':
    for a,b in [(1,1),(1,2),(2,2),(2,3),(3,3),(3,4)]:
        for mode in ['none','parts']+(['full'] if a==b else []):check(a,b,mode)
    print('ALL CHECKS PASSED')
