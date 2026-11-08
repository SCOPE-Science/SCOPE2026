#!/usr/bin/env python3
"""Independent part-count dynamics, exact binomial census, and Gaussian scaling."""
from math import comb, pi, atan, sqrt


def transition(x, n):
    total=sum(x)
    return tuple(n if total-v>n else 0 if total-v<n else v for v in x)


def formula(n):
    return 3*sum(comb(n,a)*comb(n,n-a)*comb(n,c)
                 for a in range(n+1) for c in range(n+1)
                 if min(a,n-a)<c<max(a,n-a))

for n in range(1,31):
    basin=0; immediate_period2=0; half=0
    for a in range(n+1):
        for b in range(n+1):
            for c in range(n+1):
                x=(a,b,c)
                y=transition(x,n)
                z=transition(y,n)
                zz=transition(z,n)
                zzz=transition(zz,n)
                assert z == zzz, (n,x,z,zzz)
                w=comb(n,a)*comb(n,b)*comb(n,c)
                if z != zz:
                    basin+=w
                    if x == z: immediate_period2+=w
                elif z not in [(0,0,0),(n,n,n)]:
                    assert x == z == (n//2,)*3 and n%2==0
                    half+=w
    assert basin==formula(n),(n,basin,formula(n))
    assert immediate_period2==6*(2**n-2),(n,immediate_period2)
    assert half==(comb(n,n//2)**3 if n%2==0 else 0)
    if n <= 12 or n in (20,30): print(f"n={n} basin={basin} periodic_states={immediate_period2} half_fixed={half}")
constant=6/(pi**1.5)*atan(1/sqrt(2))
for n in (100,200,500):
    # Full exact big integer count; same formula as tested against count-level iteration.
    p=formula(n)/(8**n)
    print(f"n={n}, sqrt(n)*basin_probability={sqrt(n)*p:.12f}; limit={constant:.12f}")
print('COMPRESSED_CHECK_PASS')
