"""Finite consistency checks for iterated Hardy averaging (standard library only).
The analytic infinite-dimensional and asymptotic arguments are documented separately.
"""
from fractions import Fraction
from math import factorial, exp, log, sqrt, pi, lgamma, isclose

checks = 0

def confirm(test, description):
    global checks
    checks += 1
    if not test:
        raise AssertionError(description)

def add(a, b):
    out=[Fraction(0) for _ in range(max(len(a),len(b)))]
    for i,v in enumerate(a):out[i]+=v
    for i,v in enumerate(b):out[i]+=v
    return out

def mul(a,b):
    out=[Fraction(0) for _ in range(len(a)+len(b)-1)]
    for i,ai in enumerate(a):
        for j,bj in enumerate(b):out[i+j]+=ai*bj
    return out

def derivative(a):
    return [a[i]*i for i in range(1,len(a))]

def scale(a,k):return [z*k for z in a]

def evaluate(a,x):
    v=0.0
    for c in reversed(a):v=v*x+float(c)
    return v

def q(m,L):
    term=1.0
    total=1.0
    for k in range(1,m):
        term*=L/k
        total+=term
    return exp(-L)*total

def kint(m,L):
    # The signed error in the unimodality equation; Simpson quadrature.
    if L==0:return 0.0
    n=1800
    h=L/n
    def a(y):
        if y==0:
            return (2.0 if m==1 else 0.0)
        return 2.0*exp((m-1)*log(y)-lgamma(m))*q(m,y)
    v=a(0)+a(L)
    for j in range(1,n):v+=(4 if j&1 else 2)*a(j*h)
    return v*h/3

def root(m):
    a,b=0.0,float(max(2,m*2))
    confirm(kint(m,a)<1 and kint(m,b)>1, f'bracket m={m}')
    for _ in range(44):
        z=(a+b)/2
        if kint(m,z)>1:b=z
        else:a=z
    return (a+b)/2

# Every proof-critical finite polynomial identity is tested with exact fractions.
for m in range(1,23):
    S=[Fraction(1,factorial(k)) for k in range(m)]
    T=mul(S,S)
    P=[Fraction(0) for _ in range(len(T))]
    B=Fraction(0)
    for k,a in enumerate(T):
        B+=a*factorial(k)
        for j in range(k+1):P[j]+=a*factorial(k)/factorial(j)
    lhs=add(P,scale(derivative(P),-1))
    confirm(lhs==T, f'Riccati polynomial cancellation m={m}')
    confirm(P[0]==B, f'R_m(0)=0 m={m}')
    # Exact polynomial identity for derivative of the root equation.
    coeff=[Fraction(0) for _ in range(2*m)]
    A=Fraction(0)
    for k in range(m):
        w=Fraction(2*factorial(m+k-1),factorial(m-1)*factorial(k))
        A+=w
        for j in range(m+k):coeff[j]+=w/Fraction(factorial(j))
    confirm(coeff[0]==A,f'K_m(0)=0 m={m}')
    deriv_lhs=add(coeff,scale(derivative(coeff),-1))
    rhs= [Fraction(0)]*(m-1)+scale(S,Fraction(2,factorial(m-1)))
    confirm(deriv_lhs[:len(rhs)]==rhs and all(v==0 for v in deriv_lhs[len(rhs):]),f'K_m derivative m={m}')

# Independently evaluate the sharp root and its norming equality by quadrature.
L_list=[]
for m in range(1,15):
    L=root(m); L_list.append(L)
    confirm(0<q(m,L)<1, f'gamma survival in (0,1), m={m}')
    confirm(abs(kint(m,L)-1)<2e-8, f'root balance m={m}')
    confirm(kint(m,L-0.005)<1 and kint(m,L+0.005)>1, f'one-crossing m={m}')
    # Compare residual integral with squared gamma survival at the optimum.
    h=L/1800
    # R=e^{-L} integral e^y Q(y)^2 dy; Simpson.
    sm=1.0+exp(L)*q(m,L)**2
    for j in range(1,1800):
        y=j*h
        sm+=(4 if j&1 else 2)*exp(y)*q(m,y)**2
    R=exp(-L)*sm*h/3
    confirm(abs(R-q(m,L)**2)<3e-8,f'extremal residual identity m={m}')
    b=exp((lgamma(m+1)-log(2))/m)
    confirm(L>b, f'root exceeds factorial benchmark m={m}')
    if m>1:confirm(L>L_list[-2],f'root increases m={m}')
confirm(abs(L_list[0]-log(2))<1e-10,'first iterate midpoint')
confirm(abs(L_list[1]-1.09982031418363)<1e-8,'second iterate benchmark')
confirm(abs(L_list[4]-2.29096922372183)<1e-8,'fifth iterate benchmark')

print(f'PASSED {checks} exact or numerical assertions')
for m in [1,2,3,5,10,14]:
    L=L_list[m-1]
    print(f'm={m} L={L:.11f} t={exp(-L):.11f} C={q(m,L):.11f}')
