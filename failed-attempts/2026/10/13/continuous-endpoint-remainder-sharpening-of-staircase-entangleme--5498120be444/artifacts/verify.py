from decimal import Decimal, getcontext
from math import floor
getcontext().prec = 60

def powd(a,b):
    return (b*a.ln()).exp()

def binom(x,n):
    z=Decimal(1)
    for j in range(n): z *= x-Decimal(j)
    f=Decimal(1)
    for j in range(2,n+1): f*=j
    return z/f

def ffun(x,t): return powd(Decimal(1)+t,x)-powd(t,x)

def mono_old(x,k,t):
    q=floor(float(x))
    return sum((binom(x,n)*(powd(Decimal(1)+k,x-Decimal(n))-powd(k,x-Decimal(n)))*powd(t-k,Decimal(n)) for n in range(q)), Decimal(0))

def mono_new(x,k,t):
    q=floor(float(x)); th=x-Decimal(q)
    v=mono_old(x,k,t)
    if th:
        v += binom(x,q)*(powd(Decimal(1)+t,th)-powd(t,th))*powd(t-k,Decimal(q))
    return v

def poly_old(x,k,t):
    q=floor(float(x))
    return sum((binom(x,n)*(powd(Decimal(1)+k,x-Decimal(n))-powd(k,x-Decimal(n)))*powd(t-k,Decimal(n)) for n in range(q+1)), Decimal(0))

def poly_new(x,k,t):
    q=floor(float(x)); th=x-Decimal(q)
    v=poly_old(x,k,t)
    if th:
        v += binom(x,q+1)*(powd(Decimal(1)+t,th-Decimal(1))-powd(t,th-Decimal(1)))*powd(t-k,Decimal(q+1))
    return v

# Deterministic grid: lower <= exact <= upper, with strict improvements away from integers and t=k.
xs=[Decimal('1.2'),Decimal('1.5'),Decimal('2.1'),Decimal('2.5'),Decimal('3.7'),Decimal('5.25')]
ks=[Decimal('0.5'),Decimal('1'),Decimal('2'),Decimal('5')]
ds=[Decimal('0.1'),Decimal('0.7'),Decimal('2'),Decimal('5')]
for x in xs:
    for k in ks:
        for d in ds:
            t=k+d; exact=ffun(x,t)
            lo0=mono_old(x,k,t); lo1=mono_new(x,k,t)
            up0=poly_old(x,k,t); up1=poly_new(x,k,t)
            assert lo0 < lo1 < exact
            assert exact < up1 < up0

# Integer exponents: source truncation is already exact.
for q in range(1,8):
    x=Decimal(q); k=Decimal('1.3'); t=Decimal('3.1')
    assert abs(mono_new(x,k,t)-ffun(x,t)) < Decimal('1e-45')

# Source Example 3.7, non-asymmetric bound at alpha=5, gamma=2.
x=Decimal('2.5')
c1=Decimal('0.5')
c2=(Decimal(2).sqrt())/Decimal(4)
tau=(c1*c1)/(c2*c2)
k=Decimal(1)
B=(powd(Decimal(2),x)-1) + x*(powd(Decimal(2),x-1)-1)*(tau-1)
Zold=powd(c1,Decimal(5)) + B*powd(c2,Decimal(5))
q=2; th=Decimal('0.5')
C=binom(x,q)*(powd(1+tau,th)-powd(tau,th))*powd(tau-1,Decimal(q))
Znew=Zold+C*powd(c2,Decimal(5))
S=powd(c1*c1+c2*c2,x)
closed=(Znew-Zold)/(S-Zold)
assert Zold < Znew < S
assert Decimal('0.84') < closed < Decimal('0.85')
print('VERIFY_OK')
print('Zold', Zold)
print('Znew', Znew)
print('algebraic_target', S)
print('gap_fraction_closed', closed)
