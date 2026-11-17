"""Independent full functional-graph verification of path rotor recurrence."""

def update(st, n):
    p, word = st
    if p == 0: return (1, word)
    if p == n - 1: return (n - 2, word)
    bit = 1 << (p - 1)
    new = word ^ bit
    return (p + (1 if new & bit else -1), new)


def rooted(st, n):
    p, word = st
    for i in range(1, n-1):
        pointing_right = (word >> (i - 1)) & 1
        if i < p and pointing_right != 1: return False
        if i > p and pointing_right != 0: return False
    return True


def graph_check(n):
    states = [(p, b) for p in range(n) for b in range(1 << (n - 2))]
    successor = {s: update(s,n) for s in states}
    # Identify ALL periodic states without using rooted-condition assumptions.
    in_degree = {s: 0 for s in states}
    for dst in successor.values(): in_degree[dst] += 1
    from collections import deque
    queue = deque(s for s in states if in_degree[s] == 0)
    while queue:
        s = queue.popleft()
        dst = successor[s]
        in_degree[dst] -= 1
        if in_degree[dst] == 0: queue.append(dst)
    periodic = {s for s in states if in_degree[s] > 0}
    rooted_states = {s for s in states if rooted(s,n)}
    assert periodic == rooted_states
    assert len(periodic) == 2*(n-1)
    # Actual first periodic-entry time, for all endpoint-started configurations.
    for word in range(1 << (n - 2)):
        s = (0,word); t=0
        while s not in periodic:
            s = successor[s]; t += 1
            assert t <= (n-2)**2
        marked = [i for i in range(1,n-1) if (word>>(i-1))&1]
        expected = 0 if not marked else 2*sum(marked)-marked[-1]
        assert t == expected
    return len(states), len(periodic)

if __name__ == '__main__':
    for n in range(3, 15):
        a,b = graph_check(n)
        print(f'n={n}, states={a}, periodic={b}, endpoint-formula=PASS')
    print('FULL GRAPH CHECKS PASS')
