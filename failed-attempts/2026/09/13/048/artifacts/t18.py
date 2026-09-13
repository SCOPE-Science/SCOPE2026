# Test: is [pi2] in span([Th],[sigmaTh]) in K1^*/K1^*3? i.e. exists (i,j): pi2/(Th^i sigmaTh^j) is a cube in K1.
# Local filter at split primes: char(pi2) - i*char(Th) - j*char(sigmaTh) == 0 for all roots.
from eisen import *
import math
def ksigma(A): return (A[0],emul(OMEGA,A[1]),emul(W2,A[2]))
def transversal(pi):
    N=enorm(pi); q=int(math.isqrt(N))
    if q*q==N: return [(a,b) for a in range(q) for b in range(q)]
    else: return [(a,0) for a in range(N)]
def cube_roots_mod(m,pi):
    mm=emod(m,pi); return [c for c in transversal(pi) if econg(epowmod(c,3,pi),mm,pi)]
def evalK1(Th,r,pi): return emod(eadd(eadd(Th[0],emul(Th[1],r)),emul(Th[2],emul(r,r))),pi)
primes=enum_primary_primes(1500)
pi1=(1,3); pi2=(1,6); Th=((-6,-6),(-6,-3),(-3,1)); STh=ksigma(Th)
TESTS=[pi for pi,N in primes if pi!=pi1 and pi!=pi2][:70]
def score_combo(i,j):
    tot=0; ok=0; bad=[]
    for q in TESTS:
        if eeq(q,pi1) or eeq(q,pi2): continue
        if edivides(q,pi2): continue
        if cubic_symbol(pi1,q)!=0: continue
        rts=cube_roots_mod(pi1,q)
        if len(rts)!=3: continue
        tot+=1; good=True
        for r in rts:
            tv=evalK1(Th,r,q); sv=evalK1(STh,r,q)
            if edivides(q,tv) or edivides(q,sv): good=False; break
            c2=cubic_symbol(pi2,q)
            if (c2-i*cubic_symbol(tv,q)-j*cubic_symbol(sv,q))%3!=0: good=False; break
        if good: ok+=1
        else: bad.append(e2str(q))
    return ok,tot,bad[:6]
for i in range(3):
    for j in range(3):
        ok,tot,bad=score_combo(i,j)
        print(f"(i,j)=({i},{j}): {ok}/{tot} bad={bad}")
