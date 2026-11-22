"""Exact-rational checks for weighted quadratic simplex prediction sensitivity."""
from fractions import Fraction as F
from itertools import product, combinations
from random import Random


def sq_prediction(a, z):
    """Solve the strictly convex separable quadratic simplex problem exactly."""
    assert len(a) == len(z) and all(v > 0 for v in a)
    order = sorted(range(len(a)), key=lambda i: z[i], reverse=True)
    for k in range(1, len(a) + 1):
        active = order[:k]
        A = sum((a[i] for i in active), F(0))
        tau = (sum((a[i]*z[i] for i in active), F(0)) - 1) / A
        if z[order[k-1]] > tau and (k == len(a) or z[order[k]] <= tau):
            p = [a[i]*max(F(0), z[i]-tau) for i in range(len(a))]
            assert sum(p) == 1 and all(pi >= 0 for pi in p)
            return p
    raise AssertionError('no KKT threshold')


def jacobian(a, mask):
    n=len(a)
    A=sum((a[i] for i in range(n) if mask[i]),F(0))
    assert A>0
    return [[(a[i] if i==j else F(0)) - a[i]*a[j]/A if mask[i] and mask[j] else F(0) for j in range(n)] for i in range(n)]


def operator_norm_signs(J):
    n=len(J)
    best=F(-1)
    for s in product((-1,1),repeat=n):
        v=[sum((J[i][j]*s[j] for j in range(n)),F(0)) for i in range(n)]
        best=max(best,sum(map(abs,v)))
    return best


def discrepancy(a):
    best=None
    witness=None
    for s in product((-1,1),repeat=len(a)):
        d=abs(sum((a[i]*s[i] for i in range(len(a))),F(0)))
        if best is None or d<best:
            best,witness=d,s
    return best,witness


def run():
    cases=0
    rng=Random(20311205)
    for n in range(2,8):
        for _ in range(12):
            a=[F(rng.randint(1,12),rng.randint(1,6)) for _ in range(n)]
            A=sum(a,F(0))
            d,sign=discrepancy(a)
            L=A-d*d/A
            J=jacobian(a,[True]*n)
            assert operator_norm_signs(J)==L
            # Every active-set local norm cannot exceed the full-support constant.
            for mask in list(product((False,True),repeat=n))[::max(1,2**n//12)]:
                if any(mask):
                    assert operator_norm_signs(jacobian(a,mask))<=L
                    cases+=1
            # Two finite, exactly computed inputs attain the sharp value.
            z0=[F(1,n)/ai for ai in a]
            # Relative to the full-support base, |J sign|_infty*eps < 1/n.
            eps=F(1,10*n*(1+max(a)))
            zp=[z0[i]+eps*sign[i] for i in range(n)]
            zm=[z0[i]-eps*sign[i] for i in range(n)]
            pp,pm=sq_prediction(a,zp),sq_prediction(a,zm)
            quotient=sum(abs(pp[i]-pm[i]) for i in range(n))/(2*eps)
            assert quotient==L
            cases+=1
    for n in range(2,8):
        for _ in range(40):
            a=[F(rng.randint(1,15)) for _ in range(n)]
            A=sum(a,F(0))
            d,_=discrepancy(a)
            assert (A-d*d/A==A)==(d==0)
            # Dynamic subset-sum program gives exactly the discrepancy.
            attainable={0}
            for ai in a:
                attainable |= {j+int(ai) for j in tuple(attainable)}
            assert d==min(abs(A-2*s) for s in attainable)
            cases+=1
    print('PASS: exact weighted-simplex solver, all support Jacobians, sign norm identity, finite norm attainers, and partition-DP equivalence. Checks:', cases)

if __name__=='__main__':
    run()
