"""Exact and numeric reproducibility checks for multi-partner colonization."""
from fractions import Fraction
from functools import lru_cache
import math
import random


def state_recursion(arrival, missing_hazards, initial_hazard):
    """Independent CTMC first-step equations for all subsets of acquired partners."""
    n = len(arrival)
    goal = (1 << n) - 1

    @lru_cache(None)
    def success(subset):
        if subset == goal:
            return Fraction(1)
        absent = [j for j in range(n) if not subset & (1 << j)]
        hazard = initial_hazard if subset == 0 else sum(
            (missing_hazards[j] for j in absent), Fraction(0)
        )
        total = hazard + sum((arrival[j] for j in absent), Fraction(0))
        return sum(
            (arrival[j] * success(subset | (1 << j)) for j in absent),
            Fraction(0),
        ) / total

    return success(0)


def closed_probability(arrival, missing_hazards, initial_hazard):
    total_arrival = sum(arrival, Fraction(0))
    total_hazard = sum(missing_hazards, Fraction(0))
    answer = (total_arrival + total_hazard) / (total_arrival + initial_hazard)
    for r, h in zip(arrival, missing_hazards):
        answer *= r / (r + h)
    return answer


def optimal_allocation(hazards, budget):
    """Solve the strictly concave allocation equations numerically."""
    def rate(h, multiplier):
        root = math.sqrt(h * h + 4 * h / multiplier)
        return 2 * h / (multiplier * (root + h))

    def total(multiplier):
        return sum(rate(h, multiplier) for h in hazards)

    low, high = 1.0, 1.0
    while total(low) < budget:
        low *= 0.5
    while total(high) > budget:
        high *= 2.0
    for _ in range(170):
        middle = math.sqrt(low * high)
        if total(middle) > budget:
            low = middle
        else:
            high = middle
    multiplier = math.sqrt(low * high)
    values = [rate(h, multiplier) for h in hazards]
    return values, multiplier


def test():
    rng = random.Random(452026)
    exact_cases = 0
    for n in range(2, 8):
        for _ in range(45):
            arrivals = [Fraction(rng.randrange(1, 13), rng.randrange(1, 8)) for j in range(n)]
            hazards = [Fraction(rng.randrange(1, 11), rng.randrange(1, 9)) for j in range(n)]
            initial = Fraction(rng.randrange(1, 15), rng.randrange(1, 8))
            a = state_recursion(arrivals, hazards, initial)
            b = closed_probability(arrivals, hazards, initial)
            assert a == b, (n, arrivals, hazards, initial, a, b)
            assert 0 < a < 1
            exact_cases += 1

    numeric_cases = 0
    for n in range(2, 10):
        for _ in range(25):
            hazards = [10 ** rng.uniform(-1, 2) for j in range(n)]
            budget = 10 ** rng.uniform(-1, 2)
            opt, eta = optimal_allocation(hazards, budget)
            assert abs(sum(opt) - budget) < 2e-11 * budget
            vals = [h / (v * (v + h)) for v, h in zip(opt, hazards)]
            assert max(abs(z / eta - 1) for z in vals) < 1e-10
            for i in range(n):
                for j in range(n):
                    if hazards[i] > hazards[j]:
                        assert opt[i] > opt[j]
                    elif hazards[i] == hazards[j]:
                        assert abs(opt[i] - opt[j]) < 1e-10
            def value(a):
                return sum(math.log(z/(z+h)) for z, h in zip(a, hazards))
            baseline = value(opt)
            assert baseline >= value([budget/n]*n) - 1e-11
            for _ in range(8):
                v = [rng.uniform(0.001, 1) for j in range(n)]
                candidate = [budget * z / sum(v) for z in v]
                assert baseline >= value(candidate) - 1e-10
            numeric_cases += 1

    equal_small, _ = optimal_allocation([1.0,4.0,9.0],1e-5)
    scaled_small = [v/1e-5 for v in equal_small]
    assert max(abs(v-1/3) for v in scaled_small) < 1e-5
    asymptotic_large,_ = optimal_allocation([1.0,4.0,9.0],1e6)
    scaled_large = [v/1e6 for v in asymptotic_large]
    assert max(abs(v - t) for v,t in zip(scaled_large,[1/6,2/6,3/6])) < 1e-5

    # Exact example evaluated directly from rational state probabilities.
    example = closed_probability([Fraction(2), Fraction(4), Fraction(6)],
                                 [Fraction(1), Fraction(4), Fraction(9)], Fraction(10))
    assert example == Fraction(26,165)
    print(f"PASS: {exact_cases} independent exact-subset CTMC cases; "
          f"{numeric_cases} numerical KKT/random-comparison cases; asymptotic tests")
    print(f"Equal-split exact example: {example} = {float(example):.9f}")


if __name__ == '__main__':
    test()
