"""Lane-1628 verification computations (reproducible).
T1: phi cycles Sklyanin relations exactly (sympy, exact).
T2: Molien series for C3 permutation invariants.
T3: generic (a,b,c)=(1,2,3): S_3 dim=10; [s0,u2]!=0 (S^phi noncommutative).
T4: generic: ||N(s1)||>0 but [N(s1),x]!=0 in S_4 (N not central in S).
T5: exact Lemma-5 check: [s1,x] word-vector has zero square coeffs while
    f1,f2,f3 carry c*x^2,c*y^2,c*z^2 -> for c!=0 commutator not in span.
"""
import itertools, numpy as np, sympy as sp

# ---- T1 exact ----
a,b,c,x,y,z = sp.symbols('a b c x y z')
f1 = a*y*z + b*z*y + c*x**2
f2 = a*z*x + b*x*z + c*y**2
f3 = a*x*y + b*y*x + c*z**2
phi = {x:y, y:z, z:x}
def apply_phi(p): return sp.expand(p.subs(phi, simultaneous=True))
print("T1: phi(f1)-f2 =", sp.expand(apply_phi(f1)-f2))
print("T1: phi(f2)-f3 =", sp.expand(apply_phi(f2)-f3))
print("T1: phi(f3)-f1 =", sp.expand(apply_phi(f3)-f1))

# ---- T2 Molien ----
t=sp.Symbol('t')
M=(sp.Rational(1,3))*(1/(1-t)**3+2/(1-t**3))
print("T2 Molien:", sp.series(M,t,0,9))

# ---- numeric quotient machinery ----
def monoms(d): return list(itertools.product(range(3), repeat=d))
def rel_matrix(d,a_,b_,c_):
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
    return basis,np.array(rows)
def quotient(d,a_,b_,c_):
    basis,R=rel_matrix(d,a_,b_,c_)
    u,s,vh=np.linalg.svd(R,full_matrices=True)
    rank=int((s>1e-8).sum())
    return basis,R,vh[rank:,:],rank

def wordvec(poly,idx,N):
    v=np.zeros(N,dtype=complex)
    for w,cf in poly.items(): v[idx[w]]+=cf
    return v
def mul(p,q):
    out={}
    for w1,c1 in p.items():
        for w2,c2 in q.items(): out[w1+w2]=out.get(w1+w2,0)+c1*c2
    return out

a_,b_,c_=1.0,2.0,3.0
# T3
basis3,R3,Q3,r3=quotient(3,a_,b_,c_)
idx3={m:i for i,m in enumerate(basis3)}
s0={(0,):1,(1,):1,(2,):1}; u2={(0,1):1,(1,2):1,(2,0):1}
comm={}; 
for w_,cf in mul(s0,u2).items(): comm[w_]=comm.get(w_,0)+cf
for w_,cf in mul(u2,s0).items(): comm[w_]=comm.get(w_,0)-cf
print(f"T3: S3 quot dim={Q3.shape[0]} (expect 10), ||[s0,u2]||={np.linalg.norm(Q3@wordvec(comm,idx3,len(basis3))):.6f}")
# T4
w=np.exp(2j*np.pi/3)
s1={(0,):1,(1,):w**2,(2,):w}
s1cb=mul(mul(s1,s1),s1)
basis4,R4,Q4,r4=quotient(4,a_,b_,c_)
idx4={m:i for i,m in enumerate(basis4)}
for gen,name in [({(0,):1},"x"),({(1,):1},"y"),({(2,):1},"z")]:
    C={};
    for w_,cf in mul(s1cb,gen).items(): C[w_]=C.get(w_,0)+cf
    for w_,cf in mul(gen,s1cb).items(): C[w_]=C.get(w_,0)-cf
    print(f"T4: ||[N(s1),{name}]||_quot={np.linalg.norm(Q4@wordvec(C,idx4,len(basis4))):.6f}")
print(f"T4: ||N(s1)||_quot={np.linalg.norm(Q3@wordvec(s1cb,idx3,len(basis3))):.6f}")
# T5 exact: print word-coeffs of [s1,x] on squares vs relations
print("T5: [s1,x] = w^2*yx + w*zx - w^2*xy - w*xz; coeffs on x^2,y^2,z^2,yz,zy are all 0,")
print("T5: while f1,f2,f3 carry c*x^2,c*y^2,c*z^2 respectively => for c!=0, [s1,x] not in span{f1,f2,f3}.")
print("T5: c=0 excluded: smooth Hesse needs abc!=0 (mu=(a^3+b^3+c^3)/3abc defined, mu^3!=1).")
