"""Reproduce exact Fourier boundary blocks and optimal residual identities.

Uses only Python's standard library. Finite tests illustrate the algebraic proof
in RESULT.md; they do not replace its all-cutoff argument.
"""
from fractions import Fraction as Q
from math import sqrt, cos, sin

def action_entry(m, k, beta, gamma):
    v = Q(-k*k) if m == k else Q(0)
    if m == k+1 or m == k-1:
        v -= beta*Q(k*m, 2)
    if m == k+2 or m == k-2:
        v -= gamma*Q(k*m, 2)
    return v

def exact_block(K, beta, gamma):
    # Input coefficients e_(K-1), e_K; output e_(K+1), e_(K+2).
    return [[action_entry(j,k,beta,gamma) for k in (K-1,K)]
            for j in (K+1,K+2)]

def trace_det(K, y):
    a,b,c=K*K-1,K*(K+1),K*(K+2)
    A,B,C=a*a,b*b,c*c
    tr=B+(A+C-B)*y
    det=A*C*y*y
    return tr,det

count=0
for K in range(2,45):
    a,b,c=K*K-1,K*(K+1),K*(K+2)
    A,B,C=a*a,b*b,c*c
    d=A+C-B
    delta=4*A*C-d*d
    assert d>0 and delta>0 and C>A and C>B
    count+=4
    for beta,gamma in [(Q(1,7),Q(2,9)),(Q(-1,11),Q(3,13)),(Q(4,19),Q(-2,17)),(Q(0),Q(1,3)),(Q(1,4),Q(0))]:
        z=exact_block(K,beta,gamma)
        expect=[[gamma*Q(-a,2),beta*Q(-b,2)],[Q(0),gamma*Q(-c,2)]]
        assert z==expect
        count+=1
        # Check all omitted columns and outputs vanish.
        for k in range(-K,K+1):
            for m in (-K-2,-K-1,K+1,K+2):
                v=action_entry(m,k,beta,gamma)
                nonzero=((k==K-1 and m==K+1 and gamma) or
                         (k==K and m==K+1 and beta) or
                         (k==K and m==K+2 and gamma) or
                         (k==-K+1 and m==-K-1 and gamma) or
                         (k==-K and m==-K-1 and beta) or
                         (k==-K and m==-K-2 and gamma))
                assert v==0 if not nonzero else v!=0
                count+=1
        # The two 2-by-2 boundary blocks have identical Gram spectra.
        up=[[action_entry(m,k,beta,gamma) for k in (K-1,K)] for m in (K+1,K+2)]
        lo=[[action_entry(m,k,beta,gamma) for k in (-K+1,-K)] for m in (-K-1,-K-2)]
        for z0 in (up,lo):
            g11=sum(row[0]**2 for row in z0)
            g22=sum(row[1]**2 for row in z0)
            g12=sum(row[0]*row[1] for row in z0)
            assert g11+g22==Q(A+C,4)*gamma**2 + Q(B,4)*beta**2
            assert g11*g22-g12*g12==Q(A*C,16)*gamma**4
            count+=2
    ystar=Q(2*B*d,delta)
    lstar=Q(4*A*C*B,delta)
    assert ystar>0 and (ystar<1 if K>=4 else ystar>1)
    count+=2
    if K>=4:
        tr,det=trace_det(K,ystar)
        assert lstar*lstar-tr*lstar+det==0
        assert d*lstar==2*A*C*ystar
        assert lstar>max(B,C)
        assert 0<1-ystar<1
        count+=4
    else:
        assert C-A-B>0
        count+=1
    # Check no interior crossing of the predicted optimum over dense samples.
    opt=float(lstar if K>=4 else C)
    for j in range(101):
        y=j/100
        tr,det=trace_det(K,y)
        x=(float(tr)+sqrt(max(0.0,float(tr*tr-4*det))))/2
        assert x<=opt*(1+1e-12)
        count+=1
print('VERIFY_OK',count)

# General relative Fourier phases leave both squared singular values unchanged.
from cmath import exp
for K in range(2,30):
    a,b,c=K*K-1,K*(K+1),K*(K+2)
    for phi,psi in ((0.23,1.11),(2.13,-0.8),(-2.4,0.7)):
        beta,gamma=0.13,0.22
        z=[[ -gamma*a/2*exp(-2j*psi), -beta*b/2*exp(-1j*phi)],
           [0j,-gamma*c/2*exp(-2j*psi)]]
        trace=sum(abs(w)**2 for row in z for w in row)
        det=abs(z[0][0]*z[1][1])**2
        expecttrace=(gamma**2*(a*a+c*c)+beta**2*b*b)/4
        expectdet=(gamma**4*a*a*c*c)/16
        assert abs(trace-expecttrace)<1e-9*expecttrace
        assert abs(det-expectdet)<1e-9*expectdet
        count+=2
print('PHASE_VERIFY_OK',count)
