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
ARROWS=['a','b','c']
def coords_info(F):
    offs=[];s=0
    for i in F: offs.append(s);s+=len(basis_P(i))
    return offs
def free_dim(F): return sum(len(basis_P(i)) for i in F)
def act_matrix(F,m):
    offs=coords_info(F); d=free_dim(F)
    A=np.zeros((d,d))
    for a,i in enumerate(F):
        for t,g in enumerate(basis_P(i)):
            r=lmult(m,g)
            if r is None: continue
            for b,j in enumerate(F):
                if j==src[r]:
                    A[offs[b]+basis_P(j).index(r), offs[a]+t]+=1
                    break
    return A
F=[1,1,0,1]; offs=coords_info(F); d=free_dim(F)
# map F1->P0: col per gen of F1: gen of summand a maps to m_a * g
ms=['a','c','cb','cba']
cod_basis=basis_P(0)
A=np.zeros((len(cod_basis), d))
for a,i in enumerate(F):
    for t,g in enumerate(basis_P(i)):
        r=lmult(ms[a],g)
        if r is None: continue
        A[cod_basis.index(r), offs[a]+t]+=1
print("A rank:",np.linalg.matrix_rank(A),"shape:",A.shape)
u,ss,vv=np.linalg.svd(A); rr=np.sum(ss>1e-8)
K=vv[rr:].copy()
print("K dim:",K.shape)
# check K is submodule: A_m v in row-space(K)?
for m in ARROWS:
    Am=act_matrix(F,m)
    for v in K:
        w=Am@v
        # is w in row space of K? project
        kk,sss,vvv=np.linalg.svd(K)
        r2=np.sum(sss>1e-8)
        coeff=(w@vv[:r2].T)@vv[:r2]
        if np.linalg.norm(coeff-w)>1e-6:
            print(f"NOT submodule: arrow {m}, residual {np.linalg.norm(coeff-w):.3f}")
            break
    else: continue
    break
else: print("K is a submodule OK")
# JK dim
JK=np.array([act_matrix(F,m)@v for m in ARROWS for v in K])
print("rank K:",np.linalg.matrix_rank(K,1e-8),"rank JK:",np.linalg.matrix_rank(JK,1e-8))
# Nakayama check: iterate J^n K dims
cur=K.copy()
for n in range(1,7):
    nxt=np.array([act_matrix(F,m)@v for m in ARROWS for v in cur])
    print(f"rank J^{n}K:",np.linalg.matrix_rank(nxt,1e-8) if len(nxt) else 0)
# Tor2 via tops: F1/JF1 map to F0/JF0 is zero (minimal) so Tor2 dim = #summands F1 = 4?
# Tor2 = H2 of F.\otimes S: (F1/JF1 -> F0/JF0 -> S -> 0): ker = F1/JF1 (map zero), im of next unknown.
# So b2 >= ... need F2. True b2 = dim ker(top1) - ... = 4 - 0? No: complex F2/JF2 -> F1/JF1 -> F0/JF0: H = ker(d1)/im(d2). d1=0 so H=4-im. b2 = 4 - rank(d2-top).
print("tops F1 dim:", sum(1 for i in F for g in basis_P(i) if g in ('e0','e1')))
