"""Exact rational checks of weighted-cycle zonotope circumradius formulas.

Finite checks supplement the analytic proof and do not establish the theorem for all dimensions.
"""
from fractions import Fraction as F
from itertools import product
from random import Random

def squared_norm_times_four(w, signs):
    n=len(w)
    d=[w[i]*signs[i]-w[(i-1)%n]*signs[(i-1)%n] for i in range(n)]
    return sum(x*x for x in d)

def predicted_times_four(w):
    n=len(w)
    baseline=2*sum(x*x for x in w)+2*sum(w[i]*w[(i+1)%n] for i in range(n))
    return baseline if n%2==0 else baseline-4*min(w[i]*w[(i+1)%n] for i in range(n))

def check(w):
    n=len(w)
    vals=[]
    for s in product((-1,1), repeat=n):
        vals.append((squared_norm_times_four(w,s),s))
    best=max(v for v,s in vals)
    assert best==predicted_times_four(w), (w,best,predicted_times_four(w))
    winners={s for v,s in vals if v==best}
    if n%2==0:
        expected={tuple((-1)**i for i in range(n)),tuple(-(-1)**i for i in range(n))}
    else:
        defect={i for i in range(n) if w[i]*w[(i+1)%n]==min(w[j]*w[(j+1)%n] for j in range(n))}
        expected=set()
        for i in defect:
            signs=[0]*n
            signs[i]=1
            for k in range(1,n):
                signs[(i+k)%n] = signs[(i+k-1)%n] if k==1 else -signs[(i+k-1)%n]
            # defect at edge i is sign[i]==sign[i+1], all other adjacent signs oppose.
            expected.add(tuple(signs)); expected.add(tuple(-x for x in signs))
    assert winners==expected, (w,winners,expected)
    return len(winners)

if __name__=='__main__':
    total=0
    for n in range(4,8):
        for w in product((1,2,3),repeat=n):
            check(w);total+=1
    rng=Random(9001)
    for n in range(8,12):
        for _ in range(30):
            w=tuple(rng.randint(1,20) for _ in range(n))
            check(w);total+=1
    for n in range(4,12):
        s=F(2*n)
        u=(F(2),)*n
        assert predicted_times_four(u)==(4*s*s/n if n%2==0 else 4*s*s*(n-1)/(n*n))
        if n%2==0:
            alt=tuple(F(1) if i%2==0 else F(3) for i in range(n))
            assert sum(alt)==s
            assert predicted_times_four(alt)==predicted_times_four(u)
        else:
            alt=(F(1),F(3))+(F(2),)*(n-2)
            assert sum(alt)==s
            assert predicted_times_four(alt)>predicted_times_four(u)
    print('WEIGHTED_CYCLE_OUTER_EXACT_PASS',total)
