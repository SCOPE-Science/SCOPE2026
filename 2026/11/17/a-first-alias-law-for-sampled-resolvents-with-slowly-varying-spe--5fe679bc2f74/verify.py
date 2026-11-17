#!/usr/bin/env python3
"""Supplementary scalar checks of a Fourier multiplier; not a theorem certificate."""
import math
import cmath

def h(z):
    if abs(z)<1.0e-5:
        return z/12-z**3/720+z**5/30240
    return 1/(-cmath.expm1(-z))-.5-1/z if hasattr(cmath,'expm1') else 1/(1-cmath.exp(-z))-.5-1/z

def error_at(T, frequency, damping, lam=1.0):
    z=T*(lam+damping(abs(frequency)))-1j*T*frequency
    return abs(T*h(z))

def run():
    profiles={
        'sqrt-frequency': lambda r:math.sqrt(r),
        'log-frequency': lambda r:math.log1p(r),
        'sqrt-log-frequency':lambda r:math.sqrt(math.log1p(r)),
        'bounded-damping':lambda r:1.0-math.exp(-r),
    }
    for name,a in profiles.items():
        samples=[]
        for T in (0.1,0.01,0.001):
            frequency=2*math.pi/T
            predicted=1/(1+a(frequency))
            ratio=error_at(T,frequency,a)/predicted
            assert .9 < ratio < 1.14, (name,T,ratio)
            samples.append(round(ratio,6))
        print(name,'first-alias ratios=',samples)
    assert abs(h(1e-7)-(1e-7)/12)<1e-16
    print('Supplementary cases passed; theorem requires analytical proof.')

if __name__=='__main__':run()
