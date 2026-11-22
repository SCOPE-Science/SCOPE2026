#!/usr/bin/env python3
"""Independent exhaustive direct evaluation for all binary states on 3-by-n tori."""
def update(z,n):
    out=0
    for i in range(n):
        east=(i+1)%n
        for r in range(3):
            a=(z>>(3*i+r))&1
            b=(z>>(3*i+(r+1)%3))&1
            c=(z>>(3*east+r))&1
            out|=(int(a+b+c>=2)<<(3*i+r))
    return out

expected={3:(14,6),4:(22,6),5:(38,60),6:(76,12)}
for n,(f_expected,p_expected) in expected.items():
    fixed=0;three=0
    for z in range(1<<(3*n)):
        a=update(z,n)
        b=update(a,n)
        c=update(b,n)
        if a==z:fixed+=1
        if c==z and a!=z:
            three+=1
            assert b!=z and b!=a
            # Structural temporal rotation, independently of transfer graph.
            rotated=0
            for i in range(n):
                for r in range(3):
                    rotated|=(((z>>(3*i+(r+1)%3))&1)<<(3*i+r))
            assert a==rotated,(n,z,a,rotated)
    assert fixed==f_expected,(n,fixed,f_expected)
    assert three==p_expected,(n,three,p_expected)
    print('n=%d configurations=%d fixed=%d primitive_period3_points=%d orbits=%d'%
          (n,1<<(3*n),fixed,three,three//3))
print('all independent direct assertions passed')
