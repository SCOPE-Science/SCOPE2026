"""Interpolate obstruction minor P(a,b,c): 67x67 minor of [R4; v^T] (v=[N(s1),s0]).
Homogeneous degree 66 in (a,b,c) over Q(w). Then round + factor."""
import itertools, numpy as np
w = np.exp(2j*np.pi/3)
def monoms(d): return list(itertools.product(range(3), repeat=d))
d=4
basis=monoms(d); idx={m:i for i,m in enumerate(basis)}
N=len(basis)
def build(a_,b_,c_):
    f=[[ (a_,(1,2)),(b_,(2,1)),(c_,(0,0)) ],
       [ (a_,(2,0)),(b_,(0,2)),(c_,(1,1)) ],
       [ (a_,(0,1)),(b_,(1,0)),(c_,(2,2)) ]]
    rows=[]
    for fj in f:
        for lm in range(d-1):
            rm=d-2-lm
            for left in monoms(lm):
                for right in monoms(rm):
                    row=np.zeros(N,dtype=complex)
                    for coeff,ww in fj:
                        row[idx[tuple(left)+tuple(ww)+tuple(right)]]+=coeff
                    rows.append(row)
    R=np.array(rows)
    # v row: [N,s0], N=s1^3, s1=x+w^2 y+w z
    def mul(p,q):
        out={}
        for w1,c1 in p.items():
            for w2,c2 in q.items(): out[w1+w2]=out.get(w1+w2,0)+c1*c2
        return out
    s1={(0,):1,(1,):w**2,(2,):w}; s0={(0,):1,(1,):1,(2,):1}
    NN=mul(mul(s1,s1),s1)
    C={}
    for k_,cf in mul(NN,s0).items(): C[k_]=C.get(k_,0)+cf
    for k_,cf in mul(s0,NN).items(): C[k_]=C.get(k_,0)-cf
    v=np.zeros(N,dtype=complex)
    for k_,cf in C.items(): v[idx[k_]]+=cf
    return R, v
R0,v0 = build(1.0,2.0,3.0)
A0=np.vstack([R0,v0])
print("A shape:",A0.shape,"rank:",np.linalg.matrix_rank(A0,tol=1e-8))
# select 67 independent rows then 67 cols via LU-ish (use QR with pivoting on A0.T? rows: QR on A0.T gives col pivots... we need row subset + col subset)
# row subset: QR pivoting on A0 (cols of A0.T = rows of A0): use scipy? not available. Use greedy: SVD-based: take U (82x67) from svd, then pick rows via LU on U.
U,s,Vh=np.linalg.svd(A0,full_matrices=False)
r=np.sum(s>1e-8); print("rank:",r)
U67=U[:,:r]
# greedy row select: iterated max-norm pivot (like LU row piv)
rem=list(range(82)); rows=[]
M=U67.copy()
for k in range(r):
    j=max(rem,key=lambda j: np.linalg.norm(M[j,k:]))
    rows.append(j); rem.remove(j)
    piv=M[j,k:].copy()
    if abs(piv[0])<1e-10: print("pivot fail",k); break
    for j2 in rem:
        M[j2,k:]-=M[j2,k]/piv[0]*piv
print("rows:",len(rows))
B0=A0[rows,:]
print("B0 rank:",np.linalg.matrix_rank(B0,tol=1e-8))
# col subset similarly on B0.T
Ub,sb,Vbh=np.linalg.svd(B0,full_matrices=False)
print("B0 svd rank:",np.sum(sb>1e-8))
# greedy col select on Vbh[:r,:]
rem=list(range(81)); cols=[]
M2=Vbh[:r,:].copy()
Mt=M2.T  # 81 x r; select rows of Mt
for k in range(r):
    j=max(rem,key=lambda j: np.linalg.norm(Mt[j,k:]))
    cols.append(j); rem.remove(j)
    piv=Mt[j,k:].copy()
    if abs(piv[0])<1e-10: print("col pivot fail",k); break
    for j2 in rem:
        Mt[j2,k:]-=Mt[j2,k]/piv[0]*piv
print("cols:",len(cols))
M0=A0[np.ix_(rows,cols)]
print("minor det at (1,2,3):",np.linalg.det(M0))
np.save("output/artifacts/minor_rows.npy",np.array(rows))
np.save("output/artifacts/minor_cols.npy",np.array(cols))
