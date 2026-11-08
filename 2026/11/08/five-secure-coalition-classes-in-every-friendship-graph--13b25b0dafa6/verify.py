"""Independent finite checks for the friendship-graph secure coalition theorem.

Run: python verify.py. Uses only the Python standard library.
"""

def graph(m):
    n = 2*m + 1
    adj = [(1 << n) - 2] + [0] * (n - 1)
    for j in range(m):
        a, b = 2*j+1, 2*j+2
        adj[a] = (1 << 0) | (1 << b)
        adj[b] = (1 << 0) | (1 << a)
    return adj


def direct_secure_table(m):
    adj = graph(m)
    n = len(adj)
    full = (1 << n)-1
    def dom(S):
        covered = S
        for v in range(n):
            if (S >> v) & 1:
                covered |= adj[v]
        return covered == full
    sec = [False] * (full + 1)
    for S in range(1, full + 1):
        if not dom(S):
            continue
        sec[S] = all(
            any((adj[u] & (1 << v)) and dom((S ^ (1 << v)) | (1 << u))
                for v in range(n) if (S >> v) & 1)
            for u in range(n) if not ((S >> u) & 1)
        )
    return sec


def predicted_secure(S, m):
    untouched = sum(not (S & ((1 << (2*j+1)) | (1 << (2*j+2))))
                    for j in range(m))
    return untouched <= (1 if S & 1 else 0)


def direct_partition_valid(blocks, sec):
    for i, B in enumerate(blocks):
        if sec[B]:
            return False
        if not any(not sec[A] and sec[B | A]
                   for j, A in enumerate(blocks) if i != j):
            return False
    return True


def quotient_partition_valid(blocks, m):
    block_index = {}
    for j, B in enumerate(blocks):
        for v in range(2*m+1):
            if B & (1 << v):
                block_index[v] = j
    hub = block_index[0]
    edges = [(block_index[2*j+1], block_index[2*j+2]) for j in range(m)]
    def avoid(*indices):
        return sum(a not in indices and b not in indices for a,b in edges)
    sec = [avoid(j) <= (1 if j == hub else 0) for j in range(len(blocks))]
    for j, B in enumerate(blocks):
        if sec[j] or not any(not sec[k] and avoid(j,k) <= (1 if hub in (j,k) else 0)
                                 for k in range(len(blocks)) if k != j):
            return False
    return True


def partitions_of(n):
    blocks = []
    def rec(i):
        if i == n:
            yield tuple(blocks)
            return
        for j in range(len(blocks)):
            blocks[j] |= 1 << i
            yield from rec(i+1)
            blocks[j] ^= 1 << i
        blocks.append(1 << i)
        yield from rec(i+1)
        blocks.pop()
    yield from rec(0)


def construction(m):
    big = 1
    for j in range(m-2):
        big |= (1 << (2*j+1)) | (1 << (2*j+2))
    return (big,) + tuple(1 << v for v in range(2*m-3, 2*m+1))


def run():
    for m in range(2, 8):
        sec = direct_secure_table(m)
        assert all(s == predicted_secure(S, m) for S, s in enumerate(sec))
        assert direct_partition_valid(construction(m), sec)
        print('SECURE_SET_CRITERION_AND_CONSTRUCTION_OK', m)
    for m, exact in [(2, 1), (3, 81), (4, 1174), (5, 12290)]:
        sec = direct_secure_table(m)
        maximum = count = 0
        for blocks in partitions_of(2*m+1):
            direct = direct_partition_valid(blocks, sec)
            if m <= 4:
                assert direct == quotient_partition_valid(blocks, m)
            if direct:
                k = len(blocks)
                if k > maximum:
                    maximum, count = k, 0
                if k == maximum:
                    count += 1
        assert maximum == 5 and count == exact, (m, maximum, count, exact)
        print('EXHAUSTIVE_UNLABELLED_PARTITIONS_OK', m, 'maximum', maximum,
              'optimal_partitions', count)
    print('VERIFY_OK')


if __name__ == '__main__':
    run()
