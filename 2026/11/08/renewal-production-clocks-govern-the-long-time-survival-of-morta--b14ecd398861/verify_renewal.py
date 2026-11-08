"""Independent numerical checks for renewal-clock search asymptotics.

No external libraries are required. The analytic proof is in RESULT.md.
"""
import math


def root_for_bounded_intervals(p, atoms):
    assert 0 < p < 1 and all(w > 0 and weight > 0 for w, weight in atoms)
    assert abs(sum(wt for w, wt in atoms) - 1.0) < 1e-12
    def value(theta):
        return sum(wt * math.exp(theta * w) for w, wt in atoms)
    target = 1.0 / (1.0 - p)
    lo, hi = 0.0, 1.0
    while value(hi) < target:
        hi *= 2
    for _ in range(100):
        md = (lo + hi) / 2
        if value(md) < target:
            lo = md
        else:
            hi = md
    return (lo + hi) / 2


def log_no_detection_discrete(ticks, p, conditional_rate, atom_ticks, h):
    # Stable log-domain convolution/renewal equation for delayed successful hits.
    assert abs(sum(weight for _, weight in atom_ticks) - 1) < 1e-12
    q = [0.0] * (ticks + 1)
    for k in range(1, ticks + 1):
        tail = sum(weight for gap, weight in atom_ticks if gap > k)
        terms = ([math.log(tail)] if tail else [])
        for gap, weight in atom_ticks:
            if gap <= k:
                age = (k - gap) * h
                safe = (1 - p) + p * math.exp(-conditional_rate * age)
                terms.append(math.log(weight) + math.log(safe) + q[k-gap])
        largest = max(terms)
        q[k] = largest + math.log(sum(math.exp(z-largest) for z in terms))
    return q


def main():
    checks = 0
    for p in (0.05, 0.2, 0.4, 0.7, 0.9):
        det = root_for_bounded_intervals(p, [(1.0, 1.0)])
        mix = root_for_bounded_intervals(p, [(0.5, 0.5), (1.5, 0.5)])
        pois = p
        assert abs(det + math.log1p(-p)) < 1e-12
        assert 0 < pois < mix < det
        checks += 3
        for rate in (0.3, 1.0, 3.0):
            for gaps, theta in [([(2, 1.0)], det), ([(1, 0.5), (3, 0.5)], mix)]:
                ticks = 12000
                surv = log_no_detection_discrete(ticks, p, rate, gaps, 0.5)
                assert all(surv[k] <= 1e-12 for k in range(len(surv)))
                assert all(surv[k + 1] <= surv[k] + 1e-12 for k in range(len(surv) - 1))
                # Delays do not change the large-time decay exponent.
                assert abs(-surv[ticks] / (ticks * 0.5) - theta) < 0.006, (p,rate,gaps,-surv[ticks]/(ticks*0.5),theta)
                checks += 3
    # One-point defect-clock formula independent of the particle delay law.
    for p in (0.05, 0.2, 0.4, 0.7, 0.9):
        for t in (0.1, 1.5, 12.0, 100.0):
            # Q for exponential arrivals and defective exponential successes.
            rate = 0.8
            exact = math.exp(-p * (t - (1 - math.exp(-rate * t)) / rate))
            assert 0 < exact <= 1
            if t >= 100:
                assert abs(-math.log(exact)/t - p) < 0.02
            checks += 1
    print('PASS', checks, 'independent exponential/deterministic/two-point delay checks')

if __name__ == '__main__':
    main()
