"""Reconstruct the 49-state letter-renaming quotient and prove the generating function.
Run with Python 3 and SymPy: python check_transfer.py
"""
from collections import Counter, deque
from sympy import Matrix, Symbol, Poly, factor

D_COEFFICIENTS = (1, -1, -2, -4, -4, -2, 1, 2, 1)
P_COEFFICIENTS = (1, 2, 4, 5, 8, 16, 19, 5, -8, -9, -3)

def canonical(word):
    names = {}
    return tuple(names.setdefault(c, len(names)) for c in word)

def extendable(word):
    if len(word) >= 3 and word[-1] == word[-2] == word[-3]:
        return False
    if len(word) >= 6:
        a, b, c = word[-6:-4], word[-4:-2], word[-2:]
        if sorted(a) == sorted(b) == sorted(c):
            return False
    return True

def quotient():
    queue = deque([()]); seen = {()}; adj = {}
    while queue:
        state = queue.popleft()
        children = Counter()
        for c in (0, 1, 2):
            full = state + (c,)
            if not extendable(full):
                continue
            after = canonical(full[-5:])
            children[after] += 1
            if after not in seen:
                seen.add(after); queue.append(after)
        adj[state] = children
    order = sorted(adj, key=lambda x: (len(x), x))
    index = {v: k for k, v in enumerate(order)}
    M = Matrix.zeros(len(order))
    for state, children in adj.items():
        for dest, multiplicity in children.items():
            M[index[state], index[dest]] = multiplicity
    return order, index, M

def strongly_connected_components(M):
    """Tarjan algorithm on nonzero weighted-matrix entries (no extra packages)."""
    n = M.rows
    neighbors = [[j for j in range(n) if M[i,j]] for i in range(n)]
    visited = {}; low = {}; stack = []; active = set(); comps = []
    def dfs(i):
        visited[i] = low[i] = len(visited)
        stack.append(i); active.add(i)
        for j in neighbors[i]:
            if j not in visited:
                dfs(j); low[i] = min(low[i], low[j])
            elif j in active:
                low[i] = min(low[i], visited[j])
        if low[i] == visited[i]:
            comp = []
            while True:
                j = stack.pop(); active.remove(j); comp.append(j)
                if j == i: break
            comps.append(comp)
    for i in range(n):
        if i not in visited: dfs(i)
    return comps

def main():
    states, index, M = quotient()
    assert len(states) == 49
    components = strongly_connected_components(M)
    recurrent = [c for c in components if len(c)>1 or M[c[0],c[0]]]
    assert len(recurrent) == 1 and len(recurrent[0]) == 30
    assert any(M[i,i] for i in recurrent[0])  # primitive recurrent class
    x = Symbol('x')
    q = x**8 - x**7 - 2*x**6 - 4*x**5 - 4*x**4 - 2*x**3 + x**2 + 2*x + 1
    exact_char = M.charpoly(x).as_expr()
    assert Poly(exact_char, x) == Poly(x**41 * q, x)
    v = Matrix.zeros(49, 1)
    v[index[()]] = 1
    totals = []
    for n in range(120):
        totals.append(sum(v))
        v = M.T * v
    assert totals[:11] == [1,3,9,24,66,180,468,1206,3150,8232,21462]
    # Cayley-Hamilton gives D-recurrence starting at n=49 (char M = x^41 Q).
    # Explicit integer verification of the only earlier terms n=11,...,48
    # therefore proves the recurrence for EVERY n>=11.
    for n in range(11, 49):
        assert sum(D_COEFFICIENTS[j]*totals[n-j] for j in range(9)) == 0
    # Extra tests, not needed for proof, guard the implementation.
    for n in range(49,120):
        assert sum(D_COEFFICIENTS[j]*totals[n-j] for j in range(9)) == 0
    numer = [sum(D_COEFFICIENTS[j] * totals[n-j]
                 for j in range(min(8,n)+1)) for n in range(11)]
    assert tuple(numer) == P_COEFFICIENTS
    print('PASS: 49 states, unique primitive 30-state recurrent component;')
    print('PASS: exact characteristic polynomial x^41*Q(x);')
    print('PASS: recurrence all n>=11 by finite checks and Cayley-Hamilton;')
    print('PASS: generating numerator and 120 coefficients.')

if __name__ == '__main__':
    main()
