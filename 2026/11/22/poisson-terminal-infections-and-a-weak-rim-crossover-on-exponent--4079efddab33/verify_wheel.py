"""Deterministic finite-state check of Markov SI wheel survival.
Uses no third-party modules. It is a finite-size check, not a proof of the limit theorem.
"""
import math


def survival(n, spoke_rate, rim_rate, time):
    states = 1 << n
    total_bound = n * (spoke_rate + 2 * rim_rate)
    rate_per_state = []
    for mask in range(states):
        outs = []
        for i in range(n):
            if mask & (1 << i):
                continue
            left = (mask >> ((i - 1) % n)) & 1
            right = (mask >> ((i + 1) % n)) & 1
            rate = spoke_rate + rim_rate * (left + right)
            outs.append((mask | (1 << i), rate / total_bound))
        total = sum(p for _, p in outs)
        rate_per_state.append((outs, 1.0 - total))
    probability = [0.0] * states
    probability[0] = 1.0
    poisson_weight = math.exp(-total_bound * time)
    result = poisson_weight
    # Uniformization exactly sums independent step counts. Truncation residual
    # after q*t+30*sqrt(q*t)+100 is far below double precision accuracy.
    max_steps = int(total_bound * time + 30 * math.sqrt(total_bound * time) + 100)
    for k in range(1, max_steps + 1):
        nxt = [0.0] * states
        for mask, v in enumerate(probability):
            if v == 0.0:
                continue
            outs, stay = rate_per_state[mask]
            nxt[mask] += v * stay
            for new_mask, p in outs:
                nxt[new_mask] += v * p
        probability = nxt
        poisson_weight *= total_bound * time / k
        result += poisson_weight * sum(v for mask, v in enumerate(probability) if not (mask & 1))
    return result


def infinite_line_survival(alpha, beta, t):
    return math.exp(-(alpha + 2 * beta) * t +
                    (2 * beta / alpha) * (-math.expm1(-alpha * t)))


def run():
    tests = [
        (1.0, 1.0, 0.8, [0.27293133, 0.27289829, 0.27289780]),
        (1.0, 1.0, 1.5, [0.05260053, 0.05253752, 0.05253584]),
        (2.0, 0.5, 1.0, [0.07671435, 0.07671426, 0.07671426]),
        (0.7, 1.5, 1.0, [0.21460581, 0.21388250, 0.21384540]),
    ]
    for a, b, t, reference in tests:
        lin = infinite_line_survival(a, b, t)
        err = []
        for n, want in zip([6, 8, 10], reference):
            got = survival(n, a, b, t)
            assert abs(got - want) < 6e-8, (a, b, t, n, got, want)
            assert got + 1e-10 >= lin, (a, b, t, n, got, lin)
            err.append(got - lin)
        assert err[0] > err[1] > err[2] - 1e-11, (a, b, t, err)
        print('PASS', a, b, t, 'finite errors', err)
    print('PASS: all 12 finite CTMC tests; analytic limit not inferred from these tests')


if __name__ == '__main__':
    run()
