"""Corrected: maps between right projectives act by LEFT concat: f(g)=m*g.
m in e_{cod} A e_{dom}."""
import numpy as np
paths=['e0','e1','a','b','c','ba','cb','cba']
src={'e0':0,'e1':1,'a':0,'b':1,'c':0,'ba':1,'cb':0,'cba':0}
tgt={'e0':0,'e1':1,'a':1,'b':0,'c':1,'ba':1,'cb':0,'cba':1}
def lmult(m,g):
    if m in ('e0','e1'):
        v=int(m[1]); return g if src[g]==v else None
    if g in ('e0','e1'):
        v=int(g[1]); return m if tgt[m]==v else None
    if tgt[m]!=src[g]: return None
    cand=m+g
    if 'ab' in cand or 'bc' in cand: return None
    return cand
def basis_P(i): return ['e0','a','c','cb','cba'] if i==0 else ['e1','b','ba']
def hom_basis(i,j): return [p for p in paths if src[p]==i and tgt[p]==j]
def mat_of_map(dom,cod,comps):
    db=sum([basis_P(i) for i in dom],[]); cb=sum([basis_P(i) for i in cod],[])
    doff=[];s=0
    for i in dom: doff.append(s);s+=len(basis_P(i))
    coff=[];s=0
    for i in cod: coff.append(s);s+=len(basis_P(i))
    M=np.zeros((len(cb),len(db)))
    for a,i in enumerate(dom):
        for b,j in enumerate(cod):
            m=comps.get((a,b),{})
            for t,g in enumerate(basis_P(i)):
                gi=doff[a]+t
                for mp,c in m.items():
                    r=lmult(mp,g)
                    if r is None: continue
                    row=coff[b]+basis_P(j).index(r)
                    M[row,gi]+=c
    return M
# verify candidates: P1 -a-> P0: m='a' in e0Ae1 ✓; P0 -c-> P0: m='c'? c in e0Ae0? c:0->1 no! c NOT in e0Ae0.
# gen c of K0: c in P0; cover by P0 via m in e0Ae0 with m*e0=c? m*e0=m, so need m=c, but c doesn't end at 0. NOT a map P0->P0.
# Instead cover c (top at 1? c:0->1 ends at 1, so c*e1=c, top S1) via P1 -c-> P0 with m='c' in e0Ae1 ✓.
# gens of K0=rad P0=span{a,c,cb,cba}: tops: a ends 1 (S1), c ends 1 (S1), cb ends 0 (S0), cba ends 1 (S1).
# cover: P1(-a), P1(-c), P0(-cb? m='cb' in e0Ae0 ✓), P1(-cba).
dom=[1,1,0,1]; cod=[0]
comps={(0,0):{'a':1},(1,0):{'c':1},(2,0):{'cb':1},(3,0):{'cba':1}}
M=mat_of_map(dom,cod,comps)
print("M rank:",np.linalg.matrix_rank(M),"shape:",M.shape)
# images: col0 (e1 summand): e1->a, b->ab=0, ba->aba? contains ab ->0. col for P0 summand (m=cb): e0->cb, a->cba, c->ccb? t(c)=1 vs s(cb)=0 ->None... wait lmult(cb,c): tgt(cb)=0,src(c)=0 -> cand 'cbc' contains 'bc' -> None. cb->cbcb None. cba: tgt(cb)=0, src(cba)=0 -> 'cbcba' bc->None.
u,sig,vt=np.linalg.svd(M)
r=np.sum(sig>1e-8); ker=vt[r:]
print("ker dim:",len(ker),"= 16-4 =",16-4)
# minimality + next Betti: project ker onto tops of source summands
mask=[]
for i in dom:
    for g in basis_P(i): mask.append(0 if g in ('e0','e1') else 1)
mask=np.array(mask)
topcoords=ker[:,mask==0]
print("rank of top projection (next Betti number):",np.linalg.matrix_rank(topcoords,1e-8))
print(np.round(topcoords,2))
# relations: find explicit kernel vectors with top components
