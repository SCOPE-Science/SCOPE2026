"""Step 1: smoothness, K3 type, good reduction at 3, Q-point, disc D definition. Stdlib only."""
a = [2,7,8,-17]
# (i) smoothness over Q: partials 4*ai*xi^3 vanish together only at 0 since ai!=0
assert all(v!=0 for v in a)
print("smooth over Q: OK (partials 4*ai*xi^3, ai all nonzero)")
# (ii) mod 3: ai mod3 all nonzero => smooth mod3 => good reduction at 3
mods = [v%3 for v in a]
print("coeffs mod3:", mods)
assert all(m!=0 for m in mods)
# Jacobian mod3: partials = 4*ai*xi^3 = ai*xi^3 (4=1 mod3); vanish iff all xi=0 mod3
print("smooth mod 3: OK => good reduction at 3")
# (iii) Q-point [1:1:1:1]
assert 2+7+8-17==0
print("Q-point [1:1:1:1]: OK (2+7+8-17=0)")
# (iv) K3: smooth quartic in P3 => K3 by adjunction (deg 4 = dim+1... omega = O(-4+4)=O)
print("K3 type: OK (smooth quartic in P3, omega trivial, h1(O)=0)")
# (v) disc D: 3-adic residue disc of [1:1:1:1], i.e. {x in Z_694(Q3): xi = 1 mod 3 (affine chart x3=1? or projective)}
# Define D = {[x0:x1:x2:x3] in X(Q3): xi in Z3, xi = 1 mod 3Z3 for all i} (after scaling x3=1? need units)
# Check P0 reduces to smooth F3-point [1:1:1:1] on X_{F3}: 2+1+2+... 2+7+8-17 mod3 = 2+1+2-2=3=0 mod3 yes.
print("residue of P0 mod3:", sum(mods)%3, "=> lies on X(F3), smooth point")
# (vi) bad primes: primes dividing 2*abcd for Brauer evaluation
import math
N = 2*2*7*8*17
print("2*abcd =", N, "prime divisors: 2,7,17 (3 is good, infty archimedean)")
print("STEP1_OK")
