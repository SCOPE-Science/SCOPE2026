"""Reproducibility checks for entropy-optimal tridiagonal stochastic paths.
Run with Python 3.10+, sympy, numpy and scipy. Checks supplement, not replace, the proof.
"""
import math
from fractions import Fraction
import numpy as np
import sympy as sp
from scipy.optimize import root

count=0

def check(x, explanation):
    global count
    assert x, explanation
    count+=1

# Exact half-line rational Pell profile.
h=[5,19]
for i in range(80):
    h.append(4*h[-1]-h[-2])
t=[Fraction(h[k]-5*(-1)**k,h[k]+(-1)**k) for k in range(1,81)]
check(t[0]==Fraction(4,3) and t[1]==Fraction(11,12), 'boundary fractions')
check(t[0]*(t[0]+t[1])==3, 'boundary equation')
for k in range(1,79):
    check(t[k]*(t[k-1]+t[k]+t[k+1])==3, 'half-line recurrence')
check(t[0]*t[1]/3==Fraction(11,27), 'first edge')
check(t[1]*t[2]/3==Fraction(5,16), 'second edge')
check(t[2]*t[3]/3==Fraction(41,121), 'third edge')
for k in range(1,81):
    check(h[k]>h[k-1] and h[k]>5, 'Pell increasing')
for k in range(1,80):
    check(h[k]**2-4*h[k]*h[k-1]+h[k-1]**2==6, 'Pell conic')

# Exact symbolic recurrence certificate (on conic a^2-4ab+b^2=6).
a,b,s=sp.symbols('a b s')
c=4*b-a
rec=(a+5*s)/(a-s)+(b-5*s)/(b+s)+(c+5*s)/(c-s)-3*(b+s)/(b-5*s)
num=sp.factor(sp.together(rec).as_numer_denom()[0])
for sign in (-1,1):
    check(sp.rem(sp.expand(num.subs(s,sign)), a*a-4*a*b+b*b-6,a)==0, 'symbolic recurrence')

# Convex stationary scaling numerical tests.
def solve_v(n):
    guess=np.full(n,1/math.sqrt(3))
    guess[0]=guess[-1]=0.77
    def f(y):
        v=np.exp(y)
        return v*(v+np.r_[0.,v[:-1]]+np.r_[v[1:],0.])-1
    ans=root(f,np.log(guess),tol=1e-11)
    check(ans.success or np.max(np.abs(f(ans.x)))<1e-10, 'numerical convergence')
    v=np.exp(ans.x)
    check(np.max(np.abs(f(ans.x)))<3e-10, 'normalization')
    check(np.max(np.abs(v-v[::-1]))<3e-8, 'reflection')
    P=np.diag(v*v)+np.diag(v[:-1]*v[1:],1)+np.diag(v[:-1]*v[1:],-1)
    check(np.max(np.abs(P.sum(axis=1)-1))<3e-10, 'stochastic')
    H=-np.sum(np.where(P>0,P*np.log(np.maximum(P,1e-300)),0))/n
    check(abs(H+2*np.log(v).sum()/n)<3e-10, 'entropy formula')
    return v,H

sigma=2-math.sqrt(3)
limit_v1=4/(3*math.sqrt(3))
limit_e1=11/27
surface=4*sum(math.log(float(q)) for q in t)
for n in (3,4,5,6,8,12,20,32,48,80):
    v,H=solve_v(n)
    check(abs(v[0]-limit_v1)<max(1e-10,25*sigma**(n//2)), 'left endpoint limit')
    check(abs(v[0]*v[1]-limit_e1)<max(1e-10,25*sigma**(n//2)), 'left transition limit')
    if n>=12:
        check(abs(n*(math.log(3)-H)-surface)<max(1e-8,150*n*sigma**(n//2)), 'surface entropy asymptotic')

check(0.87<surface<0.88, 'surface constant')
print('PASSED',count,'supplementary exact and numerical checks')
print('surface_constant', format(surface,'.14f'))
print('infinite_edge_first',format(limit_e1,'.15f'))
