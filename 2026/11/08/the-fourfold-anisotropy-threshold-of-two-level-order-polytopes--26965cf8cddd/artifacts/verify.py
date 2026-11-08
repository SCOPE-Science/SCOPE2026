"""Exact checks for covariance of the uniform-volume two-layer order polytope.

Python 3 standard library only. Exhaustive rank assignments are finite checks,
not a substitute for the all-parameter analytical proof.
"""
from fractions import Fraction as F
from itertools import permutations
from math import factorial, sqrt


def theoretical(p, q):
    n = p+q
    lp = F((p+1)*(p+2), 12*(n+1)*(n+2))
    lq = F((q+1)*(q+2), 12*(n+1)*(n+2))
    va = F((p+1)*(p*p+4*p*q+3*p+2*q+2),12*p*(n+1)**2*(n+2))
    vb = F((q+1)*(q*q+4*p*q+3*q+2*p+2),12*q*(n+1)**2*(n+2))
    cab=F((p+1)*(q+1),4*(n+1)**2*(n+2))
    C=[]
    for i in range(n):
        row=[]
        for j in range(n):
            if i<p and j<p:
                val=lp*(int(i==j)-F(1,p))+va
            elif i>=p and j>=p:
                val=lq*(int(i==j)-F(1,q))+vb
            else:
                val=cab
            row.append(val)
        C.append(row)
    return C,lp,lq,p*va,q*vb,p*q*cab*cab


def independent_enumeration(p,q):
    n=p+q
    mu=[F(0) for _ in range(n)]
    raw=[[F(0) for _ in range(n)] for _ in range(n)]
    num=factorial(p)*factorial(q)
    # The simplices of the Stanley triangulation are indexed by these assignments.
    for left in permutations(range(1,p+1)):
        for right in permutations(range(p+1,n+1)):
            ranks=left+right
            for i,a in enumerate(ranks):
                mu[i]+=F(a,n+1)
                for j,b in enumerate(ranks):
                    raw[i][j]+=F(min(a,b)*(max(a,b)+1),(n+1)*(n+2))
    mu=[v/num for v in mu]
    return [[raw[i][j]/num-mu[i]*mu[j] for j in range(n)] for i in range(n)]


def spectral_verification(p,q,lp,lq,A,B,C2):
    # Rational characteristic polynomial of the 2x2 block-constant restriction.
    n=p+q
    tr=A+B
    det=A*B-C2
    assert det>0 and tr>0
    disc=tr*tr-4*det
    assert disc>0
    small=float(tr-sqrt(float(disc)))/2
    big=float(tr+sqrt(float(disc)))/2
    assert big>max(float(lp),float(lq))
    assert small>0
    if p<=q:
        if q<=p+1: assert small<float(lp)
        else: assert small>float(lp)
        assert small<float(lq)
    else:
        if p<=q+1: assert small<float(lq)
        else: assert small>float(lq)
        assert small<float(lp)
    # Exact determinant comparison identities, with no floating-point assumption.
    left_p=(A-lp)*(B-lp)-C2
    pred_p=F(p*q*(p+1)*(q*q-p*p-3*p-3),48*(n+1)**3*(n+2)**2)
    left_q=(A-lq)*(B-lq)-C2
    pred_q=F(p*q*(q+1)*(p*p-q*q-3*q-3),48*(n+1)**3*(n+2)**2)
    assert left_p==pred_p and left_q==pred_q
    # The all-ones Rayleigh quotient is universally 1/12.
    # The all-ones covariance is a weighted block expression.
    # Using C2 with the known positive cross-covariance.
    cross=F((p+1)*(q+1),4*(n+1)**2*(n+2))
    assert p*A+q*B+2*p*q*cross==F(n,12)
    if p==q:
        assert tr==F(1,12)+F(p*p+p+1,12*(2*p+1)**2)
        assert F(1,12)**2-tr*F(1,12)+det==0
        assert (2*p+1)**2>0 and (2*p+1)**2<4*(p*p+p+1)
    elif abs(p-q)==1:
        r=min(p,q)
        expected=F(5*r*r+50*r+44,576*(r+1)**2*(2*r+3)**2)
        assert 25*det-4*tr*tr==expected and expected>0
    else:
        r=min(p,q); h=max(p,q)
        lr=F((r+1)*(r+2),12*(p+q+1)*(p+q+2))
        assert lr<F(1,48)


def run():
    profiles=0; entries=0
    for p in range(2,6):
        for q in range(2,7):
            if p+q>9: continue
            C,lp,lq,A,B,C2=theoretical(p,q)
            E=independent_enumeration(p,q)
            assert C==E,(p,q)
            profiles+=1; entries+=(p+q)**2
    spectral=0
    for p in range(2,80):
        for q in range(2,80):
            n=p+q
            lp=F((p+1)*(p+2),12*(n+1)*(n+2)); lq=F((q+1)*(q+2),12*(n+1)*(n+2))
            A=F((p+1)*(p*p+4*p*q+3*p+2*q+2),12*(n+1)**2*(n+2))
            B=F((q+1)*(q*q+4*p*q+3*q+2*p+2),12*(n+1)**2*(n+2))
            C2=F(p*q*(p+1)**2*(q+1)**2,16*(n+1)**4*(n+2)**2)
            spectral_verification(p,q,lp,lq,A,B,C2)
            spectral+=1
    print('TWO_LAYER_ORDER_COVARIANCE_CHECKS_PASSED exact_profiles=%d entries=%d spectral_profiles=%d'%(profiles,entries,spectral))

if __name__=='__main__': run()
