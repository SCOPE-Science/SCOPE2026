"""Exact rational certificate: reciprocal positivity for the standard odd [m/m]
Padé denominators of the exponential, m=9,13.

Run: python3 positivity_certificate.py
Uses only Python standard library. Rouché bounds are exact rational comparisons;
no floating-point test is used as a proof.
"""
from fractions import Fraction as F
from math import factorial, comb, isqrt

# The centers were selected numerically but are checked solely by exact rational
# Rouché tests. All conjugates and the real center are listed explicitly.
CENTERS = {
    9: [("12.594038", "0"), ("12.258736", "3.475697"), ("11.208844", "6.996314"), ("9.276880", "10.634543"), ("5.958522", "14.582927")],
   13: [("17.895419", "0"), ("17.660504", "3.473333"), ("16.941184", "6.967737"), ("15.688761", "10.509807"), ("13.800746", "14.141289"), ("11.061362", "17.944496"), ("6.899734", "22.147857")],
}
RADIUS = F(1, 1000)
MOD_SCALE = 10**18

# Complex rational operations. Tuples (real, imaginary).
def add(x,y): return (x[0]+y[0], x[1]+y[1])
def mul(x,y): return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def norm_up(x): return abs(x[0])+abs(x[1])
def sqnorm(x): return x[0]*x[0]+x[1]*x[1]
def rational_sqrt_floor(t):
    assert t >= 0
    q = (t.numerator*MOD_SCALE**2)//t.denominator
    a = F(isqrt(q), MOD_SCALE)
    assert a*a<=t<(a+F(1,MOD_SCALE))**2
    return a

def pade(m):
    return [(-1)**j*F(comb(m,j)*factorial(2*m-j),factorial(2*m)) for j in range(m+1)]

def centered_taylor(q,c):
    m=len(q)-1
    return [complex_sum(mul((q[j]*comb(j,k),F(0)),cpow(c,j-k)) for j in range(k,m+1)) for k in range(m+1)]

def complex_sum(items):
    ans=(F(0),F(0))
    for item in items: ans=add(ans,item)
    return ans

def cpow(c,n):
    t=(F(1),F(0))
    for _ in range(n):t=mul(t,c)
    return t

def circle_cert(q,c):
    b=centered_taylor(q,c)
    # Rouché: p(c+w) and p'(c)w have same zeros in disk if strict.
    remainder = norm_up(b[0])+sum(norm_up(b[j])*RADIUS**j for j in range(2,len(b)))
    linear_lower = rational_sqrt_floor(sqnorm(b[1]))*RADIUS
    assert remainder < linear_lower, 'Rouché fails'
    shift=sum(j*norm_up(b[j])*RADIUS**(j-1) for j in range(2,len(b)))
    derivative_lower=rational_sqrt_floor(sqnorm(b[1]))-shift
    derivative_upper=norm_up(b[1])+shift
    assert derivative_lower>0
    modulus_lower=rational_sqrt_floor(sqnorm(c))-RADIUS
    modulus_upper=rational_sqrt_floor(sqnorm(c))+F(1,MOD_SCALE)+RADIUS
    assert modulus_lower>0
    return modulus_lower,modulus_upper,derivative_lower,derivative_upper

def prove(m):
    assert m in CENTERS
    q=pade(m)
    # Count a real root and both members of every conjugate pair.
    centers=[(F(re),F(im)) for re,im in CENTERS[m]]
    assert centers[0][1]==0 and len(centers)==(m+1)//2
    allcenters=[centers[0]]
    for c in centers[1:]:
        assert c[1]>0
        allcenters += [c,(c[0],-c[1])]
    assert len(allcenters)==m
    for i,x in enumerate(allcenters):
        for y in allcenters[i+1:]:
            assert sqnorm(add(x,(-y[0],-y[1])))>4*RADIUS**2
    certs=[circle_cert(q,c) for c in allcenters]
    real_jet=centered_taylor(q,centers[0])
    real_derivative_shift=sum(j*norm_up(real_jet[j])*RADIUS**(j-1) for j in range(2,len(real_jet)))
    assert real_jet[1][1]==0 and real_jet[1][0]+real_derivative_shift<0, "real residue sign"
    l0,u0,dl0,du0=certs[0]
    assert l0>0 and u0>0
    A_lower=F(1)/(u0*du0)
    second=[]
    for lo,hi,dl,du in certs[1:]:
        assert lo>u0, 'dominant root condition fails'
        second.append((F(1)/(lo*dl),u0/lo))
    # Residue partial fraction of 1/q: c_n = sum_j B_j z_j^{-n}.
    # The real pole contributes >=A_lower/u0^n and all others are bounded.
    N=0
    while True:
        s=sum(b*r**N for b,r in second)
        if s < A_lower: break
        N+=1
        assert N<3000
    # Fully exact small-index check. Both the finite cutoff and tail are proven.
    coefficients=[F(1)]
    for n in range(1,N):
        coefficients.append(-sum(q[j]*coefficients[n-j] for j in range(1,min(m,n)+1)))
        assert coefficients[-1]>0, (m,n)
    assert sum(b*r**N for b,r in second)<A_lower
    return {"m":m,"poles":m,"small_indices_checked":N,"tail_from":N,
        "real_pole_upper":str(u0),"other_pole_min_lower":str(min(c[0] for c in certs[1:])),
        "dominant_residue_lower":str(A_lower),"tail_bound_ratio":float(sum(b*r**N for b,r in second)/A_lower)}

if __name__=='__main__':
    for m in CENTERS:
        out=prove(m)
        print('PASS m=%d poles=%d exact_coefficients=%d tail_from=%d tail_bound_ratio=%.6g'%
            (m,out['poles'],out['small_indices_checked'],out['tail_from'],out['tail_bound_ratio']))
    print('CERTIFICATE_OK')
