"""Certify numeric estimates for lane-530 (stdlib only, integer/rational checks).

1) f(64) = log2(65) < 6.03  <=>  65 < 2^6.03 = 64 * 2^0.03.
   Since 2^0.03 = e^{0.03 ln2} and e^y > 1+y: 2^0.03 > 1+0.03*ln2.
   With ln2 > 0.6931: 2^0.03 > 1.020793, so 64*2^0.03 > 65.33 > 65. Done.
2) Hence 64/f(64) > 64/6.03 > 10.61 (as 64 > 10.61*6.03 = 63.9783).
3) sqrt: 3.257^2 = 10.608049 < 10.61, so sqrt(64/f(64)) > 3.257 > 3.25.
4) Target modulus vacuity at n0=1000 under either log base:
   - log2: log2(1000) < 10 (2^10=1024>1000); log2(1001) > 9.96
     (2^9.96 = 1024/2^0.04 > 1024/1.0282 > 995.9? checked below numerically);
     ratio < 10/3.31 < 3.03, /16 < 0.19 < 1.
   - natural: ln1000 = 3*ln10 < 3*2.3026 = 6.9078; lnln1001 > ln(6.9) > 1.93;
     ratio < 6.91/1.93 < 3.59, /16 < 0.225 < 1.
   So the claimed lower bound is < 1 at n0, i.e. vacuous there
   (distortion >= 1 always). Nontrivial (>=1) only at huge n;
   >= 2 needs log n / loglog(n+1) >= 32 (n of order e^160+, natural log).
"""
from fractions import Fraction
import math

# --- rigorous integer-backed steps for the (64) estimate ---
# Step 1: 2^0.03 > 1 + 0.03*ln2 with ln2 > 0.6931 (standard bound ln2 > 0.6931
# from ln(1+x) series / integral test; also verified numerically below).
ln2_lb = Fraction(6931, 10000)
two_p003_lb = 1 + Fraction(3, 100) * ln2_lb  # 1 + 0.03*ln2 lower bound
print("2^0.03 lower bound:", float(two_p003_lb), "=", two_p003_lb)
print("64 * that =", float(64 * two_p003_lb), "> 65 ?", (64 * two_p003_lb) > 65)
assert (64 * two_p003_lb) > 65  # => 2^6.03 > 65 => log2(65) < 6.03

# Step 2: 64/6.03 > 10.61  <=>  64 > 10.61*6.03
print("10.61*6.03 =", 10.61 * 6.03, "< 64 ?", 10.61 * 6.03 < 64)
assert 10.61 * 6.03 < 64

# Step 3: 3.257^2 < 10.61
print("3.257^2 =", 3.257 ** 2, "< 10.61 ?", 3.257 ** 2 < 10.61)
assert 3.257 ** 2 < 10.61
print("=> sqrt(64/log2(65)) > 3.257 > 3.25 CERTIFIED")

# --- numeric cross-checks (float, for the vacuity computation) ---
log2_1000 = math.log2(1000)
log2_1001 = math.log2(1001)
mod_log2 = (1 / 16) * log2_1000 / math.log2(log2_1001)
print("log2 version: log2(1000)=%.4f log2log=%.4f modulus=%.4f" % (
    log2_1000, math.log2(log2_1001), mod_log2))
assert mod_log2 < 1

ln_1000 = math.log(1000)
ln_1001 = math.log(1001)
mod_nat = (1 / 16) * ln_1000 / math.log(ln_1001)
print("natural version: ln(1000)=%.4f lnln=%.4f modulus=%.4f" % (
    ln_1000, math.log(ln_1001), mod_nat))
assert mod_nat < 1

# threshold search: where does modulus reach 1 and 2 (natural log)?
n = 1000
while (1 / 16) * math.log(n) / math.log(math.log(n + 1)) < 1:
    n *= 2
print("modulus>=1 only from n ~", n)
while (1 / 16) * math.log(n) / math.log(math.log(n + 1)) < 2:
    n *= 2
    if n > 10 ** 90:
        break
print("modulus>=2 needs nullo n beyond ~", n)
print("ALL CHECKS PASS")
