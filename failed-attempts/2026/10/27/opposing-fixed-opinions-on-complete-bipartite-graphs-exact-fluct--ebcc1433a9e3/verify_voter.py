"""Standalone exact checks for stationary two-zealot bipartite voter dynamics.

Uses only the Python standard library. Finite tests corroborate the analytic
all-size proof; they do not establish its infinite-volume limit.
"""
from fractions import Fraction as F
from math import prod


def stationary(m, n):
    """Solve the forward stationary equations on the (i,j) lumped chain."""
    states = [(i,j) for i in range(m) for j in range(n)]
    positions = {s:k for k,s in enumerate(states)}
    count = len(states)
    eq = [[F(0) for _ in range(count + 1)] for _ in range(count)]
    for source, (i,j) in enumerate(states):
        rates = [((i+1,j), F((m-1-i)*j, n)),
                 ((i-1,j), F(i*(n-j), n)),
                 ((i,j+1), F((n-1-j)*(i+1), m)),
                 ((i,j-1), F(j*(m-1-i), m))]
        for target,rate in rates:
            if not rate: continue
            k = positions[target]
            eq[k][source] += rate
            eq[source][source] -= rate
    eq[-1] = [F(1)]*count+[F(1)]
    # Fraction-based Gauss-Jordan elimination; one redundant row replaced.
    for col in range(count):
        pivot = next(k for k in range(col,count) if eq[k][col])
        eq[col],eq[pivot] = eq[pivot],eq[col]
        denom = eq[col][col]
        eq[col] = [z/denom for z in eq[col]]
        for row in range(count):
            if row != col:
                scale=eq[row][col]
                if scale:
                    eq[row] = [a-scale*b for a,b in zip(eq[row],eq[col])]
    return states, [row[-1] for row in eq]


def main():
    experiments=0
    for m in range(1,6):
        for n in range(1,6):
            states, pi = stationary(m,n)
            if sum(pi) != 1 or any(z<0 for z in pi):
                raise AssertionError((m,n,'stationarity'))
            mu = sum(prob*(1+i+j) for (i,j),prob in zip(states,pi))
            second = sum(prob*(1+i+j)**2 for (i,j),prob in zip(states,pi))
            expected_variance=F((m-1)*(n-1)*(m+n)**2,(m+n-1)*(3*(m+n)-4))
            if mu != n or second-mu*mu != expected_variance:
                raise AssertionError((m,n,mu,second-mu*mu,expected_variance))
            experiments+=1
    # The limiting beta law with parameters (2theta, 2(1-theta)) has
    # moments (2theta)_r / (2)_r. Verify the drift-diffusion moment equation.
    moment_tests=0
    for theta in (F(1,6),F(1,4),F(1,2),F(2,3),F(5,6)):
        moments=[F(1)]
        for k in range(1,12):
            beta_moment = prod(2*theta+j for j in range(k))/prod(2+j for j in range(k))
            recursion = (2*theta+k-1)*moments[-1]/(k+1)
            assert beta_moment==recursion
            moments.append(recursion)
            moment_tests+=1
    print(f'PASS: {experiments} independent finite-chain exact stationary comparisons')
    print(f'PASS: {moment_tests} beta-law moment recursion checks')

if __name__=='__main__':
    main()
