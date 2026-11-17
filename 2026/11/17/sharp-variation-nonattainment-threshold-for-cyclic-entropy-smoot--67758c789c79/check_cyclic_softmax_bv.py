"""Reproducibility checks for cyclic window log-sum-exp total-variation stability.
Uses exact rational arithmetic on every Jacobian factorization and finite numerical
secants only as diagnostic checks; the general theorem is analytical.
"""
from fractions import Fraction as Q
from random import Random
from math import exp, log

def edge_factor(a, w):
    n = len(a)
    assert 1 <= w < n
    C = [[Q(0) for _ in range(n)] for _ in range(n)]
    def cdf(start, k):
        total = sum(a[j % n] for j in range(start,start+w))
        return sum(a[j % n] for j in range(start, min(start+w,k+1))) / total
    for i in range(n):
        for k in range(i,i+w):
            C[i][k % n] = cdf(i,k)-cdf(i+1,k)
    return C

def softmax_filter(x,w,tau=1.0,weights=None):
    n=len(x)
    if weights is None: weights=[1.0]*n
    out=[]
    for i in range(n):
        terms=[x[(i+j)%n]/tau+log(weights[(i+j)%n]) for j in range(w)]
        m=max(terms)
        out.append(tau*(m+log(sum(exp(t-m) for t in terms))))
    return out

def tv(x):return sum(abs(x[(i+1)%len(x)]-x[i]) for i in range(len(x)))

def test():
    rng=Random(32003)
    exact_cases=0
    strict_cases=0
    sharp_cases=0
    secants=0
    for n in range(2,13):
        for w in range(1,n):
            for trial in range(12):
                a=[Q(rng.randint(1,20),rng.randint(1,20)) for _ in range(n)]
                C=edge_factor(a,w)
                for k in range(n):
                    assert sum(C[i][k] for i in range(n))==1
                for i in range(n):
                    for k in range(n):
                        expected=(((k-i)%n)<w)
                        assert (C[i][k]>0)==expected
                h=[Q(rng.randint(-10,10),rng.randint(1,8)) for _ in range(n)]
                jh=[]
                for i in range(n):
                    total=sum(a[j%n] for j in range(i,i+w))
                    jh.append(sum(a[j%n]*h[j%n] for j in range(i,i+w))/total)
                grad=[h[(k+1)%n]-h[k] for k in range(n)]
                for i in range(n):
                    assert jh[(i+1)%n]-jh[i]==sum(C[i][k]*grad[k] for k in range(n))
                if 2*w>n:
                    for k in range(n):
                        for j in range(k+1,n):
                            assert any(C[i][k]>0 and C[i][j]>0 for i in range(n))
                    strict_cases+=1
                exact_cases+=1
            x=[rng.uniform(-5,5) for _ in range(n)]
            y=[rng.uniform(-5,5) for _ in range(n)]
            q=[rng.uniform(.3,5) for _ in range(n)]
            for tau in (.2,1.0,3.0):
                xx=softmax_filter(x,w,tau,q)
                yy=softmax_filter(y,w,tau,q)
                assert tv([xx[i]-yy[i] for i in range(n)]) <= tv([x[i]-y[i] for i in range(n)])+3e-10
                secants+=1
            if 2*w<=n:
                z=[rng.uniform(-3,3) for _ in range(n)]
                h=[1 if j<w else 0 for j in range(n)]
                f=softmax_filter([z[j]+h[j] for j in range(n)],w,1.7,q)
                g=softmax_filter(z,w,1.7,q)
                assert abs(tv([f[j]-g[j] for j in range(n)])/tv(h)-1)<1e-12
                sharp_cases+=1
            else:
                x=[35.0]+[0.0]*(n-1)
                y=[36.0]+[0.0]*(n-1)
                f=softmax_filter(x,w)
                g=softmax_filter(y,w)
                ratio=tv([g[j]-f[j] for j in range(n)])/tv([y[j]-x[j] for j in range(n)])
                assert ratio>0.99999999
    for n in range(2,13):
        x=[rng.uniform(-3,3) for _ in range(n)]
        assert tv(softmax_filter(x,n)) < 1e-12
    print('EXACT_RATIONAL_JACOBIAN_COLUMN_STOCHASTIC_CASES_PASS',exact_cases)
    print('STRICT_COLUMN_OVERLAP_CASES_PASS',strict_cases)
    print('FINITE_ATTAINMENT_CASES_PASS',sharp_cases)
    print('WEIGHTED_POSITIVE_TEMPERATURE_TWO_INPUT_CHECKS_PASS',secants)
    print('FULL_WINDOW_CONSTANT_OUTPUT_PASS')
    print('ALL_CYCLIC_SOFTMAX_BV_CHECKS_PASS')

if __name__=='__main__':test()
