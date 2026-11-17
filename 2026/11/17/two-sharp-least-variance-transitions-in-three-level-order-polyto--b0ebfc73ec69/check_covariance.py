"""Exact-rational regression checks for three-level order-polytope covariance.

Standard-library only. Tests independent order-statistic moment summations against
block formulas and integer spectral transition signs. This is finite corroboration;
the accompanying proof handles all positive integer parameters.
"""
from fractions import Fraction as F


def moments_by_order_stats(p, q):
    n = 2*p+q
    d = (n+1)**2*(n+2)
    ranks = [list(range(1,p+1)),
             list(range(p+1,p+q+1)),
             list(range(p+q+1,n+1))]
    # Mean covariance in each block from ALL order-statistic pair moments.
    mean_cov = [[sum((F(min(r,s)*(n+1-max(r,s)),d)
                       for r in left for s in right),F(0))/len(left)/len(right)
                 for right in ranks] for left in ranks]
    # Covariance of a specified coordinate in two different blocks equals
    # covariance of the block means. Within a group, contrast eigenvalue
    # is half the mean squared difference of two randomly assigned ranks.
    contrast = []
    for block in ranks:
        if len(block)<2:
            contrast.append(None)
        else:
            v = sum((F(abs(r-s)*(abs(r-s)+1), (n+1)*(n+2))
                     for r in block for s in block if r!=s),F(0))
            contrast.append(v/(2*len(block)*(len(block)-1)))
    return mean_cov, contrast


def closed(p,q):
    n=2*p+q
    d=(n+1)*(n+2)
    c_p=F((p+1)*(p+2),12*d)
    c_q=F((q+1)*(q+2),12*d)
    # Normalized block-constant covariance in an orthonormal 3-vector basis:
    # [[A,B,C],[B,T,B],[C,B,A]]. B = sqrt(p*q)*(p+1)/(4*d).
    A=F((p+1)*(5*p*p+4*p*q+5*p+2*q+2),12*(n+1)*d)
    C=F(p*(p+1)**2,4*(n+1)*d)
    T=F(6*p*q+q*q+3*q+2,12*d)
    B2=F(p*q*(p+1)**2,16*d*d)
    S=A+C
    anti=A-C
    def f(x):return (S-x)*(T-x)-2*B2
    return A,C,T,B2,c_p,c_q,S,anti,f


def run():
    cases=0
    exact_pair_terms=0
    for p in range(2,18):
        for q in range(1,2*p+12):
            cases+=1
            n=2*p+q
            d=(n+1)*(n+2)
            exact_pair_terms+=n*n
            mc,contrast=moments_by_order_stats(p,q)
            A,C,T,B2,cp,cq,S,anti,f=closed(p,q)
            assert mc[0][0]*p==A
            assert mc[0][2]*p==C
            assert mc[1][1]*q==T
            assert mc[0][1]**2*p*q==B2
            assert mc[1][2]==mc[0][1]
            assert mc[2][2]==mc[0][0]
            assert contrast[0]==cp and contrast[2]==cp
            if q>=2:assert contrast[1]==cq
            else:assert contrast[1] is None
            # Exact algebraic certificates, no floating-point eigenvalues.
            assert f(cp)==F(-p*(p+1)*(p+q)*(p-q+3),48*d*d)
            assert f(cq)==F(p*q*(p*p-q*q-3*q-3),24*d*d)
            assert f(anti)<0
            assert S>cp and T>cq and C>0 and B2>0
            # λ_+ > both contrast eigenvalues, λ_- < anti < λ_+.
            # Hence sign(f(c)) is sign(λ_- - c).
            assert (f(cp)>0) == (q>=p+4)
            assert (f(cp)==0) == (q==p+3)
            if q>=2:
                assert (f(cq)>0)==(q<=p-2)
                assert (f(cq)<0)==(q>=p-1)
            # Decide minimum eigenmode from independently computed signs.
            vals={'sym_low':0}
            if q==1: expected='sym_low'
            elif q<=p-2:expected='middle_contrast'
            elif q<=p+2:expected='sym_low'
            elif q==p+3:expected='tie_outer_sym_low'
            else:expected='outer_contrast'
            if q==1 or q>=p-1 and q<=p+2:
                assert f(cp)<0 and (q==1 or f(cq)<0)
                observed='sym_low'
            elif q<=p-2 and q>=2:
                assert cq<cp and f(cq)>0
                observed='middle_contrast'
            elif q==p+3:
                assert f(cp)==0 and cp<cq
                observed='tie_outer_sym_low'
            else:
                assert f(cp)>0 and cp<cq
                observed='outer_contrast'
            assert observed==expected,(p,q,expected,observed)
    print('THREE_LEVEL_ORDER_COVARIANCE_EXACT_PASS profiles=%d order_statistic_pairs=%d'% (cases,exact_pair_terms))

if __name__=='__main__':run()
