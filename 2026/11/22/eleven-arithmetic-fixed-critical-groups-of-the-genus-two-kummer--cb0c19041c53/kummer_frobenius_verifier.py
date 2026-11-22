"""Exact arithmetic replay for Frobenius-fixed critical groups of the Kummer node--trope graph.
Run: python3 kummer_frobenius_verifier.py kummer_frobenius_certificate.json
Python 3 standard library only; no network or external packages.
"""
import sys, json, math, itertools
from collections import Counter

def model():
    labels=set(range(6)); pairs=list(itertools.combinations(range(6),2)); ns=[()]+pairs
    ts=[('odd',i) for i in range(6)]+[('even',t) for t in itertools.combinations(range(6),3) if 0 in t]
    B=[]
    for nd in ns:
        B.append([int((not nd or t in nd) if typ=='odd' else
                      bool(nd) and (set(nd)<=set(t) or set(nd)<=labels-set(t)))
                  for typ,t in ts])
    assert all(sum(r)==6 for r in B)
    assert all(sum(B[i][j] for i in range(16))==6 for j in range(16))
    for i in range(16):
        for j in range(16):
            assert sum(B[i][k]*B[j][k] for k in range(16))==(6 if i==j else 2)
    L=[[0]*32 for _ in range(32)]
    for i in range(16):
        L[i][i]=6;L[i+16][i+16]=6
        for j in range(16): L[i][j+16]=-B[i][j];L[j+16][i]=-B[i][j]
    assert all(sum(row)==0 for row in L)
    return ns,ts,B,[row[:31] for row in L[:31]]

def action(parts,ns,ts):
    perm=list(range(6)); k=0
    for z in parts:
        cyc=list(range(k,k+z));k+=z
        for a,b in zip(cyc,cyc[1:]+cyc[:1]): perm[a]=b
    assert k==6
    def canon(t):
        t=tuple(sorted(t));return t if 0 in t else tuple(sorted(set(range(6))-set(t)))
    pno=[ns.index(tuple(sorted(perm[i] for i in nd))) for nd in ns]
    pto=[16+ts.index((typ,perm[t] if typ=='odd' else canon(perm[i] for i in t))) for typ,t in ts]
    p=pno+pto
    assert sorted(p)==list(range(32))
    return p

def presentation(parts,ns,ts,B,M):
    p=action(parts,ns,ts)
    for i in range(16):
        for j in range(16): assert B[i][j]==B[p[i]][p[16+j]-16]
    return [M[i]+[int(p[j]==i)-int(p[31]==i)-int(i==j) for j in range(31)] for i in range(31)]

def replay(A,ops):
    A=[r[:] for r in A];n=len(A);m=len(A[0]);
    for inst in ops:
        op,i=inst[:2]
        if op=='rs':
            j=inst[2];assert 0<=i<n and 0<=j<n and i!=j
            A[i],A[j]=A[j],A[i]
        elif op=='cs':
            j=inst[2];assert 0<=i<m and 0<=j<m and i!=j
            for row in A: row[i],row[j]=row[j],row[i]
        elif op=='ra':
            j,c=inst[2:];assert i!=j and 0<=i<n and 0<=j<n and c
            for h in range(m):A[i][h]+=c*A[j][h]
        elif op=='ca':
            j,c=inst[2:];assert i!=j and 0<=i<m and 0<=j<m and c
            for row in A:row[i]+=c*row[j]
        elif op=='rf': A[i]=[-u for u in A[i]]
        else:raise ValueError('invalid elementary operation')
    return A

def verify(z):
    assert z['certificate_version']==1 and len(z['cases'])==11
    ns,ts,B,M=model()
    assert len(M)==31 and len(M[0])==31
    seen=[]
    for case in z['cases']:
        parts=tuple(case['cycle_partition']);seen.append(parts)
        H=presentation(parts,ns,ts,B,M)
        diagonal=case['diagonal']
        assert len(diagonal)==31 and all(type(u)==int and u>0 for u in diagonal)
        assert all(diagonal[i+1]%diagonal[i]==0 for i in range(30))
        assert replay(H,case['elementary_operations'])==[[diagonal[i] if i==j else 0 for j in range(62)] for i in range(31)]
        assert math.prod(diagonal)==int(case['order'])
        assert dict(sorted(Counter(u for u in diagonal if u>1).items()))=={int(k):v for k,v in case['nonunit_invariants'].items()}
    assert seen==[(1,1,1,1,1,1),(2,1,1,1,1),(2,2,1,1),(2,2,2),(3,1,1,1),(3,2,1),(3,3),(4,1,1),(4,2),(5,1),(6,)]
    assert int(z['cases'][0]['order'])==3*2**72
    print('KUMMER_FROBENIUS_ALL_ELEVEN_INTEGRAL_FIXED_GROUPS_OK')

if __name__=='__main__':
    with open(sys.argv[1],encoding='utf-8') as f:z=json.load(f)
    verify(z)
