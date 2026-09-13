# Understand the 3-adic condition structurally instead of brute force.
# Th(r) mod lambda^3 must be in {0,+-1} for all 9 roots r (3 primes x 3 lifts?). Actually 9 roots mod lambda^3:
# 3 primes above lambda x 3 roots each? No: each prime has residue F3, T^3-pi1=(T-1)^3there... the 9 roots = 3 primes
# x 3 Hensel-lifts that DON'T all lift further (ramified!). Since K1/K ramified at lambda (Newton polygon showed
# e=3!), there is ONE prime above lambda in K1, totally ramified. The 9 roots mod lambda^3 = approximations within
# the single ramified prime. Condition "Th(r) in {0,+-1}" for ramified prime: valuation language: L/K1_L... 
# For Kummer over ramified prime: unramified iff 3|v(Th) and unit part ≡ cube mod lambda_L^{?}. Since e(L/Q3)=6
# (2*3), uniformizer t with t^6~3. Cubes mod...: condition = Th(r)/lambda^{v} ≡ +-1 mod lambda^3-ish.
# ALTERNATIVE STRATEGY — sidestep lambda entirely: note the TARGET only demands ramification "exactly at pi1,pi2".
# If ramification at lambda is unavoidable in general, maybe for SOME pair it's avoidable (Th can be chosen
# 3-adically a cube). Rather than brute-forcing one pair, note the condition Th(r)∈{0,±1} mod lambda^3 is a
# CONGRUENCE condition on (X,Y,Z) mod lambda^3: 27^3=19683 combos — TRIVIAL to enumerate! For each residue class,
# check the condition; then search for actual theta in a GOOD class with N=pi2*cube.
from eisen import *
from u3lib import *
m3=(-3,-6)
def classes_mod(m):
    import math
    B=int(math.isqrt(enorm(m)))+2
    seen=[]
    for a in range(-B,B+1):
        for b in range(-B,B+1):
            c=(a,b)
            if any(econg(c,s,m) for s in seen): continue
            seen.append(c)
    return seen
cl3=classes_mod(m3)
CUBES=set(emod(epowmod(c,3,m3),m3) for c in cl3)
pi1=(-5,-3)
rts=[c for c in cl3 if econg(epowmod(c,3,m3),emod(pi1,m3),m3)]
def good_class(X,Y,Z):
    S=ksigma((X,Y,Z))
    for r in rts:
        tv=emod(eadd(eadd(X,emul(Y,r)),emul(Z,emul(r,r))),m3)
        sv=emod(eadd(eadd(S[0],emul(S[1],r)),emul(S[2],emul(r,r))),m3)
        if tv not in CUBES or sv not in CUBES: return False
    return True
ngood=0; examples=[]
for X in cl3:
    for Y in cl3:
        for Z in cl3:
            if X==ZERO and Y==ZERO and Z==ZERO: continue
            if good_class(X,Y,Z):
                ngood+=1
                if len(examples)<10: examples.append((e2str(X),e2str(Y),e2str(Z)))
print("ngood classes:",ngood,"/",27**3)
for e in examples: print(e)
