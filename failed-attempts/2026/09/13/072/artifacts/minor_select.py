"""Greedy minor selection with correct pivoting (max abs entry, Schur update on trailing block)."""
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
    R=np.zeros((81,N),dtype=complex); rr=0
    for fj in f:
        for lm in range(d-1):
            rm=d-2-lm
            for left in monoms(lm):
                for right in monoms(rm):
                    for coeff,ww in fj:
                        R[rr,idx[tuple(left)+tuple(ww)+tuple(right)]]+=coeff
                    rr+=1
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
    return np.vstack([R,v])
A0=build(1.0,2.0,3.0)
print("rank:",np.linalg.matrix_rank(A0,tol=1e-8))
# greedy: maintain list of remaining rows/cols, residual block via Schur complement
rrows=list(range(82)); rcols=list(range(81))
rows=[]; cols=[]
T=A0.copy()
# do full LU with partial pivoting on the fly: at step k, among remaining, pick (i,j) max |T[i,j]|, record, eliminate.
T=T.copy()
for k in range(82):
    best=None; bv=-1
    for i in rrows:
        for j in rcols:
            a=abs(T[i,j])
            if a>bv: bv=a; best=(i,j)
    if bv<1e-10:
        print("stop at",k,"pivot",bv); break
    i,j=best; rows.append(i); cols.append(j)
    rrows.remove(i); rcols.remove(j)
    piv=T[i,j]
    for i2 in rrows:
        for j2 in rcols:
            T[i2,j2]-=T[i2,j]*T[i,j2]/piv
print("selected:",len(rows),len(cols))
M0=A0[np.ix_(rows,cols)]
print("det:",np.linalg.det(M0))
np.save("output/artifacts/minor_rows.npy",np.array(rows))
np.save("output/artifacts/minor_cols.npy",np.array(cols))
