# k=4: NO roots of T^3-pi1 mod lambda^4! So lambda is NOT unramified-split: the 3 roots mod lambda^2/lambda^3 are
# approximate; the true factorization: K1/K RAMIFIED at lambda after all (roots don't lift to lambda^4 => ramified).
# So K1/K ramified at lambda. Then R/K ramified at lambda too?? Hmm. But wait: primary condition pi=1 mod lambda^3
# was supposed to give unramified... pi1=-5-3w: pi1-1=-6-3w; is it divisible by lambda^3=-3-6w? (-6-3w)/(-3-6w):
# (-6-3w)*conj/(-3-6w)... N=27; num=(-6-3w)*(-3+3w)? conj(-3-6w)=(-3+3w)? conj((a,b))=(a-b,-b): conj(-3,-6)=(3,6).
# (-6-3w)(3+6w)= -18-36w-9w-18w^2 = -18-45w-18(-1-w)=-27w... = (0,-27). /27 = (0,-1). Exact! So pi1 IS 1 mod lambda^3.
# Yet T^3-pi1 has no root mod lambda^4?? For UNRAMIFIED C3 over K_lambda, need pi1 ≡ cube mod lambda^?... The
# splitting mod lambda^3 (9 roots!) but none mod lambda^4 means: residue field got bigger? If K1_L/K_lambda unramified
# C3, residue F27, roots mod lambda would be... T^3-pi1 mod lambda (F3): pi1=-5-3w ≡ -2-0=1 mod lambda. T^3-1=(T-1)^3
# in F3! Triple root (in char 3). So Hensel needs care; root count mod powers is subtle. The ramification question
# needs the discriminant: disc(T^3-pi1) = -27 pi1^2 = lambda^6 * unit * pi1^2. Different = lambda^6*pi1^2So
# different divisible by lambda^6: either ramified (if...). Since K1/K is C3 (Galois), ramification at lambda is
# all-or-nothing: e=3 (totally ramified) or e=1. disc valuation 6*... v_lambda(disc)=6+v(pi1^2)=6 (pi1 a unit at lambda).
# If unramified, disc would be a square... v=6 even, no info. Use Dedekind: T^3-pi1 mod lambda = (T-1)^3: repeated
# factor => lambda divides index or ramifies. Check Eisenstein-type: substitute T=S+1: ((S+1)^3-pi1)/... =
# S^3+3S^2+3S+(1-pi1). 1-pi1 = 6+3w = 3(2+w) = -lambda^2 w^?... v_lambda(1-pi1): N(6+3w)=36-18+9=27 => v=3? N=lambda^6?
# N(6+3w)=27 => ideal (1-pi1) has norm 27 = lambda^6... wait N(lambda^3)=27. So (1-pi1)=lambda^3 as ideals?? 
# Then S^3+3S^2+3S+(1-pi1): v(coeffs): 3=lambda^2 u, constant v=3. Newton polygon: points (0,3),(1,2),(2,2),(3,0):
# slopes: min slope from (0,3): to (3,0): -1; check (1,2): 3-1=2 on line y=3-x? x=1: y=2. yes on line. So single
# segment slope -1, length 3 => TOTALLY RAMIFIED (e=3) at lambda! So K1/K ramified at lambda. Hmm!
# So the Heisenberg extension R/K is ramified at lambda as well. The target's "ramification exactly at pi1,pi2"
# LITERALLY fails for this theta — but this is EXPECTED: in the cubic Redei theory, the Heisenberg extension is
# ramified at lambda too unless theta satisfies extra 3-adic conditions (Amano's "3 is ..."). Actually in
# Morishita's theory, the triple symbol is defined using the maximal... the Redei extension is unramified outside
# S={pi1,pi2,lambda}? or the "mod 3 Heisenberg extension ramified at pi1,pi2" might allow lambda (3 is the coefficient
# characteristic — "ramification exactly at pi1,pi2" might mean "outside lambda"/"among the pi's").
# The TARGET says: "the mod-3 Heisenberg degree-27 extension with ramification exactly at pi1,pi2 and defining
# equations". Hmm. Strictly, ramification at lambda may be unavoidable. But maybe a BETTER theta (satisfying
# 3-adic congruence, e.g. Th ≡ 1 mod lambda^N) kills ramification at lambda. Our Th(r) mod lambda^2 = -1-2w... 
# units; is -1-2w a cube mod lambda^3? cubes set computed: Th(r) NOT a cube mod lambda^2 even. So R/K1 ramified at
# lambda. To fix: need Th ≡ cube mod lambda^{3e+1}... i.e., adjust Th by K1-cubes/units? Changing Th by a cube
# doesn't change R. Changing by unit of norm... The available freedom: Th has N=pi2*u*eta^3; eta choice = cube
# (no change); u a unit. Units mod cubes: {1,w}. w: is w a cube in K1? w is a cube in K (w=((1+w)/...)? w =? 
# In K=Q(w), w is NOT a cube (units mu_6, cubes = {1,-1}? (-1)^... cubes of units: 1^3=1,(-1)^3=-1,w^3=1,(-w)^3=-1.
# So unit-cubes={1,-1}, w not a cube). So Th' = w*Th gives a DIFFERENT extension. Also different (X,Y,Z) solutions
# give different extensions. The ramification at lambda depends on Th mod lambda-powers: need Th'(r) ≡ cube mod
# lambda^{?}. Since residue F3^*/cubes trivial, need higher precision: Th' ≡ cube mod lambda^3-ish per branch.
# SEARCH: among MANY theta solutions, find one with Th(r_i), sTh(r_i) cubes mod lambda^3 for all branches r_i.
# The branches mod lambda^3: 9 roots (3 per prime). Condition per branch...
# ALSO alternative: maybe accept ramification at lambda and READ the target as "ramified exactly at pi1,pi2
# apart from the prime above 3" — but the target says "exactly". Hmm. The target ALSO says "or proves no such
# triple exists in the stated norm bound". A cleaner path: find theta with GOOD 3-adic behavior. Let me search.
from eisen import *
from u3lib import *
lam=(1,-1)
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
m3=ONE
for _ in range(3): m3=emul(m3,lam)
cl3=classes_mod(m3)
cubes3=set(emod(epowmod(c,3,m3),m3) for c in cl3)
print("ncubes mod lam3:",len(cubes3))
pi1=(-5,-3)
rts=[c for c in cl3 if econg(epowmod(c,3,m3),emod(pi1,m3),m3)]
print("nroots:",len(rts))
# condition: Th(r), sTh(r) in cubes3 for every root r
def lam3_good(X,Y,Z,P):
    Th=(X,Y,Z); S=ksigma(Th)
    for r in rts:
        tv=emod(eadd(eadd(X,emul(Y,r)),emul(Z,emul(r,r))),m3)
        sv=emod(eadd(eadd(S[0],emul(S[1],r)),emul(S[2],emul(r,r))),m3)
        if tv not in cubes3 or sv not in cubes3: return False
    return True
print("current theta good?",lam3_good((-4,-4),(-4,-4),(4,0),pi1))
# search other thetas for pair (pi1,pi2): enumerate box B=6, test N=pi2*u*cube AND lam3_good
import time
pi2=(-2,3)
t0=time.time()
rng=range(-6,7); n=0; goods=[]
for xa in rng:
 for xb in rng:
  X=(xa,xb)
  for ya in rng:
   for yb in rng:
    Y=(ya,yb)
    for za in rng:
     for zb in rng:
      Z=(za,zb)
      if X==ZERO and Y==ZERO and Z==ZERO: continue
      N=knormXYZ(X,Y,Z,pi1)
      if eeq(N,ZERO) or not edivides(pi2,N): continue
      q,_=edivmod(N,pi2)
      ok=False
      for u in UNITS:
          if cube_root_Zw(emul(q,u)) is not None: ok=True; break
      if not ok: continue
      n+=1
      if lam3_good(X,Y,Z,pi1):
          goods.append((X,Y,Z))
          print("GOOD:",list(map(e2str,(X,Y,Z))))
print(f"nsols={n} ngood={len(goods)} time={time.time()-t0:.0f}s")
