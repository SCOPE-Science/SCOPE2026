"""Finite reproducibility checks for the no-nesting scheduling boundary.

Run: python CHECK.py (Python 3 standard library only).
Finite checks do not substitute for the universal analytic proof.
"""
from fractions import Fraction
from itertools import combinations, product


def greedy(jobs, machines):
    """Jobs have nondecreasing starts and ends (proper presentation)."""
    assert all(jobs[i][0] <= jobs[i+1][0] and
               jobs[i][1] <= jobs[i+1][1]
               for i in range(len(jobs)-1))
    assigned = [[] for _ in range(machines)]
    accepted = []
    for interval in jobs:
        start, end = interval
        assert start < end
        active = sum(a <= start < b for a, b in accepted)
        if active < machines:
            color = len(accepted) % machines
            assert not assigned[color] or assigned[color][-1][1] <= start
            assigned[color].append(interval)
            accepted.append(interval)
        counts = [len(x) for x in assigned]
        assert max(counts) - min(counts) <= 1
    return len(accepted)


def maximum_feasible(jobs, machines):
    best = 0
    for mask in range(1 << len(jobs)):
        k = mask.bit_count()
        if k <= best:
            continue
        events = []
        for i, (a, b) in enumerate(jobs):
            if mask & (1 << i):
                events.extend(((a, +1), (b, -1)))
        load = 0
        valid = True
        for _, delta in sorted(events):  # ends before starts on ties
            load += delta
            if load > machines:
                valid = False
                break
        if valid:
            best = k
    return best


def equitable_feasible(jobs, machines):
    jobs = sorted(jobs)
    finish = [Fraction(-100)] * machines
    load = [0] * machines
    def rec(i):
        if i == len(jobs):
            return max(load) - min(load) <= 1
        start, end = jobs[i]
        for j in range(machines):
            if finish[j] <= start:
                old = finish[j]
                finish[j] = end
                load[j] += 1
                if rec(i+1):
                    return True
                finish[j] = old
                load[j] -= 1
        return False
    return rec(0)


def fair_optimum(jobs, machines):
    best = 0
    for mask in range(1 << len(jobs)):
        if mask.bit_count() <= best:
            continue
        selected = [jobs[i] for i in range(len(jobs)) if mask & (1 << i)]
        if equitable_feasible(selected, machines):
            best = len(selected)
    return best


def main():
    checks = 0
    # Non-identical lengths and exact endpoint order; no containment.
    for n in range(9):
        for starts in combinations(range(8), n):
            for k in (1, 2, 3):
                jobs = [(Fraction(s), Fraction(s + 2 + (i % k)))
                        for i, s in enumerate(starts)]
                if any(jobs[i][1] > jobs[i+1][1]
                       for i in range(n-1)):
                    continue
                for machines in (1, 2, 3, 4):
                    assert greedy(jobs, machines) == maximum_feasible(jobs, machines)
                    checks += 1
    # Coincident intervals: arbitrary deterministic tie order.
    for starts in product(range(4), repeat=6):
        jobs = sorted((Fraction(s), Fraction(s+1)) for s in starts)
        for machines in (1, 2, 3):
            assert greedy(jobs, machines) == maximum_feasible(jobs, machines)
            checks += 1
    # Arbitrarily near unit lengths; verify optimum and fair optimum.
    for machines in (2, 3, 4, 5, 6):
        eps = Fraction(1, 100)
        jobs = [(Fraction(i), Fraction(i+1)) for i in range(3)]
        jobs += [(Fraction(1) - eps, Fraction(2) + eps)] * (machines - 1)
        assert maximum_feasible(jobs, machines) == machines + 2
        if machines <= 4:
            assert fair_optimum(jobs, machines) == machines + 1
        checks += 1
    print(f"PASS: {checks} finite instances (greedy, fairness and obstruction).")

if __name__ == '__main__':
    main()
