"""Interpolate obstruction D(a,b,c) = det A[a,b,c] over Q(w), homogeneous degree 67.
A = 81 rows of R4 (deg 1 each) with v-row (deg 0) -> det deg 81? R4 rows each carry one of a,b,c -> every entry deg<=1, v-row deg 0. Minor of size 67 with v-row: deg 66.
Sample D on line (a,b,c)=(1,t,t^2) -> univariate degree <=132? deg in t: each entry deg<=2 in t (a=1 const, b=t, c=t^2) -> minor deg<= 66*2=132. Interpolate at 140 roots of unity, round coeffs (Gaussian integers in w), factor.
"""
import itertools, numpy as np
w = np.exp(2j*np.pi/3)
def monoms(d): return list(itertools.product(range(3), repeat=d))
d=4
basis=monoms(d); idx={m:i for i,m in enumerate(basis)}
N=len(basis)
s1t={(0,):1,(1,):w**2,(2,):w}; s0t={(0,):1,(1,):1,(2,):1}
def mul(p,q):
    out={}
    for w1,c1 in p.items():
        for w2,c2 in q.items(): out[w1+w2]=out.get(w1+w2,0)+c1*c2
    return out
NNt=mul(mul(s1t,s1t),s1t)
Ct={}
for k_,cf in mul(NNt,s0t).items(): Ct[k_]=Ct.get(k_,0)+cf
for k_,cf in mul(s0t,NNt).items(): Ct[k_]=Ct.get(k_,0)-cf
vrow=np.zeros(N,dtype=complex)
for k_,cf in Ct.items(): vrow[idx[k_]]+=cf
# relation row pattern: entries labeled by param: store coefficient slots
def row_pattern():
    pats=[]
    f=[[ ('a',(1,2)),('b',(2,1)),('c',(0,0)) ],
       [ ('a',(2,0)),('b',(0,2)),('c',(1,1)) ],
       [ ('a',(0,1)),('b',(1,0)),('c',(2,2)) ]]
    for fj in f:
        for lm in range(d-1):
            rm=d-2-lm
            for left in monoms(lm):
                for right in monoms(rm):
                    slots=[]
                    for tag,ww in fj:
                        slots.append((tag, idx[tuple(left)+tuple(ww)+tuple(right)]))
                    pats.append(slots)
    return pats
pats=row_pattern(); print("rows:",len(pats))
rows=np.load("output/artifacts/minor_rows.npy"); cols=np.load("output/artifacts/minor_cols.npy")
print("minor size:",len(rows),len(cols))
# find v-row position in rows (row index 81)
print("vrow in minor:", 81 in rows)
def minor_det(a_,b_,c_):
    M=np.zeros((len(rows),len(cols)),dtype=complex)
    for i,r in enumerate(rows):
        if r==81:
            M[i,:]=vrow[cols]
        else:
            for tag,j in pats[r]:
                M[i,cols.tolist().index(j)]+= {'a':a_,'b':b_,'c':c_}[tag] if False else 0
    # fill properly:
    return M
# build evaluation directly (vectorized)
def eval_det(t):
    a_,b_,c_=1.0,t,t**2
    M=np.zeros((len(rows),len(cols)),dtype=complex)
    for i,r in enumerate(rows):
        if r==81: M[i,:]=vrow[cols]; continue
        for tag,j in pats[r]:
            pass
    # faster: precompute R
    R=np.zeros((81,N),dtype=complex)
    f=[[ (a_,(1,2)),(b_,(2,1)),(c_,(0,0)) ],
       [ (a_,(2,0)),(b_,(0,2)),(c_,(1,1)) ],
       [ (a_,(0,1)),(b_,(1,0)),(c_,(2,2)) ]]
    rr=0
    for fj in f:
        for lm in range(d-1):
            rm=d-2-lm
            for left in monoms(lm):
                for right in monoms(rm):
                    for coeff,ww in fj:
                        R[rr,idx[tuple(left)+tuple(ww)+tuple(right)]]+=coeff
                    rr+=1
    A=np.vstack([R,vrow])
    return np.linalg.det(A[np.ix_(rows,cols)])
ts=np.exp(2j*np.pi*np.arange(140)/140)
vals=np.array([eval_det(t) for t in ts])
print("max|D|:",np.max(np.abs(vals)), " D(1) [t=1 -> (1,1,1) singular] =",vals[0])
# DFT -> coeffs of t^k, k=0..139; true deg<=132 so top coeffs ~0
coeffs=np.fft.ifft(vals)*len(vals)  # coeffs[k] of t^k? ifft ordering: vals_j = sum c_k w^{jk} -> c=ifft* n. yes
print("tail |c_133..139|:",np.abs(coeffs[133:]))
print("leading |c_126..132|:",np.abs(coeffs[126:133]))
# round to Z[w]: map z -> round in basis {1,w}: solve [Re;Im] [[1,-1/2],[0,sqrt3/2]] [m;n]
def to_zw(z):
    n=round(z.imag/(np.sqrt(3)/2)); m=round(z.real+n/2); return m,n
pairs=[to_zw(c) for c in coeffs[:133]]
res=[coeffs[k]-(pairs[k][0]+pairs[k][1]*w) for k in range(133)]
print("max round resid:",max(abs(r) for r in res))
nz=[(k,pairs[k]) for k in range(133) if pairs[k]!=(0,0)]
print("nonzero coeffs:",len(nz))
print(nz[:40])
np.save("output/artifacts/Dcoeffs Zw.npy",np.array(pairs))
