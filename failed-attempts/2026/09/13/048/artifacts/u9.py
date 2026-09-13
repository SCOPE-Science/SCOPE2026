# lambda splits completely in K1 (3 roots mod lambda^2). So primes above lambda: L1,L2,L3, residue F3.
# Kummer u^3=Th unramified at Li iff Th is a cube in K1_{Li} iff Th(r_i) != 0 mod Li and ... residue char:
# residue field F3: F3^*/F3^*3 trivial => any UNIT is a cube mod Li! Need higher: Th unit at Li => unramified iff
# Th ≡ cube mod Li^{3e+1}? For 3-adic Kummer (e=1 for K1_L/Q3? K1_L = Q3 since residue F3 and... K1_L/Q3 unramified
# of degree... K1/K unramified at lambda, K/lambda = Q3( w)/... residue F9? K=Q(w): lambda residue field = F3? 
# N(lambda)=3, residue F3. Wait Z[w]/(1-w) = F3? (1-w)|3? N=3 yes residue field F3. K1_Li residue: roots mod lambda
# unique? 1 root mod lambda but 3 mod lambda^2: unramified splitting => residue degree 1, so K1_Li/Q3 unramified
# with residue F3?? Q3 residue F3, unramified ext with residue F3 = Q3 itself. So K1_Li = K_lambda = Q3(w)? K_lambda:
# K=Q(w), lambda above 3 ramified in K/Q (3 ramifies in Q(w)? disc Q(w)=-3, yes ramified, e=2). K_lambda/Q3: e=2,f=1.
# K1_Li/K_lambda unramified, residue F3=same => TRIVIAL extension?! But 3 roots mod lambda^2 means 3 distinct primes,
# each with e=1,f=1 over K_lambda. OK so K1_Li = K_lambda, e(K1_Li/Q3)=2.
# Kummer C3 over L=K_lambda (containing w, e=2): unramified C3-extension exists (residue char 3: Artin-Schreier-Witt...
# residue F3 has no C3 ext (F3^* = C2); unramified C3 over local field with residue F3? unramified exts correspond to
# residue field exts: F3 has unique C3?? Gal(F3bar/F3)=Zhat: C3 quotient EXISTS (x^3-1... F27/F3 cyclic C3). Yes exists.)
# Criterion: L^*/L^*3: L contains mu3; unramified C3 = ? The Kummer class unramified iff valuation divisible by 3
# AND unit part ≡ cube mod (1+lambda_L ...)? Precisely: theta gives unramified iff v(theta)≡0 mod 3 and
# theta/pi_L^{v} mod cubes in residue... For exponent-3 Kummer over L containing mu_3: H^1_unr = ...
# COMPUTE DIRECTLY: is Th a cube modulo Li^N for large N (Hensel)? Search r-lifts: Th(r) mod lambda^k is a cube in
# O_K/lambda^k for the compatible root sequence. Test k=2,3,4 with the 3-adic root branches.
from eisen import *
from u3lib import *
lam=(1,-1)
pi1=(-5,-3)
Th=((-4,-4),(-4,-4),(4,0)); STh=ksigma(Th)
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
def lkpow(k):
    m=ONE
    for _ in range(k): m=emul(m,lam)
    return m
for k in (2,3,4):
    m=lkpow(k)
    cl=classes_mod(m)
    print(f"k={k} N={enorm(m)} nclass={len(cl)}")
    rts=[c for c in cl if econg(epowmod(c,3,m),emod(pi1,m),m)]
    print(f"  nroots={len(rts)}")
    for r in rts:
        tv=emod(eadd(eadd(Th[0],emul(Th[1],r)),emul(Th[2],emul(r,r))),m)
        sv=emod(eadd(eadd(STh[0],emul(STh[1],r)),emul(STh[2],emul(r,r))),m)
        # is tv a cube mod m?
        cubes=set()
        for c in cl:
            cubes.add((emod(epowmod(c,3,m),m)))
        print(f"  r={e2str(r)} Th(r)={e2str(tv)} cube?{tv in cubes} sTh(r)={e2str(sv)} cube?{sv in cubes}")
