"""Exact rational verification of deformed-binary edge bias (a=1/2).
All checks use fractions.Fraction (exact). Run: python3 verify_edge_bias.py
"""
from fractions import Fraction as F

ok = True
def check(name, cond, detail=""):
    global ok
    print(("PASS" if cond else "FAIL"), name, detail)
    if not cond:
        ok = False

# h(s,alpha) = alpha/(s-a)^2 + (1-alpha)/(s+a)^2, a=1/2
def h(s, alpha):
    a = F(1, 2)
    return alpha / (s - a) ** 2 + (F(1, 1) - alpha) / (s + a) ** 2

# 1) root bracket at alpha=1/2: h(1.27)>1>h(1.272)
check("h(1.27,1/2)>1", h(F(127, 100), F(1, 2)) > 1,
      str(float(h(F(127, 100), F(1, 2)))))
check("h(1.272,1/2)<1", h(F(1272, 1000), F(1, 2)) < 1,
      str(float(h(F(1272, 1000), F(1, 2)))))

# 2) uniform enclosure s(alpha) in (1.2,1.35) for alpha in [1/2,3/5]:
# h_{1/2}(1.2)>1 implies s(alpha)>1.2 (h increasing in alpha);
# h_{3/5}(1.35)<1 implies s(alpha)<1.35.
check("h(1.2,1/2)>1", h(F(6, 5), F(1, 2)) > 1,
      str(float(h(F(6, 5), F(1, 2)))))
check("h(1.35,3/5)<1", h(F(27, 20), F(3, 5)) < 1,
      str(float(h(F(27, 20), F(3, 5)))))
# monotonicity in alpha at fixed s>a: coefficient 1/(s-a)^2-1/(s+a)^2>0
check("h increasing in alpha at s=1.2",
      F(1, 1) / (F(6, 5) - F(1, 2)) ** 2 > F(1, 1) / (F(6, 5) + F(1, 2)) ** 2)

# 3) derivative lower bound: E'(alpha)=2a/(s^2-a^2)=1/(s^2-1/4) >= 1/(1.35^2-1/4)
dmin = F(1, 1) / ((F(27, 20)) ** 2 - F(1, 4))
print("min E' bound =", float(dmin))
check("E'(alpha)>0.635 on [1/2,3/5]", dmin > F(635, 1000))
check("E'(alpha)>0.63", dmin > F(63, 100))

# 4) exact derivative at alpha=1/2 equals sqrt(3)-1: verify (u-1/4)=(1+sqrt3)/2 route
# numerically: 1/(s0^2-1/4) with s0^2 in ((1.27)^2,(1.272)^2)
lo = F(1, 1) / ((F(1272, 1000)) ** 2 - F(1, 4))
hi = F(1, 1) / ((F(127, 100)) ** 2 - F(1, 4))
print("E'(1/2) bracket = (", float(lo), ",", float(hi), ") vs sqrt3-1 =", 3 ** 0.5 - 1)
check("E'(1/2) in (0.73,0.74)", lo > F(73, 100) and hi < F(74, 100))

# 5) curvature gamma0=(2/|Fmm|)^{1/3} >= 0.94 at alpha=1/2:
# |Fmm| <= 1/0.77^3+1/1.77^3 <= 2.371  =>  gamma0^3 >= 2/2.371 >= 0.94^3
Fmm_ub = F(10 ** 6, 77 ** 3) + F(10 ** 6, 177 ** 3)
print("|Fmm| upper =", float(Fmm_ub))
check("|Fmm|<=2.371", Fmm_ub <= F(2371, 1000))
check("2/2.371 >= 0.94^3", F(2, 1) / F(2371, 1000) >= F(94, 100) ** 3)
# gamma0 <= 1.5: |Fmm| >= 1/0.772^3 >= 2.17 => gamma0^3 <= 2/2.17 <= 1.5^3
Fmm_lb = F(10 ** 9, 772 ** 3)  # 1/0.772^3; drops the positive second term for a lower bound
check("|Fmm|>=2.17 (first term only)", Fmm_lb >= F(217, 100))
check("2/2.17 <= 1.5^3", F(2, 1) / F(217, 100) <= F(3, 2) ** 3)

# 6) uniform regularity on s in [1.2,1.35], alpha in [1/2,3/5]:
# Phi''(s,alpha)=2a1/(s-a)^3+2a2/(s+a)^3, a=1/2
# upper: 2alpha/(s-a)^3 <= (6/5)/(7/10)^3 and 2(1-alpha)/(s+a)^3 <= 1/(17/10)^3
up = F(6, 5) / (F(7, 10) ** 3) + F(1, 1) / (F(17, 10) ** 3)
print("uniform Phi'' upper =", float(up))
check("Phi''(s,alpha)<=4 uniform", up <= 4)
# lower: 2alpha/(s-a)^3 >= 1/(17/20)^3 (using alpha>=1/2, s-a<=0.85)
lob = F(1, 1) / (F(17, 20) ** 3)
print("uniform Phi'' lower (first term) =", float(lob))
check("Phi''(s,alpha)>=1.62 uniform", lob >= F(162, 100))

print("ALL_OK" if ok else "SOME_CHECKS_FAILED")
assert ok
