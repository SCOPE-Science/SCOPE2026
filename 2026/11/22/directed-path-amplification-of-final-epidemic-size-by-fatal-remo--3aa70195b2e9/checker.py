"""Reproducibility probes for the multigroup active-population SIRD sensitivity theorem.

The accompanying mathematical proof establishes the general result; these finite
calculations test an example, a directed-network boundary, and derivative identities.
"""
import math
import random


def solve(s, k, q, tolerance=1e-14):
    n = len(s)
    h = [0.0] * n
    for iteration in range(100000):
        z = [1.0-s[i]*math.exp(-h[i]) for i in range(n)]
        g = [(-math.log1p(-q[i]*z[i])/q[i]) if q[i] else z[i]
             for i in range(n)]
        update = [sum(k[i][j]*g[j] for j in range(n)) for i in range(n)]
        if max(abs(update[i]-h[i]) for i in range(n)) <= tolerance:
            h = update
            break
        h = update
    else:
        raise AssertionError('Fixed-point iteration did not converge')
    z = [1.0-s[i]*math.exp(-h[i]) for i in range(n)]
    err = max(abs(h[i]-sum(k[i][j]*((-math.log1p(-q[j]*z[j])/q[j])
              if q[j] else z[j]) for j in range(n))) for i in range(n))
    assert err < 1e-10, err
    return z,h


def derivative_formula(s,k,q):
    z,h = solve(s,k,q)
    n = len(s)
    jac = [[k[i][j]*(1-z[j])/(1-q[j]*z[j]) for j in range(n)]
           for i in range(n)]
    # Solve (I-J) v=K[:,j] using a geometric Neumann series.
    derivative = [[0.0]*n for _ in range(n)]
    for source in range(n):
        zsrc = z[source]
        qsrc = q[source]
        if qsrc:
            phi = zsrc/(qsrc*(1-qsrc*zsrc))+math.log1p(-qsrc*zsrc)/(qsrc*qsrc)
        else:
            phi = zsrc*zsrc/2
        current = [k[i][source]*phi for i in range(n)]
        total = [0.0]*n
        for _ in range(5000):
            total = [total[i]+current[i] for i in range(n)]
            current = [sum(jac[i][j]*current[j] for j in range(n)) for i in range(n)]
            if max(abs(t) for t in current) < 1e-14:
                break
        else:
            raise AssertionError('Neumann series did not converge')
        for i in range(n):
            derivative[i][source]=(1-z[i])*total[i]
    return derivative


def run():
    # Exact rational input rates, evaluated numerically; no claim of exact roots.
    s = [49/50,97/100]
    k = [[5/4,4/5],[13/20,27/20]]
    q0 = [1/10,1/10]
    q1 = [3/5,1/10]
    z0,_=solve(s,k,q0)
    z1,_=solve(s,k,q1)
    assert abs(z0[0]-0.83510923)<2e-7
    assert abs(z0[1]-0.82887977)<2e-7
    assert abs(z1[0]-0.90944400)<2e-7
    assert abs(z1[1]-0.88122095)<2e-7
    assert all(z1[i]>z0[i] for i in range(2))
    eps=1e-5
    q=[3/10,2/5]
    formula=derivative_formula(s,k,q)
    for source in range(2):
        before=q[:];after=q[:]
        before[source]-=eps;after[source]+=eps
        za,_=solve(s,k,before);zb,_=solve(s,k,after)
        for target in range(2):
            fd=(zb[target]-za[target])/(2*eps)
            assert abs(fd-formula[target][source])<2e-7, (source,target,fd,formula[target][source])
            assert formula[target][source]>0
    # Sparse case: 0 -> 1 -> 2; no feedback to group 0.
    sparse=[[1.1,0,0],[.4,.8,0],[0,.7,.6]]
    q=[.15,.20,.25]
    sens=derivative_formula([.96,.94,.95],sparse,q)
    assert sens[0][2]==0 and sens[1][2]==0
    assert sens[2][0]>0 and sens[1][0]>0
    # Source 2 can influence only itself in this directed lower-triangular graph.
    assert sens[0][1]==0
    rng=random.Random(20261117)
    for n in range(2,7):
        for trial in range(40):
            s=[rng.uniform(.76,.98) for _ in range(n)]
            q=[rng.uniform(.02,.78) for _ in range(n)]
            k=[[rng.uniform(.12,.38) for _ in range(n)] for _ in range(n)]
            derivative=derivative_formula(s,k,q)
            assert all(derivative[i][j]>0 for i in range(n) for j in range(n))
    print('PASS: witness, 4 finite-difference derivatives, directed support, 200 random positive systems')


if __name__ == '__main__':
    run()
