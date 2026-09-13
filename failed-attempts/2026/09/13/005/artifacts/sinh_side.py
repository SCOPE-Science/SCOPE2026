"""Independent check of route (i): GJV sinh closed formula P_{g,n} at (g,n)=(2,4), mu=(3,2,1,1).
h = d^{2g-2+n} [t^{2g}] prod_i S(t mu_i)/S(t), S(x)=sinh(x/2)/(x/2).
Exact rational arithmetic on the Taylor series up to t^4."""
from fractions import Fraction
N=6
# series of S(x) in x up to x^4: S = 1 + x^2/24 + x^4/1920
def S_series(mu):
    return [Fraction(1), Fraction(0), Fraction(mu*mu,24), Fraction(0), Fraction(mu**4,1920), Fraction(0)]
def mul(a,b):
    c=[Fraction(0)]*N
    for i in range(N):
        for j in range(N-i):
            c[i+j]+=a[i]*b[j]
    return c
num=[Fraction(1)]+[Fraction(0)]*(N-1)
for mu in (3,2,1,1):
    num=mul(num,S_series(mu))
# 1/S(t) series: S(t)=1+t^2/24+t^4/1920 -> inverse
S1=S_series(1)
inv=[Fraction(0)]*N; inv[0]=Fraction(1)
for k in range(1,N):
    s=Fraction(0)
    for j in range(1,k+1): s+=S1[j]*inv[k-j]
    inv[k]=-s
P=mul(num,inv)
print("P coeffs:",P)
h=Fraction(7**(2*2-2+4))*P[4]
print("h =",h, float(h))
open("output/artifacts/sinh_result.txt","w").write(f"P4={P[4]}\nh={h}\n")
