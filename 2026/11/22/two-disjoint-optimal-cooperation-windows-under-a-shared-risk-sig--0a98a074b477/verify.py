"""Exact-rational checker for two-window decisions in a three-person risk game.

Run: python verify.py
Only the Python standard library is required.
"""
from fractions import Fraction as F
from itertools import combinations

b, c, tau = F(1), F(3, 19), F(1, 2)
other = tuple('C' * 10 + 'A' * 8 + 'D' * 2)
pairs = list(combinations(range(len(other)), 2))
assert len(pairs) == 190


def cooperator_count(pair, r):
    return sum(other[i] == 'C' or (other[i] == 'A' and r >= tau)
               for i in pair)


def payoff(pair, r, focal_cooperates):
    contributors = cooperator_count(pair, r) + int(focal_cooperates)
    # Success saves the endowment, while failure has risk r of total loss.
    return (b if contributors >= 2 else b * (1 - r)) - c * focal_cooperates


def average_difference(r):
    return sum((payoff(pair, r, True) - payoff(pair, r, False)
                for pair in pairs), F(0)) / len(pairs)


def pivotal_count(r):
    return sum(cooperator_count(pair, r) == 1 for pair in pairs)


assert pivotal_count(F(1, 4)) == 100
assert pivotal_count(F(3, 4)) == 36
p0, p1 = F(100, 190), F(36, 190)
assert (p0, p1) == (F(10, 19), F(18, 95))
for r in [F(0), F(1, 4), F(3, 10), F(2, 5), F(1, 2),
          F(3, 5), F(5, 6), F(9, 10), F(1)]:
    p = p0 if r < tau else p1
    assert average_difference(r) == b * p * r - c

alpha, gamma = c / (b * p0), c / (b * p1)
assert (alpha, tau, gamma) == (F(3, 10), F(1, 2), F(5, 6))


def interval_integral(lo, hi, p):
    # Integral of the cooperation-minus-defection payoff difference.
    return b * p * (hi ** 2 - lo ** 2) / 2 - c * (hi - lo)


def threshold_gain(t):
    if t <= tau:
        return interval_integral(t, tau, p0) + interval_integral(tau, F(1), p1)
    return interval_integral(t, F(1), p1)


positive_early = interval_integral(alpha, tau, p0)
negative_middle = -interval_integral(tau, gamma, p1)
positive_late = interval_integral(gamma, F(1), p1)
assert (positive_early, negative_middle, positive_late) == (
    F(1, 95), F(1, 95), F(1, 380))
oracle_gain = positive_early + positive_late
best_threshold_gain = max(threshold_gain(alpha), threshold_gain(gamma))
assert oracle_gain == F(1, 76)
assert threshold_gain(alpha) == threshold_gain(gamma) == F(1, 380)
assert oracle_gain - best_threshold_gain == F(1, 95)
# Supplementary finite-sample check, not a proof of optimization over real t.
for k in range(1001):
    t = F(k, 1000)
    assert threshold_gain(t) <= best_threshold_gain

print('190 co-player pairs checked exactly')
print('pivotal probabilities', p0, p1)
print('cooperation windows', (alpha, tau), (gamma, F(1)))
print('early positive gain, middle loss, late positive gain:',
      positive_early, negative_middle, positive_late)
print('oracle and best monotone gain:', oracle_gain, best_threshold_gain)
print('strict payoff gap:', oracle_gain - best_threshold_gain)
print('All exact checks passed')
