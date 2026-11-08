"""Finite exact and numerical checks for the 3D heterochaos cross-covariance law.

Run with Python >=3.9, standard library only: python verify.py.
The analytic proof in RESULT.md, not this finite script, establishes all orders.
"""
from fractions import Fraction as Q
from itertools import product
from math import sqrt, pi


def direct_covariance(n):
    """Independent exact cube integral using ternary paths and dyadic midpoint cells."""
    total=Q(0)
    for digits in product(range(3),repeat=n):
        for j in range(1 << n):
            z0=Q(2*j+1, 2**(n+1))
            z=z0
            y=Q(1,2)  # conditional mean of initially uniform stable coordinate
            for digit in digits:
                if digit==0:
                    y=Q(2,3)*y
                    z=z/2
                elif digit==1:
                    y=Q(2,3)*y
                    z=(1+z)/2
                elif z<Q(1,2):
                    y=Q(2,3)+y/6
                    z=2*z
                else:
                    y=Q(5,6)+y/6
                    z=2*z-1
            total+=(z0-Q(1,2))*(y-Q(1,2))
    return total/(3**n*2**n)


def bit_recurrence(N):
    """An independent operator calculation from the stationary binary digits."""
    h={j:Q(1,2**(j+1)) for j in range(1,2*N+9)}
    vals=[Q(0)]
    for _ in range(N):
        vals.append(vals[-1]/2 + h[1]/36)
        h={j:(h[j+1]/3 if j==1 else (2*h[j-1]+h[j+1])/3)
           for j in range(1,max(h)-1)}
    return vals


def convolution(a,b,N):
    return [sum((a[k]*b[n-k] for k in range(n+1)),Q(0))
            for n in range(N+1)]


def generating_coefficients(N):
    """Formal series from 3r=z(2+r*r), D=(r*r+2)/(4(4-r))."""
    r=[Q(0)]*(N+1)
    for n in range(1,N+1):
        r2=convolution(r,r,n-1)
        r[n]=(2*int(n==1)+r2[n-1])/3
    r2=convolution(r,r,N)
    # 4(4-r) D = 2+r*r
    D=[Q(0)]*(N+1)
    for n in range(N+1):
        D[n]=(Q(2 if n==0 else 0)+r2[n]
              +4*sum((r[k]*D[n-k] for k in range(1,n+1)),Q(0)))/16
    C=[Q(0)]*(N+1)
    for n in range(1,N+1):
        C[n]=C[n-1]/2+D[n-1]/18
    return C


N=16
series=generating_coefficients(N)
operator=bit_recurrence(N)
assert series==operator, (series,operator)
for n in range(6):
    assert direct_covariance(n)==series[n],n
assert series[1]==Q(1,144)
assert series[2]==Q(1,216)
assert series[3]==Q(7,1728)
assert series[5]==Q(131,62208)
assert all(c>0 for c in series[1:])

# Large-n operator coefficients; no assumed asymptotic constants are used here.
Nlong=240
h=[2.0**(-j-1) for j in range(1,Nlong+10)]
large=[0.0]
for _ in range(Nlong):
    large.append(large[-1]/2+h[0]/36)
    h=[h[1]/3]+[(2*h[j-1]+h[j+1])/3
                  for j in range(1,len(h)-1)]
R=3/(2*sqrt(2))
dplus=2*sqrt(2)/(4-sqrt(2))**2
dminus=2*sqrt(2)/(4+sqrt(2))**2
Aplus=R*dplus/(18*(1-R/2))
Aminus=R*dminus/(18*(1+R/2))
assert 0<Aminus<Aplus
for n in [60,80,100,120,160,200]:
    pred=R**(-n)*n**(-1.5)*(Aplus-(-1)**n*Aminus)/sqrt(pi)
    assert abs(large[n]/pred-1)<0.04, (n,large[n]/pred)
print('PASS: 17 formal-series identities, 17 operator identities, '
      '6 exact cube integrals, 6 asymptotic checks and auxiliary checks.')
print('Initial cross-covariances:',[(n,str(series[n])) for n in range(6)])
print('A_plus,A_minus:',Aplus,Aminus)
