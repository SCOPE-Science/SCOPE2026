#!/usr/bin/env python3
"""Exact integer and polynomial certificates for 16-curve boundary Picard-point groups.

Requires sympy 1.14.0. The Smith algorithm uses only unimodular
operations over Z[t]; specializing t to any prime-power q preserves them.
"""
from itertools import combinations
from sympy import Matrix, eye, Symbol, Poly, ZZ, factor, zeros
from sympy.matrices.normalforms import smith_normal_form

q = Symbol('q')
zero = Poly(0, q, domain=ZZ)
one = Poly(1, q, domain=ZZ)

VERTICES = [('E',i) for i in range(5)] + [ ('L',i,j) for i,j in combinations(range(5),2)] + [('Q',)]
LABELS = {v:i for i,v in enumerate(VERTICES)}
EDGES = []
for a,b in combinations(VERTICES,2):
    meet = (a[0]=='E' and b[0]=='L' and a[1] in b[1:]) or (a[0]=='E' and b[0]=='Q') or (a[0]=='L' and b[0]=='L' and set(a[1:]).isdisjoint(b[1:]))
    if meet: EDGES.append((LABELS[a], LABELS[b]))
EDGE_IDS={e:i for i,e in enumerate(EDGES)}
assert len(VERTICES)==16 and len(EDGES)==40
assert sorted(sum(int(v in edge) for edge in EDGES) for v in range(16))==[5]*16
assert not any((min(a,c),max(a,c)) in EDGE_IDS for a,b in EDGES for x,c in EDGES if x==b)

# Choose the first 15 cycle-free edges, with the remaining 25 as chords.
parent = list(range(16))
def root(x):
    while parent[x]!=x: x=parent[x]
    return x
TREE,CHORDS=[],[]
for j,(a,b) in enumerate(EDGES):
    ra,rb=root(a),root(b)
    if ra==rb: CHORDS.append(j)
    else: parent[ra]=rb;TREE.append(j)
assert len(TREE)==15 and len(CHORDS)==25
B=zeros(16,40)
for j,(a,b) in enumerate(EDGES):
    B[a,j]=-1; B[b,j]=1
BT=B[:,TREE]
F=zeros(40,25)
BTINV=BT[1:,:].inv()
for j,e in enumerate(CHORDS):
    t=-(BTINV * B[1:,e])
    for k,tree_e in enumerate(TREE):F[tree_e,j]=t[k]
    F[e,j]=1
assert all(x.q==1 for x in F)   # integral cycle basis
assert B*F==zeros(16,25)
assert F[CHORDS,:]==eye(25)

def Frobenius_matrix(p):
    def act(v):
        if v[0]=='E':return ('E',p[v[1]])
        if v[0]=='L':return ('L',*sorted([p[v[1]],p[v[2]]]))
        return ('Q',)
    vperm=[LABELS[act(v)] for v in VERTICES]
    P=zeros(40,40)
    for j,(a,b) in enumerate(EDGES):
        aa,bb=vperm[a],vperm[b]
        P[EDGE_IDS[min(aa,bb),max(aa,bb)],j]=1 if aa<bb else -1
    G=(P*F)[CHORDS,:]
    assert P*F==F*G and all(x.q==1 for x in G)
    return G

CYCLES={
    '1^5':[0,1,2,3,4],
    '2 1^3':[1,0,2,3,4],
    '2^2 1':[1,0,3,2,4],
    '3 1^2':[1,2,0,3,4],
    '3 2':[1,2,0,4,3],
    '4 1':[1,2,3,0,4],
    '5':[1,2,3,4,0],
}
# Each polynomial occurs with its multiplicity among the 25 Smith entries.
EXPECTED={
    '1^5':[(q-1,25)],
    '2 1^3':[(1,10),(q-1,5),(q**2-1,10)],
    '2^2 1':[(1,11),(q+1,3),(q**2-1,11)],
    '3 1^2':[(1,16),(q-1,1),(q**3-1,8)],
    '3 2':[(1,20),(q**3-1,1),((q**3-1)*(q+1),1),(q**6-1,3)],
    '4 1':[(1,18),(q**2+1,1),((q**2+1)*(q+1),1),(q**4-1,5)],
    '5':[(1,20),(q**5-1,5)],
}

def polynomial_smith_diagonal(M):
    """Return an exact Z[q]-diagonal from elementary unimodular operations.

    The successful execution is a finite certificate, not polynomial-
    field Smith form: every polynomial quotient is in Z[q], and no
    division by a nonunit is performed as a row/column operation.
    """
    n=M.rows
    A=[[Poly(c,q,domain=ZZ) for c in row] for row in M.tolist()]
    k=0;steps=0
    while k<n:
        nz=[(A[i][j].degree(),max(abs(int(t)) for t in A[i][j].all_coeffs()),i,j)
            for i in range(k,n) for j in range(k,n) if A[i][j]!=zero]
        assert nz, 'unexpected zero remainder'
        _,_,i,j=min(nz)
        A[k],A[i]=A[i],A[k]  # unimodular row swap
        for row in A:row[k],row[j]=row[j],row[k] # unimodular column swap
        if A[k][k].LC()<0:A[k]=[-x for x in A[k]]
        while True:
            steps+=1
            assert steps<1000, 'unbounded polynomial elimination'
            d=A[k][k]
            assert abs(int(d.LC()))==1, 'nonunit leading coefficient'
            again=False
            for i in range(k+1,n):
                a=A[i][k]
                if a==zero:continue
                h,r=a.div(d)
                assert h*d+r==a and all(c in ZZ for c in h.all_coeffs()+r.all_coeffs())
                if h!=zero:
                    for j in range(k,n):A[i][j]-=h*A[k][j]
                if r!=zero:
                    A[k],A[i]=A[i],A[k]
                    again=True;break
            if again:continue
            for j in range(k+1,n):
                a=A[k][j]
                if a==zero:continue
                h,r=a.div(d)
                assert h*d+r==a
                if h!=zero:
                    for i in range(k,n):A[i][j]-=h*A[i][k]
                if r!=zero:
                    for i in range(n):A[i][k],A[i][j]=A[i][j],A[i][k]
                    again=True;break
            if again:continue
            assert all(A[i][k]==zero for i in range(k+1,n))
            assert all(A[k][j]==zero for j in range(k+1,n))
            bad=next(((i,j) for i in range(k+1,n) for j in range(k+1,n)
                      if A[i][j].rem(d)!=zero), None)
            if bad:
                i,j=bad
                for h in range(n):A[k][h]+=A[i][h]
                continue
            k+=1;break
    assert all(A[i][j]==zero for i in range(n) for j in range(n) if i!=j)
    return [Poly(-A[i][i] if A[i][i].LC()<0 else A[i][i],q,domain=ZZ).as_expr() for i in range(n)]

def run():
    for name,p in CYCLES.items():
        G=Frobenius_matrix(p)
        d=1
        seen=set()
        for i in range(5):
            if i not in seen:
                j=i; k=0
                while j not in seen:seen.add(j); j=p[j]; k+=1
                from math import lcm
                d=lcm(d,k)
        assert G**d==eye(25)
        P=polynomial_smith_diagonal(q*eye(25)-G)
        ex=[factor(poly) for poly,num in EXPECTED[name] for _ in range(num)]
        assert len(P)==25 and [factor(t) for t in P]==ex, (name,P,ex)
        for a,b in zip(P,P[1:]):
            assert Poly(b,q,domain=ZZ).rem(Poly(a,q,domain=ZZ))==zero
        # independent exact INTEGER Smith comparisons at several field sizes
        for field_size in (2,3,5,8,11):
            direct=smith_normal_form(field_size*eye(25)-G,domain=ZZ)
            vals=sorted(abs(int(direct[i,i])) for i in range(25))
            expected=sorted(abs(int(poly.subs(q,field_size))) for poly in P)
            assert vals==expected,(name,field_size,vals,expected)
        print(f'{name}: 25 symbolic invariant factors, five integer specializations: OK')
    print('QUARTIC_DEL_PEZZO_ALL_SEVEN_PICARD_POINT_GROUPS_OK')

if __name__=='__main__':run()
