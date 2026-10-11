from collections import deque, Counter

def check(n):
    vertices = [m for m in range(1, (1 << n) - 1)]
    adj = {
        u: {v for v in vertices if v != u and (u & v) == 0}
        for u in vertices
    }

    counts = Counter()
    for i, u in enumerate(vertices):
        dist = {u: 0}
        q = deque([u])
        while q:
            x = q.popleft()
            for y in adj[x]:
                if y not in dist:
                    dist[y] = dist[x] + 1
                    q.append(y)
        for v in vertices[i + 1:]:
            counts[dist[v]] += 1

    d1 = (3**n - 2**(n + 1) + 1) // 2
    d2 = 2**(2*n - 1) + 1 - 3**n
    d3 = (3**n - 3*(2**n) + 3) // 2
    w = d1 + 2*d2 + 3*d3
    formula = 4**n - 11*(2**(n - 1)) + 7

    assert len(vertices) == 2**n - 2
    assert counts[1] == d1
    assert counts[2] == d2
    assert counts[3] == d3
    assert sum(counts.values()) == len(vertices)*(len(vertices)-1)//2
    assert w == formula

for n in range(2, 9):
    check(n)

print("VERIFY_OK")
