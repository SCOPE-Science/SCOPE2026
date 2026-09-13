"""Exact Farkas certificate: [s0,u2] != 0 in S_3 over QQ(a,b,c).
Find w with R w = 0 (dual functional on S_3) and w.v != 0, all over QQ(a,b,c).
R is 18x27 of rank 17, so nullspace is 10-dim; generic null vector pairs non-trivially.
Certificate: explicit rational vector w0 (specialize a=1,b=2,c=3 first for a
concrete exact rational certificate, then lift: check R(1,2,3) w0=0, w0.v!=0).
A single exact rational certificate at one smooth point proves noncommutativity there;
for the universal claim we exhibit the minor: find 17x17 minor of R nonzero as
polynomial + 18x18 minor of [R;v^T] nonzero. Print both factored.
"""
import itertools, sympy as sp
a,b,c = sp.symbols('a b c')
def monoms(d): return list(itertools.product(range(3), repeat=d))
d=3
basis=monoms(d); idx={m:i for i,m in enumerate(basis)}
f=[[ (a,(1,2)),(b,(2,1)),(c,(0,0)) ],
   [ (a,(2,0)),(b,(0,2)),(c,(1,1)) ],
   [ (a,(0,1)),(b,(1,0)),(c,(2,2)) ]]
rows=[]
for fj in f:
    for lm in range(d-1):
        rm=d-2-lm
        for left in monoms(lm):
            for right in monoms(rm):
                row=[sp.Integer(0)]*len(basis)
                for coeff,w_ in fj:
                    row[idx[tuple(left)+tuple(w_)+tuple(right)]] += coeff
                rows.append(row)
R=sp.Matrix(rows)
print("R:", R.shape, "rank:", R.rank())
def mul(p,q):
    out={}
    for w1,c1 in p.items():
        for w2,c2 in q.items(): out[w1+w2]=out.get(w1+w2,0)+c1
    return out
s0={(0,):1,(1,):1,(2,):1}; u2={(0,1):1,(1,2):1,(2,0):1}
C={}
for w_,cf in mul(s0,u2).items(): C[w_]=C.get(w_,0)+cf
for w_,cf in mul(u2,s0).items(): C[w_]=C.get(w_,0)-cf
v=sp.Matrix([C.get(m,0) for m in basis])
# exact rational certificate at (1,2,3)
R0=R.subs({a:1,b:2,c:3}); v0=v.subs({a:1,b:2,c:3})
ns=R0.nullspace()
print("null dim at (1,2,3):", len(ns))
for k,w_ in enumerate(ns):
    print(f"pairing w{k}.v0 =", (w_.T*v0)[0])
# universal: 18x18 minor of aug=[R;v^T] as polynomial; find nonzero one cheaply:
# use the (1,2,3) point: pick 18 cols where aug0 has full rank -> det of that minor is polynomial, nonzero at point => not identically zero.
aug0=sp.Matrix.vstack(R0, v0.T)
print("aug rank at (1,2,3):", aug0.rank())
sub=aug0.rref()[1]  # pivot cols
print("pivot cols:", sub)
M=aug.col_extract(list(sub)) if False else None
import itertools as it
# build symbolic minor with those cols
A=sp.Matrix.vstack(R, v.T)
Ms=A.col_extract(list(sub))
print("symbolic minor degree check: computing det...")
detM=sp.factor(Ms.det())
print("det =", detM)
