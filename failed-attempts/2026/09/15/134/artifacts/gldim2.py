"""Minimal projective resolutions for shape 4 via matrices over k.
Basis: e0,e1,a,b,c,ba,cb,cba (paths, source->target recorded)."""
import numpy as np

paths=['e0','e1','a','b','c','ba','cb','cba']
src={'e0':0,'e1':1,'a':0,'b':1,'c':0,'ba':1,'cb':0,'cba':0}
tgt={'e0':0,'e1':1,'a':1,'b':0,'c':1,'ba':1,'cb':0,'cba':1}
idx={p:i for i,p in enumerate(paths)}
def rmult(p, q):
    """right multiply path p by arrow-path q (string of arrows or 'e0','e1'); None if 0"""
    if q in ('e0','e1'):
        v=int(q[1])
        return p if tgt[p]==v else None
    # q arrow word
    cur=p
    for nm in q:
        s,t={'a':(0,1),'b':(1,0),'c':(0,1)}[nm]
        if tgt[cur]!=s: return None
        cand = ('' if cur in ('e0','e1') else cur)+nm
        if 'ab' in cand or 'bc' in cand: return None
        cur=cand
    return cur

P0_idx=[idx[p] for p in ['e0','a','c','cb','cba']]
P1_idx=[idx[p] for p in ['e1','b','ba']]
# Endo: Hom(Pi,Pj) = ej A ei
Hom01=[p for p in paths if src[p]==1 and tgt[p]==0]  # e1 A e0: maps P0->P1? f(e0)=e0? use f in e1Ae0
Hom10=[p for p in paths if src[p]==0 and tgt[p]==1]
Hom00=[p for p in paths if src[p]==0 and tgt[p]==0]
Hom11=[p for p in paths if src[p]==1 and tgt[p]==1]
print("Hom(P0,P1)=e1Ae0:",Hom01," Hom(P1,P0)=e0Ae1:",Hom10)
print("Hom(P0,P0):",Hom00," Hom(P1,P1):",Hom11)
# Resolution of S0: P0 --d0--> S0, K0=rad P0 = span{a,c,cb,cba}
# map phi: P1(-|b|) --b--> P0 hits b? b-action: e1|->b? f(e1)=b in e0Ae1? b:1->0 yes.
# Actually minimal: K0/aA ~ cA. Let's build iteratively with graded shifts ignored (ungraded gldim):
# Step1: cover K0 by P1 (+) P0: gen a (top S1) via P1 -b-> P0? right-mult by b: e1->b not in P0 (b starts at 1, P0=paths from 0). WRONG direction.
# Right modules: P0=e0A. maps P1->P0 given by left mult? No: Hom_A(e1A,e0A)=e0Ae1? f(e1)=e0*x*e1... f(e1) in e0A with e1*f=f => f in e0Ae1.
# e0Ae1 = paths 0->1 = {a,c,cba}. So Hom(P1,P0)=span{a,c,cba} (as right mult by those).
# e1Ae0 = paths 1->0 = {b}. So Hom(P0,P1)=span{b}.
# Cover K0=span{a,c,cb,cba}: gen a: P1 --(.a)--> P0 (e1|->a); gen c: P0 --(.c)--> P0 (e0|->c).
# psi: P1(+)P0 -> P0. ker psi = ?
# psi(x,y)=x.a+y.c. x in P1={e1,b,ba}, y in P0.
# x.a: e1.a=a, b.a=ba, ba.a=baa invalid(0 arrows from 1? a starts 0, ba ends 1 -> ba.a=baa composable, nonzero? contains 'aa'? rels only ab,bc so baa NONZERO!) wait baa: b then a then a; t(a)=1,s(a)=0 mismatch -> None. recompute: ba:1->1; a:0->1 needs t(ba)=1 vs s(a)=0 -> None. so (ba).a=0.
# So x.a in {a,ba}. y.c: y in P0, c:0->1; y.c needs t(y)=0: e0.c=c, a.c? t(a)=1 no, c.c? t(c)=1 no, cb.c? t(cb)=0 -> cb.c=cbc: contains 'bc' -> 0, cba.c? t=1 no. So y.c in {c} (plus y=e0 gives c; y with t=0 gives cbc=0).
# surjectivity onto K0: a yes, c yes, cb? cb = c.b: y=b?? b not in P0. y.c gives only c. cb = ? psi(0,?) no; psi(x,0): x.a in{a,ba} no cb. So need third generator: cb has top S0: add P0 --(.cb)--> P0.
# psi2: P1(+)P0(+)P0 -> P0, (x,y,z)|->x.a+y.c+z.cb.
# z.cb: z in P0: e0.cb=cb, a? t=1 no, c? t=1 no, cb.cb? t(cb)=0: cb.cb=cbcb contains bc ->0, cba? t=1 no. So gives cb. cba = z.cb with z=a? no (t(a)=1,s(cb)=0). z=c? t(c)=1 no. x? no. y? y.c in{c}. So cba still missing: cba=c.ba: gen via P1 --(.cba)--> P0? cba in e0Ae1 yes.
# psi3: P1(+)P0(+)P0(+)P1 -> P0. ker?
# This is getting long: chain of gen's a,c,cb,cba with relations among them. Let's just compute Betti numbers by linear algebra iteratively.
from itertools import product as P

def basis_P(i):
    return ['e0','a','c','cb','cba'] if i==0 else ['e1','b','ba']

def hom_basis(i,j):
    # maps Pi->Pj: right mult by paths src i -> tgt j... f(ei)=ei*m*ej? m: i->j
    return [p for p in paths if src[p]==i and tgt[p]==j]

print("hom bases:", {k:hom_basis(*k) for k in [(0,0),(0,1),(1,0),(1,1)]})

def mat_of_map(dom, cod, comps):
    """dom=sum of P's (list of indices), cod similar; comps[(a,b)]=element of e_{cod_b} A e_{dom_a} as dict path->scalar.
    Returns matrix in bases."""
    db=sum([basis_P(i) for i in dom],[])
    cb=sum([basis_P(i) for i in cod],[])
    # track shifts of summands
    doff=[]; s=0
    for i in dom:
        doff.append(s); s+=len(basis_P(i))
    coff=[]; s=0
    for i in cod:
        coff.append(s); s+=len(basis_P(i))
    M=np.zeros((len(cb),len(db)))
    for a,i in enumerate(dom):
        for b,j in enumerate(cod):
            m=comps.get((a,b),{})
            for gk,gi in enumerate([doff[a]+t for t in range(len(basis_P(i)))]):
                # gen g of summand a maps to basis_P(i)[gk]-times-m in Pj
                g=basis_P(i)[gk-doff[a]]
                img=rmult(g if False else (g), 'e0')  # placeholder
                # right multiply path g by m: g in A, m word
                tot={}
                for mp,c in m.items():
                    r=rmult(g,mp)
                    if r is not None: tot[r]=tot.get(r,0)+c
                # express in cod basis
                for rp,c in tot.items():
                    # find in summand b basis
                    try: row=coff[b]+basis_P(j).index(rp)
                    except ValueError: raise Exception(f"image {rp} not in P{j}")
                    M[row,gi]+=c
    return M

# S0 resolution: F0=P0, eps; K0 gens: a (P1), c (P0), cb (P0), cba (P1)
dom=[1,0,0,1]; cod=[0]
comps={(0,0):{'a':1},(1,0):{'c':1},(2,0):{'cb':1},(3,0):{'cba':1}}
M=mat_of_map(dom,cod,comps)
print("M shape",M.shape,"rank",np.linalg.matrix_rank(M))
# kernel basis
u,sig,vt=np.linalg.svd(M)
ker=vt[np.sum(sig>1e-8):]
print("ker dim:",len(ker))
# Minimality: mod out radicals: gens all in rad => minimal. Next Betti = dim ker - (nonminimal part=0) = dim ker.
# ker lives in P1+P0+P0+P1 (dims 3+5+5+3=16), rank M = dim K0 = 4 => ker dim 12.
# Next differential minimal part: project ker onto tops.
# tops: P1 top S1 (1-dim), P0 top S0. ker/rad(ker) dimension = ?
# rad of source = span of non-lazy paths in each summand.
def rad_mask(dom):
    m=[]
    for i in dom:
        for g in basis_P(i):
            m.append(0 if g in ('e0','e1') else 1)
    return np.array(m)
mask=rad_mask(dom)
# reduce ker rows: quotient by rad coords: look at top coords of ker
topcoords=ker[:,mask==0]
print("top coords of ker:\n",np.round(topcoords,3))
print("rank of top projection:",np.linalg.matrix_rank(topcoords,1e-8))
