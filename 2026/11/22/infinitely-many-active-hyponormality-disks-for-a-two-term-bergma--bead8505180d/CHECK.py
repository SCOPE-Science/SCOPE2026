#!/usr/bin/env python3
"""Independent exact-rational diagnostics for the two-term Bergman shift model.

This checks finite algebraic identities only. The all-index proof is in RESULT.md.
Run: python3 CHECK.py
"""
from fractions import Fraction as F
import math

def A(k): return (k + 3) * (k + 4)**2
def B(k): return 4 * (k + 2) * (k + 3) * (k + 4)
def C(k): return (k + 2)**2 * (3*k + 11)
def L(k, x): return -F(A(k) + B(k)*x, C(k))
def X(k): return -F(5*k**3 + 54*k**2 + 187*k + 206, 8*(k+2)*(k+3)*(k+4))
def Y(k): return F(k+5,2*(k+2))
def q(k, x, y): return A(k) + B(k)*x + C(k)*y

def W2(n, x, y):
    # exact squared shift weight, with x=Re(lambda), y=|lambda|^2
    return F(n+1,n+2) * (1+2*x*F(n+2,n+3)+y*F((n+2)**2,(n+3)**2))

checks = 0
for k in range(80):
    for x,y in [(F(-1,1),F(5,4)), (F(-3,4),F(7,8)), (F(2,3),F(2,1)), (F(-7,5),F(49,25))]:
        left=W2(k+1,x,y)-W2(k,x,y)
        right=F(q(k,x,y),(k+2)*(k+3)**2*(k+4)**2)
        assert left==right, (k,x,y)
        checks+=1
    assert L(k,X(k))==L(k+1,X(k))==Y(k),k
    checks+=2
    assert X(k)<X(k+1)<-F(5,8), k
    checks+=1
    assert Y(k)>X(k)*X(k), k
    checks+=1
    assert B(k)**2-4*A(k)*C(k)==4*(k+1)*(k+2)**2*(k+3)*(k+4)**2
    checks+=1
    for j in range(1,12):
        kk=j
        # On the interval between adjacent switches, a designated line is maximal.
        xx=(X(kk-1)+X(kk))/2
        assert L(kk,xx)>=L(k,xx)
        checks+=1

for k in range(1,80):
    assert X(k)-X(k-1) == F(3*(3*(k-1)+14), 8*(k+1)*(k+3)*(k+4))
    checks+=1

# A few direct finite matrix / self-commutator tests in diagonal form.
for lam in [-2.0,-1.41,-1.4,-1.0,-0.5,-1/3,0,1,2]:
    weights=[math.sqrt((n+1)/(n+2))*abs(1+lam*(n+2)/(n+3)) for n in range(600)]
    ok=all(weights[n+1]**2>=weights[n]**2-1.e-12 for n in range(len(weights)-1))
    classified=(lam<=(-12-2*math.sqrt(3))/11 +1.e-14 or lam>=-1/3-1.e-14)
    assert ok==classified,(lam,ok,classified)
    checks+=1
print(f'CHECK PASSED: {checks} exact algebraic plus finite diagnostic tests')
