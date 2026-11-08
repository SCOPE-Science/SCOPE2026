"""Reproducible finite checks for the fixed-two-support partition-transfer component theorem.

Python 3.10+, no dependencies. This is evidence of finite tests, not an infinite proof.
"""
from collections import Counter, deque


def full_partitions(n, max_part=None):
    if max_part is None:
        max_part = n
    if n == 0:
        yield ()
        return
    for first in range(min(n, max_part), 0, -1):
        for tail in full_partitions(n - first, first):
            yield (first,) + tail


def step_neighbors(part):
    """Unit moves using only distinct part values, independent of row labels."""
    counts = Counter(part)
    answer = set()
    for donor in counts:
        for receiver in list(counts) + [0]:
            if donor == receiver and counts[donor] < 2:
                continue
            out = counts.copy()
            out[donor] -= 1
            if receiver:
                out[receiver] -= 1
            if donor > 1:
                out[donor - 1] += 1
            out[receiver + 1] += 1
            nxt = tuple(x for s in sorted(out, reverse=True)
                        for x in [s] * out[s] if out[s] > 0)
            if nxt != part:
                answer.add(nxt)
    return answer


def indexed_step_neighbors(part):
    """Independent explicit row-index moves for small n."""
    answer = set()
    rows = list(part)
    for donor in range(len(rows)):
        for receiver in range(len(rows) + 1):
            if receiver == donor:
                continue
            out = rows.copy()
            out[donor] -= 1
            if receiver == len(rows):
                out.append(1)
            else:
                out[receiver] += 1
            nxt = tuple(sorted((x for x in out if x), reverse=True))
            if nxt != part:
                answer.add(nxt)
    return answer


def two_support_vertices(n):
    """A separate parametrization, independent of full partition generation."""
    verts = set()
    for a in range(2, n):
        for b in range(1, a):
            for p in range(1, (n - b) // a + 1):
                remaining = n - a * p
                if remaining > 0 and remaining % b == 0:
                    verts.add((a,) * p + (b,) * (remaining // b))
    return verts


def proposed_component(n):
    assert n >= 3
    h = {(a,) + (1,) * (n - a) for a in range(2, n)}
    t = {(n - k, k) for k in range(1, (n - 1) // 2 + 1)}
    u = {(2,) * k + (1,) * (n - 2 * k)
         for k in range(1, (n - 1) // 2 + 1)}
    out = h | t | u
    if n >= 7 and n % 2:
        b = (n - 1) // 2
        out.add((b, b, 1))
        out.add((3,) + (2,) * ((n - 3) // 2))
    return out


def connected_component(root, vertices):
    todo = deque([root])
    seen = {root}
    while todo:
        v = todo.popleft()
        for w in step_neighbors(v):
            if w in vertices and w not in seen:
                seen.add(w)
                todo.append(w)
    return seen


def expected_size(n):
    if n == 3:
        return 1
    if n == 5:
        return 5
    if n % 2:
        return 2 * n - 3
    return 2 * n - 6


def run():
    # Independent whole-partition construction, including all row indices.
    for n in range(3, 23):
        allp = set(full_partitions(n))
        direct = {v for v in allp if len(set(v)) == 2}
        analytic = two_support_vertices(n)
        assert analytic == direct, (n, 'vertices differ')
        for v in direct:
            assert indexed_step_neighbors(v) == step_neighbors(v), (n, v)
            assert step_neighbors(v) <= allp, (n, v)
        comp = connected_component((n - 1, 1), direct)
        named = proposed_component(n)
        assert comp == named, (n, 'component differs', comp ^ named)
        assert len(named) == expected_size(n), (n, 'size differs')
        if n <= 7:
            assert comp == direct, ('early connectivity', n)
        else:
            assert (n - 4, 2, 2) in direct - comp, ('outside witness', n)
        print('FULL_PARTITION_GRAPH_OK', n, len(direct), len(comp))

    # Larger parameters: independent two-size generator, exact reachable
    # component and exact boundary closure through all transfer operations.
    for n in range(23, 151):
        vertices = two_support_vertices(n)
        named = proposed_component(n)
        assert named <= vertices, n
        assert all((step_neighbors(v) & vertices) <= named for v in named), n
        assert connected_component((n - 1, 1), vertices) == named, n
        assert len(named) == expected_size(n), n
        assert (n - 4, 2, 2) in vertices - named, n
    print('TWO_SIZE_PARAMETRIZATION_AND_CLOSURE_OK 23..150')
    print('VERIFY_OK')


if __name__ == '__main__':
    run()
