from __future__ import annotations
import random


def decision_unweighted(alpha, gamma, losses, scores, stest):
    n = len(losses)
    M = list(scores) + [stest]
    Astar = sum(L for L,s in zip(losses,scores) if s <= stest)
    Q = (1.0 + Astar)/(n+1)
    if gamma <= alpha:
        return int(Q <= gamma + 1e-12)
    if Q > gamma + 1e-12:
        return 0
    # Proposition 4.4 extra condition: no candidate value in (alpha,gamma].
    # Because candidate ell varies continuously over [0,1], it suffices here
    # to test interval intersection for each finite threshold.
    for t in M:
        A = sum(L for L,s in zip(losses,scores) if s <= t)
        lo = A/(n+1)
        hi = (A+1.0)/(n+1)
        # Is there x in [lo,hi] intersecting (alpha,gamma]?
        if hi > alpha + 1e-12 and lo <= gamma + 1e-12:
            return 0
    return 1


def decision_weighted(alpha, gamma, losses, scores, stest, weights, wtest):
    den = sum(weights) + wtest
    Astar = sum(w*L for w,L,s in zip(weights,losses,scores) if s <= stest)
    Q = (wtest + Astar)/den
    if gamma <= alpha:
        return int(Q <= gamma + 1e-12)
    if Q > gamma + 1e-12:
        return 0
    M = list(scores) + [stest]
    for t in M:
        A = sum(w*L for w,L,s in zip(weights,losses,scores) if s <= t)
        lo = A/den
        hi = (A+wtest)/den
        if hi > alpha + 1e-12 and lo <= gamma + 1e-12:
            return 0
    return 1


def random_checks():
    rng = random.Random(20261001)
    for _ in range(5000):
        n = rng.randint(1,8)
        losses = [rng.random() for _ in range(n)]
        scores = [rng.random() for _ in range(n)]
        stest = rng.random()
        alpha = rng.uniform(0.03,0.95)
        gamma = rng.uniform(0.01,0.99)
        da = decision_unweighted(alpha, alpha, losses, scores, stest)
        dg = decision_unweighted(alpha, gamma, losses, scores, stest)
        assert dg <= da
        weights = [10**rng.uniform(-1,1) for _ in range(n)]
        wtest = 10**rng.uniform(-1,1)
        daw = decision_weighted(alpha, alpha, losses, scores, stest, weights, wtest)
        dgw = decision_weighted(alpha, gamma, losses, scores, stest, weights, wtest)
        assert dgw <= daw


def strict_witness_low():
    alpha, gamma = 0.30, 0.20
    n = 4
    q = 0.25
    total = (n+1)*q - 1.0
    losses = [total,0,0,0]
    scores = [0.1,0.2,0.3,0.4]
    stest = 0.9
    assert decision_unweighted(alpha, alpha, losses, scores, stest) == 1
    assert decision_unweighted(alpha, gamma, losses, scores, stest) == 0


def strict_witness_high():
    alpha, gamma = 0.30, 0.45
    n = 4
    # Test score below all positive-risk calibration scores: Q=1/5=0.2<=alpha.
    # At the largest threshold, choose total loss 1.0 so candidate ell=1 gives 2/5=0.4 in (alpha,gamma].
    losses = [0.4,0.3,0.2,0.1]
    scores = [0.6,0.7,0.8,0.9]
    stest = 0.1
    assert decision_unweighted(alpha, alpha, losses, scores, stest) == 1
    assert decision_unweighted(alpha, gamma, losses, scores, stest) == 0


if __name__ == '__main__':
    random_checks()
    strict_witness_low()
    strict_witness_high()
    print('VERIFY_OK')
