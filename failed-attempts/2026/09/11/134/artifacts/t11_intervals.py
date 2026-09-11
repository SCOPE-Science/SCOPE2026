from fractions import Fraction as F
lo,hi=F("1.2207"),F("1.2208")
# S(u)=2/u+u^2+1/u^2, decreasing or increasing on interval? S'(u)=-2/u^2+2u-2/u^3; check sign via exact
for s in (lo,hi):
    Sp=-2/s**2+2*s-2/s**3
    print(s, "S'=",Sp, float(Sp))
# S' sign: evaluate numerator N=-2u+2u^4-2 =2(u^4-u-1)=2f(u); f(lo)<0,f(hi)>0 so S' changes sign inside!
# So minimum inside interval; bound Smin by min(endpoint vals) above and below by S(u*)>=?
# Upper bound: min(S(lo),S(hi)); lower bound: use S(u)>= 2/u+u^2+1/u^2 with u in [lo,hi]: 1/u in [1/hi,1/lo] etc.
Slo=2/lo+lo**2+F(1,1)/lo**2; Shi=2/hi+hi**2+F(1,1)/hi**2
print("S(lo)=",Slo,float(Slo)); print("S(hi)=",Shi,float(Shi))
# crude lower bound: 2/hi + lo^2 + 1/hi^2
Slow=2/hi+lo**2+F(1,1)/hi**2
print("lower crude=",Slow,float(Slow))
# r^2 = u/(2(u^4+u+1)); monotone? numerator/denom; bound by endpoints with u increasing: f inc? check derivative sign on interval
# g(u)=u/(2(u^4+u+1)); g'(u)=( (u^4+u+1) - u(4u^3+1) )/(2(...)^2) = (1-3u^4)/(2D^2) <0 since u^4>1. So decreasing.
print("u^4 lo:",lo**4, " 3u^4>1 so g decreasing")
glo=lo/(2*(lo**4+lo+1)); ghi=hi/(2*(hi**4+hi+1))
print("g(lo)=",glo,float(glo),"g(hi)=",ghi,float(ghi))
print("r in (sqrt(ghi),sqrt(glo)) =", (float(ghi)**0.5, float(glo)**0.5))
import math
print("r bounds:", math.sqrt(float(ghi)), math.sqrt(float(glo)))
# alpha = pi/acos(-r); acos decreasing in (-r)? -r in (-0.371,-0.370); acos decreasing so alpha=pi/acos increasing in r? acos(-r) decreasing in r? d/dr acos(-r)=1/sqrt(1-r^2)>0, so acos increasing in r, alpha decreasing in r.
# So alpha in (pi/acos(-r_lo'), pi/acos(-r_hi')) with r_lo=sqrt(ghi), r_hi=sqrt(glo)
rlo=math.sqrt(float(ghi)); rhi=math.sqrt(float(glo))
print("alpha in:", math.pi/math.acos(-rlo), math.pi/math.acos(-rhi))
