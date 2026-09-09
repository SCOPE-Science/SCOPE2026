"""S5d (completed window): integral x=a (d=1), |a|<=1e6 on Y^2=a^3-Da, D=799657^2. Exact isqrt."""
import math
n=799657; D=n*n; AMAX=10**6
hits=[]
for a in range(-AMAX,AMAX+1):
    m=a*(a*a-D)
    if m<0: continue
    r=math.isqrt(m)
    if r*r==m:
        hits.append(a)
print("hits:",hits)
