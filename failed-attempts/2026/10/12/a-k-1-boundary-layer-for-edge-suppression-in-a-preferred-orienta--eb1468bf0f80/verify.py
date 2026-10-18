#!/usr/bin/env python3
import cmath, math

def S_entries(k):
    den=k*k+3.0
    return [
        [(k*k-1.0)/den, 2.0*(k+1.0)/den, 2.0*(1.0-k)/den],
        [2.0*(1.0-k)/den, (k*k-1.0)/den, 2.0*(k+1.0)/den],
        [2.0*(k+1.0)/den, 2.0*(1.0-k)/den, (k*k-1.0)/den],
    ]

def exact_ratios(k, theta, q):
    z=cmath.exp(1j*theta)
    D=(k*k*q*q*z-k*k*z-2*k*q*z*z+2*k*q-q*q*z+2*q*z*z+2*q-3*z)
    a=2*q*(k+1)*(q-z)*z/D
    b=-2*(k-1)*(q*z-1)*z/D
    S=S_entries(k)
    d=S[2][0]*a+S[2][1]*b*q/z+S[2][2]
    return a,b,d,D

def matvec(M,v):
    return [sum(M[i][j]*v[j] for j in range(3)) for i in range(3)]

max_eq=0.0
for k,theta,phase in [(17.0,0.4,1.3),(43.0,-1.1,2.2),(101.0,2.0,-0.7)]:
    q=cmath.exp(1j*phase)
    a,b,d,D=exact_ratios(k,theta,q)
    z=cmath.exp(1j*theta)
    lhs=matvec(S_entries(k),[a,b*q/z,1.0])
    rhs=[b,a/q/z,d]
    max_eq=max(max_eq,max(abs(lhs[i]-rhs[i]) for i in range(3)))
assert max_eq < 2e-12

max_limit=0.0
for s in (1,-1):
    for theta,xi in [(0.7,3.1),(-0.5,2.2),(1.2,-1.7)]:
        if abs(s*xi-2*math.sin(theta))<0.2:
            continue
        R=(s-cmath.exp(1j*theta))/(1j*(s*xi-2*math.sin(theta)))
        k=200000.0
        q=s*cmath.exp(1j*xi/k)
        a,b,d,D=exact_ratios(k,theta,q)
        max_limit=max(max_limit,abs(a-R),abs(b-R),abs(d-1.0))
assert max_limit < 2e-3

# Corroborate the outer estimate along a shrinking detuning delta=k^{-1/2}.
scaled=[]
for k in (2000.0,8000.0,32000.0):
    delta=k**-0.5
    q=cmath.exp(1j*delta)
    a,b,d,D=exact_ratios(k,0.9,q)
    scaled.append(k*abs(math.sin(delta))*max(abs(a),abs(b)))
assert max(scaled) < 10.0
print('VERIFY_OK max_eq=%.3e max_limit=%.3e scaled_max=%.6f' % (max_eq,max_limit,max(scaled)))
