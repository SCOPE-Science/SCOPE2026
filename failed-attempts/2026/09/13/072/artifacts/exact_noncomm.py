"""Exact symbolic check: [s0,u2] != 0 in S_3 for all smooth Sklyanin params.
S_3: 27 words, relations = {m*f_j*m'} : 3 rels x 9 splits (lm=0..2? d=3: lm+rm=1 -> 2 splits x3 words... lm in {0,1}, rm=1-lm: left 1 or 3 words) => 3* (1*3+3*1)=18 rows.
Solve R*special: express [s0,u2] word-vector; check it is NOT in row-space of R over Q(a,b,c)
by exact Gauss elimination; print a maximal nonvanishing minor / obstruction.
Then: specialize obstruction at generic smooth point + confirm.
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
print("R shape:", R.shape, "rank:", R.rank())
# commutator [s0,u2], s0=x+y+z, u2=xy+yz+zx
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
# augmented: is v in rowspace(R)? rowspace = colspace(R.T). Solve R.T y = v over Q(a,b,c).
y=sp.symbols('y0:%d'%len(rows))
sol, params = R.T.gauss_jordan_solve(v)
resid = R.T*sol - v
resid = sp.simplify(resid)
nres = sum(1 for e in resid if e != 0)
print("residual nonzero entries:", nres, "of", len(resid))
for i,e in enumerate(resid):
    if e != 0:
        print("resid[",basis[i],"] =", sp.factor(e))
        break
# obstruction numerator at smooth test points
print("rank R at (1,2,3):", R.subs({a:1,b:2,c:3}).rank())
