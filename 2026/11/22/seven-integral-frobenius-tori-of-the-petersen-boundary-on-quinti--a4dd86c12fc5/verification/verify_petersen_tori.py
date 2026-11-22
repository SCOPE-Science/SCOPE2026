#!/usr/bin/env python3
"""Exact integral Frobenius torus certificates for the ten-line quintic del Pezzo boundary.
Uses SymPy; all 7 conjugacy classes checked, no probabilistic steps.
"""
import itertools
from collections import Counter,deque
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

PARTS=[(1,1,1,1,1),(1,1,1,2),(1,1,3),(1,2,2),(1,4),(2,3),(5,)]
VERTICES=list(itertools.combinations(range(5),2))
EDGES=[(i,j) for i,j in itertools.combinations(range(10),2) if set(VERTICES[i]).isdisjoint(VERTICES[j])]
TREE=[(0,7),(0,8),(0,9),(1,5),(1,6),(1,9),(2,4),(2,6),(3,4)]
NONTREE=[e for e in EDGES if e not in set(TREE)]
assert len(EDGES)==15 and len(NONTREE)==6
NEIGH={i:[] for i in range(10)}
for i,j in TREE:NEIGH[i].append(j);NEIGH[j].append(i)
def path(start,end):
    q=deque([(start,[start])]);seen={start}
    while q:
        x,p=q.popleft()
        if x==end:return p
        for y in NEIGH[x]:
            if y not in seen:seen.add(y);q.append((y,p+[y]))
    raise AssertionError('not tree')
def fundamental_basis():
    cycles=[]
    for i,j in NONTREE:
        col=[0]*15;col[EDGES.index((i,j))]=1
        p=path(j,i)
        for a,b in zip(p,p[1:]):col[EDGES.index(tuple(sorted((a,b))))]+=1 if a<b else -1
        cycles.append(sp.Matrix(col))
    B=sp.Matrix.hstack(*cycles)
    incidence=sp.zeros(10,15)
    for k,(i,j) in enumerate(EDGES):incidence[i,k]=-1;incidence[j,k]=1
    assert incidence*B==sp.zeros(10,6)
    assert B[[EDGES.index(e) for e in NONTREE],:]==sp.eye(6)
    return B
BGRAPH=fundamental_basis();CHORDROWS=[EDGES.index(e) for e in NONTREE]
def permutation(part):
    perm=[];start=0
    for c in part:
        perm += [start+(i+1)%c for i in range(c)];start+=c
    return tuple(perm)
def graph_action(perm):
    pvert=[VERTICES.index(tuple(sorted(perm[x] for x in pair))) for pair in VERTICES]
    medge=sp.zeros(15,15)
    pedge=[]
    for k,(i,j) in enumerate(EDGES):
        a,b=pvert[i],pvert[j];w=EDGES.index(tuple(sorted((a,b))))
        pedge.append(w);medge[w,k]=1 if a<b else -1
    A=(medge*BGRAPH)[CHORDROWS,:]
    assert BGRAPH*A==medge*BGRAPH
    inc=[(e,v) for e,(i,j) in enumerate(EDGES) for v in (i,j)]
    pinc=[inc.index((pedge[e],pvert[v])) for e,v in inc]
    return A,pvert,pedge,pinc
# Certificate matrix columns are integral basis vectors of H_1(Petersen,Z).
CERTIFICATES={
(1,1,1,1,1):sp.eye(6),
(1,1,1,2):sp.Matrix([[-1,0,0,1,-1,0],[1,-1,-1,-1,1,0],[0,-1,1,0,0,-1],[1,1,1,1,0,0],[-1,-1,0,-1,0,-1],[-1,-1,-1,0,-1,0]]),
(1,1,3):sp.Matrix([[-1,0,0,1,1,0],[0,1,-1,1,0,0],[0,-1,0,0,1,1],[1,-1,1,-1,-1,0],[1,1,-1,0,-1,-1],[-1,1,1,-1,0,-1]]),
(1,2,2):sp.Matrix([[0,1,1,-1,0,1],[1,0,-1,1,0,-1],[-1,0,-1,2,1,-1],[0,0,-1,-1,0,0],[0,0,-1,1,-1,-1],[1,-1,0,0,1,0]]),
(1,4):sp.Matrix([[-1,-2,2,1,-1,0],[1,-1,-2,2,0,-1],[0,0,0,-1,0,0],[-1,1,1,-1,0,1],[-1,1,-1,1,0,0],[1,1,-1,-1,1,0]]),
(2,3):sp.Matrix([[1,-1,0,0,0,0],[0,0,0,0,-1,0],[0,0,0,0,1,-1],[-1,0,0,0,0,1],[0,0,0,1,-1,0],[0,1,-1,0,0,0]]),
(5,):sp.Matrix([[1,1,0,1,1,1],[-1,1,0,0,0,0],[1,0,1,0,1,1],[0,-1,0,-1,-1,-1],[-1,0,-1,-1,-1,-1],[0,0,0,1,-1,0]])
}
def cycle_mat(n):
    M=sp.zeros(n,n)
    for j in range(n):M[(j+1)%n,j]=1
    return M
def canonical(part):
    if part==(1,1,1,1,1):return sp.eye(6)
    if part==(1,1,1,2):return sp.diag(*(cycle_mat(2) for _ in range(3)))
    if part==(1,1,3):return sp.diag(cycle_mat(3),cycle_mat(3))
    if part==(1,2,2):return sp.diag(cycle_mat(2),cycle_mat(2),sp.Matrix([[-1]]),sp.Matrix([[-1]]))
    if part==(1,4):return sp.diag(cycle_mat(4),sp.Matrix([[0,-1],[1,0]]))
    if part==(2,3):return cycle_mat(6)
    if part==(5,):return sp.diag(cycle_mat(5),sp.Matrix([[1]]))
def cycle_lengths(p):
    unseen=set(range(len(p)));out=[]
    while unseen:
        start=min(unseen);j=start;d=0
        while j in unseen:unseen.remove(j);d+=1;j=p[j]
        out.append(d)
    return tuple(sorted(out))
def multiplicities(p):return {str(k):v for k,v in sorted(Counter(cycle_lengths(p)).items())}
def group_order(part,q):
    return {
      (1,1,1,1,1):(q-1)**6,(1,1,1,2):(q*q-1)**3,
      (1,1,3):(q**3-1)**2,(1,2,2):(q*q-1)**2*(q+1)**2,
      (1,4):(q**4-1)*(q*q+1),(2,3):q**6-1,
      (5,):(q-1)*(q**5-1)
    }[part]
def point_count_D(pv,pe,pi,q):return (q+1)*sum(i==x for i,x in enumerate(pv))+sum(i==x for i,x in enumerate(pe))-sum(i==x for i,x in enumerate(pi))
def point_count_U(part,pv,pe,pi,q):return q*q+1+q*sum(i==x for i,x in enumerate(permutation(part)))-point_count_D(pv,pe,pi,q)
def verify():
    report=[]
    for part in PARTS:
        A,pv,pe,pi=graph_action(permutation(part));U=CERTIFICATES[part]
        assert U.det() in (1,-1), (part,'nonunimodular',U.det())
        assert A*U==U*canonical(part), (part,'intertwiner mismatch')
        assert sp.factor((sp.Symbol('t')*sp.eye(6)-A).det())==sp.factor((sp.Symbol('t')*sp.eye(6)-canonical(part)).det())
        for q in (2,3,4,5,7,8,9,11,16,17,19):
            assert (q*sp.eye(6)-A).det()==group_order(part,q)
            assert smith_normal_form(q*sp.eye(6)-A,domain=ZZ).diagonal()==smith_normal_form(q*sp.eye(6)-canonical(part),domain=ZZ).diagonal()
        assert len(pv)==10 and len(pe)==15 and len(pi)==30
        assert sorted(sum(1 for i,x in enumerate(v) if i==x) for v in (pv,pe,pi))
        # Test exact D and U formulas at powers 1..6 of Frobenius, including branch-reversal nodes.
        pp=permutation(part)
        for n in range(1,7):
            pnp=tuple(pp[i] for i in range(5))
            for _ in range(n-1):pnp=tuple(pp[i] for i in pnp)
            _,pv2,pe2,pi2=graph_action(pnp)
            for q in (2,3,5):
                Q=q**n
                f=sum(i==j for i,j in enumerate(pnp));v=sum(i==j for i,j in enumerate(pv2));e=sum(i==j for i,j in enumerate(pe2));h=sum(i==j for i,j in enumerate(pi2))
                assert point_count_D(pv2,pe2,pi2,Q)==(Q+1)*v+e-h
                assert Q*Q+1+Q*f-((Q+1)*v+e-h)>=0
        report.append({'partition':list(part),'determinant':int(U.det()),
            'characteristic_polynomial':str(sp.factor((sp.Symbol('t')*sp.eye(6)-A).det())),
            'vertex_cycles':multiplicities(pv),'node_cycles':multiplicities(pe),'branch_cycles':multiplicities(pi),
            'boundary_Fq_polynomial':[sum(i==j for i,j in enumerate(pv)),sum(i==j for i,j in enumerate(pv))+sum(i==j for i,j in enumerate(pe))-sum(i==j for i,j in enumerate(pi))],
            'open_Fq_polynomial':[1,sum(i==j for i,j in enumerate(permutation(part)))-sum(i==j for i,j in enumerate(pv)),1-sum(i==j for i,j in enumerate(pv))-sum(i==j for i,j in enumerate(pe))+sum(i==j for i,j in enumerate(pi))]})
    print('PETERSEN_SEVEN_INTEGRAL_TORI_VERIFIED')
    return report
if __name__=='__main__':
    import json
    print(json.dumps(verify(),separators=(',',':')))
