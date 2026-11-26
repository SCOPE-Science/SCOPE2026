#!/usr/bin/env python3
"""Exact integer certificate for the seven Petersen boundary-torus types.

Run: python3 verification/verify.py (from the directory containing RESULT.md).
Only the Python standard library is needed.
"""
import itertools
import json
import pathlib

V = list(itertools.combinations(range(5), 2))
E = [(i, j) for i in range(10) for j in range(i + 1, 10)
     if set(V[i]).isdisjoint(V[j])]
TREE = [(0,7), (0,8), (0,9), (1,5), (1,6), (1,9), (2,4), (2,6), (3,4)]
CHORDS = [e for e in E if e not in TREE]
TYPES = [(1,1,1,1,1), (2,1,1,1), (2,2,1), (3,1,1),
         (3,2), (4,1), (5,)]
BLOCKS = {
    (1,1,1,1,1): (1,1,1,1,1,1),
    (2,1,1,1): (2,2,2),
    (2,2,1): (2,2,-1,-1),
    (3,1,1): (3,3),
    (3,2): (6,),
    (4,1): (4,-2),
    (5,): (5,1),
}

def transpose(a):
    return [list(r) for r in zip(*a)]

def matmul(a,b):
    bt=transpose(b)
    return [[sum(x*y for x,y in zip(r,c)) for c in bt] for r in a]

def identity(n):
    return [[int(i==j) for j in range(n)] for i in range(n)]

def det(a):
    """Bareiss exact determinant for square integer matrices."""
    m=[list(r) for r in a]
    n=len(m); denom=1; sign=1
    if n==1:return m[0][0]
    for k in range(n-1):
        if m[k][k]==0:
            p=next((i for i in range(k+1,n) if m[i][k]!=0),None)
            if p is None:return 0
            m[k],m[p]=m[p],m[k];sign=-sign
        piv=m[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                val=m[i][j]*piv-m[i][k]*m[k][j]
                assert val%denom==0
                m[i][j]=val//denom
            m[i][k]=0
        denom=piv
    return sign*m[n-1][n-1]

def path(start,finish):
    adj={i:[] for i in range(len(V))}
    for u,v in TREE:adj[u].append(v);adj[v].append(u)
    todo=[(start,[start])]
    while todo:
        u,p=todo.pop()
        if u==finish:return p
        todo.extend((v,p+[v]) for v in adj[u] if v not in p)
    raise AssertionError('Disconnected spanning tree')

def cycles():
    A=[[0]*len(CHORDS) for _ in E]
    for j,(u,v) in enumerate(CHORDS):
        A[E.index((u,v))][j]=1
        for a,b in zip(path(v,u),path(v,u)[1:]):
            edge=(a,b) if a<b else (b,a)
            A[E.index(edge)][j]+= 1 if a<b else -1
    return A

def action(sigma,A):
    vp=[V.index(tuple(sorted((sigma[i],sigma[j])))) for i,j in V]
    image=[]
    for u,v in E:
        a,b=vp[u],vp[v]
        image.append((E.index((a,b) if a<b else (b,a)), 1 if a<b else -1))
    # The chord coordinates of a graph cycle are its coefficients in the fundamental-cycle basis.
    result=[[0]*6 for _ in range(6)]
    for i,c in enumerate(CHORDS):
        ei=E.index(c)
        for j in range(6):
            result[i][j]=sum(sign*A[old][j] for old,(new,sign) in enumerate(image) if new==ei)
    # Validate the identity on every oriented graph edge, not only the chords.
    for old,(new,sign) in enumerate(image):
        for j in range(6):
            lhs=sign*A[old][j]
            rhs=sum(A[new][k]*result[k][j] for k in range(6))
            assert lhs==rhs
    return result

def sigma_for(typ):
    a=list(range(5));offset=0
    for n in typ:
        cyc=list(range(offset,offset+n));offset+=n
        for j,x in enumerate(cyc):a[x]=cyc[(j+1)%len(cyc)]
    assert offset==5
    return a

def cyclic_block(n):
    if n==1:return [[1]]
    if n==-1:return [[-1]]
    if n>1:return [[int(i==(j+1)%n) for j in range(n)] for i in range(n)]
    n=-n
    # Signed n-cycle; for n=2 it is a 90-degree rotation, eigenvalues ±i.
    return [[(-1 if j==n-1 else 1) if i==(j+1)%n else 0
             for j in range(n)] for i in range(n)]

def blockdiag(ns):
    a=[[0]*sum(abs(n) for n in ns) for _ in range(sum(abs(n) for n in ns))]
    offset=0
    for n in ns:
        b=cyclic_block(n)
        for i in range(abs(n)):
            for j in range(abs(n)):
                a[offset+i][offset+j]=b[i][j]
        offset+=abs(n)
    return a

def cycle_type(sigma):
    seen=set(); lengths=[]
    for i in range(5):
        if i in seen:continue
        x=i;n=0
        while x not in seen:
            seen.add(x);n+=1;x=sigma[x]
        lengths.append(n)
    return tuple(sorted(lengths,reverse=True))

def main():
    assert len(V)==10 and len(E)==15 and len(TREE)==9 and len(CHORDS)==6
    A=cycles()
    for u in range(10):
        for j in range(6):
            assert sum(A[i][j]*((1 if e[0]==u else 0)-(1 if e[1]==u else 0))
                       for i,e in enumerate(E))==0
    assert [A[E.index(e)] for e in CHORDS]==identity(6)
    cert=json.loads((pathlib.Path(__file__).resolve().parent/'certificates.json').read_text(encoding='utf-8'))
    assert set(cert)=={','.join(map(str,t)) for t in TYPES}
    for typ in TYPES:
        M=action(sigma_for(typ),A)
        U=cert[','.join(map(str,typ))]
        assert len(U)==6 and all(len(row)==6 for row in U)
        assert abs(det(U))==1,(typ,det(U))
        C=blockdiag(BLOCKS[typ])
        assert matmul(M,U)==matmul(U,C),typ
        print('type',typ,'determinant',det(U),'integral_blocks',BLOCKS[typ])
    # Completeness: all 120 permutations are accounted for by seven cycle types.
    counts={t:0 for t in TYPES}
    for sigma in itertools.permutations(range(5)):
        typ=cycle_type(sigma)
        assert typ in counts
        M=action(sigma,A)
        assert len(M)==6
        counts[typ]+=1
    assert counts==dict(zip(TYPES,(1,10,15,20,20,30,24))),counts
    # Exact determinants for q=2,3,4,5,7,8,11.
    factors={
        (1,1,1,1,1):lambda q:[q-1]*6,
        (2,1,1,1):lambda q:[q*q-1]*3,
        (2,2,1):lambda q:[q*q-1]*2+[q+1]*2,
        (3,1,1):lambda q:[q**3-1]*2,
        (3,2):lambda q:[q**6-1],
        (4,1):lambda q:[q**4-1,q*q+1],
        (5,):lambda q:[q**5-1,q-1],
    }
    for q in (2,3,4,5,7,8,11):
        for typ in TYPES:
            M=action(sigma_for(typ),A)
            diff=[[q*int(i==j)-M[i][j] for j in range(6)] for i in range(6)]
            order=abs(det(diff));pred=1
            for m in factors[typ](q):pred*=m
            assert order==pred,(q,typ,order,pred)
    print('PETERSEN_SEVEN_INTEGRAL_TORUS_TYPES_OK')

if __name__=='__main__':main()
