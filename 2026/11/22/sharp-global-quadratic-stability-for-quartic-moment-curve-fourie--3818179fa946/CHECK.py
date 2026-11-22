"""Independent finite tests of a four-draw rearrangement remainder.
Run: python3 CHECK.py. Only Python standard-library dependencies.
"""
from fractions import Fraction as F
from itertools import product
from collections import Counter
from math import factorial, comb, pi
import cmath


def elementary(p, degree):
    v=[F(1)]+[F(0)]*degree
    for x in p:
        for j in range(degree,0,-1): v[j]+=x*v[j-1]
    return v


def expected_direct(p):
    d=4; v=F(0)
    for t in product(range(len(p)),repeat=d):
        mult=Counter(t)
        arrangements=F(factorial(d))
        for n in mult.values(): arrangements=F(arrangements,factorial(n))
        pr=F(1)
        for x in t: pr*=p[x]
        v+=pr*arrangements
    return v


def expected_e(p):
    e=elementary(p,4)
    return F(1)+12*e[2]+6*e[2]**2+60*e[3]+132*e[4]


def expected_power(p):
    s2=sum(x*x for x in p); s3=sum(x**3 for x in p); s4=sum(x**4 for x in p)
    return 24-72*s2+18*s2*s2+64*s3-33*s4


def evaluate(p):
    q=len(p)
    assert sum(p)==1 and all(x>=0 for x in p)
    h=expected_direct(p)
    assert h==expected_e(p)==expected_power(p),(p,h,expected_e(p),expected_power(p))
    a=24-F(72,q)+F(82,q*q)-F(33,q**3)
    c=23-F(49,q)+F(33,q*q)
    v=sum((x-F(1,q))**2 for x in p)
    rem=a-h-c*v
    assert rem>=0,(p,rem)
    if rem==0:
        assert len(set(p))==1 or sum(x>0 for x in p)==1,(p,rem)
    if len(set(p))==1 or sum(x>0 for x in p)==1:
        assert rem==0,(p,rem)
    assert h<=1+2*c*elementary(p,4)[2]
    return rem


def compositions(n,k):
    if k==1:
        yield (n,);return
    for j in range(n+1):
        for tail in compositions(n-j,k-1): yield (j,)+tail


def direct_fourier(p, phases):
    q=len(p); z=cmath.exp(2j*pi/q)
    coeff=[((float(q*float(v)))**.5)*phases[i] for i,v in enumerate(p)]
    # Since f norms have 1/q sum |f|^2 =1, check Fourier eighth moment.
    tot=0.0
    for x in product(range(q),repeat=4):
        e=sum(coeff[t]*z**(sum(x[j]*pow(t,j+1,q) for j in range(4))%q) for t in range(q))/q
        tot+=abs(e)**8
    return tot


def main():
    cases=0
    for q in range(2,6):
        for total in [1,2,3,4,5,6,8]:
            for z in compositions(total,q):
                p=tuple(F(v,total) for v in z)
                evaluate(p); cases+=1
    examples=0
    for q in [5,7]:
        vecs=[[F(1,q)]*q,[F(1)]+[F(0)]*(q-1),[F(i+1,sum(range(1,q+1))) for i in range(q)]]
        for p in vecs:
            phases=[cmath.exp(2j*pi*i*i/(q+1)) for i in range(q)]
            v=direct_fourier(p,phases)
            exact=float(expected_direct(p))
            assert abs(v-exact)<5e-8*(1+exact),(q,p,v,exact)
            examples+=1
    # Verify the pairwise Schur derivative numerator algebra and sign for sample vectors.
    deriv_tests=0
    for q in range(3,7):
        for z in compositions(5,q):
            p=[F(v,5) for v in z]
            for i in range(q):
                for j in range(i+1,q):
                    others=[p[k] for k in range(q) if k not in (i,j)]
                    ez=elementary(others,4)
                    for r in (3,4):
                        numerator=ez[r-2]*ez[2]-ez[r]+(p[i]+p[j])*(ez[r-2]*ez[1]-ez[r-1])
                        assert numerator>=0, (q,p,r,i,j,numerator)
                        deriv_tests+=1
    print(f'CHECK_OK exact_probability_vectors={cases} complex_Fourier_eighth_moments={examples} Schur_derivative_checks={deriv_tests}')

if __name__=='__main__':main()
