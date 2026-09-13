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
R0=R.subs({a:1,b:2,c:3})
ns=R0.nullspace()
# save first vector with nonzero pairing vs [s0,u2]
def mul(p,q):
    out={}
    for w1,c1 in p.items():
        for w2,c2 in q.items(): out[w1+w2]=out.get(w1+w2,0)+c1
    return out
s0={(0,):1,(1,):1,(2,):1}; u2={(0,1):1,(1,2):1,(2,0):1}
C={}
for w_,cf in mul(s0,u2).items(): C[w_]=C.get(w_,0)+cf
for w_,cf in mul(u2,s0).items(): C[w_]=C.get(w_,0)-cf
v0=sp.Matrix([C.get(m,0) for m in basis])
cert=[w_ for w_ in ns if (w_.T*v0)[0]!=0][0]
print("cert pairing:", (cert.T*v0)[0])
print("R0*cert = 0 ?", (R0*cert).norm()==0)
sp.Matrix.hstack(R0.T, v0)
A=sp.Matrix.vstack(R0, v0.T)
print("aug rank:", A.rank(), " R0 rank:", R0.rank())
with open("output/artifacts/farkas_certificate.txt","w") as fh:
    fh.write("Rational Farkas certificate at (a,b,c)=(1,2,3): dual vector w in QQ^27 with R0*w=0, w.[s0,u2]=1\n")
    fh.write("basis order: "+repr(basis)+"\n")
    fh.write("w = "+repr(list(cert))+"\n")
    fh.write("pairing w.v0 = "+str((cert.T*v0)[0])+"\n")
print("saved.")
