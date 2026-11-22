#!/usr/bin/env python3
"""Exact six-character moment checks and independently evaluated Poisson-mode thresholds."""
from fractions import Fraction as F
from math import comb, cos, sin, pi, sqrt
import random

checks=0
def check(cond,why=''):
    global checks
    checks+=1
    if not cond: raise AssertionError(why or checks)

def monomial_moment(i,j,m,n):
    return F(sum(comb(i,a)*comb(j,b) for a in range(i+1) for b in range(j+1)
                 if (i-2*a)*m+(j-2*b)*n==0),2**(i+j))

base={0:F(5,16),2:F(3,16),4:F(3,16),6:F(5,16)}
for m in range(1,25):
    for n in range(m+1,75):
        extra={2:{4:F(1,32)},3:{3:F(3,32),5:F(5,32)},5:{5:F(1,32)}}.get(n//m if n % m == 0 else 0,{})
        for i in range(7):
            j=6-i
            check(monomial_moment(i,j,m,n)==base.get(i,F(0))+extra.get(i,F(0)),
                  f'frequency {m},{n}; exponent {i}')

# Exact cubic coefficients of H(y)=1+A*y+B*y**2+C*y**3.
def coeff(t,octave):
    c=F(21,2) if octave else F(9)
    return c*t-3, 3-2*c*t+9*t*t, -1+c*t-9*t*t+t*t*t
for octave,tc,bexpect,cexpect in [(False,F(1,3),F(-2),F(28,27)),(True,F(2,7),F(-111,49),F(442,343))]:
    a,b,c=coeff(tc,octave)
    check(a==0)
    check(b==bexpect and c==cexpect)
    check(b<0 and b+c<0)
    for t in [F(i,100) for i in range(1,101)]:
        a,b,c=coeff(t,octave)
        if t<=tc:
            for y in [F(j,101) for j in range(1,102)]:
                check(a*y+b*y*y+c*y*y*y < 0 if y>0 else True)
        else:
            check(a>0)
            # H'(1)=3t^2(t-3), so a unique interior root for a quadratic.
            check(a+2*b+3*c==3*t*t*(t-3))
            check(a+2*b+3*c<0)

# Direct Fourier-sum evaluation with arbitrary phases checks general phase formulas.
def actual_moment(m,n,a,b,ph1,ph2):
    modes={m:a*complex(cos(ph1),sin(ph1))/2,-m:a*complex(cos(-ph1),sin(-ph1))/2,
           n:b*complex(cos(ph2),sin(ph2))/2,-n:b*complex(cos(-ph2),sin(-ph2))/2}
    # Coefficient convolution, then Parseval for the cube.
    vals={0:1+0j}
    for _ in range(3):
        nxt={}
        for k,v in vals.items():
            for j,w in modes.items():nxt[k+j]=nxt.get(k+j,0)+v*w
        vals=nxt
    return sum(abs(v)**2 for v in vals.values())

def expected(m,n,a,b,ph1,ph2):
    core=5*(a**6+b**6)/16+45*(a**4*b*b+a*a*b**4)/16
    if n==2*m:core+=15*a**4*b*b*cos(2*(ph2-2*ph1))/32
    if n==3*m:core+=(15*a**5*b/16+15*a**3*b**3/8)*cos(ph2-3*ph1)
    if n==5*m:core+=3*a**5*b*cos(ph2-5*ph1)/16
    return core
r=random.Random(26262026)
for m,n in [(1,2),(1,3),(1,5),(1,6),(2,4),(2,6),(2,10),(2,3),(3,7),(4,9),(5,8)]:
    for _ in range(35):
        a,b=r.random()+.01,r.random()+.01
        ph1,ph2=r.random()*2*pi,r.random()*2*pi
        v=actual_moment(m,n,a,b,ph1,ph2)
        e=expected(m,n,a,b,ph1,ph2)
        check(abs(v-e)<3e-11*max(1,e), f'phase {m,n} {v} {e}')

# Explicit exponent-sector formulas after input L2 normalization.
def H(t,y,k):
    p=1-y
    h=p**3+t**3*y**3+9*t*p**2*y+9*t*t*p*y*y
    if k==2:h+=1.5*t*p*p*y
    if k==3:h+=3*sqrt(t)*p**2.5*sqrt(y)+6*t**1.5*p**1.5*y**1.5
    if k==5:h+=.6*sqrt(t)*p**2.5*sqrt(y)
    return h
for t in [1e-8,1e-6,.0003,.004,.09,.2,.26,.29,1/3,.38,.6,1]:
    for k in [2,3,5,7]:
        # independent normalized exact Fourier sum at aligned phase
        m=1;n=k
        for j in range(1,50):
            y=j/50
            a=sqrt(2*(1-y));b=sqrt(2*y)*sqrt(t)
            v=actual_moment(m,n,a,b,0,0)
            e=2.5*H(t,y,k)
            check(abs(v-e)<1e-10*max(1,e),(t,k,j,v,e))

print(f'PASS {checks} exact and numerical assertions')
