"""Reproducible exact checks for two-orbit shrinking collision variance."""
from fractions import Fraction
from math import gcd, log, isclose
from itertools import product


def gcd_pair(a, b):
    for r in range(1, 15):
        for t in range(1, 15):
            if a**r == b**t:
                return r, t, a**r
    return None


def covariance(q, eps):
    assert 0 < eps < Fraction(1,2)
    y = q * eps
    n = y.numerator // y.denominator
    u = y - n
    integral = 2*eps*n + min(u, eps) + max(Fraction(0), u+eps-1)
    probability = Fraction(2, q)*integral
    return probability - 4*eps**2


def covariance_independent(q, eps):
    """Count intersection lengths of the two sets of modulo-one windows directly."""
    arcs = ((Fraction(0), eps), (1-eps, Fraction(1)))
    vals=[]
    for k in range(q):
        for lower, upper in arcs:
            vals.append(((k+lower)/q,(k+upper)/q))
    hit = 0
    for a,b in arcs:
        for c,d in vals:
            hit += max(Fraction(0), min(b,d)-max(a,c))
    return hit - 4*eps**2


def variance(a,b,s,N):
    eps = Fraction(s,N)
    assert eps < Fraction(1,2)
    base = N*N*2*eps*(1-2*eps)
    resonance = gcd_pair(a,b)
    if resonance is None: return base
    r,t,q = resonance
    for k in range(1, min((N-1)//r, (N-1)//t)+1):
        base += 2*(N-r*k)*(N-t*k)*covariance(q**k,eps)
    return base


def variance_direct_pairs(a,b,s,N):
    """Pairwise covariance sum by determinant, independent of grouped resonance count."""
    eps = Fraction(s,N)
    total = N*N*2*eps*(1-2*eps)
    pairs = list(product(range(N),repeat=2))
    for idx,(i,j) in enumerate(pairs):
        for i2,j2 in pairs[idx+1:]:
            if a**i*b**j2==a**i2*b**j:
                # compute directed integer scaling of dependent rows
                k_num = a**i2
                k_den = a**i
                if k_num < k_den:
                    k_num,k_den=k_den,k_num
                qval=k_num//k_den
                assert k_num%k_den==0
                total+=2*covariance(qval,eps)
    return total


def main():
    n_intersections=0
    for q in (2,3,4,5,7,8,9,16,25,27,64):
        for eps in (Fraction(1,13),Fraction(2,13),Fraction(3,11),Fraction(1,4),Fraction(4,11)):
            assert covariance(q,eps) == covariance_independent(q,eps),(q,eps)
            n_intersections+=1
    n_exact=0
    for a,b in ((2,2),(3,3),(2,3),(4,2),(2,4),(4,8),(8,4),(3,9),(3,4)):
        for N in (3,4,5,7,9):
            for s in (Fraction(1,3),Fraction(3,4)):
                assert variance(a,b,s,N)==variance_direct_pairs(a,b,s,N), (a,b,N,s)
                n_exact+=1
    assert variance(2,3,Fraction(2,3),25)==2*Fraction(2,3)*25-4*Fraction(2,3)**2
    n_asymptotic=0
    for a,b in ((2,2),(2,4),(4,8),(3,3),(2,3)):
        for s in (Fraction(1,3),Fraction(3,4)):
            resonance = gcd_pair(a,b)
            for N in (200,400,800):
                v=float(variance(a,b,s,N))
                if resonance:
                    r,t,q = resonance
                    residual=v - (2*float(s)*N*(q+1)/(q-1)) + 8*float(s)**2*log(N)/log(q)
                    assert abs(residual)<50,(a,b,s,N,residual)
                else:
                    assert v == float(2*s*N-4*s*s)
                n_asymptotic+=1
    print(f'VERIFY_OK independent_arc_intersections={n_intersections} grouped_pair_covariances={n_exact} asymptotic_residual_tests={n_asymptotic} independent_base_exact=True')

if __name__=='__main__': main()
