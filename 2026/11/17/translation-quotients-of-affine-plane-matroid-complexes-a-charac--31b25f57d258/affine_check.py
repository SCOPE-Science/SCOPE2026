"""Exact barycentric orbit-chain checks for affine-plane independence quotients.

No external datasets. Finite models here corroborate an independently stated general proof.
"""
import itertools
from collections import defaultdict
from math import comb
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ


def compute(q, smith=True):
    if q not in (2, 3, 4, 5):
        raise ValueError('supported test field orders: 2, 3, 4, 5')
    def add(a,b):
        return a^b if q==4 else (a+b)%q
    def neg(a):
        return a if q==4 else (-a)%q
    def sub(a,b):
        return add(a,neg(b))
    def mul(a,b):
        if q!=4: return (a*b)%q
        a0,a1=a&1,(a>>1)&1; b0,b1=b&1,(b>>1)&1
        return (a0*b0 ^ a1*b1) | (((a0*b1) ^ (a1*b0) ^ (a1*b1))<<1)
    pts=list(range(q*q))
    coords=lambda i:(i//q,i%q)
    toind=lambda x,y:x*q+y
    trans=[(u,v) for u in range(q) for v in range(q)]
    translate=lambda i,t:toind(add(coords(i)[0],t[0]),add(coords(i)[1],t[1]))
    def noncol(a,b,c):
        x1,y1=coords(a);x2,y2=coords(b);x3,y3=coords(c)
        d=sub(mul(sub(x2,x1),sub(y3,y1)),mul(sub(y2,y1),sub(x3,x1)))
        return d!=0
    faces=[(i,) for i in pts]+list(itertools.combinations(pts,2)) + [z for z in itertools.combinations(pts,3) if noncol(*z)]
    face_set=set(faces)
    index={f:j for j,f in enumerate(faces)}
    edges=[]
    for f in faces:
        for g in faces:
            if len(g)==len(f)+1 and set(f).issubset(g): edges.append((f,g))
            if len(f)==1 and len(g)==3 and set(f).issubset(g): edges.append((f,g))
    flags=[]
    for f in faces:
        if len(f)!=3:continue
        for e in itertools.combinations(f,2):
            for v in e:flags.append(((v,),e,f))
    def norm(flag):
        return min(tuple(tuple(sorted(translate(i,t) for i in f)) for f in flag) for t in trans)
    rep=[{norm((f,)) for f in faces},{norm(e) for e in edges},{norm(z) for z in flags}]
    cells=[sorted(x) for x in rep]
    ix=[{f:i for i,f in enumerate(cells[k])} for k in range(3)]
    B1=sp.zeros(len(cells[0]),len(cells[1]))
    for i,edge in enumerate(cells[1]):
        v1=ix[0][norm((edge[0],))]; v2=ix[0][norm((edge[1],))]
        B1[v2,i]+=1;B1[v1,i]-=1
    B2=sp.zeros(len(cells[1]),len(cells[2]))
    for i,flag in enumerate(cells[2]):
        for j in range(3):
            e=flag[:j]+flag[j+1:]
            B2[ix[1][norm(e)],i]+=(-1)**j
    assert B1*B2==sp.zeros(B1.rows,B2.cols)
    parent=list(range(len(cells[0])))
    def root(i):
        while parent[i]!=i:
            i=parent[i]
        return i
    tree=set()
    for j,edge in enumerate(cells[1]):
        a,b=[ix[0][norm((f,))] for f in edge]
        ra,rb=root(a),root(b)
        if ra!=rb:
            parent[ra]=rb;tree.add(j)
    assert len(tree)==len(cells[0])-1
    rest=[i for i in range(len(cells[1])) if i not in tree]
    reduced=B2[rest,:]
    if smith:
        d=smith_normal_form(reduced,domain=ZZ)
        diag=[abs(int(d[i,i])) for i in range(min(d.rows,d.cols)) if d[i,i]!=0]
        rank=len(diag)
        H1=[v for v in diag if v>1]
        H1_free=len(rest)-rank
        H2=len(cells[2])-rank
    else:
        rank=reduced.rank()
        H1=[];H1_free=len(rest)-rank;H2=len(cells[2])-rank
    expected_h2=q*(q-1)**2*(q+1)//6 if q%2==0 else (q-1)*(q+1)*(q*q-q-3)//6
    expect_H1=[] if q%2==0 else [q//3 if q%3==0 else q]*0 # intentionally not used
    print(f'q={q} original_faces={[sum(len(f)==k for f in faces) for k in (1,2,3)]} quotient_flag_cells={[len(x) for x in cells]} rank_delta2={rank} H1torsion={H1} H1free={H1_free} H2rank={H2} predictedH2={expected_h2}',flush=True)
    assert H1_free==0 and H2==expected_h2
    if q==2 or q==4: assert H1==[]
    if q==3: assert H1==[3,3]
    if q==5: assert H1==[5,5]
    return cells,B1,B2

if __name__=='__main__':
    for q in (2,3,4): compute(q)
    print('AFFINE_PLANE_TRANSLATION_QUOTIENT_CHECK_PASS q=2,3,4')
