"""Exact arithmetic checks of an optimum for a one-link trophic-coherence repair.

Self-contained Python 3. Source and target indices are numbered from zero.
Biological links run from prey to consumer. No empirical or dynamical
stability statements are tested.
"""
from fractions import Fraction as Q


def incoherence_squared(n, edges):
    """Evaluate the original trophic-level recurrence, not a closed formula."""
    incoming = [[] for _ in range(n)]
    for prey, consumer in edges:
        assert 0 <= prey < consumer < n
        incoming[consumer].append(prey)
    levels = [Q(1)] * n
    for consumer in range(n):
        if incoming[consumer]:
            levels[consumer] = Q(1) + sum(
                (levels[prey] for prey in incoming[consumer]), Q(0)
            ) / len(incoming[consumer])
    return sum(
        ((levels[consumer] - levels[prey] - 1) ** 2 for prey, consumer in edges),
        Q(0)
    ) / len(edges)


def starting_edges(n):
    return tuple([(i, i + 1) for i in range(n - 1)] + [(0, n - 1)])


def predicted(n, prey, consumer):
    k = n - 2
    if consumer < n - 1:
        h = consumer - prey - 1
        return (Q(h*h) + (Q(k) - Q(h, 2))**2) / (2*(n+1))
    return Q(2, 3) * (k*k - k*prey + prey*prey) / (n+1)


def verify():
    configurations = 0
    improvement = 0
    winning_edges = 0
    sum_of_winners = 0
    for n in range(4, 33):
        base = starting_edges(n)
        baseline = incoherence_squared(n, base)
        assert baseline == Q((n-2)**2, 2*n)
        candidates = []
        for prey in range(n):
            for consumer in range(prey + 1, n):
                if (prey, consumer) in base:
                    continue
                value = incoherence_squared(n, base + ((prey, consumer),))
                assert value == predicted(n, prey, consumer), (n, prey, consumer, value)
                candidates.append((value, prey, consumer))
                configurations += 1
        optimal = min(value for value, _, _ in candidates)
        hstar = (2*(n-2)+2)//5
        best_links = {(i, i+hstar+1) for i in range(n-2-hstar)}
        attained = {(i,j) for value,i,j in candidates if value == optimal}
        assert best_links == attained, (n,best_links,attained)
        assert optimal < baseline
        assert optimal == (Q(hstar*hstar) + (Q(n-2)-Q(hstar,2))**2)/(2*(n+1))
        assert all(j != n-1 for i,j in attained)
        improvement += 1
        winning_edges += len(attained)
        sum_of_winners += len(best_links)
    assert winning_edges == sum_of_winners
    print(f"PASS: {configurations} admissible link configurations over n=4..32")
    print(f"PASS: {improvement} sizes with complete optimum-and-improvement checks")
    print(f"PASS: {winning_edges} winning links checked without the formula")
    print("n=4 baseline:", incoherence_squared(4, starting_edges(4)))
    print("n=4 chosen:", incoherence_squared(4, starting_edges(4)+((0,2),)))
    print("n=9 optimum:", min(incoherence_squared(9, starting_edges(9)+((i,j),)) for i in range(9) for j in range(i+1,9) if (i,j) not in starting_edges(9)))

if __name__ == '__main__':
    verify()
