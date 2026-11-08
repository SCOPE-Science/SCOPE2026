"""Reproducibility checks for fourth moments on zero-completed anisotropic conics.

Run: python3 verify.py. Standard library only.
Finite tests corroborate an analytic all-prime-power proof.
"""
from collections import Counter
from cmath import exp
from math import pi
from random import Random
from fractions import Fraction

PRIMES=(7,19,31,43,67,79)
seed=260805
rng=Random(seed)
checks=0
fourier=0
for q in PRIMES:
    assert q%12==7
    circle=[(x,y) for x in range(q) for y in range(q) if (x*x+y*y)%q==1]
    m=q+1
    assert len(circle)==m
    T=set(circle)
    zero=(0,0)
    S=[zero]+circle
    pairs=Counter(((a[0]+b[0])%q,(a[1]+b[1])%q) for a in circle for b in circle)
    assert pairs[zero]==m
    assert all(pairs[s]==0 for s in T) # no center/conic two-sum resonance
    assert all(n in (0,1,2,m) for n in pairs.values())
    E_C=sum(v*v for v in pairs.values())
    assert E_C==3*q*m
    completed=Counter(((a[0]+b[0])%q,(a[1]+b[1])%q) for a in S for b in S)
    E_S=sum(v*v for v in completed.values())
    assert E_S==m*(3*q+6)+1
    checks+=5

    # Exact rational optimal magnitude square ratio 3/2 on the center.
    # All antipodal products must share the phase of f(0)^2.
    # Verify the rational target energy quotient, avoiding floating point.
    B=Fraction(m,1)
    center2=Fraction(3,2)
    E=Fraction(3*q*m,1)+6*m*center2+center2*center2
    ratio=E/(B+center2)**2
    sharp=Fraction(3*(2*q+3),2*q+5)
    assert ratio==sharp
    checks+=1

    for case in range(16):
        amps={}
        if case==0:
            # Equality with arbitrary independent opposite-pair phases.
            amps[zero]=(3/2)**0.5
            for x,y in circle:
                if (x,y) in amps: continue
                phi=rng.uniform(-pi,pi)
                z=complex(exp(1j*phi))
                amps[(x,y)]=z
                amps[((-x)%q,(-y)%q)]=z.conjugate()
        else:
            amps={s:complex(rng.uniform(-2,2),rng.uniform(-2,2)) for s in S}
        conv={}
        for a in S:
            for b in S:
                t=((a[0]+b[0])%q,(a[1]+b[1])%q)
                conv[t]=conv.get(t,0j)+amps[a]*amps[b]
        Q=sum(abs(v)**2 for v in conv.values())
        P=sum(abs(v)**2 for v in amps.values())
        if case==0:
            assert abs(Q/(P*P)-float(sharp))<1e-10
        else:
            assert Q<=float(sharp)*P*P+1e-8
        # Independent structural identity using antipodal products.
        B=sum(abs(amps[z])**2 for z in circle)
        D=sum(abs(amps[z])**4 for z in circle)
        R=sum(abs(amps[z]*amps[(-z[0]%q,-z[1]%q)])**2 for z in circle)
        H=sum(amps[z]*amps[(-z[0]%q,-z[1]%q)] for z in circle)
        c=amps[zero]
        rhs=2*B*B-D-2*R+abs(c*c+H)**2+4*abs(c)**2*B
        assert abs(Q-rhs)<max(1e-8,1e-10*Q)
        # An independent exact six-term nonnegative deficit decomposition.
        sjs=[]; pjs=[]
        visited=set()
        for z in circle:
            if z in visited: continue
            zz=((-z[0])%q,(-z[1])%q)
            visited.add(z); visited.add(zz)
            sjs.append(abs(amps[z])**2+abs(amps[zz])**2)
            pjs.append(abs(amps[z]*amps[zz]))
        J=m//2
        psum=sum(pjs)
        y=abs(c)**2
        massvar=sum(v*v for v in sjs)-B*B/J
        prodvar=2*(sum(v*v for v in pjs)-psum*psum/J)
        prodgap=(4-4/m)*(B*B/4-psum*psum)
        centergap=4*y*(B/2-psum)
        phasegap=(y+2*psum)**2-abs(c*c+H)**2
        massgap=(2+3/m)*(B-2*m/(2*m+3)*(B+y))**2
        terms=(massvar,prodvar,prodgap,centergap,phasegap,massgap)
        assert all(t>=-max(1e-8,1e-10*Q) for t in terms)
        assert abs(sum(terms)-(float(sharp)*P*P-Q))<max(1e-8,1e-9*Q)
        checks+=3
        if q in (7,19) and case in (0,1,2):
            # Fourier orthogonality with a genuinely independent computation.
            Z=[exp(2j*pi*k/q) for k in range(q)]
            tot=0.
            for u in range(q):
                for v in range(q):
                    F=sum(amps[(x,y)]*Z[(u*x+v*y)%q] for x,y in S)
                    tot+=abs(F)**4
            assert abs(tot/(q*q)-Q)<1e-7*max(1.,Q)
            fourier+=1
print(f'COMPLETED_ANISOTROPIC_CONIC_VERIFY_PASS fields={len(PRIMES)} checks={checks} independent_fourier={fourier} prime_fields={PRIMES}')
