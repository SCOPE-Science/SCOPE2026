"""Exact Dirichlet polynomial checks of ranked-spacing/Greenwood covariance.

Uses Python's standard library; no external data or dependencies.
The finite verifier corroborates the separately supplied all-size proof.
"""
from fractions import Fraction as F
from math import factorial, log, sqrt


def h(n, power=1):
    return sum((F(1, j**power) for j in range(1, n+1)), F(0))


def formula(m, k):
    a = h(m)-h(k-1)
    b = h(m, 2)-h(k-1, 2)
    return (a*a+b-2*a)/F(m*(m+1)*(m+2))


def moment(m, *indices):
    """Direct normalized simplex monomial integration, independent of covariance formula."""
    count = {}
    for j in indices:
        count[j] = count.get(j, 0)+1
    top = 1
    for n in count.values():
        top *= factorial(n)
    return F(top*factorial(m-1), factorial(m+len(indices)-1))


def brute_cov(m, k):
    # Ordered spacings X_(k)=sum_{j>=k} P_j/j; Q=sum_{a,b} P_a P_b/max(a,b).
    ey = sum((moment(m, j)/j for j in range(k, m+1)), F(0))
    eq = sum((moment(m, a, b)/max(a,b) for a in range(1, m+1) for b in range(1, m+1)), F(0))
    eyq = sum((moment(m, j, a, b)/F(j*max(a,b))
              for j in range(k, m+1)
              for a in range(1, m+1) for b in range(1, m+1)), F(0))
    return eyq-ey*eq


def var_rank(m, k):
    a = h(m)-h(k-1)
    b = h(m, 2)-h(k-1, 2)
    return F(m*b-a*a, m*m*(m+1))


def var_greenwood(m):
    return F(4*(m-1), (m+1)**2*(m+2)*(m+3))


def cutoff(m):
    return sum(formula(m,k)>0 for k in range(1,m+1))


def main():
    checked=0
    for m in range(2,18):
        for k in range(1,m+1):
            assert formula(m,k)==brute_cov(m,k), (m,k)
            checked+=1
    # Crucial moment and boundary equalities.
    for m in range(2,100):
        assert formula(m,1)>0 and formula(m,m)<0
        checked+=2
        signs=[(formula(m,k)>0)-(formula(m,k)<0) for k in range(1,m+1)]
        assert all(signs[i]>=signs[i+1] for i in range(m-1)), (m,signs)
        assert var_rank(m,1)>0 and var_rank(m,m)>0 and var_greenwood(m)>0
        checked+=2
    for m in [100,300,1000,3000,10000]:
        # Float-based large-size sign profile and analytic cutoff.
        hm=sum(1/j for j in range(1,m+1))
        h2=sum(1/(j*j) for j in range(1,m+1))
        positive=0
        aa=hm; bb=h2
        for k in range(1,m+1):
            val=aa*aa+bb-2*aa
            if val>0: positive+=1
            aa-=1/k;bb-=1/(k*k)
        assert abs(positive/m-__import__('math').exp(-2))<.025, (m, positive)
        checked+=1
    for alpha in [0.05, 0.1, 0.1353352832366127, 0.2, 0.4, 0.7]:
        m=3000;k=max(1,int(m*alpha))
        c=float(formula(m,k)); v1=float(var_rank(m,k));v2=float(var_greenwood(m))
        correlation=c/sqrt(v1*v2)
        ll=log(1/alpha)
        target=(ll*ll-2*ll)/(2*sqrt(1/alpha-1-ll*ll))
        assert abs(correlation-target)<.035,(alpha, correlation,target)
        checked+=1
    print(f'PASS: {checked} exact/analytic checks plus asymptotic tests')
    print('positive rank counts: '+str({m:cutoff(m) for m in [4,8,20,50,100,200]}))

if __name__=='__main__':main()
