"""Independent finite checks for the sharp Gaussian-Hermite BV projection error.
This numerical/algebraic script supplements, but does not replace, the proof.
Python standard library only.
"""
from math import erf, exp, sqrt, pi, comb, factorial, lgamma


def add(a,b):
    return [ (a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b))) ]
def scale(a,c): return [c*x for x in a]
def mul(a,b):
    z=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):z[i+j]+=x*y
    return z
def deriv(a):return [i*a[i] for i in range(1,len(a))] or [0]
def shift(a):return [0]+a

def hermites(n):
    P=[[1]]
    if n==0:return P
    P.append([0,1])
    for k in range(1,n):P.append(add(shift(P[-1]),scale(P[-2],-k)))
    return P

def trim(p):
    while len(p)>1 and p[-1]==0:p.pop()
    return p

def ev(p,x):
    s=0.0
    for v in p[::-1]:s=s*x+v
    return s

checks=0
for n in range(0,25):
    H=hermites(n)
    Q=[0]
    for k in range(1,n+1):
        Q=add(Q,scale(mul(H[k-1],H[k]),1/factorial(k)))
    # Integer exact identity after clearing n!: n! (Q' - x Q -1)=-He_n^2.
    # We instead calculate rational coefficients as integer multiples at denominator n!.
    Q_int=[0]
    for k in range(1,n+1):
        Q_int=add(Q_int,scale(mul(H[k-1],H[k]),factorial(n)//factorial(k)))
    L=add(add(deriv(Q_int),scale(shift(Q_int),-1)),[-factorial(n)])
    assert trim(add(L,mul(H[n],H[n])))==[0],n
    checks+=1

for n in range(0,14):
    H=hermites(n)
    for j in range(1,160):
        x=3.0*j/160
        phi=exp(-x*x/2)/sqrt(2*pi)
        Phi=(1+erf(x/sqrt(2)))/2
        E=Phi*(1-Phi)
        for k in range(1,n+1):
            E-=phi**2*ev(H[k-1],x)**2/factorial(k)
        E0=0.25
        for k in range(1,n+1):
            E0-=(1/(2*pi))*ev(H[k-1],0)**2/factorial(k)
        assert E>=-1e-13 and E<E0+1e-13,(n,x,E,E0)
        checks+=1

# Verify pairwise degree plateau and full center expression by different formulas.
for m in range(1,80):
    c2=0.25-(1/(2*pi))*sum(comb(2*j,j)/4**j/(2*j+1) for j in range(m))
    assert c2>0
    if m<=15:
        H=hermites(2*m)
        alt=0.25-sum((1/(2*pi))*ev(H[k-1],0)**2/factorial(k) for k in range(1,2*m+1))
        assert abs(c2-alt)<1e-13
        checks+=1

# Exact limiting constant check at large degree using loggamma for numerical stability.
K=2**(-0.25)*pi**(-0.75)
for m in (100,300,1000,3000,10000):
    # numerical tail as 1/4 - partial sum loses precision, so sum 100000 terms + bound
    s=0.0
    for j in range(m,100000):
        s+=exp(lgamma(2*j+1)-2*lgamma(j+1)-j*__import__('math').log(4))/(2*j+1)
    # bound tail by integral, no exact guarantee; use centered leading asymptotic as approximation.
    s+=1/sqrt(pi*100000)
    csq=s/(2*pi)
    ratio=(2*m)**0.25*sqrt(csq)/K
    assert abs(ratio-1)<0.013,(m,ratio)
    checks+=1
print(f'VERIFY_OK checks={checks}, asymptotic_constant={K:.12f}, C0={0.5:.12f}, C1={(0.25-1/(2*pi))**0.5:.12f}')
