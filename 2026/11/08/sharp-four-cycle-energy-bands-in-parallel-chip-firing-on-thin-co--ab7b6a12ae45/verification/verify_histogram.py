"""Independent group-histogram exhaustive check for all K_{2,b} primitive 4 states.
Each right-side histogram contributes its multinomial number of labelled states.
"""
from math import factorial, comb
from collections import Counter

def step(a,c,h,b):
    fa=(a>=b);fc=(c>=b);nfire=h[2]+h[3]
    h2=[0,0,0,0]
    for j,qty in enumerate(h):h2[j+fa+fc-2*(j>=2)]+=qty
    return a+nfire-b*fa,c+nfire-b*fc,tuple(h2)

def expected(b):
    out=Counter()
    for r in range(1,b):
        for i in range(r):
            for j in range(b-r):
                m=2*b+i+j
                out[m]+=4*comb(b,r)
                out[7*b-2-m]+=4*comb(b,r)
    return out

for b in range(2,13):
    fact=[factorial(t) for t in range(b+1)]
    obs=Counter()
    for z0 in range(b+1):
        for z1 in range(b-z0+1):
            for z2 in range(b-z0-z1+1):
                z3=b-z0-z1-z2
                h=(z0,z1,z2,z3)
                wt=fact[b]//(fact[z0]*fact[z1]*fact[z2]*fact[z3])
                for a in range(2*b):
                    for c in range(2*b):
                        s=(a,c,h)
                        s2=step(*step(*s,b),b)
                        s4=step(*step(*s2,b),b)
                        if s4==s and s2!=s:
                            m=a+c+z1+2*z2+3*z3
                            obs[m]+=wt
    assert obs==expected(b),(b,obs,expected(b))
    print('b=%d total=%d bins=%d'%(b,sum(obs.values()),len(obs)))
print('HISTOGRAM_OK')
