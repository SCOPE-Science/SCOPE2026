"""Finite checks of graph-inverse-semigroup power persistence.

Run: python3 CHECK.py
No third-party dependencies. Independent normal-form multiplication versus
coefficient calculations from powers of the adjacency matrix.
"""


def path_lists(adjacency, cutoff):
    n = len(adjacency)
    paths = [[(v, (), v) for v in range(n)]]
    for length in range(1, cutoff + 1):
        paths.append([
            (start, edges + ((end, finish, parallel),), finish)
            for start, edges, end in paths[-1]
            for finish in range(n)
            for parallel in range(adjacency[end][finish])
        ])
    return paths


def append_paths(x, tail):
    assert x[2] == tail[0]
    return (x[0], x[1] + tail[1], tail[2])


def suffix_if_prefix(longer, shorter):
    if longer[0] != shorter[0]:
        return None
    if longer[1][:len(shorter[1])] != shorter[1]:
        return None
    return (shorter[2], longer[1][len(shorter[1]):], longer[2])


def multiply(x, y):
    if x is None or y is None:
        return None
    a, b = x
    c, d = y
    gamma = suffix_if_prefix(c, b)
    if gamma is not None:
        return (append_paths(a, gamma), d)
    delta = suffix_if_prefix(b, c)
    if delta is not None:
        return (a, append_paths(d, delta))
    return None


def matrix_multiply(x, y):
    n = len(x)
    return [[sum(x[i][k] * y[k][j] for k in range(n))
             for j in range(n)] for i in range(n)]


def predicted(adjacency, cutoff):
    n = len(adjacency)
    powers = [[[int(i == j) for j in range(n)] for i in range(n)]]
    for _ in range(cutoff):
        powers.append(matrix_multiply(powers[-1], adjacency))
    path_end = [[sum(powers[k][start][end] for start in range(n))
                 for end in range(n)] for k in range(cutoff + 1)]
    total, persistent = [], []
    for degree in range(cutoff + 1):
        total.append(sum(path_end[a][v] * path_end[degree-a][v]
                         for v in range(n) for a in range(degree+1)))
        idem = sum(path_end[degree//2]) if degree % 2 == 0 else 0
        other = 2 * sum(path_end[base][v] * powers[degree-2*base][v][v]
                        for v in range(n) for base in range((degree-1)//2+1))
        persistent.append(idem + other)
    return total, persistent


def enumerated(adjacency, cutoff):
    p = path_lists(adjacency, cutoff)
    total = [0]*(cutoff+1)
    persistent = [0]*(cutoff+1)
    for degree in range(cutoff+1):
        for a in range(degree+1):
            for left in p[a]:
                for right in p[degree-a]:
                    if left[2] != right[2]:
                        continue
                    x = (left, right)
                    total[degree] += 1
                    x2 = multiply(x, x)
                    if x2 is None:
                        continue
                    persistent[degree] += 1
                    x3 = multiply(x2, x)
                    x4 = multiply(x3, x)
                    assert x3 is not None and x4 is not None, (adjacency, x)
    return total, persistent


def run():
    cases = {
        'two parallel loops': [[2]],
        'Fibonacci graph': [[1,1], [1,0]],
        'full two-vertex graph': [[1,1], [1,1]],
        'period-two multigraph': [[0,2], [1,0]],
        'acyclic three-vertex graph': [[0,1,1], [0,0,1], [0,0,0]],
        'irregular strongly connected multigraph': [[1,2], [1,1]],
        'one loop': [[1]],
        'isolated vertices': [[0,0], [0,0]],
    }
    for label, adjacency in cases.items():
        cutoff = 8 if sum(map(sum, adjacency)) <= 2 else 6
        predicted_counts = predicted(adjacency, cutoff)
        enumerated_counts = enumerated(adjacency, cutoff)
        assert predicted_counts == enumerated_counts, (label, predicted_counts, enumerated_counts)
        print(label, 'PASS', 'degree 0..', cutoff, 'counts', predicted_counts)
    print('ALL EIGHT GRAPH CHECKS PASSED')


if __name__ == '__main__':
    run()
