"""Exact finite-state certificate for temporal-five Rule 73 ring dynamics.

Uses the Python standard library only. Every identity is tested from the
local truth table and independently computable finite integer matrices.
"""
from collections import defaultdict

RULE = 73


def local(a, b, c):
    return (RULE >> (4 * a + 2 * b + c)) & 1


def graph(p):
    m = 1 << p
    adj = [[] for _ in range(m*m)]
    for a in range(m):
        for b in range(m):
            v = a*m + b
            for c in range(m):
                if all(((b >> ((t+1) % p)) & 1) == local((a >> t) & 1, (b >> t) & 1, (c >> t) & 1) for t in range(p)):
                    adj[v].append(b*m + c)
    return adj


def recurrent_subgraph(adj):
    size = len(adj)
    reverse = [[] for _ in range(size)]
    for v, out in enumerate(adj):
        for w in out:
            reverse[w].append(v)
    visited, order = set(), []
    for start in range(size):
        if start in visited:
            continue
        visited.add(start)
        stack = [(start, 0)]
        while stack:
            v, i = stack[-1]
            if i == len(adj[v]):
                order.append(v)
                stack.pop()
                continue
            w = adj[v][i]
            stack[-1] = (v, i + 1)
            if w not in visited:
                visited.add(w)
                stack.append((w, 0))
    visited.clear()
    cyclic = []
    for start in reversed(order):
        if start in visited:
            continue
        component = []
        todo = [start]
        visited.add(start)
        while todo:
            v = todo.pop()
            component.append(v)
            for w in reverse[v]:
                if w not in visited:
                    visited.add(w)
                    todo.append(w)
        if len(component) > 1 or start in adj[start]:
            cyclic.append(sorted(component))
    assert len(cyclic) == 1, [len(c) for c in cyclic]
    vertices = cyclic[0]
    ix = {v:i for i,v in enumerate(vertices)}
    small = [[ix[w] for w in adj[v] if w in ix] for v in vertices]
    return vertices, small


def traces(adj, limit):
    counts = [0]*(limit+1)
    for start in range(len(adj)):
        distribution = {start:1}
        for n in range(1, limit+1):
            nxt = defaultdict(int)
            for i, weight in distribution.items():
                for j in adj[i]:
                    nxt[j] += weight
            distribution = nxt
            counts[n] += distribution.get(start, 0)
    return counts


def determinant_from_traces(trace, d):
    # Newton identities: det(I-zA)=1+sum(c_k z^k).
    coefficients = [1]
    for k in range(1, d+1):
        numerator = sum(coefficients[k-i] * trace[i] for i in range(1, k+1))
        assert numerator % k == 0
        coefficients.append(-numerator//k)
    return coefficients


def polynomial(degree_terms):
    out = [0]*(max(degree_terms)+1)
    for exponent, coefficient in degree_terms.items():
        out[exponent] = coefficient
    return out


def product(a, b):
    ans = [0]*(len(a)+len(b)-1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            ans[i+j] += ai*bj
    return ans


def test():
    p1verts, g1 = recurrent_subgraph(graph(1))
    p3verts, g3 = recurrent_subgraph(graph(3))
    p5verts, g5 = recurrent_subgraph(graph(5))
    assert (len(g1),len(g3),len(g5)) == (4,19,49)
    assert sum(map(len,g5)) == 70
    t1 = traces(g1, 55)
    t5 = traces(g5, 55)
    D1 = polynomial({0:1, 3:-1, 4:-1})
    A = polynomial({0:1, 8:1, 9:1, 16:-1, 17:-2, 18:-1})
    B = polynomial({0:1, 3:-1, 4:-1, 8:-2, 9:-2, 11:-3, 12:-1, 13:2})
    D5 = product(product(A,A),B)
    assert len(D5) == 50
    assert determinant_from_traces(t1,4) == D1
    assert determinant_from_traces(t5,49) == D5
    assert all((t5[n]-t1[n]) % 5 == 0 for n in range(1,56))
    expected = {11:11, 12:12, 13:0, 14:14, 15:30, 16:32,
                17:51, 18:72, 19:95, 20:120, 21:126,
                22:231, 23:368, 24:348, 25:475,
                26:884, 27:1134, 28:1414, 29:2175, 30:3150}
    c = {n: (t5[n]-t1[n])//5 for n in range(1,56)}
    assert all(c[n] == 0 for n in range(3,11))
    assert all(c[n] == value for n,value in expected.items())
    assert c[13] == 0
    assert all(c[n] > 0 for n in range(14,56))

    # Collatz-Wielandt comparison with already-known temporal-three growth:
    # nonnegative powers of a primitive adjacency have positive row sums.
    def enclose(g, power):
        v = [1]*len(g)
        for _ in range(power):
            v = [sum(v[j] for j in row) for row in g]
            assert all(t > 0 for t in v)
        w = [sum(v[j] for j in row) for row in g]
        return min(w[i]/v[i] for i in range(len(v))),max(w[i]/v[i] for i in range(len(v))),v,w
    lower3, upper3, v3, w3 = enclose(g3,50)
    lower5, upper5, v5, w5 = enclose(g5,100)
    assert all(2*a > 3*b for a,b in zip(w3,v3))
    assert all(5*a < 7*b for a,b in zip(w5,v5))
    assert lower3 > 1.5 and upper5 < 1.4
    assert 1.37 < lower5 < upper5 < 1.39
    print('TRANSFER_OK')
    print('states_p1,p3,p5:',len(g1),len(g3),len(g5))
    print('edge_count_p5:',sum(map(len,g5)))
    print('determinant_D1:',D1)
    print('determinant_D5:',D5)
    print('c_3_to_30:',[(n,c[n]) for n in range(3,31)])
    print('spectral_comparison_rho3:',round(lower3,10),round(upper3,10))
    print('spectral_comparison_rho5:',round(lower5,10),round(upper5,10))

if __name__ == '__main__':
    test()
