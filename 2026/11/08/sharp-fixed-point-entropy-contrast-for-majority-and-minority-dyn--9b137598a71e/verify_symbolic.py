#!/usr/bin/env python3
"""Exact transfer/cyclic-run checks and asymptotic diagnostics for helm fixed states."""
from math import comb, pi, sqrt, log, exp
import sympy as sp

states=('00','01','10','11')

def transfer(forbidden):
    y=sp.symbols('y')
    T=sp.zeros(4)
    for i,a in enumerate(states):
        for c in '01':
            if a+c != forbidden:
                T[i,states.index(a[1]+c)]+=y**int(c)
    return T

def counts(n,forbidden):
    # Coefficients of trace(T(y)^n), computed by closed-walk dynamic programming.
    ans=[0]*(n+1)
    for initial in range(4):
        dp={(initial,0):1}
        for _ in range(n):
            nxt={}
            for (i,k),v in dp.items():
                a=states[i]
                for c in '01':
                    if a+c==forbidden:continue
                    j=states.index(a[1]+c)
                    key=(j,k+int(c))
                    nxt[key]=nxt.get(key,0)+v
            dp=nxt
        for k in range(n+1):ans[k]+=dp.get((initial,k),0)
    return ans

def run_minority(n):
    # Let k be rim sites equal to the hub, z=n-k the others.
    tot=0
    for k in range(n//2+1):
        z=n-k
        ways=sum(comb(z,j)*comb(z-j,k-2*j) if 0<=k-2*j<=z-j else 0
                 for j in range(k//2+1))
        assert (n*ways)%z==0
        tot+=n*ways//z
    return 2*tot

def run_majority(n):
    # Let k be rim sites opposite the hub, z=n-k.
    ans=2 # only the zero-opposite word, with both hub colours
    for k in range(2,n//2+1):
        z=n-k
        for r in range(1,min(k//2,z)+1):
            term=n*comb(k-r-1,r-1)*comb(z-1,r-1)
            assert term%r==0
            ans+=2*(term//r)
    return ans

x,y=sp.symbols('x y')
Tmin=transfer('111');Tmaj=transfer('010')
cpmin=sp.factor(Tmin.charpoly(x).as_expr())
cpmaj=sp.factor(Tmaj.charpoly(x).as_expr())
assert sp.expand(cpmin-x*(x**3-x**2-y*x-y**2))==0
assert sp.expand(cpmaj-x*(x**3-(1+y)*x**2+y*x-y**2))==0
print('CHAR_POLYNOMIALS PASS:',cpmin,';',cpmaj)

p=x**3-(1+y)*x**2+x*y-y**2
assert p.subs({x:sp.Rational(3,2),y:sp.Rational(3,4)})==0
py=sp.diff(p,y);px=sp.diff(p,x)
point={x:sp.Rational(3,2),y:sp.Rational(3,4)}
dxdy=(-py/px).subs(point)
d2=(-(sp.diff(p,y,2)+2*sp.diff(p,x,y)*dxdy+sp.diff(p,x,2)*dxdy**2)/px).subs(point)
mu=(y*dxdy/x).subs(point)
variance=sp.simplify((y*dxdy/x+y*y*d2/x-(y*dxdy/x)**2).subs(point))
assert (dxdy,d2,mu,variance)==(1,sp.Rational(2,9),sp.Rational(1,2),sp.Rational(1,3))
print('SADDLE PASS: weight=3/4; eigenvalue=3/2; mean=1/2; variance=1/3')

for n in range(3,55):
    cmin=counts(n,'111');cmaj=counts(n,'010')
    left=2*sum(cmin[:n//2+1]);right=2*sum(cmaj[:n//2+1])
    a=run_minority(n);b=run_majority(n)
    assert left==a and right==b,(n,left,a,right,b)
    if n in [3,4,5,6,7,8,9,10,12,20,40,54]:print('n=%d minority=%d majority=%d' %(n,a,b))
print('TRACE/RUN EQUALITY PASS: all 3<=n<=54')
# For n>=50, compare the exact finite-n count with the derived sharp parity asymptotic.
lam=1.839286755214161
for n in [50,51,100,101,200,201]:
    u=2*sum(counts(n,'111')[:n//2+1]);v=2*sum(counts(n,'010')[:n//2+1])
    pred_u=2*lam**n
    pred_v=8*(sqrt(3)/2)**(n%2)*sqrt(3/(2*pi*n))*3**(n/2)
    print('ASYMPTOTIC_DIAGNOSTIC n=%d minority_ratio=%.8f majority_ratio=%.8f' %(n,u/pred_u,v/pred_v))
print('SYMBOLIC AND COUNT CHECKS PASS')
