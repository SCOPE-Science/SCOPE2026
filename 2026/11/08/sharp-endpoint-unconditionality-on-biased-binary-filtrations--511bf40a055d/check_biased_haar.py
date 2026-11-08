#!/usr/bin/env python3
"""Exact rational diagnostics for endpoint norms of finite binary martingale transforms."""
from fractions import Fraction as F
from itertools import product


def predict(probs):
    a, b = F(0), F(1)
    for p in reversed(probs):
        a, b = a + (1-p)*(1+b), (1-p)-p*b
    return a+b


def closed(d, p):
    return F(1) + 2*(1-p)*d/(1+p) - 4*p*p*(1-(-p)**d)/(1+p)**2


def row_value(probs, x, signs):
    d = len(probs)
    leafs = list(product((0,1), repeat=d))
    masses = {}
    for y in leafs:
        mass=F(1)
        for k, yi in enumerate(y):
            mass *= probs[k] if yi==0 else (1-probs[k])
        masses[y]=mass
    ancestors=[F(1)]
    for k, xi in enumerate(x):
        ancestors.append(ancestors[-1]*(probs[k] if xi==0 else (1-probs[k])))
    total=F(0)
    for y in leafs:
        kernel=F(signs[0])
        for j in range(1,d+1):
            s = 1 if x[:j] == y[:j] else 0
            t = 1 if x[:j-1] == y[:j-1] else 0
            kernel += signs[j]*(F(s)/ancestors[j] - F(t)/ancestors[j-1])
        total += masses[y]*abs(kernel)
    return total


def run():
    configs = [(), (F(1,2),), (F(1,3),), (F(1,5),),
               (F(1,3),F(1,2)), (F(1,2),F(1,4)),
               (F(1,5),F(2,5),F(1,3)), (F(1,4),)*3,
               (F(2,5),)*4, (F(1,3),)*4,
               (F(1,5),F(1,3),F(1,4),F(2,5)),
               (F(2,5),F(1,3),F(1,5),F(1,4)),
               (F(1,3),)*5, (F(1,4),)*5,
               (F(1,2),)*5,
               (F(1,4),F(1,3),F(1,5),F(2,5),F(1,3))]
    checked=0
    for probs in configs:
        d=len(probs)
        expected=predict(probs)
        best = F(-1)
        maximizing = []
        for x in product((0,1), repeat=d):
            for signs in product((-1,1),repeat=d+1):
                v=row_value(probs,x,signs)
                checked+=1
                if v>best:
                    best, maximizing = v, [(x, signs)]
                elif v == best:
                    maximizing.append((x,signs))
        assert best==expected,(probs,best,expected)
        if d and all(p<F(1,2) for p in probs):
            assert all(x==(0,)*d for x, _ in maximizing)
            assert all(tuple(signs[i] for i in range(d+1))
                       in (tuple((-1)**i for i in range(d+1)),
                           tuple(-(-1)**i for i in range(d+1)))
                       for _, signs in maximizing), (probs,maximizing)
        if len(set(probs))==1:
            assert best==closed(d,probs[0])
    for p in (F(1,2), F(1,3), F(2,5), F(1,8)):
        for d in range(30):
            assert predict((p,)*d)==closed(d,p)
    print('EXACT_INDEPENDENT_MATRIX_ROW_CASES_PASSED',len(configs), 'configurations,',checked,'rows and sign settings')
    print('HOMOGENEOUS_CLOSED_FORM_RATIONAL_IDENTITIES_PASSED',4*30)
    print('MINORITY_PATH_AND_ALTERNATING_SIGN_RIGIDITY_PASSED')
    print('ALL_NONHOMOGENEOUS_HAAR_ENDPOINT_CHECKS_PASSED')

if __name__=='__main__':
    run()
