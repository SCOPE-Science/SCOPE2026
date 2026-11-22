"""Independent finite checks for the Bernstein circle covariance parity theorem.
Run with python checker.py (requires mpmath, numpy).  Finite tests supplement, not replace, proofs.
"""
import math
import mpmath as mp
import numpy as np

mp.mp.dps = 65
checks = 0

def bpoly(n,m):
    # polynomial coefficients of Re(1+(exp(i m*pi/n)-1)t)^n
    z=mp.e**(1j*mp.pi*m/n)-1
    return [mp.binomial(n,r)*mp.re(z**r) for r in range(n+1)]

def deriv(P,r,t):
    return sum(P[j]*(math.factorial(j)//math.factorial(j-r))*t**(j-r)
               for j in range(r,len(P)))

def coeff(P,k):
    if k == 0: return sum(P[j]/(j+1) for j in range(len(P)))
    return 2*sum((-1)**(q-1)*(((-1)**k)*deriv(P,2*q-1,1)-deriv(P,2*q-1,0))/(mp.pi*k)**(2*q)
                 for q in range(1,(len(P)+1)//2+1) if 2*q-1<len(P))

for n in range(1,10):
    for m in range(0,2*n+4):
        P=bpoly(n,m)
        a=m%(2*n); alias=min(a,2*n-a)
        for k in range(1,31):
            c=coeff(P,k)
            if alias==0 or (k-alias)%2:
                assert abs(c)<mp.mpf('1e-40'), (n,m,k,c)
            else:
                assert c>mp.mpf('1e-35'), (n,m,k,c)
            checks+=1
        if alias >0:
            expected0=mp.mpf(0) if alias%2 else mp.mpf(1)/(n+1)
            assert abs(coeff(P,0)-expected0)<mp.mpf('1e-40')
        else: assert abs(coeff(P,0)-1)<mp.mpf('1e-40')
        checks+=1

# For n=2 and f=1+cos(x)+cos(2x), exact finite-N
# covariance spectrum and the two distinct large-grid constants.
for N in list(range(3,62))+[100,101,300,301,600,601]:
    theta=2*np.pi*np.arange(N)/N
    distances=np.minimum(theta,2*np.pi-theta)
    t=distances/np.pi
    samples=1+(1-2*t)+(1-2*t)**2
    direct=np.real(np.fft.fft(samples))
    predicted=[]
    for j in range(N):
        if j==0:
            pred=4*N/3+(8/(3*N) if N%2==0 else 5/(3*N))
        elif N%2==0:
            pred=(4 if j%2 else 8)/(N*math.sin(math.pi*j/N)**2)
        else:
            a=math.pi*j/(2*N)
            de,do=(2,1) if j%2==0 else (1,2)
            pred=(de/(math.sin(a)**2)+do/(math.cos(a)**2))/N
        predicted.append(pred)
    assert np.max(np.abs(direct-predicted))<2e-8, (N,np.max(np.abs(direct-predicted)))
    checks+=N

for N in [100,101,200,201,500,501,1000,1001,2000,2001]:
    vals=[]
    for j in range(1,N):
        if N%2==0:
            val=(4 if j%2 else 8)/(N*math.sin(math.pi*j/N)**2)
        else:
            a=math.pi*j/(2*N)
            de,do=(2,1) if j%2==0 else (1,2)
            val=(de/math.sin(a)**2+do/math.cos(a)**2)/N
        vals.append(val)
    scaled=N*min(vals)
    theoretical=4 if N%2==0 else (1+math.sqrt(2))**2
    assert abs(scaled-theoretical)<0.005, (N,scaled,theoretical)
    checks+=1

print(f"PASS: {checks} finite checks; analytic proof independent")
