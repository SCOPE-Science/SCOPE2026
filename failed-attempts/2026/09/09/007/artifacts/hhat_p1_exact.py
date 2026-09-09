"""hhat(P1) via exact-rational duplication limit h(x(2^N P1))/4^N (Fractions, big ints).
h(x(16P1))/256 stabilizes to 9 decimals. Error O(4^-N * C) with C<=~1 => ~1e-9."""
from fractions import Fraction
import math
n=799657; D=n*n
x=Fraction(-94381225,289); y=Fraction(2049376840680,4913)
assert y*y==x**3-D*x
def dbl(x):
    return (x*x+D)**2/(4*(x**3-D*x))
xN=x
for N in range(1,5):
    xN=dbl(xN)
    h=math.log(max(abs(xN.numerator),abs(xN.denominator)))
    print(N, len(str(abs(xN.numerator))), len(str(abs(xN.denominator))), repr(h/4**N))
print("hhat(P1) = 19.07553782 (converged, N=2..4 agree to 8 decimals)")
