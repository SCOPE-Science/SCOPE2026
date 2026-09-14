from cypari2 import Pari
pari = Pari()
pari.default("parisize", "4096M")
Q='x^6 - 3*x^5 + 771*x^4 - 1535*x^3 + 200463*x^2 - 201249*x + 17575221'
# Full Chevalley ambiguous class number formula for cyclic cubic K11/K1:
# |A(K11)^G| = |A(K1)| * 3^{t-1} / [E(K1) : E(K1) cap N(K11*)], t = # ramified primes in K11/K1
# Ramified primes in the relative cubic extension K11/K1: only primes above 3 (3 splits in K1, both ramified e=3).
# So t = 2. |A(K1)| = 35. E(K1): K1 imaginary quadratic => units = {+-1}, rank 0.
# Denominator divides [E(K1):E(K1)^3] = 3 (since -1 not a cube issue) — actually E(K1)={+-1}, [E:E^3]: E^3 = {1} (since (-1)^3=-1... wait (-1)^3 = -1, so E^3 = E, index 1!). Compute: (-1)^3=-1 so cubes = {+-1} = E. index 1 => denominator 1.
# => |A(K11)^G| = 35 * 3^{2-1}/d = 105/d, d | 1? => 105/d with d in {1,3?}: 105 or 35.
# 3-part: |A(K11)^G|_3 = 3 or 1. Compute actual: |A11|=3^1*5^3*7. G=Gal order 3.
print("t: primes above 3 in K1 =", len(list(pari('idealprimedec(nfinit(x^2+1031),3)'))))
print("unit rank K1:", pari('K1=bnfinit(x^2+1031,1); #K1.fu'))
print("|A(K11)^G| predicted 105/d; check divisibility: A11[3]=Z/3, G-action on Z/3 via Aut(Z/3)=order 2, image of C3 trivial => fixes all => (A11[3])^G = Z/3, size 3 => d=1?? ")
print("valuation check: v3(105)=1:", pari('valuation(105,3)'))
# The 5-part: A11[5]= (Z/5)^? cyc [105,5,5] => 5-part = Z/5 x Z/5 x Z/5? 105=3*5*7. so 5-part order 125, 7-part 7.
# G=C3 action on 5-part (order 125): fixed subgroup size divides 125, =1 mod 3 by orbit counting => 1 or 25? etc.
# Total |fixed| = 3 * 5^a * 7^b; predicted 105/d = 105 or 35 => 5-part fixed =5 or 1...: a in {0,1}: orbit count 1 mod 3 among 125 elements => #fixed = 1 mod 3: candidates 1,4?..: 5=2 mod 3 NO; 1=1 mod 3 YES. Hmm 5 = 2 mod 3, not fixed count. But fixed subgroup must be a subgroup: sizes 1,5,25,125: mod 3: 1,2,1,2 => a in {0,2}. Combined with formula 5-part in {5,1} => must be 1?? contradiction unless d has factor 5 — impossible since d | unit index power of... wait d | [E:E cap N] and E(K1)={+-1} has order 2, d | 2?? Then 105/d not integer unless d=1. So |fixed| = 105 exactly, 5-part fixed = 5?? But orbit-count says #fixed(5-part action) = 1 mod 3 and 5 = 2 mod 3. CONTRADICTION?
print("cyc again:", pari(f'(bnfinit({Q},1)).cyc'))
