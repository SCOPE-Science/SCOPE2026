"""Theory checks for the 5/4 extension-field sum-product target.
(1) Elekes + Stevens-de Zeeuw exponent arithmetic (barrier).
(2) Reduction: target => prime-field 5/4 bound (hardness evidence).
(3) p=3 vacuity check logic.
"""
import math

print("=== (1) Elekes incidence arithmetic ===")
# Elekes: P=(A+A)x(AA), |P|<=M^2 where M=max(|A+A|,|AA|); L has |A|^2 lines, each with >=|A| points => I>=|A|^3.
# ST over R: I << |P|^{2/3}|L|^{2/3} => |A|^3 << M^{4/3}|A|^{4/3} => M >> |A|^{5/4}. Good.
# SDZ over F_q: I << |P|^{3/4}|L|^{3/4} (+ lower terms) => |A|^3 << M^{3/2}|A|^{3/2} => M >> |A|. Trivial.
print("ST(2/3,2/3):  |A|^3 << (M^2)^{2/3}(|A|^2)^{2/3} = M^{4/3}|A|^{4/3} => M >> |A|^{5/4}  [Elekes over R]")
print("SDZ(3/4,3/4): |A|^3 << (M^2)^{3/4}(|A|^2)^{3/4} = M^{3/2}|A|^{3/2} => M >> |A|      [trivial]")
print("=> Elekes route cannot reach 5/4 with any 3/4-exponent incidence. Barrier confirmed.")
print()
print("=== (2) Reduction: target(F_{p^2}) => prime-field 5/4 for |B|<=sqrt(p) ===")
print("Embed B subset F_p^x into F_{p^2}. Only proper subfield is F_p.")
print("F_p-affine lines in F_{p^2}: line == F_p iff a in F_p^x,b in F_p (else meets F_p in <=1 pt).")
print("So if |B|<=sqrt(p): cap holds (A=B meets own line in |B|<=sqrt(p), others in <=1).")
print("|A+A|,|AA| identical in F_p and F_{p^2} (subfield closed).")
print("|A|=|B|<=sqrt(p)<=c0*p=c0*q^{1/2} for p>=c0^{-2}.")
print("=> target gives max(|B+B|,|BB|)>=C|B|^{5/4} in F_p: the OPEN prime-field 5/4 bound,")
print("   beyond current records (~1.20-1.23: RNRS 6/5, RSSS/Mohammadi-Stevens/Shakan-Shkredov).")
print("=> Target is breakthrough-hard: implies improving the prime-field exponent to 5/4.")
print()
print("=== (3) p=3 vacuity ===")
print("Any two distinct x,y in F_{3^n} lie on some F_3-affine line aF_3+b (take a=(x-y)u, u in F_3^x).")
print("Cap |A cap (aF_3+b)| <= sqrt(3) < 2 forces |A|<=1 when F_3 is a proper subfield (n>1).")
print("Then max(|A+A|,|AA|)=1 >= C*1 needs only C<=1. So p=3 is vacuous; content is in p>=5.")
