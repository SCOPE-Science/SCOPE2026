# A: span test ([R:K1]=9?) + B: [pi2*w^j] in span? (R/K Galois?) for FINAL theta.
from eisen import *
from u3lib import *
pi1=(-5,-3); pi2=(-2,3); pi3=(-23,-21)
Th=((-4,-4),(-4,-4),(4,0)); STh=ksigma(Th)
primes=enum_primary_primes(3000)
TESTS=[pi for pi,N in primes if pi not in (pi1,pi2)]
def fiber_chars(Th,STh,extra,pi1,q):
    """chars of (Th, sTh, extra) at the 3 primes above q. None if bad prime."""
    if eeq(q,pi1): return None
    if cubic_symbol(pi1,q)!=0: return None
    rts=cube_roots_mod(pi1,q)
    if len(rts)!=3: return None
    rows=[]
    for r in rts:
        tv=evalK1(Th,r,q); sv=evalK1(STh,r,q)
        if edivides(q,tv) or edivides(q,sv): return None
        row=(cubic_symbol(tv,q),cubic_symbol(sv,q))
        if extra is not None:
            if edivides(q,extra): return None
            row=row+(cubic_symbol(extra,q),)
        rows.append(row)
    return rows
# A: span
vecs=set(); nq=0
for q in TESTS:
    f=fiber_chars(Th,STh,None,pi1,q)
    if f is None: continue
    nq+=1
    for a,b in f: vecs.add((a,b))
print("A: nq=",nq,"vecs=",sorted(vecs))
span=set([(0,0)])
for v in vecs:
    span=span|{((x[0]+v[0])%3,(x[1]+v[1])%3) for x in list(span)}|{((x[0]+2*v[0])%3,(x[1]+2*v[1])%3) for x in list(span)}
print("A: span size=",len(span),"[R:K1]=9?",len(span)==9)
# B: relation [pi2*w^j] = a[Th]+b[sTh]?
w=OMEGA
pw=[pi2, emul(pi2,w), emul(pi2,emul(w,w))]
for j,extra in enumerate(pw):
    for a in range(3):
        for b in range(3):
            tot=0; ok=0
            for q in TESTS:
                f=fiber_chars(Th,STh,extra,pi1,q)
                if f is None: continue
                tot+=1
                if all((c-a*x-b*y)%3==0 for x,y,c in f): ok+=1
            if ok==tot and tot>0:
                print(f"B: PASS j={j} (a,b)=({a},{b}) {ok}/{tot}")
print("B done")
