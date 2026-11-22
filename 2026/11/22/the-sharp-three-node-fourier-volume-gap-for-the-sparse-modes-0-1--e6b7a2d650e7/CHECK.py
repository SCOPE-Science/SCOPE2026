"""Supplementary checks for a sparse Fourier three-node determinant theorem.
Standard-library only; random/numeric tests are not proofs of global optimality.
"""
import cmath
import itertools
import math
import random
from fractions import Fraction

checks=0

def check(condition, message):
    global checks
    checks+=1
    assert condition, message

def poly_eval(p,x):
    return sum(c*x**i for i,c in enumerate(p))

def poly_mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c

def derivative(a):
    return [i*a[i] for i in range(1,len(a))]

# Exact derivative identities for the three r-branch polynomials.
r=[0,1]
fminus=[0,0,1]
for factor in [[1,-1],[1,2,1],[27,27,9,1]]:
    fminus=poly_mul(fminus,factor)
expected=poly_mul([-2],poly_mul([0,1],poly_mul([1,1],poly_mul([9,6,1],[-3,-4,7,4]))))
check(derivative(fminus)==expected,"minus-branch derivative")
fplus=[0,0,1]
for factor in [[27,-27,9,-1],[1,-2,1],[1,1]]:
    fplus=poly_mul(fplus,factor)
expected=poly_mul([-2],poly_mul([0,1],poly_mul([9,-6,1],poly_mul([-1,1],[3,-4,-7,4]))))
check(derivative(fplus)==expected,"plus-branch derivative")

# Exact bracket inequalities and uniqueness conditions.
for frac,sign in [(Fraction(3,4),-1),(Fraction(4,5),1)]:
    check(sign*(4*frac**3+7*frac**2-4*frac-3)>0,"cubic bracket")
check(poly_eval([-27,0,22,16,5],Fraction(5,6))<0,"left clipping root")
check(poly_eval([-27,0,22,-16,5],Fraction(8,5))<0,"right root lower")
check(poly_eval([-27,0,22,-16,5],Fraction(9,5))>0,"right root upper")
check(Fraction(8089,432)**2/Fraction(16)<22,"middle-branch upper bound")
check(Fraction(1654191,100000)<22,"high-branch upper bound")
check(poly_eval(fminus,Fraction(3,4))>22,"low branch witness")

lo,hi=.75,.8
for _ in range(100):
    mid=(lo+hi)/2
    if 4*mid**3+7*mid**2-4*mid-3 < 0:lo=mid
    else:hi=mid
rho=(lo+hi)/2
angle=math.acos(-(1+rho)/2)
sharp=rho*rho*(1-rho)*(1+rho)**2*(3+rho)**3
check(abs(sharp-22.906751936366292)<1e-11,"sharp value")


def det3(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
           -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
           +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))

def volume(z,m=4):
    return abs(det3([[1,w,w**m] for w in z]))**2

z_opt=[1,cmath.exp(1j*angle),cmath.exp(-1j*angle)]
check(abs(volume(z_opt)-sharp)<1e-11,"attainment")
check(abs(sum(z_opt)+rho)<1e-11,"symmetric sum")

rng=random.Random(250411)
for _ in range(2000):
    a,b,c=(rng.random()*2*math.pi for _ in range(3))
    z=[cmath.exp(1j*t) for t in (a,b,c)]
    S=sum(z)
    P=z[0]*z[1]+z[1]*z[2]+z[2]*z[0]
    V=math.prod(abs(z[j]-z[i])**2 for i,j in ((0,1),(0,2),(1,2)))
    h2=S*S-P
    d=volume(z)
    check(abs(d-V*abs(h2)**2)<1e-9,"Schur product")
    check(d<sharp+1e-8,"random no larger competitor")

# Independent dense angular grid, with one node fixed by rotation.
for i in range(241):
    p=2*math.pi*i/240
    zp=cmath.exp(1j*p)
    for j in range(241):
        q=2*math.pi*j/240
        check(volume((1,zp,cmath.exp(1j*q)))<=sharp+1e-8,"grid competitor")

# Analytic arithmetic criterion, checked on representative equilateral samples.
w=cmath.exp(2j*math.pi/3)
for m in range(2,61):
    val=volume((1,w,w*w),m)
    check(abs(val-(27 if m%3==2 else 0))<1e-8,"equilateral tightness pattern")

# Rotation and permutation equality tests.
for _ in range(50):
    eta=cmath.exp(1j*rng.uniform(-math.pi,math.pi))
    base=[eta*x for x in z_opt]
    for perm in itertools.permutations(base):
        check(abs(volume(perm)-sharp)<1e-9,"equality orbit")

print("CHECKS_PASSED",checks)
print("rho",format(rho,'.16f'))
print("angle",format(angle,'.16f'))
print("squared_determinant",format(sharp,'.16f'))
print("normalized_squared_determinant",format(sharp/27,'.16f'))
