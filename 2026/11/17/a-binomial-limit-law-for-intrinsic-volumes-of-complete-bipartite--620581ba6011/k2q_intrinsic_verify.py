"""Independent finite checks of Euclidean forest Gram determinants and Steiner coefficients.

Requires Python >=3.10, sympy, scipy, numpy. No network or external data.
"""
from collections import Counter, defaultdict
from itertools import combinations, product
from math import comb, sqrt, isclose
from sympy import Matrix


def predicted_counts(q):
    out = [Counter() for _ in range(q+2)]
    for k in range(q+1):
        for a in range(k+1):
            b=k-a
            out[k][(a+1)*(b+1)] += comb(q,k)*comb(k,a)
    for k in range(2,q+2):
        out[k][k+1] += q*comb(q-1,k-2)*2**(k-2)
    return out


def brute_counts(q):
    n=q+2
    columns=[]
    for j in range(q):
        for i in range(2):
            v=[0]*n;v[i]=1;v[j+2]=-1;columns.append(v)
    out=[Counter() for _ in range(q+2)]
    tests=0
    for k in range(0,q+2):
        for sub in combinations(range(len(columns)),k):
            gram=Matrix([[sum(columns[i][h]*columns[j][h] for h in range(n)) for j in sub] for i in sub])
            d=int(gram.det(method='bareiss')) if k else 1
            if d:
                out[k][d]+=1
            tests+=1
    return out,tests


def weighted_profile(q,t):
    pred=predicted_counts(q)
    return [sum(count*sqrt(det) for det,count in tab.items()) *t**k for k,tab in enumerate(pred)]


def asymptotic_check(q,t):
    p=2*t/(1+2*t)
    w=weighted_profile(q,t)
    total=sum(w)
    asym=(1+2*t)**q *q**1.5 *t*t*sqrt(p)/(1+2*t)
    target=[0.]*(q+2)
    for k in range(2,q+2):
        target[k]=comb(q-1,k-2)*p**(k-2)*(1-p)**(q-k+1)
    tv=0.5*sum(abs(x/total-y) for x,y in zip(w,target))
    return total/asym,tv


def main():
    assertions=0
    for q in range(1,7):
        actual,tests=brute_counts(q)
        expect=predicted_counts(q)
        assert actual==expect,(q,actual,expect)
        assertions+=tests
        if q>=2:
            assert actual[q+1] == Counter({q+2:q*2**(q-1)})
            assertions+=1
        print(f'q={q}: {tests} exact Gram determinants; coefficient-shell multiplicities agree')
    for t in (0.3,1.0,1.8):
        values=[asymptotic_check(q,t) for q in (20,50,100,250)]
        print(f't={t}: (W/leading, TV distance to 2+Bin(q-1,p)) = {values}')
        assert values[-1][1] < values[0][1]
        assertions+=1
    try:
        import numpy as np
        from scipy.spatial import ConvexHull
        from scipy.linalg import null_space
        for q in (2,3):
            n=q+2;cols=[]
            for j in range(q):
                for i in range(2):
                    v=np.zeros(n);v[i]=1;v[j+2]=-1;cols.append(v)
            points=[sum((bit*col for bit,col in zip(bits,cols)),np.zeros(n)) for bits in product((0,1),repeat=len(cols))]
            basis=null_space(np.ones((1,n)))
            pts=np.array(points)@basis
            vol=ConvexHull(pts).volume
            expected=q*2**(q-1)*sqrt(q+2)
            assert isclose(vol,expected,rel_tol=1e-9),(q,vol,expected)
            assertions+=1
            print(f'q={q}: independent ambient Euclidean hull volume {vol:.12g} equals {expected:.12g}')
    except ImportError:
        print('SciPy absent; optional convex-hull checks skipped')
    print(f'PASS: {assertions} exact determinant/combinatorial/analytic checks, plus optional hull checks')

if __name__=='__main__':main()
