# Ramification analysis.
# R = K1(u,v), u^3=Th, v^3=sTh. R/K1 Kummer of exponent 3 ramified exactly at primes dividing 3*Th*sTh.
# (Th): N(Th)=pi2*w*eta^3 with pi2 prime. So (Th) = Q * I^3 with Q|pi2. Since N(Q)|N(pi2)=19^2... 
# pi2 has N=19 (rational prime 19 =1 mod 3? 19%3=1 yes split). pi2 splits?? pi2 in K with N=19: (pi2) is PRIME in K
# (norm = rational prime). In K1=K(t)/t^3-pi1: does (pi2) split? (pi2/...) — pi2 splits completely iff pi1 is a cube
# mod pi2, i.e. (pi1/pi2)_3=1. We have s12=0! So (pi2)=Q1 Q2 Q3 in K1, each degree 1. (Th) has norm (pi2)*cube =>
# (Th)=Qi * (cube ideal) for exactly one i. So R/K1 ramified at exactly one prime above pi2 per generator... 
# (u): ramified at support of Th = {Qi} + primes above lambda (3) where Kummer ramifies if... at lambda: K1/K
# already ramified at lambda? K1=K(pi1^{1/3}): pi1 primary (clean mod lambda^3) => K1/K UNRAMIFIED at lambda
# (standard: x^3-pi1 Eisenstein? No — pi1 has N=19, not divisible by lambda. K1/K ramified exactly at (pi1) and
# possibly lambda. Since pi1 = 1 mod lambda^3, the extension is unramified at lambda. Good.)
# Kummer u^3=Th over K1: ramified at primes dividing Th not... and at lambda unless Th ≡ unit-cube mod lambda^?.
# Th=(-4-4w)+(-4-4w)t+4t^2: is Th a cube mod lambda? Need Th mod primes above lambda in K1. lambda splits? in K1:
# K1/K unramified at lambda with residue F9/K... Gal acts; lambda's splitting in K1: determined by pi1 mod lambda?
# This is getting deep but STANDARD: Amano shows with primary theta the Redei field is unramified at lambda.
# Our theta: check Th ≡ 1 mod lambda^? in O_K1? Compute Th - 1 = (-5-4w)+... divisible by lambda? N科...
# Let me just COMPUTE: is Th ≡ cube mod lambda^k in O_K1 for the relevant k, and determine exact ramified set by
# discriminant ideal computation in the K1-orders? Full rigor on ramification at lambda requires local analysis.
# SIMPLER CERTIFICATE: compute ramification via the RESOLVENT: R/K1 with group C3xC3; conductor divides
# 3*Th*sTh. Then R/K ramified only above {pi1, pi2, lambda}. To pin "exactly {pi1,pi2}": show unramified at lambda
# via local cube condition: Th and sTh are cubes in K1_{P} for P|lambda (then Kummer unramified there).
# Local cube test at lambda: O_K1/lambda^3-ish... implement: find all primes above lambda in K1 = roots of T^3-pi1
# mod lambda^k, lift, test Th(r) is a cube mod lambda^k. Let me first find splitting of lambda in K1.
from eisen import *
from u3lib import *
lam=(1,-1)
pi1=(-5,-3)
# roots of T^3 - pi1 mod lambda^k: lambda-adic. Represent residues mod lambda^k as pairs with bounded coeffs?
# Norm of lambda^k = 3^k. transversal: pairs (a,b) with a,b in range(3^k)? gives 9^k elements; want 3^k.
# O_K/(lambda^k): use reps a (0<=a<3^k) as (a,0)? differences: (a-a',0) divisible by lambda^k iff 3^k | (a-a')N?...
# (d,0) with d in Z: divisible by lambda^k iff lambda^k | d in Z[w] iff 3^{ceil(k/2)}|d (for even k=2m: lambda^{2m}=-3^m w^?..).
# Simplest transversal: enumerate pairs (a,b) in range(3^k)xrange(3^k), quotient by congruence. For k=2: 81 pairs -> 9 classes.
def classes_mod(m):
    N=enorm(m)
    import math
    B=int(math.isqrt(N))+2
    reps=[]
    seen=[]
    for a in range(-B,B+1):
        for b in range(-B,B+1):
            c=(a,b)
            if any(econg(c,s,m) for s in seen): continue
            seen.append(c)
    return seen
for k in (1,2,3):
    lk=ONE
    for _ in range(k): lk=emul(lk,lam)
    cl=classes_mod(lk)
    print(f"lambda^{k}={e2str(lk)} N={enorm(lk)} nclasses={len(cl)}")
    # roots of T^3-pi1
    rts=[c for c in cl if econg(epowmod(c,3,lk),emod(pi1,lk),lk)]
    print(f"  roots of T^3-pi1: {len(rts)}: {[e2str(r) for r in rts]}")
