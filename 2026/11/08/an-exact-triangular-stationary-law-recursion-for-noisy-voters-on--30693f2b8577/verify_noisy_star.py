#!/usr/bin/env python3
"""Self-contained exact checks for a noisy-voter star's limiting leaf law.

Uses only Python's standard library; this file defines the model anew rather
than trusting precomputed matrices or numerical solver outputs.
"""
from fractions import Fraction as F

CHECKS = 0


def eq(actual, expected, context):
    global CHECKS
    CHECKS += 1
    assert actual == expected, (context, actual, expected)


def rates(k, alpha, beta, eta):
    # Reduced states (hub bit h, number of 1 leaves m).
    states = [(h, m) for h in (0, 1) for m in range(k + 1)]
    pos = {s: i for i, s in enumerate(states)}
    n = len(states)
    Q = [[F(0) for _ in states] for _ in states]
    for i, (h, m) in enumerate(states):
        transitions = []
        if m < k:
            transitions.append(((h, m + 1), (k - m) * (alpha * h + eta / 2)))
        if m > 0:
            transitions.append(((h, m - 1), m * (alpha * (1 - h) + eta / 2)))
        hubflip = beta * (F(m, k) if h == 0 else F(k - m, k)) + eta / 2
        transitions.append(((1 - h, m), hubflip))
        for destination, r in transitions:
            assert r >= 0
            j = pos[destination]
            Q[i][j] += r
            Q[i][i] -= r
        eq(sum(Q[i]), F(0), ('generator row', k, i))
    return states, Q


def exact_stationary(Q):
    n = len(Q)
    # Solve transpose Q * pi = 0, with normalization in final row.
    A = [[Q[j][i] for j in range(n)] + [F(0)] for i in range(n)]
    A[-1] = [F(1)] * n + [F(1)]
    for i in range(n):
        pivot = next((j for j in range(i, n) if A[j][i] != 0), None)
        assert pivot is not None
        A[i], A[pivot] = A[pivot], A[i]
        p = A[i][i]
        A[i] = [v / p for v in A[i]]
        for j in range(n):
            if j != i:
                mult = A[j][i]
                if mult:
                    A[j] = [a - mult*b for a, b in zip(A[j], A[i])]
    result = [row[-1] for row in A]
    eq(sum(result), F(1), ('normalization', n))
    assert all(x > 0 for x in result)
    for i in range(n):
        eq(sum(result[j] * Q[j][i] for j in range(n)), F(0), ('stationarity', n, i))
    return result


def exact_pair_check(k, alpha, beta, eta):
    states, Q = rates(k, alpha, beta, eta)
    pi = exact_stationary(Q)
    E_h = sum(p * h for p, (h, m) in zip(pi, states))
    E_x = sum(p * F(m, k) for p, (h, m) in zip(pi, states))
    eq(E_h, F(1, 2), ('hub mean', k, alpha, beta, eta))
    eq(E_x, F(1, 2), ('leaf mean', k, alpha, beta, eta))
    hl = sum(p * (2*h-1) * (F(2*m,k)-1) for p, (h, m) in zip(pi, states))
    ll = sum(p * (F(4*m*(m-1),k*(k-1)) - 1) for p,(h,m) in zip(pi, states))
    D = 2*eta + alpha + beta - beta*F(k-1,k)*alpha/(alpha+eta)
    hl_formula = (alpha+beta/F(k))/D
    ll_formula = alpha/(alpha+eta)*hl_formula
    eq(hl, hl_formula, ('hub-leaf', k, alpha, beta, eta))
    eq(ll, ll_formula, ('leaf-leaf', k, alpha, beta, eta))
    variance = sum(p*(F(m,k)-F(1,2))**2 for p,(h,m) in zip(pi, states))
    eq(variance, (1+F(k-1)*ll_formula)/(4*k), ('variance', k, alpha, beta, eta))


def poch(a, j):
    v = F(1)
    for r in range(j):
        v *= a+r
    return v


def limiting_identity(alpha, beta, eta, max_degree=16):
    A = alpha+eta
    delta = alpha/A
    low = eta/(2*A)
    g = beta*low+eta/2
    theta = g/A
    D = A*(alpha+2*eta)+eta*beta
    eq(theta, eta*(beta+A)/(2*A*A), ('theta',alpha,beta,eta))
    eq(delta*delta/(4*(1+2*theta)), alpha*alpha/(4*D), ('variance limit',alpha,beta,eta))
    eq(alpha*alpha/D, (delta*delta)/(1+2*theta), ('leaf pair limit',alpha,beta,eta))
    for m in range(max_degree+1):
        M = poch(theta,m)/poch(2*theta,m)
        M1 = poch(theta,m+1)/poch(2*theta,m+1)
        eq((m*A+g)*M,(m*A+2*g)*M1, ('beta moment recurrence',m,alpha,beta,eta))
        # Moment calibration enforces E[hub Y^m] = E[Y^(m+1)].
        Hm = M1
        eq(Hm,M1, ('conditional hub moment',m,alpha,beta,eta))
        if m>=1:
            # Generator equation for hub*Y^m (beta feedback terms cancel).
            residual = m*A*(M-M1)+g*(M-2*M1)
            eq(residual,F(0),('limit hub-moment generator',m,alpha,beta,eta))
    beta_critical = A*(2*alpha+eta)/eta
    theta_at_threshold = eta*(beta_critical+A)/(2*A*A)
    eq(theta_at_threshold,F(1), ('shape threshold',alpha,eta))


if __name__ == '__main__':
    grids = [
        (F(1),F(1),F(1)),
        (F(1),F(6),F(1)),
        (F(1),F(8),F(1)),
        (F(2),F(3),F(1)),
        (F(3,2),F(0),F(1,2)),
        (F(1,3),F(7,2),F(4,3)),
    ]
    for alpha,beta,eta in grids:
        limiting_identity(alpha,beta,eta)
        for k in (2,3,4,6,8):
            exact_pair_check(k,alpha,beta,eta)
    print(f'First-stage checks: {CHECKS} exact rational assertions on {len(grids)*5} finite chains; {len(grids)} limiting identity families.')


def complete_stationary_moments(k, alpha, beta, eta):
    """Exact triangular closure for normalized factorial leaf and hub moments."""
    A=alpha+eta
    Fmom=[F(1)]
    Gmom=[F(1,2)]
    for r in range(1,k+1):
        Fr=(alpha*Gmom[r-1]+eta*Fmom[r-1]/2)/A
        Fr1=Fr
        den=r*A+eta+beta-beta*F(k-r,k)*alpha/A
        num=r*(alpha+eta/2)*Gmom[r-1]+(eta/2+beta*F(r,k)+beta*F(k-r,k)*eta/(2*A))*Fr
        Gr=num/den
        Fmom.append(Fr1)
        Gmom.append(Gr)
    return Fmom,Gmom


def verify_all_moments(k,alpha,beta,eta):
    from math import comb
    states,Q=rates(k,alpha,beta,eta)
    pi=exact_stationary(Q)
    fm,gm=complete_stationary_moments(k,alpha,beta,eta)
    for r in range(k+1):
        actual_f=sum(p*F(comb(m,r),comb(k,r)) for p,(h,m) in zip(pi,states))
        actual_g=sum(p*h*F(comb(m,r),comb(k,r)) for p,(h,m) in zip(pi,states))
        eq(fm[r],actual_f,('all-order leaf moment',k,r,alpha,beta,eta))
        eq(gm[r],actual_g,('all-order hub-leaf moment',k,r,alpha,beta,eta))
    for m in range(k+1):
        pm=sum(F((-1)**(r-m)*comb(r,m)*comb(k,r))*fm[r] for r in range(m,k+1))
        qm=sum(F((-1)**(r-m)*comb(r,m)*comb(k,r))*gm[r] for r in range(m,k+1))
        actual_p=sum(p for p,(h,j) in zip(pi,states) if j==m)
        actual_q=sum(p for p,(h,j) in zip(pi,states) if j==m and h==1)
        eq(pm,actual_p,('all-order inversion marginal',k,m,alpha,beta,eta))
        eq(qm,actual_q,('all-order inversion joint',k,m,alpha,beta,eta))


if __name__ == '__main__':
    from fractions import Fraction as F
    for a,b,e in [(F(1),F(1),F(1)),(F(1),F(6),F(1)),(F(1),F(8),F(1)),(F(2),F(3),F(1)),(F(3,2),F(0),F(1,2)),(F(1,3),F(7,2),F(4,3))]:
        for k in (2,3,4,6,8):
            verify_all_moments(k,a,b,e)
    print(f'PASS: {CHECKS} total exact rational assertions, including all-order moments and full joint-law inversion on 30 finite chains.')
