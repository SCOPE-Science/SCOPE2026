"""Exact finite checks for independent fair orientations of uniform labeled trees."""
from fractions import Fraction
from itertools import product


def prufer_edges(sequence):
    n = len(sequence) + 2
    degree = [1] * n
    for vertex in sequence:
        degree[vertex] += 1
    edges = []
    for vertex in sequence:
        leaf = next(i for i in range(n) if degree[i] == 1)
        edges.append((leaf, vertex))
        degree[leaf] -= 1
        degree[vertex] -= 1
    pair = [i for i in range(n) if degree[i] == 1]
    edges.append(tuple(pair))
    return edges


def expected(n):
    c = Fraction(n - 1, n) ** (n - 2)
    d = Fraction(2 * n - 1, 2 * n) ** (n - 2)
    mean = Fraction(n, 2) * d
    covariance = Fraction(n * n, 4) * (c - d * d)
    variance = covariance + Fraction(n, 2) * (d - c)
    diagonal_joint = Fraction(0)
    offdiagonal_joint = Fraction(n, 4 * (n - 1)) * c
    return mean, covariance, variance, diagonal_joint, offdiagonal_joint


def enumerated(n):
    first = second = first_squared = product_total = marked_diagonal = marked_off = 0
    count = (n ** (n - 2)) * (2 ** (n - 1))
    for sequence in product(range(n), repeat=n - 2):
        edges = prufer_edges(sequence)
        for bits in product((0, 1), repeat=n - 1):
            indegree = [0] * n
            outdegree = [0] * n
            for (u, v), bit in zip(edges, bits):
                if bit:
                    u, v = v, u
                outdegree[u] += 1
                indegree[v] += 1
            sources = [degree == 0 for degree in indegree]
            sinks = [degree == 0 for degree in outdegree]
            s, k = sum(sources), sum(sinks)
            first += s
            second += k
            first_squared += s * s
            product_total += s * k
            marked_diagonal += int(sources[0] and sinks[0])
            marked_off += int(sources[0] and sinks[1])
    mean = Fraction(first, count)
    assert mean == Fraction(second, count)
    return (mean, Fraction(product_total, count) - mean * mean,
            Fraction(first_squared, count) - mean * mean,
            Fraction(marked_diagonal, count), Fraction(marked_off, count))


def main():
    cases = 0
    for n in range(2, 7):
        actual = enumerated(n)
        wanted = expected(n)
        assert actual == wanted, (n, actual, wanted)
        assert wanted[1] == 0 if n == 2 else wanted[1] < 0
        c = Fraction(n - 1, n) ** (n - 2)
        d = Fraction(2 * n - 1, 2 * n) ** (n - 2)
        assert wanted[4] - (d / 2) ** 2 > 0
        cases += n ** (n - 2) * (2 ** (n - 1))
    for n in range(2, 201):
        c = Fraction(n - 1, n) ** (n - 2)
        d = Fraction(2 * n - 1, 2 * n) ** (n - 2)
        assert c * n > d * d * (n - 1)
        assert n == 2 or c < d * d
    print('EXACT_PRUFER_AND_ORIENTATION_CASES', cases)
    print('MARKED_JOINT_PROBABILITIES_PASS 5')
    print('FINITE_SIGN_DIAGNOSTICS_PASS 199')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
