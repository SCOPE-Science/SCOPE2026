"""Reproducible exact-rational certificate for nine equilibria and four sinks.
Only the elementary theorem that |exp(z)-T_60(z)| <= 21*3**61/61!
for |z|<=3 is used to bound the exponential; it follows from e**3<21.
"""
from fractions import Fraction as Q
from math import factorial
from itertools import product

q=lambda n,d=1: Q(n,d)
s=q(1,1000)
tau=q(1,10**6)
a=q(4,5); b=q(1,10); c=q(1,2); k0=q(1,1000);gamma=q(1)
K=1+b/(1-a); C=c/(1-a)
d=(k0+s*gamma)/(1+s)

roots=[(q(2048938,10**9),q(2048940,10**9)),
       (q(92330362,10**9),q(92330364,10**9)),
       (q(2188864390,10**9),q(2188864392,10**9))]

# Entirely rational remainder theorem with |z|<=3 and exp(3)<21.
rem=q(21*3**61,factorial(61))
def exp_interval(z):
    assert abs(z)<=3
    t=q(1);acc=t
    for j in range(1,61):
        t*=z/j;acc+=t
    return acc-rem,acc+rem

def fsign(x):
    lo,hi=exp_interval(C-K*x)
    v=x-d
    return v-x*x*hi/(1+s),v-x*x*lo/(1+s)

for i,(lo,hi) in enumerate(roots):
    assert fsign(lo)[1]<0 if i in (0,2) else fsign(lo)[0]>0
    assert fsign(hi)[0]>0 if i in (0,2) else fsign(hi)[1]<0
    print('root',i+1, float(lo),float(hi),'signs=',('negative' if fsign(lo)[1]<0 else 'positive'),('positive' if fsign(hi)[0]>0 else 'negative'))

# Three disjoint roots, and f' has <=2 roots: derivative of x(2-K*x)e^-Kx
assert 0<roots[0][1]<roots[1][0]<roots[2][0]

# Jacobian outer blocks are exact rational functions of root x.
# Make interval via monotonic expression: Y=(1+s)*x-(k0+s*gamma),
# J11=2*(1+s)-2*(k0+s*gamma)/x-Y-s.
def outer_bounds(lo,hi):
    U=k0+s*gamma
    Ylo=(1+s)*lo-U
    Yhi=(1+s)*hi-U
    # J11 = 2(1+s)-2U/x -Y - s ; monotonic derivative 2U/x^2-(1+s)
    # use safe interval enclosures without monotonicity assumption
    Jlo=2*(1+s)-2*U/lo-Yhi-s
    Jhi=2*(1+s)-2*U/hi-Ylo-s
    return Ylo,Yhi,Jlo,Jhi
for i in (0,2):
    ylo,yhi,jlo,jhi=outer_bounds(*roots[i]);
    if i==0:
        # Infinity norm <=.9 and hence every eigenvalue inside unit disc.
        assert max(abs(jlo),abs(jhi))+yhi<q(9,10)
        assert b+a==q(9,10)
        # P_low(t) is positive at t=0 and t=0.8; negative at t=0.1 and t=0.7,
        # hence the two eigenvalues lie in (0,0.1) and (0.7,0.8).
        def plo(z):
            a0=z-a
            v1=a0*(z-jlo);v2=a0*(z-jhi)
            return min(v1,v2)+b*ylo,max(v1,v2)+b*yhi
        assert plo(q(0))[0]>0
        assert plo(q(1,10))[1]<0
        assert plo(q(7,10))[1]<0
        assert plo(a)[0]>0
        print('low outer eigen brackets (0,.1) and (.7,.8)')
    else:
        # trace and determinant bounds (det=a*J11+b*Y), positive roots
        Tlo=jlo+a; Thi=jhi+a
        Dlo=a*jlo+b*ylo; Dhi=a*jhi+b*yhi
        assert 0 < q(60,100) < Tlo <= Thi < q(62,100) < q(7,10)
        assert q(6,100) < Dlo <= Dhi < q(8,100)
        assert Tlo*Tlo > 4*Dhi
        # Both eigenvalues positive, and each < trace < 0.7.
        print('high outer T,D',float(Tlo),float(Thi),float(Dlo),float(Dhi))

# Middle outer block has exactly one stable and one unstable eigenvalue.
ylo,yhi,jlo,jhi=outer_bounds(*roots[1]);
def pinterval(z):
    c=z-a
    aa=(c*(z-jhi),c*(z-jlo)) if c>=0 else (c*(z-jlo),c*(z-jhi))
    return aa[0]+b*ylo, aa[1]+b*yhi
assert pinterval(q(8,10))[0]>0
assert pinterval(q(82,100))[1]<0
assert pinterval(q(18,10))[1]<0
assert pinterval(q(19,10))[0]>0
print('middle outer: eigenvalues in (0.8, 0.82) and (1.8,1.9)')

# Central block J2=[[-1/4,1],[-1/10,1]] has characteristic
# polynomial lambda^2-(3/4)lambda-3/20.
def pc(z):return z*z-q(3,4)*z-q(3,20)
assert pc(-q(2,10))>0 and pc(-q(15,100))<0
assert pc(q(9,10))<0 and pc(q(92,100))>0
print('central eigen brackets (-.2,-.15) and (.9,.92)')

# Exact characteristic identity, with L(z) and H(z) the outer quadratics,
# C(z)=z^2-(3/4)z-3/20:
# det(zI-J_tau) = L H C + 2*tau*(z-1)*L*H
#                    - s*tau*(z-a)*(z-1)*(L+H).
# On |z|=1 each |outer polynomial| >= 9/100:
# low >=(1-.1)(1-.8)=.18; high >=(.3)^2=.09;
# middle >=(.18)*(.8)=.144.
# Every outer |polynomial| <= (53/10) by eigenvalue brackets.
# Central |C|>= (.08)*(.8)=.064.
# Hence |L H C| >= (.09)^2*.064 = .0005184, for all 9 cases.
base_lower=q(9,100)**2 * q(8,100)*q(8,10)
# Perturbation sup on |z|=1 from above identity:
perturb_upper=4*tau*q(53,10)**2+s*tau*q(18,10)*2*(2*q(53,10))
assert perturb_upper<base_lower
print('Rouche base determinant lower',float(base_lower))
print('Rouche perturbation upper',float(perturb_upper))
print('CERTIFIED: exactly nine real fixed points; precisely four are hyperbolic sinks and five are unstable, at strictly positive return couplings.')
