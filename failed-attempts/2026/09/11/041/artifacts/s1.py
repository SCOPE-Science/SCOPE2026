import sys
from math import isqrt, gcd
def N_val(a,b):
    return a**6 - 3*a**5*b + a**4*b**2 + 3*a**2*b**4 - a*b**5 + b**6
B=400
pts=[]
for b in range(1,B+1):
    for a in range(-B,B+1):
        if gcd(a,b)!=1: continue
        N = N_val(a,b)
        if N < 0: continue
        D = b**6
        M = N*D
        r = isqrt(M)
        if r*r==M:
            pts.append((a,b,r))
print("found", pts)
