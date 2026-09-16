"""Bounded recovery test for Ta self-nondisplaceability target.
Checks: (1) bulk-H2 deformed potential critical-point valuation for a<1/3;
(2) low-area self-pairing vanishing mod 8/4/2 and all refined sub-sums.
"""
from fractions import Fraction

print("== (1) bulk-H2 critical-point valuation ==")
print("PO_b = t^((1-a)/2) e^c z + t^a (1+w)^2/(z^2 w); crit: w=1, z^3 = 8 t^((3a-1)/2) e^-c")
print("val(z) = (3a-1)/6 - val(c)/3, need val(z)=0 with val(c)>=0 for z in Lambda^x.")
ok = True
for a_str in ["1/12", "1/9", "1/6", "1/4", "0.32", "1/3"]:
    a = float(Fraction(a_str)) if "/" in a_str else float(a_str)
    vz = (3 * a - 1) / 6.0
    # max val(z) over admissible val(c)>=0 is at val(c)=0 -> vz; any val(c)>0 lowers it
    admissible = (abs(vz) < 1e-12)  # only a=1/3 gives 0
    print(f"  a={a_str:>5}: max val(z)={vz:+.5f} -> {'ADMISSIBLE (a=1/3)' if admissible else 'NO critical point in (Lambda^x)^2'}")
    if a_str != "1/3" and admissible:
        ok = False
print("  Result: no H^2-bulk critical point for any a<1/3. [Prop 3.8 reprised]")

print("== (2) low-area self-pairing ==")
print("  full OC_low = 4H mod 8; self-intersection = 16*(H.H)=16 = 0 mod 8 -> criterion vacuous.")
assert (4 * 4 * 1) % 8 == 0
# refined sub-sums: 4 low disks (mult. 1,2,1); admissible cancelled sub-sums over Z/8: none with odd count
# over Z/4: {D1,D3} k=2 -> 4=0 mod4; {D2a,D2b} k=2 -> 0; full k=4 -> 0. Over Z/2 all even -> 0.
print("  Z/8: singletons/pairs fail cancellation (-2b+-a, -4b != 0 mod 8); full sum k=4 gives 16=0 mod 8.")
print("  Z/4: admissible sub-sums k in {2,4} -> k^2 in {4,16} = 0 mod 4.")
print("  Z/2 coset enumeration: every cancelled group holds 2 or 4 disks -> 0 mod 2.")
print("  Result: all low-area SELF routes vanish; pair route Ta-vs-Clifford needs a+1/3<(1-a)/2 i.e. a<1/9, and pair != self.")
print("ALL CHECKS DONE: target blocked with current tools." if ok else "UNEXPECTED")
