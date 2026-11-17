"""Reproduce exact moment identities for the odd Cerny automaton under fair letters.

Requires Python 3.10+ and sympy. Run: python verify_moments.py
The direct solver enumerates unordered state pairs, independent of the
reduced-coordinate proof, and computes first and second absorption moments.
"""
import sympy as s


def verify_symbolic_identity():
    m, j = s.symbols('m j', integer=True, positive=True)
    h = lambda k: (16*m*m + 8*m)*k - (8*m + 2)*k*k
    e = lambda k: 1 + (h(k-1) + h(k))/2
    L = lambda k: 2*m - k
    A = lambda k: s.expand(L(k)*(4*h(k)-2) - 4*L(k)*(L(k)-1))
    B = lambda k: s.expand((k-1)*(4*e(k)-2) + 4*k*(k-1))
    ru = lambda k: 4*(h(k) - 2*L(k)) - 2
    r0 = lambda k: 4*e(k) - 2
    F = s.factor(4*A(j) + 2*(B(j) + B(j+1) + ru(j)) + r0(j) + r0(j+1))
    Fstar = s.factor(4*A(m) + 2*B(m) + 2*ru(m) + r0(m))
    H = s.factor(m*Fstar + s.summation(j*F, (j, 1, m-1)))
    expected_H = 2*m*(160*m**5 + 240*m**4 + 98*m**3 + 16*m**2 - 3*m - 4)/3
    expected_V = 2*m*(2*m+1)*(32*m**4+32*m**3+6*m**2+5*m-4)/3
    assert s.simplify(H-expected_H)==0
    assert s.simplify(H-h(m)**2-expected_V)==0
    assert s.simplify(h(m)-(8*m**3+6*m**2))==0
    print('SYMBOLIC_SECOND_MOMENT_AND_VARIANCE_OK')


def direct_unordered_pair_moments(n):
    states = [(i, j) for i in range(n) for j in range(i+1,n)]
    lookup = {pair: index for index, pair in enumerate(states)}
    K = len(states)
    M = s.eye(K)*2
    for t, (i, j) in enumerate(states):
        transitions = [((i+1)%n,(j+1)%n), (1 if i == 0 else i, 1 if j == 0 else j)]
        for (u,v) in transitions:
            if u != v:
                M[t, lookup[tuple(sorted((u,v)))]] -= 1
    ones = s.ones(K,1)
    mean = M.inv(method='DM') * (2*ones) if False else M.LUsolve(2*ones)
    second = M.LUsolve(4*mean-2*ones)
    index = lookup[(1,(n+1)//2)]
    return s.factor(mean[index]), s.factor(second[index]-mean[index]**2)


def verify_independent_pair_graph():
    for n in (3,5,7,9,11):
        mean, variance = direct_unordered_pair_moments(n)
        expected_mean = (n-1)*(2*n*n-n-1)//2
        expected_variance = n*(n-1)*(4*n**4-8*n**3+3*n*n+7*n-14)//6
        assert mean == expected_mean, (n,mean,expected_mean)
        assert variance == expected_variance, (n,variance,expected_variance)
        print(f'INDEPENDENT_PAIR_MARKOV_OK n={n} E={mean} Var={variance}')


if __name__ == '__main__':
    verify_symbolic_identity()
    verify_independent_pair_graph()
    print('ALL_CHECKS_PASSED')
