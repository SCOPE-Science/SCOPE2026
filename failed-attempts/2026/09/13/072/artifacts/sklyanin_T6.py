"""T6: is N(s1) central in S^phi? test [N(s1), inv] for invariant gens in S_4/S_5/S_6.
Also test [s0,u2] etc. Generic (1,2,3).
Invariant gens: s0=x+y+z (deg1); deg2 invariants: t1=xy+yz+zx, t2=yx+zy+xz, d1=x^2+y^2+z^2;
deg3: s0^3, N(s1)=s1^3, N(s2)=s2^3, xyz+yzx+zxy etc.
Test centrality of N(s1) against s0 (in S_4) and against t1 (in S_5).
"""
import itertools, numpy as np
def monoms(d): return list(itertools.product(range(3), repeat=d))
def quotient(d,a_,b_,c_):
    basis=monoms(d); idx={m:i for i,m in enumerate(basis)}
    f=[[ (a_,(1,2)),(b_,(2,1)),(c_,(0,0)) ],
       [ (a_,(2,0)),(b_,(0,2)),(c_,(1,1)) ],
       [ (a_,(0,1)),(b_,(1,0)),(c_,(2,2)) ]]
    rows=[]
    for fj in f:
        for lm in range(d-1):
            rm=d-2-lm
            for left in monoms(lm):
                for right in monoms(rm):
                    row=np.zeros(len(basis),dtype=complex)
                    for coeff,w in fj:
                        row[idx[tuple(left)+tuple(w)+tuple(right)]]+=coeff
                    rows.append(row)
    R=np.array(rows)
    u,s,vh=np.linalg.svd(R,full_matrices=True)
    rank=int((s>1e-8).sum())
    return basis,idx,R,vh[rank:,:],rank
def wv(poly,idx,N):
    v=np.zeros(N,dtype=complex)
    for w_,cf in poly.items(): v[idx[w_]]+=cf
    return v
def mul(p,q):
    out={}
    for w1,c1 in p.items():
        for w2,c2 in q.items(): out[w1+w2]=out.get(w1+w2,0)+c1*c2
    return out
a_,b_,c_=1.0,2.0,3.0
w=np.exp(2j*np.pi/3)
s0={(0,):1,(1,):1,(2,):1}
s1={(0,):1,(1,):w**2,(2,):w}
t1={(0,1):1,(1,2):1,(2,0):1}
N=mul(mul(s1,s1),s1)
# [N,s0] in S_4
b4,i4,R4,Q4,r4=quotient(4,a_,b_,c_)
C={};
for w_,cf in mul(N,s0).items(): C[w_]=C.get(w_,0)+cf
for w_,cf in mul(s0,N).items(): C[w_]=C.get(w_,0)-cf
print(f"[N,s0] quot norm in S4 = {np.linalg.norm(Q4@wv(C,i4,len(b4))):.6f}")
# [N,t1] in S_5
b5,i5,R5,Q5,r5=quotient(5,a_,b_,c_)
C2={};
for w_,cf in mul(N,t1).items(): C2[w_]=C2.get(w_,0)+cf
for w_,cf in mul(t1,N).items(): C2[w_]=C2.get(w_,0)-cf
print(f"[N,t1] quot norm in S5 = {np.linalg.norm(Q5@wv(C2,i5,len(b5))):.6f} (qdim5={Q5.shape[0]})")
# also [s0,t1] already nonzero (T3). print Hilbert check: S4 dim expect 15, S5 21?
print(f"S4 quot dim={Q4.shape[0]} (expect 15), S5 quot dim={Q5.shape[0]} (expect 21)")
# s1 itself: is s1 in S? check [s1, s0] in S_3?
b3,i3,R3,Q3,r3=quotient(3,a_,b_,c_)
Cs={};
for w_,cf in mul(s1,s0).items(): Cs[w_]=Cs.get(w_,0)+cf
for w_,cf in mul(s0,s1).items(): Cs[w_]=Cs.get(w_,0)-cf
print(f"[s1,s0] quot norm in S3 = {np.linalg.norm(Q3@wv(Cs,i3,len(b3))):.6f}")
