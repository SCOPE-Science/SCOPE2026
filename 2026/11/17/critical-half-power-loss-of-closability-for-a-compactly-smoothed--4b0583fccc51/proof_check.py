"""Finite rational checks of the exact graph-capacity identity; analytical proof needed for infinite claims."""
from fractions import Fraction
from math import sqrt, log

def exact_capacity(alpha, N):
    # Integral powers keep all arithmetic rational.
    w=[Fraction(1)+Fraction(n)**(2-2*alpha) for n in range(1,N+1)]
    S=sum((1/wi for wi in w),Fraction(0))
    x=[1/(wi*S) for wi in w]
    assert sum(x)==1
    cost=sum((wi*xi*xi for wi,xi in zip(w,x)),Fraction(0))
    assert cost==1/S
    # For every perturbation h with sum h=0, the derivative vanishes.
    for k in range(N-1):
        assert w[k]*x[k]==w[k+1]*x[k+1]
    return cost
for alpha in [0,1,2]:
    for N in [1,2,3,5,10,25]:
        assert exact_capacity(alpha,N)>0
print('18 exact-rational capacity and stationarity checks passed')
# At alpha=1/2 and alpha>1/2 the graph-norm cost decreases to 0.
for alpha in [0.5,0.75,1.0,1.5]:
    vals=[]
    for N in [100,10000,100000]:
        S=sum(1/(1+n**(2-2*alpha)) for n in range(1,N+1))
        vals.append(1/sqrt(S))
    assert vals[0]>vals[1]>vals[2]>0
    print('alpha',alpha,'costs',*[round(v,6) for v in vals])
# Closed T inverse formula: A=(I+e1 tensor u), u=(1/n); A^-1=I-(e1 tensor u)/2.
for N in [2,3,10]:
    z=[Fraction(1,n) for n in range(1,N+1)]
    u=[Fraction(1,n) for n in range(1,N+1)]
    # T=D+e1(sum), where 'sum' acts on coordinates.
    Tz=[n*z[n-1] for n in range(1,N+1)]
    Tz[0]+=sum(z)
    # Reconstruct D z=A^-1 Tz, then invert D.
    norm=sum(u[n]*Tz[n] for n in range(N))
    AinvTz=Tz.copy();AinvTz[0]-=norm/2
    recovered=[AinvTz[n-1]/n for n in range(1,N+1)]
    assert recovered==z
print('3 exact-rational finite-section inverse checks passed')
