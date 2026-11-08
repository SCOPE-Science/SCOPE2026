"""Independent Eulerian-support census for cyclic binary trigram profiles.

Enumerates nonnegative balanced edge multiplicities, decides realizability
by connectivity of the entire nonzero edge support, and compares coefficients
with the four-case closed form. No external dependencies.
Run: python verify_flows.py
"""


def coefficient(n):
    value = 2 + int(n >= 2 and n % 2 == 0)
    for t in range(1, n // 2 + 1):
        for b in range(1, t + 1):
            if 2 * t + b <= n:
                value += 2
            for d in range(1, t + 1):
                rest = n - 2 * t - b - d
                if rest >= 0:
                    value += rest + 1
    return value


# Index triples 000 through 111, with source and target two-symbol vertices.
ARC = [(0, 0), (0, 1), (1, 2), (1, 3),
       (2, 0), (2, 1), (3, 2), (3, 3)]


def connected_support(m):
    adjacency = [set() for _ in range(4)]
    used = set()
    for multiplicity, (u, v) in zip(m, ARC):
        if multiplicity > 0:
            used.update((u, v))
            adjacency[u].add(v)
            adjacency[v].add(u)
    if not used:
        return False
    reached = {min(used)}
    frontier = list(reached)
    while frontier:
        for neighbor in adjacency[frontier.pop()]:
            if neighbor not in reached:
                reached.add(neighbor)
                frontier.append(neighbor)
    return used == reached


def census(n):
    count = 0
    for t in range(n // 2 + 1):
        # Balance implies m001=m100=b, m011=m110=d, and
        # m101=t-b, m010=t-d, with 0<=b,d<=t.
        for b in range(t + 1):
            for d in range(t + 1):
                remainder = n - (2 * t + b + d)
                if remainder < 0:
                    continue
                for a in range(remainder + 1):
                    h = remainder - a
                    m = (a, b, t-d, d, b, t-b, d, h)
                    if connected_support(m):
                        count += 1
    return count


def main():
    for n in range(1, 41):
        a = census(n)
        b = coefficient(n)
        assert a == b, (n, a, b)
    print('FLOWS_VERIFY_OK lengths=1..40')


if __name__ == '__main__':
    main()
