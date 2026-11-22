"""Reproduce exact boundaries and independent numerical checks for a two-assay, three-target model."""
from fractions import Fraction
from math import exp, expm1, log, sqrt, isfinite
import random

B = (Fraction(1), Fraction(2), Fraction(3))
D = (Fraction(-1,10), Fraction(7381,5800), Fraction(-10101,5800))
A = tuple(B[i]+D[i] for i in range(3))
assert all(x>0 for x in A+B)
assert A[1]>A[2] and -D[2]>D[1]>0 and D[0]<0

# Polynomial algebra over rational numbers, coefficients in ascending powers.
def add(p,q):
    r=[Fraction(0)]*max(len(p),len(q))
    for i,x in enumerate(p):r[i]+=x
    for i,x in enumerate(q):r[i]+=x
    return r
def mul(p,q):
    r=[Fraction(0)]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):r[i+j]+=a*b
    return r

def scale(p,c):return [c*x for x in p]

# The common denominator of sum_i d_i/(t^(i+1)-1) is (t-1)(t^2-1)(t^3-1).
term=[]
for i in range(3):
    product=[Fraction(1)]
    for j in range(3):
        if i!=j:
            poly=[Fraction(-1)]+[Fraction(0)]*(j)+[Fraction(1)]
            product=mul(product,poly)
    term=add(term,scale(product,D[i]))
expected=scale(mul(mul([-10,1],[-6,5]),[55,116]),Fraction(-1,5800))
# Expected above is numerator after cancellation of common (t-1)^2:
assert term==mul(expected,mul([-1,1],[-1,1])),(term,expected)

# E'(0) = z(-580+7381 z-10101 z^2)/5800, z=exp(-T).
assert [D[0],D[1],D[2]]==[Fraction(-580,5800),Fraction(7381,5800),Fraction(-10101,5800)]
Q=lambda z: -580+7381*z-10101*z*z
assert Q(Fraction(5,6))<0 and Q(Fraction(1,10))>0 and Q(Fraction(1,100))<0
assert 7381**2-4*10101*580 == 31044841
zm=(7381-sqrt(31044841))/20202
zp=(7381+sqrt(31044841))/20202
assert 0<zm<.1<zp<5/6<1
F_on,F_off=log(1.2),log(10)
E_on,E_off=-log(zp),-log(zm)
assert F_on<E_on<F_off<E_off

BF=tuple(map(float,B)); DF=tuple(map(float,D)); AF=tuple(map(float,A))
def mu(T,x,i): return BF[i]*T+DF[i]*x
def der(T,x,which):
    if which=='all': return sum(DF[i]/expm1(mu(T,x,i)) for i in range(3))
    return sum(DF[i]*exp(-mu(T,x,i)) for i in range(3))
def objective(T,x,which):
    vals=[-expm1(-mu(T,x,i)) for i in range(3)]
    if which=='all': return vals[0]*vals[1]*vals[2]
    return sum(vals)
def optimizer(T,which):
    if der(T,0,which)<=0: return 0.
    assert der(T,T,which)<0
    lo,hi=0.,T
    for _ in range(65):
        mid=(lo+hi)/2
        if der(T,mid,which)>0:lo=mid
        else:hi=mid
    return (lo+hi)/2

rng=random.Random(20261121)
checked=0
for _ in range(1800):
    T=exp(rng.uniform(log(.02),log(50)))
    for which in ('all','richness'):
        opt=optimizer(T,which)
        optval=objective(T,opt,which)
        for _ in range(18):
            x=rng.random()*T
            # Error tolerance accounts for floating point arithmetic.
            assert objective(T,x,which)<=optval+3e-12, (T,which,x,opt)
            checked+=1
        d0=der(T,0,which)
        if which=='all': expected_sign=(F_on<T<F_off)
        else: expected_sign=(E_on<T<E_off)
        if abs(d0)>5e-10:
            assert (d0>0)==expected_sign,(T,which,d0)
        assert der(T,T,which)<0,(T,which)

for T,aim_all,aim_rich in ((.1,False,False),(.3,True,False),(.6,True,True),(2.35,False,True),(2.8,False,False)):
    xall=optimizer(T,'all');xr=optimizer(T,'richness')
    assert (xall>1e-7)==aim_all and (xr>1e-7)==aim_rich,(T,xall,xr)
    print('T=',T,'optimal_A_fraction_all=',round(xall/T,9),'optimal_A_fraction_richness=',round(xr/T,9))

# One-/two-taxon obstruction is analytic in RESULT.md: for distinct baseline rates
# the ratio (exp(b2*T)-1)/(exp(b1*T)-1) is strictly monotone.
# Test the ratio's derivative on a broad positive mesh as a sanity check only.
for b1,b2 in ((.5,1.),(1.,3.),(2.,5.),(1.,.5)):
    vals=[]
    for j in range(1,300):
        T=j/100
        vals.append(expm1(b2*T)/expm1(b1*T))
    sense=1 if b2>b1 else -1
    assert all(sense*(vals[k+1]-vals[k])>0 for k in range(len(vals)-1))

print('exact symbolic identities verified')
print('thresholds',format(F_on,'.12f'),format(E_on,'.12f'),format(F_off,'.12f'),format(E_off,'.12f'))
print('finite objective comparisons',checked)
print('analytic proof, not finite experiment, establishes uniqueness and sharpness')
