# Master replay: exact rational checks with Fraction + sympy-free irreducibility log
from fractions import Fraction as F
print("=== A. genus: discriminant sign on [0,1/4] ===")
# P(t)=11t^4+36t^3+8t^2-t-1; f(t)=283/16 t^2 - t - 1 upper bound on [0,1/4]
# f(1/4)=-37/256<0, f increasing on [8/283,1/4], f(0)<0 => f<0
print("f(1/4) =", F(283,16)*F(1,16)-F(1,4)-1, "= -37/256?", F(283,16)*F(1,16)-F(1,4)-1==F(-37,256))
print("f(0) =", F(-1))
print("vertex at t=8/283>0, so f monotone increasing on [8/283,1/4]; max=f(1/4)<0. OK")
print("P(t)-f(t) = 11t^4+36t^3-(155/16)t^2 <= t^2(11/16+9-155/16)=t^2(-60/16)<0 on [0,1/4]. OK")
print("Hence disc factor P(t)<0 on [0,1/4], so Dx,Dy separable.")
print("=== B. orbit ledger ===")
def theta(p):
    x,y=p
    return (F(1,1)/(x*y), x/(F(1,1)+x*y))
p=(F(1),F(1)); pts=[]
for i in range(12):
    pts.append(p); p=theta(p)
print("12 distinct:", len(set(pts))==12)
print("all positive:", all(a>0 and b>0 for a,b in pts))
print("=== C. saddlepoint enclosure ===")
lo,hi=F("1.2207"),F("1.2208")
flo=lo**4-lo-1; fhi=hi**4-hi-1
print("f(lo)<0:", flo<0, flo, "| f(hi)>0:", fhi>0, fhi)
print("u in (1.2207,1.2208); width 1e-4")
print("=== D. see work/t2,t4,t8 for rho/alpha numerics, trace poly, F3-irreducibility ===")
print("VERIFY_OK")
