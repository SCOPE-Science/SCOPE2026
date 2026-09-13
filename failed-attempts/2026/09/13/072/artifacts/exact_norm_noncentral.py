"""Exact rational certificate: N(s1)=s1^3 is NOT central in S^phi at smooth point (1,2,3).
Dual vector w in QQ(w)^81 with R4*w=0 and w.[N,s0]!=0, where R4 = degree-4 relations.
Saves certificate to farkas_norm_certificate.txt. Exact via sympy QQ(w) with w^2+w+1=0.
"""
import itertools, sympy as sp
w = sp.Symbol('w')
def mod(x): return sp.rem(sp.expand(x), w**2+w+1, w)
a0,b0,c0 = sp.Integer(1), sp.Integer(2), sp.Integer(3)
def monoms(d): return list(itertools.product(range(3), repeat=d))
d=4
basis=monoms(d); idx={m:i for i,m in enumerate(basis)}
f=[[ (a0,(1,2)),(b0,(2,1)),(c0,(0,0)) ],
   [ (a0,(2,0)),(b0,(0,2)),(c0,(1,1)) ],
   [ (a0,(0,1)),(b0,(1,0)),(c0,(2,2)) ]]
rows=[]
for fj in f:
    for lm in range(d-1):
        rm=d-2-lm
        for left in monoms(lm):
            for right in monoms(rm):
                row=[sp.Integer(0)]*len(basis)
                for coeff,ww in fj:
                    row[idx[tuple(left)+tuple(ww)+tuple(right)]] += coeff
                rows.append(row)
R=sp.Matrix(rows)
print("R4 shape:", R.shape, "rank:", R.rank())  # expect rank 66, null 15
def mul(p,q):
    out={}
    for w1,c1 in p.items():
        for w2,c2 in q.items():
            k=w1+w2; out[k]=out.get(k, sp.Integer(0))+c1*c2
    return {k:mod(v) for k,v in out.items()}
s1={(0,):sp.Integer(1),(1,):w**2,(2,):w}
s0={(0,):sp.Integer(1),(1,):sp.Integer(1),(2,):sp.Integer(1)}
N=mul(mul(s1,s1),s1)
C={}
for k_,cf in mul(N,s0).items(): C[k_]=mod(C.get(k_,sp.Integer(0))+cf)
for k_,cf in mul(s0,N).items(): C[k_]=mod(C.get(k_,sp.Integer(0))-cf)
v=sp.Matrix([mod(C.get(m,0)) for m in basis])
A=sp.Matrix.vstack(R, v.T)
print("aug rank:", A.rank())
ns=R.nullspace()
print("null dim:", len(ns))
cert=None
for u_ in ns:
    p=mod((u_.T*v)[0])
    if p!=0: cert=u_; print("pairing:", p); break
assert cert is not None
assert (R*cert).norm()==0
with open("output/artifacts/farkas_norm_certificate.txt","w") as fh:
    fh.write("Exact certificate: N(s1) not central in S^phi at (a,b,c)=(1,2,3), w^2+w+1=0.\n")
    fh.write("R4 shape %s rank %s; aug rank %s; pairing w.v = %s\n"%(repr(R.shape), R.rank(), A.rank(), repr(mod((cert.T*v)[0]))))
    fh.write("basis order: "+repr(basis)+"\n")
    fh.write("w = "+repr(list(cert))+"\n")
print("saved.")
