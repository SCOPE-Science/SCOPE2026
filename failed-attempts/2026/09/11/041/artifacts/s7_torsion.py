# Rigorous torsion lemma: #J(F13)=252, #J(F17)=334 (from s4 zeta counts).
# For good odd p, prime-to-p torsion injects J(Q)->J(Fp).
# l not in {13,17}: order | gcd(252,334)=2. 13-part via p=17: 13 !| 334 -> trivial.
# 17-part via p=13: 17 !| 252 -> trivial. 2-part injects at both (2!=13,17): | gcd(4,2)=2.
import math
print("gcd(252,334) =", math.gcd(252,334))
print("252 =", 252, "factors: 252=4*63:", 252//4)
print("334 = 2*167:", 334//2)
print("13 | 334?", 334%13==0, " 17 | 252?", 252%17==0)
print("=> #J(Q)_tors divides 2")
