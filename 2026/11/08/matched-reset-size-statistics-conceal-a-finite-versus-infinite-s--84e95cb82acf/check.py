"""Reproducible algebraic and numerical checks for the two random-reset laws."""
from fractions import Fraction as Q
from math import exp, log, isclose

A = ((Q(0), Q(1, 2)), (Q(2), Q(1, 2)))
B = ((Q(1, 2), Q(4, 5)), (Q(3), Q(1, 5)))
checks = 0

def check(condition, reason):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(reason)

def moment(law, power):
    return sum((w * u**power for u, w in law), Q(0))

def amp_moment(law, s, power):
    return sum((w * (1-s*u)**power for u,w in law), Q(0))

def psi_scaled(law, s, p):
    return p/2 + (sum(float(w)*(1-float(s*u))**p for u,w in law)-1)/float(s)

def root(law, s):
    low=2.0
    high=2.0/float(s)
    check(psi_scaled(law, s, low)<0, 'finite variance')
    check(psi_scaled(law, s, high)>0, 'upper threshold')
    for _ in range(90):
        mid=(low+high)/2
        if psi_scaled(law, s, mid)>0: high=mid
        else: low=mid
    return (low+high)/2

for law in (A,B):
    check(sum(w for _,w in law)==1, 'normalization')
    check(moment(law,1)==1, 'matching first reset amplitude moment')
    check(moment(law,2)==2, 'matching second reset amplitude moment')
s=Q(1,4)
check(amp_moment(A,s,2)==Q(5,8),'A second multiplier moment')
check(amp_moment(B,s,2)==Q(5,8),'B second multiplier moment')
check(amp_moment(A,s,4)==Q(17,32),'A fourth multiplier moment')
check(amp_moment(B,s,4)==Q(481,1024),'B fourth multiplier moment')
check(Q(2)+4*(amp_moment(A,s,4)-1)==Q(1,8),'A fourth growth exponent')
check(Q(2)+4*(amp_moment(B,s,4)-1)==-Q(31,256),'B fourth growth exponent')
check(12*4*256/Q(31)==Q(12288,31),'fourth spatial moment for B at D=lambda=1')
for s in (Q(1,20),Q(1,10),Q(1,6),Q(1,4),Q(3,10)):
    for n in range(3,36):
        check(amp_moment(A,s,n)>amp_moment(B,s,n),'third divided difference ordering')
    kA=root(A,s)
    kB=root(B,s)
    check(2<kA<kB<2/float(s), 'root ordering')

def asymptotic_root(law):
    def f(z): return z/2+sum(float(w)*exp(-float(u)*z) for u,w in law)-1
    a,b=.01,4.0
    check(f(a)<0 and f(b)>0, 'positive limit root bracket')
    for _ in range(80):
        m=(a+b)/2
        if f(m)>0:b=m
        else:a=m
    return (a+b)/2
zA,zB=asymptotic_root(A),asymptotic_root(B)
check(isclose(zA,.79681213002002,rel_tol=0,abs_tol=1e-11),'first weak-reset root')
check(isclose(zB,1.02097510062615,rel_tol=0,abs_tol=1e-11),'second weak-reset root')
check(zB>zA>.5,'sharp distinct asymptotic roots')
for s in (Q(1,50),Q(1,100),Q(1,200),Q(1,500)):
    a,b=root(A,s),root(B,s)
    check(abs(float(s)*a-zA)<.04, 'weak reset root A convergence')
    check(abs(float(s)*b-zB)<.04, 'weak reset root B convergence')
print('PASS:', checks, 'assertions; z_A=',format(zA,'.13f'),'z_B=',format(zB,'.13f'))
