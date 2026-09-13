# BREAKTHROUGH pattern: b-a is CONSTANT across the 3 primes above pi3 in EVERY case tested!
# e.g. pi3=67: (0,1),(1,2),(2,0) -> b-a=1,1,1. pi3=223: (1,0),(2,1),(0,2) -> 2,2,2. pi3=619: (2,2)x3 -> 0.
# This is exactly the Heisenberg-center prediction: Frobenius elements at conjugate primes differ by conjugation
# in Gal(R/K), and conjugation acts trivially on the CENTER. So [pi1,pi2,pi3]_3 := b-a (central component) is
# well-defined independent of the choice of prime above pi3. 
# Nontrivial examples: pi3 with value 1 or 2 (e.g. 67 -> 1, 223 -> 2). Trivial: 619 -> 0.
# Now I must (1) prove the group-theoretic claim rigorously, (2) verify [R:K]=27 and Heisenberg structure,
# (3) verify ramification, (4) confirm the triple symbol identification with Massey product.
# First, extend the scan: full norm<5000, all pi3, record values; pick the BEST triple for the final certificate.
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
def charval(v,pi):
    if edivides(pi,v): return None
    return cubic_symbol(v,pi)
def central_value(Th,STh,pi1,pi):
    rts=cube_roots_mod(pi1,pi)
    if len(rts)!=3: return None
    vals=set()
    for r in rts:
        a=charval(evalK1(Th,r,pi),pi); b=charval(evalK1(STh,r,pi),pi)
        if a is None or b is None: return None
        vals.add((b-a)%3)
    if len(vals)==1: return vals.pop()
    return 'MIXED:'+str(vals)
pi1=(1,3); pi2=(1,6); Th=((-6,-6),(-6,-3),(-3,1)); STh=ksigma(Th)
primes=enum_primary_primes(5000)
nontriv=[]; triv=[]; mixed=[]; zerodiv=[]
for pi,N in primes:
    if eeq(pi,pi1) or eeq(pi,pi2): continue
    if enorm(pi)==7 or enorm(pi)==31: continue  # associates of pi1/pi2 (same norm, check below)
    if cubic_symbol(pi1,pi)!=0 or cubic_symbol(pi2,pi)!=0: continue
    if cubic_symbol(pi,pi1)!=0 or cubic_symbol(pi,pi2)!=0: continue
    v=central_value(Th,STh,pi1,pi)
    if v==1 or v==2: nontriv.append((pi,N,v))
    elif v==0: triv.append((pi,N,v))
    elif v is None: zerodiv.append((pi,N))
    else: mixed.append((pi,N,v))
print("nontriv:",len(nontriv),"triv:",len(triv),"mixed:",len(mixed),"zerodiv:",len(zerodiv))
print("MIXED:",[(e2str(p),n,v) for p,n,v in mixed])
print("ZERODIV:",[(e2str(p),n) for p,n in zerodiv][:20])
print("NONTRIV (first 30):",[(e2str(p),n,v) for p,n,v in nontriv[:30]])
print("TRIV (first 10):",[(e2str(p),n,v) for p,n,v in triv[:10]])
