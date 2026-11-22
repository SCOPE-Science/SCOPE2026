"""Numerical diagnostics for affine-Fock composition-difference theorem.

Only diagnostic finite-dimensional checks; the infinite-dimensional statements
are established by analytical estimates in RESULT.md.
"""
import math
import numpy as np

def coefficient(n,k,q,u,v):
    if k == 0:
        return 0j
    # m=n-k and sqrt(n!/m!)/k! expressed through log gamma
    m=n-k
    log_amp=0.5*(math.lgamma(n+1)-math.lgamma(m+1))-math.lgamma(k+1)
    return math.exp(log_amp)*(q**m)*((1-q)**k)*(u**k-v**k)

def hs_closed(q,u,v):
    a=(1-q)/(1+q)
    return (math.exp(a*abs(u)**2)+math.exp(a*abs(v)**2)
            -2*(np.exp(a*u*complex(v).conjugate())).real)/(1-q*q)

def matrix(q,u,v,n):
    out=np.zeros((n,n),dtype=complex)
    for col in range(n):
        for k in range(1,col+1):
            out[col-k,col]=coefficient(col,k,q,u,v)
    return out

def leading_norm(q,delta,p,N=6000):
    a=np.arange(1,N+1,dtype=float)
    w=(1-q)*abs(delta)*np.sqrt(a)*np.exp((a-1)*math.log(q))
    return float(w.max() if p==math.inf else (np.sum(w**p))**(1/p))

def asymp_const(delta,p):
    return abs(delta)/math.sqrt(2*math.e) if p==math.inf else abs(delta)*math.gamma(1+p/2)**(1/p)/p**(1/p+0.5)

def check():
    tests=0; worst_hs=0; worst_matrix=0
    for q in (0.5,0.75,0.9):
        for u,v in ((1+0j,0j),(0.6+0.2j,-0.3+0.4j),(1j,0.25-0.75j)):
            mat=matrix(q,u,v,260)
            empirical=float(np.sum(np.abs(mat)**2))
            target=hs_closed(q,u,v)
            rel=abs(empirical-target)/max(1e-12,target)
            assert rel<1e-9,(q,u,v,rel,empirical,target)
            worst_matrix=max(worst_matrix,rel);tests+=1
            # Independent direct sum over columns for the Hilbert-Schmidt norm
            series=0.0
            for n in range(1,261):
                for k in range(1,n+1):
                    series+=abs(coefficient(n,k,q,u,v))**2
            rel=abs(series-target)/max(1e-12,target)
            assert rel<1e-9,(q,u,v,rel)
            worst_hs=max(worst_hs,rel);tests+=1
    # Verify the asymptotic constants for the explicit leading weighted shift.
    asymptotic=[]
    for q in (0.97,0.985,0.992):
        for p in (1,2,4,math.inf):
            got=leading_norm(q,1+0.25j,p)
            norm=got/((1-q)**(0.5-(0 if p==math.inf else 1/p)))
            c=asymp_const(1+0.25j,p)
            err=abs(norm/c-1)
            assert err<0.06,(q,p,err)
            asymptotic.append((q,p,round(err,6)))
            tests+=1
    # Actual finite-dimensional difference vs its first derivative term.
    for q in (0.65,0.78,0.86):
        u,v=0.6+0.2j,-0.3+0.4j
        mat=matrix(q,u,v,180)
        leading=np.zeros_like(mat)
        for n in range(1,180):
            leading[n-1,n]=(1-q)*(u-v)*math.sqrt(n)*q**(n-1)
        err=float(np.linalg.norm(mat-leading,2))
        assert err < 6*(1-q), (q,err)
        tests+=1
    print('PASS',tests,'test groups; worst HS direct-matrix relative error',worst_matrix,
          'worst independently resummed error',worst_hs)
    print('Leading-shift asymptotic relative errors:',asymptotic)
if __name__=='__main__':
    check()
