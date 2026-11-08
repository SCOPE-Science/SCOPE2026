#!/usr/bin/env python3
"""Reproduce exact-rational finite checks for the generalized tent periodic-census transport identity.

All finite checks below are supplementary: the all-period theorem is proved in RESULT.md.
"""
from fractions import Fraction as Q
from itertools import product


def branch(word, H):
    # Return a, b for S_word(x) = a*x + b with S_0(x)=x/H,
    # S_1(x)=1-x/H. The first symbol is the outermost branch.
    a,b=Q(1),Q(0)
    r=1/H
    for d in reversed(word):
        if d==0: a,b=r*a,r*b
        else: a,b=-r*a,1-r*b
    return a,b


def fixed_points(n,H):
    for w in product((0,1),repeat=n):
        a,b=branch(w,H)
        yield w,b/(1-a)


def tent(t,H):
    return H*min(t,1-t)


def phi_periodic(p,n,H):
    # Phi(t)=E_mu |X-t|; exact functional equation
    # Phi(t)=Phi(f(t))/(2H)+c(t) on the repeller.
    q=1/(2*H)
    v=p; total=Q(0)
    for j in range(n):
        c=(Q(1,2)-Q(1,4)/H-v/Q(2)) if v<=Q(1,2) else (v/Q(2)-Q(1,4)/H)
        total += q**j*c
        v=tent(v,H)
    assert v==p
    return total/(1-q**n)


def formula(n,H):
    return H**(-n)*(H-1)/(2*H-1)*(1+1/(2*(H**(2*n)-1)))


def check_symbolic():
    cases=0; points=0
    for H in (Q(2),Q(3),Q(4),Q(5,2),Q(7,3)):
        for n in range(1,9):
            pts=list(fixed_points(n,H))
            assert len(pts)==2**n and len(set(p for _,p in pts))==2**n
            for w,p in pts:
                assert Q(0)<=p<=Q(1)
                a,b=branch(w,H)
                assert a*p+b==p
            mean=sum((p for _,p in pts),Q(0))/len(pts)
            target_mean=(1-H**(-(2*n-1)))/(2*(1-H**(-2*n)))
            assert mean==target_mean,(H,n,mean,target_mean)
            phi_average=sum((phi_periodic(p,n,H) for _,p in pts),Q(0))/len(pts)
            assert phi_average == Q(1,2)-mean/(2*H-1)
            answer=H**(-n)*phi_average
            assert answer==formula(n,H),(H,n,answer,formula(n,H))
            cases+=1;points+=len(pts)
    return cases,points


def midpoint_approx(n,k,H):
    # Finite n-point law vs finite-k midpoint discretization of Cantor law.
    # Monotone coupling assigns each cylinder K_w to its unique point p_w;
    # using S_v(1/2), v of length k, yields an independent finite approximation.
    assert k>=n
    total=Q(0)
    for v in product((0,1),repeat=k):
        a,b=branch(v,H)
        a0,b0=branch(v[:n],H)
        p=b0/(1-a0)
        total+=abs(a*Q(1,2)+b-p)
    return total/Q(2**k)


def check_independent():
    trials=0
    for H in (Q(2),Q(3),Q(5,2)):
        for n in range(1,5):
            k=11
            w_mid=midpoint_approx(n,k,H)
            # Each depth-k point differs from its true cylinder remainder by <= H^-k/2.
            assert abs(w_mid-formula(n,H)) <= H**(-k)/2, (H,n,w_mid,formula(n,H))
            trials+=1
    return trials


if __name__=='__main__':
    c,p=check_symbolic()
    k=check_independent()
    print('PASS:',c,'exact (slope,period) cases,',p,'fixed points; ',k,'independent cylinder transport approximations')
    for H,n in ((Q(2),1),(Q(2),3),(Q(3),1),(Q(3),3),(Q(5,2),4)):
        print('H =',H,'n =',n,'W1 =',formula(n,H))
