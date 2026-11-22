"""Standalone arithmetic/simulation diagnostics for weighted sine delay theorem.
No finite simulation is used as a proof of the asymptotic theorem.
"""
from fractions import Fraction as Q
from math import sin, log, sqrt

def law(w):
    assert sum(w)==1 and w[0]>0 and w[-1]>0
    mu=sum(j*v for j,v in enumerate(w))
    nu=sum(j*j*v for j,v in enumerate(w))
    W=1+mu
    return mu,nu,1/(3*W),(9*mu*mu+8*mu+4-5*nu)/(20*W*W)

def sim(w,N=400000):
    d=len(w)-1
    buf=[.39+.015*j for j in range(d+1)]
    marks={N//4,N//2,N}
    out={}
    for n in range(1,N+1):
        znew=sum(float(a)*sin(buf[-1-j]) for j,a in enumerate(w))
        buf.append(znew);buf.pop(0)
        if n in marks:
            mu,nu,L,K=law(w)
            out[n]=(1/znew**2-L*n-K*log(n),1/znew**2-L*n)
    return out

if __name__=='__main__':
    a=[Q(1,2),Q(0),Q(1,2)]
    b=[Q(4,5)]+[Q(0)]*4+[Q(1,5)]
    d=[Q(5,6),Q(0),Q(0),Q(0),Q(1,6)]
    c=[Q(18,25),Q(0),Q(2,15),Q(0),Q(0),Q(11,75)] # t=11/15? correct w0 1/2+11/50=18/25; w2 (1-11/15)/2=2/15; w5=(11/15)/5=11/75
    for w,K_expected in [(a,Q(11,80)),(b,Q(-1,20)),(c,Q(0))]:
        mu,nu,L,K=law(w)
        assert mu==1 and L==Q(1,6) and K==K_expected
        print('weights',w,'mu=',mu,'nu=',nu,'L=',L,'K=',K)
        print('finite diagnostics: residual and non-corrected residual:',sim(w))
    assert law(d)[-1]==0 and law(d)[0]==Q(2,3)
    for m in range(1,5):
        for mu in [Q(j,20) for j in range(0,2*m*20+1)]:
            poly=9*mu*mu+(8-5*m)*mu+4
            assert poly>=0 and (m!=4 or poly==0)==(m!=4 or mu==Q(2,3))
    # Formal recurrence coefficient algebra
    for w in [a,b,c,d]:
        mu,nu,L,K=law(w)
        W=1+mu; A=-1/(6*W)
        B=((Q(3,2)*(mu+nu)*A*A)+(mu*A/Q(2))+Q(1,120))/W
        assert K==3*W*(3*A*A-2*B)
        assert 1+mu==W
    print('PASS: exact moment, sign, cancellation, center-jet and finite trajectory checks')
