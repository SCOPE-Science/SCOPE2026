"""Exact algebraic checks for a two-node memory-based compressed-gossip theorem.

Requires Python 3.10+ and SymPy >= 1.11.  Run: python verify.py
"""
from itertools import product
import sympy as S

Q, Z = S.symbols('q z', real=True)
D, H, C = S.symbols('d h c', real=True)
HALF = S.Rational(1, 2)


def step_matrix(b1, b2):
    """Map (node difference, cache difference, cache sum) to next state."""
    ss = S.Rational(b1+b2, 2)
    tt = S.Rational(b2-b1, 2)
    return S.Matrix([[1-ss, ss-1, -tt],
                     [ss, 1-ss, tt],
                     [-tt, tt, 1-ss]])


def cases():
    return [(step_matrix(0, 0), Q),
            (step_matrix(0, 1), HALF-Q),
            (step_matrix(1, 0), HALF-Q),
            (step_matrix(1, 1), Q)]


def check_original_update():
    x1, x2 = D/2, -D/2
    h1, h2 = (C+H)/2, (C-H)/2
    for b1, b2 in product((0, 1), repeat=2):
        h1n = h1+b1*(x1-h1)
        h2n = h2+b2*(x2-h2)
        x1n = x1+(h2n-h1n)/2
        x2n = x2+(h1n-h2n)/2
        direct = S.Matrix([x1n-x2n, h1n-h2n, h1n+h2n])
        pred = step_matrix(b1, b2)*S.Matrix([D, H, C])
        assert all(S.expand(t)==0 for t in direct-pred), (b1,b2)


def exact_moment_matrix():
    m = S.Matrix([D*D, D*H, H*H, C*C])
    state = S.Matrix([D, H, C])
    rows = S.zeros(4,4)
    monoms = [D*D,D*H,H*H,C*C]
    for i, form in enumerate(m):
        f = sum((w*form.subs(dict(zip(state,A*state)), simultaneous=True)
                 for A,w in cases()),S.Integer(0))
        f = S.Poly(S.expand(f),D,H,C)
        assert f.coeff_monomial(D*C)==0 and f.coeff_monomial(H*C)==0
        for j,mon in enumerate(monoms):
            rows[i,j]=f.coeff_monomial(mon)
    return rows


def check():
    check_original_update()
    T = exact_moment_matrix()
    target = S.Matrix([
       [Q/2+S.Rational(1,4), -Q-HALF, Q/2+S.Rational(1,4), S.Rational(1,4)-Q/2],
       [S.Rational(1,4)-Q/2, Q, -Q/2-S.Rational(1,4), Q/2-S.Rational(1,4)],
       [Q/2+S.Rational(1,4), HALF-Q, Q/2+S.Rational(1,4), S.Rational(1,4)-Q/2],
       [S.Rational(1,4)-Q/2, Q-HALF, S.Rational(1,4)-Q/2, Q/2+S.Rational(1,4)]])
    assert T==target

    den = (2*Q*Z**4-(6*Q+1)*Z**3+(18*Q+1)*Z**2-(20*Q+6)*Z+8)
    numerator = -2*(Z-2)*(Q*Z**2-4*Q*Z+2)
    M=S.eye(4)-Z*T
    assert S.expand(8*M.det()-den)==0
    assert S.expand(8*M.minor_submatrix(0,0).det()-numerator)==0
    assert S.expand(den.subs(Z,1)-2*(1-3*Q))==0
    assert S.limit((1-Z)*numerator.subs(Q,S.Rational(1,3))/den.subs(Q,S.Rational(1,3)),Z,1)==S.Rational(2,5)
    assert S.factor(den.subs(Q,S.Rational(1,3))) == (Z-1)*(2*Z**3-7*Z**2+14*Z-24)/3

    P = S.Matrix([[2*(2-3*Q)/(1-3*Q),-1/(1-3*Q),0],
                  [-1/(1-3*Q),(5-6*Q)/(1-3*Q),0],
                  [0,0,(5-12*Q)/(1-3*Q)]])
    EPTP=sum((w*A.T*P*A for A,w in cases()),S.zeros(3))
    assert all(S.cancel(v)==0 for v in (P-EPTP-S.eye(3)))
    assert all(S.cancel(a-b)==0 for a,b in zip([P[:i,:i].det() for i in range(1,4)], [
        2*(2-3*Q)/(1-3*Q),
        (36*Q**2-54*Q+19)/(1-3*Q)**2,
        (5-12*Q)*(36*Q**2-54*Q+19)/(1-3*Q)**3]))

    n_cases=0
    for q in (S.Integer(0), S.Rational(1,4), S.Rational(1,3), HALF):
        weights = [q,HALF-q,HALF-q,q]
        AA = [A for A,_ in cases()]
        states=[(S.Matrix([1,0,0]),S.Integer(1))]
        m0=S.Matrix([1,0,0,0])
        Ti=T.subs(Q,q)
        for k in range(7):
            risk=sum((w*v[0]**2 for v,w in states), S.Integer(0))
            assert risk==(Ti**k*m0)[0],(q,k)
            n_cases+=len(states)
            if k<6:
                states=[(A*v,wp*w) for v,wp in states
                        for A,w in zip(AA,weights) if wp*w!=0]
    print('PASS: original updates, symbolic transfer, rational generating law,')
    print('      strict-Lyapunov identity, and finite-path enumeration')
    print('Finite exact path cases:',n_cases)

if __name__=='__main__':
    check()
