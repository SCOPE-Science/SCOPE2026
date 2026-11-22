"""Exact symbolic checks for the period-three kinetic Glauber one-spin spectrum.

Requires Python 3 and sympy. Run: python verify.py
"""
from fractions import Fraction
from itertools import product
import sympy as S


def symbolic_checks():
    g, h, mu, z = S.symbols('g h mu z', nonzero=True)
    B = S.Matrix([[0, g/2, g/(2*z)],
                  [g/2, 0, g/2],
                  [-h*z/2, -h/2, 0]])
    characteristic = S.expand((mu*S.eye(3)-B).det())
    expected = mu**3-g*(g-2*h)*mu/4+g*g*h*(z+1/z)/8
    assert S.simplify(characteristic-expected)==0
    u=S.symbols('u')
    assert S.simplify((1-2*u)**3-27*u**2-(1+u)**2*(1-8*u))==0
    assert S.simplify(characteristic.subs({z:1,h:g/8})-(mu-g/4)**2*(mu+g/2))==0
    assert S.simplify(characteristic.subs({z:-1,h:g/8})-(mu+g/4)**2*(mu-g/2))==0
    C=B.subs({h:g/2,z:S.I})
    assert S.simplify(C**3)==S.zeros(3)
    assert S.simplify(C**2)!=S.zeros(3)
    assert C.rank()==2
    assert S.simplify((C**2)[2,0])==-g*g/8
    # The same cubic is real for every physical Fourier wavenumber.
    for kval in [S.Integer(0), S.pi/2, S.pi, 2*S.pi/3]:
        zz=S.exp(S.I*kval)
        q=S.expand(characteristic.subs(z,zz))
        qref=mu**3-g*(g-2*h)*mu/4+(g*g*h/4)*S.cos(kval)
        assert S.simplify(S.expand_complex(q-qref))==0
    return 10


def generator_checks():
    # Independent state-by-state application of the actual spin-flip generator.
    tests=0
    for n in (3,6,9):
        gamma=[Fraction(3,5),Fraction(3,5),Fraction(-1,5)]*(n//3)
        for sigma in product((-1,1),repeat=n):
            for i in range(n):
                expected=-sigma[i]+gamma[i]*(sigma[(i-1)%n]+sigma[(i+1)%n])/2
                rate=Fraction(1,2)*(1-gamma[i]*sigma[i]*(sigma[(i-1)%n]+sigma[(i+1)%n])/2)
                actual=rate*(-2*sigma[i])
                assert actual==expected
                assert rate>0
                tests+=1
    return tests


def numeric_checks():
    # A full finite-ring 1-spin linear operator is block-diagonalized by the 3-site Bloch transform.
    import numpy as np
    checks=0
    for n in (6,9,12):
        for g,h in ((.6,.03),(.6,.075),(.6,.15),(.6,.29),(.6,.45)):
            A=np.zeros((n,n),dtype=float)
            gamma=np.array([g,g,-h]*(n//3))
            for i in range(n):
                A[i,i]=-1.
                A[i,(i-1)%n]=gamma[i]/2
                A[i,(i+1)%n]=gamma[i]/2
            all_bloch=[]
            for j in range(n//3):
                z=np.exp(2j*np.pi*j/(n//3))
                B=np.array([[-1,g/2,g/(2*z)],
                            [g/2,-1,g/2],
                            [-h*z/2,-h/2,-1]],dtype=complex)
                all_bloch.extend(np.linalg.eigvals(B))
            a=np.sort_complex(np.round(np.linalg.eigvals(A),decimals=9))
            b=np.sort_complex(np.round(np.array(all_bloch),decimals=9))
            # compare via min over permutations not necessary for residual: sort real/imag lexicographically.
            a=sorted(a,key=lambda x:(round(x.real,7),round(x.imag,7)))
            b=sorted(b,key=lambda x:(round(x.real,7),round(x.imag,7)))
            assert np.max(np.abs(np.array(a)-np.array(b)))<1.e-7,(n,g,h,a,b)
            checks+=1
    return checks


if __name__=='__main__':
    a,b,c=symbolic_checks(),generator_checks(),numeric_checks()
    print(f'THREE_BATH_GLAUBER_CHECKS_PASSED symbolic={a} exact_generator={b} finite_spectra={c}')
