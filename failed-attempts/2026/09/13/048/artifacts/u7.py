from eisen import *
from u3lib import *
pi1=(-5,-3); pi2=(-2,3)
Th=((-4,-4),(-4,-4),(4,0)); STh=ksigma(Th)
primes=enum_primary_primes(3000)
vecs=set(); nq=0; ramcount=0
for pi,N in primes:
    if eeq(pi,pi1) or eeq(pi,pi2): continue
    if cubic_symbol(pi1,pi)!=0: continue
    rts=cube_roots_mod(pi1,pi)
    if len(rts)!=3: continue
    nq+=1
    for r in rts:
        tv=evalK1(Th,r,pi); sv=evalK1(STh,r,pi)
        if edivides(pi,tv) or edivides(pi,sv): ramcount+=1; continue
        vecs.add((cubic_symbol(tv,pi),cubic_symbol(sv,pi)))
print("nq:",nq,"ram hits:",ramcount,"distinct char vectors:",sorted(vecs))
# span of vectors in F3^2
span=set([(0,0)])
for v in vecs:
    new=set()
    for x in list(span):
        new.add(((x[0]+v[0])%3,(x[1]+v[1])%3))
        new.add(((x[0]+2*v[0])%3,(x[1]+2*v[1])%3))
    span=span|new
print("span size:",len(span))
