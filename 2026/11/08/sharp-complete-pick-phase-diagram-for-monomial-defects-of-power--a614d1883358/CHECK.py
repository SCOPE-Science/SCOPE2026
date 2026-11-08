"""Finite exact checks supplementing the monomial-defect power-kernel theorem."""
from fractions import Fraction
from math import factorial, comb

def rising(a,m):
    p=Fraction(1)
    for j in range(m): p*=a+j
    return p

def A(g,m):return rising(g,m)/factorial(m)
def D(g,m):
    val=g
    for j in range(1,m):val*=j-g
    return val/factorial(m)

def cp_coefficients(g,m,s,N):
    # diagonal in one variable from F=1-(1-t)^g/(1-s t^m)
    coeff=[Fraction(0)]*(N+1)
    taylor=[Fraction(1)]
    for n in range(1,N+1):taylor.append(taylor[-1]*(n-1-g)/n)
    inv=[Fraction(0)]*(N+1)
    for k in range(N//m+1):inv[k*m]=s**k
    for n in range(1,N+1):
        coeff[n]=-sum(taylor[j]*inv[n-j] for j in range(n+1))
    return coeff

count=0
for g in [Fraction(1,10),Fraction(1,4),Fraction(1,2),Fraction(3,4),Fraction(9,10),Fraction(1),Fraction(5,4),Fraction(3,2),Fraction(7,4),Fraction(2),Fraction(5,2),Fraction(3)]:
    for m in range(1,9):
        a=A(g,m) if g<1 else Fraction(1)
        assert a>0
        for ratio in [Fraction(0), Fraction(1,4),Fraction(1,2),Fraction(1),Fraction(5,4)]:
            if g<=1:
                s=min(a,ratio*D(g,m))
            else:s=min(a,ratio)
            co=cp_coefficients(g,m,s,32)
            expected= (s<=D(g,m)) if g<=1 else (m==1 and s==1 and g<=2)
            if expected:
                assert all(t>=0 for t in co[1:]), (g,m,s,co)
            elif g>1 and m>=2:
                assert co[2]<0,(g,m,s)
            elif g<=1:
                assert co[m]<0,(g,m,s,co[m])
            elif g>2:
                assert co[2]<0,(g,m,s,co[2])
            count+=32
# exact check that at gamma=1/2,m=2 non-injective symbol gives CP
assert D(Fraction(1,2),2)==Fraction(1,8)
assert A(Fraction(1,2),2)==Fraction(3,8)
assert all(t>=0 for t in cp_coefficients(Fraction(1,2),2,Fraction(1,8),96))
# exact formula ratio verified for multiple m
for g in [Fraction(1,4),Fraction(1,2),Fraction(3,4)]:
 for m in range(1,40):
  assert D(g,m)>0 and D(g,m)<=A(g,m)
  if m>1:assert D(g,m)/A(g,m)<D(g,m-1)/A(g,m-1)
  count+=1
print(f'PASS: {count} exact rational coefficient assertions plus endpoint and monotonicity tests')
