#!/usr/bin/env python3
"""Reproduce the stationary cubic-moment formulas for a biased telegraph oscillator.

Requires Python 3 standard library only. No symbolic-algebra package or network.
"""
from fractions import Fraction as F
import math


def solve(A, z):
    n=len(z)
    B=[[F(t) for t in A[i]] + [F(z[i])] for i in range(n)]
    for j in range(n):
        pivot=next((i for i in range(j,n) if B[i][j]),None)
        if pivot is None: raise AssertionError('singular balance matrix')
        B[j],B[pivot]=B[pivot],B[j]
        fac=B[j][j]
        B[j]=[a/fac for a in B[j]]
        for i in range(n):
            if i!=j and B[i][j]:
                fac=B[i][j]
                B[i]=[B[i][k]-fac*B[j][k] for k in range(n+1)]
    return [B[i][-1] for i in range(n)]


def direct_moments(b, q, delta, thermal=F(0)):
    """Solve the generator equations independently degree by degree."""
    b,q,delta,thermal=map(F,(b,q,delta,thermal))
    assert b>0 and q>0 and -1<delta<1 and thermal>=0
    M={(0,0):F(1)}
    N={(0,0):F(0)}
    for n in range(1,4):
        for table in (M,N):
            A=[[F(0)]*(n+1) for _ in range(n+1)]
            rhs=[F(0)]*(n+1)
            for i in range(n+1):
                j=n-i
                A[i][i]+=j+(q if table is N else 0)
                if i:
                    A[i][i-1]-=i
                if j:
                    A[i][i+1]+=j*b
                    if table is N:
                        rhs[i]+=j*((1-delta**2)*M.get((i,j-1),0)
                                    -2*delta*N.get((i,j-1),0))
                    else:
                        rhs[i]+=j*N.get((i,j-1),0)
                if j>=2:
                    rhs[i]+=thermal*j*(j-1)*table.get((i,j-2),0)
            vals=solve(A,rhs)
            for i,v in enumerate(vals):table[(i,n-i)]=v
    return M,N


def formulas(b,q,delta):
    b,q,delta=map(F,(b,q,delta))
    H=(b+2)*(q+1)*(b+q*q+q)*(4*b+q*q+2*q)
    A=4*delta*(1-delta**2)
    return {
       'xxx':-A*(5*b*q+2*b+2*q**3+8*q*q+10*q+4)/(b*H),
       'xxv':F(0),
       'xvv':-A*q*(b+q*q+4*q+2)/H,
       'vvv':A*q*q*(3*b-2*(q+1))/H,
    }


def analytic_checks():
    tests=0
    for b in (F(1,5), F(1,4),F(3,10),F(4,5),F(4,3), F(2),F(9)):
        for q in (F(1,5),F(1),F(7,3)):
            for d in (-F(2,3),-F(1,4),F(0),F(1,3),F(3,4)):
                expect=formulas(b,q,d)
                for therm in (F(0),F(2,5)):
                    m,n=direct_moments(b,q,d,therm)
                    got={'xxx':m[3,0],'xxv':m[2,1],
                         'xvv':m[1,2],'vvv':m[0,3]}
                    assert got==expect,(b,q,d,therm,got,expect)
                    tests+=4
                if d:
                    assert (expect['xxx']>0)==(d<0)
                    assert (expect['xvv']>0)==(d<0)
                    if 3*b==2*(q+1): assert expect['vvv']==0
                    elif 3*b>2*(q+1):assert (expect['vvv']>0)==(d>0)
                    else: assert (expect['vvv']>0)==(d<0)
                    tests+=3
    b,q,d=F(2),F(1),F(1,3)
    assert formulas(b,q,d)=={'xxx':-F(19,297),'xxv':F(0),
                             'xvv':-F(1,33),'vvv':F(2,297)}
    tests+=4
    return tests


def time_ordered_check(b,q,typ,steps=14000,tmax=42.):
    """Independent filter integral for a stationary telegraph third cumulant.
    Six-fold ordered-time integral becomes 6 int h(t) F(t) G(t) dt,
    F(t)=int_0^t h(u)exp[-q(t-u)]du,
    G(t)=int_t^infty h(w)exp[-q(w-t)]dw.
    """
    assert b>0.25
    dt=tmax/steps
    om=math.sqrt(b-.25)
    h=[]
    for j in range(steps+1):
        t=j*dt
        e=math.exp(-t/2)
        h.append(e*math.sin(om*t)/om if typ=='x' else
                 e*(math.cos(om*t)-math.sin(om*t)/(2*om)))
    A=math.exp(-q*dt)
    B=-math.expm1(-q*dt)/q
    forward=[0.]*(steps+1)
    backward=[0.]*(steps+1)
    for j in range(steps):forward[j+1]=A*forward[j]+B*(h[j]+h[j+1])/2
    for j in range(steps-1,-1,-1):backward[j]=A*backward[j+1]+B*(h[j]+h[j+1])/2
    vals=[6*h[j]*forward[j]*backward[j] for j in range(steps+1)]
    return dt*(sum(vals)-0.5*(vals[0]+vals[-1]))


def expected_integral(b,q,typ):
    f=formulas(F(str(b)),F(str(q)),F(1,3))
    # Third drive cumulant = -2*delta*(1-delta**2)*exp(-q*range)
    return float(f[typ*3]/(-2*F(1,3)*(1-F(1,3)**2)))


def integral_checks():
    tests=0
    for b,q in ((0.30,0.25),(0.8,1.),(4./3.,1.),(2.,1.),(5.,0.6),(9.,2.)):
        for typ in ('x','v'):
            n=time_ordered_check(b,q,typ)
            e=expected_integral(b,q,typ)
            assert abs(n-e)<7.e-5, (b,q,typ,n,e)
            tests+=1
    return tests

if __name__=='__main__':
    n=analytic_checks();m=integral_checks()
    print(f'PASS: {n} exact-rational generator assertions and {m} independent impulse-filter quadratures')
