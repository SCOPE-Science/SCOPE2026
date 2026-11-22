#!/usr/bin/env python3
"""Exact cyclotomic-frequency and endpoint projection check for the quartic graph."""
from collections import Counter
P=7
S=[(x,pow(x,4,P)) for x in range(P)]

def cycloint(exponents):
    """Reduce a rational integer sum of seventh roots modulo Phi_7."""
    c=Counter(t%P for t in exponents)
    return tuple(c[j]-c[6] for j in range(6))

def abs_square(c):
    v=Counter((i-j)%P for i in range(P) for j in range(P) for _ in range(c[i]*c[j]))
    d=tuple(v[t]-v[6] for t in range(6))
    assert all(q==0 for q in d[1:])
    return d[0]

mag=Counter(); zeros=[]
for u in range(P):
  for v in range(P):
    e=[(u*x+v*y)%P for x,y in S]
    count=Counter(e)
    m=abs_square(count)
    mag[m]+=1
    if m==0: zeros.append((u,v))
assert mag=={49:1,14:12,7:18,0:18}
H={1,2,4}
chi=lambda x: 0 if x%P==0 else (1 if x%P in H else -1)
assert set(zeros)=={(u,v) for u in range(P) for v in range(P)
                   if chi(u+v)*chi(u-v)==1}

kernel_numerators={}
for x in range(P):
 for y in range(P):
    h=cycloint([(u*x+v*y)%P for u,v in zeros])
    assert all(z==0 for z in h[1:])
    kernel_numerators[(x,y)]=(49 if (x,y)==(0,0) else 0)-h[0]
assert Counter(kernel_numerators.values())=={31:1,3:30,-4:18}
assert sum(abs(v) for v in kernel_numerators.values())==193
print('Fourier squared magnitudes:',dict(sorted(mag.items())))
print('range projection kernel numerator multiplicities:',dict(sorted(Counter(kernel_numerators.values()).items())))
print('sharp projection L1/Linf norm: 193/49')
