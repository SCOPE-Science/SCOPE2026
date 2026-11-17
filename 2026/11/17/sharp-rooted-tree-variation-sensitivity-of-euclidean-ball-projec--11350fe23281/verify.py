"""Independent finite diagnostics for the rooted-tree BV norm of Euclidean ball projection.

The all-tree and all-input conclusion is proved analytically in RESULT.md.
No finite computation substitutes for that proof.
"""
from itertools import product
from math import sqrt
from fractions import Fraction


def rooted(prufer, n):
    # Decode labelled tree; orient every edge away from fixed root 0.
    degree = [1] * n
    for t in prufer:
        degree[t] += 1
    edges = []
    for t in prufer:
        leaf = next(i for i in range(n) if degree[i] == 1)
        edges.append((leaf, t))
        degree[leaf] -= 1
        degree[t] -= 1
    u, v = [i for i in range(n) if degree[i] == 1]
    edges.append((u, v))
    neighbors = [[] for _ in range(n)]
    for u, v in edges:
        neighbors[u].append(v)
        neighbors[v].append(u)
    parent = [-1] * n
    depth = [0] * n
    queue = [0]
    for v in queue:
        for w in neighbors[v]:
            if w == parent[v]:
                continue
            parent[w] = v
            depth[w] = depth[v] + 1
            queue.append(w)
    assert len(queue) == n
    return parent, depth


def check_tree(parent, depth, exhaustive):
    n = len(parent)
    children = [[] for _ in range(n)]
    for v in range(1, n):
        children[parent[v]].append(v)
    S = sum((1 + len(ch)) ** 2 for ch in children)
    alt = [1 if d % 2 == 0 else -1 for d in depth]
    def dual_square(s):
        return sum((s[v] - sum(s[w] for w in children[v])) ** 2
                   for v in range(n))
    assert dual_square(alt) == S
    if exhaustive:
        assert max(dual_square(signs) for signs in product((-1,1), repeat=n)) == S
    # Test D^{-1} e_v = the descendant indicator for each vertex v.
    for v in range(n):
        descendants = [0] * n
        for w in range(n):
            p = w
            while p != -1:
                if p == v:
                    descendants[w] = 1
                    break
                p = parent[p]
        diff = [descendants[0]] + [descendants[w] - descendants[parent[w]]
                                    for w in range(1, n)]
        assert diff == [int(w == v) for w in range(n)]
    return S


count = 0
for n in range(2, 7):
    for prufer in product(range(n), repeat=n - 2):
        p, depth = rooted(prufer, n)
        S = check_tree(p, depth, exhaustive=True)
        assert 4*n - 3 <= S <= n*n + n - 1
        count += 1
print('ALL_LABELLED_TREES_TO_N6_SIGN_AND_SUBTREE_CERTIFICATES_PASS', count)

for n in range(2, 71):
    path = [-1] + [j - 1 for j in range(1, n)]
    star = [-1] + [0] * (n - 1)
    pd = list(range(n));sd = [0] + [1]*(n-1)
    Sp = check_tree(path, pd, exhaustive=False)
    Ss = check_tree(star, sd, exhaustive=False)
    assert Sp == 4*n-3
    assert Ss == n*n+n-1
print('PATH_STAR_EXACT_ALL_N2_TO_N70_PASS')

# Independently test the sharp tangent witness and near-boundary finite pairs.
def norm(a, parent):
    return abs(a[0]) + sum(abs(a[v] - a[parent[v]]) for v in range(1, len(a)))

def dot(a,b):
    return sum(x*y for x,y in zip(a,b))

def euclid(a):
    return sqrt(dot(a,a))

def proj(a,R):
    scale = min(1.0, R / euclid(a)) if euclid(a) else 1.0
    return [scale*x for x in a]

for parent in [[-1,0],[-1,0,1,2],[-1,0,0,0],[-1,0,1,1,0,4],[-1,0,0,2,2,4,4,4]]:
    n = len(parent)
    depth = [0] * n
    for v in range(1,n):
        depth[v] = depth[parent[v]] + 1
    signs = [1 if d%2==0 else -1 for d in depth]
    children = [[] for _ in range(n)]
    for v in range(1,n):children[parent[v]].append(v)
    a = [signs[v]-sum(signs[w] for w in children[v]) for v in range(n)]
    h = [1.0]*n
    A = [v/euclid(a) for v in a]
    H = [v/euclid(h) for v in h]
    u = [x-y for x,y in zip(A,H)]
    u = [x/euclid(u) for x in u]
    tangent = [h[v]-dot(u,h)*u[v] for v in range(n)]
    C = (1+sqrt(n*sum((1+len(ch))**2 for ch in children)))/2
    assert abs(norm(tangent,parent)-C) < 1e-10
    R = 1.7
    eps = 1e-6
    x = [(R+1e-5)*v for v in u]
    y = [x[v]+eps*h[v] for v in range(n)]
    ratio = norm([b-a for a,b in zip(proj(x,R),proj(y,R))],parent)/norm([eps*v for v in h],parent)
    assert 0 < C-ratio < 1e-3, (n, C,ratio)
print('TANGENT_SPECTRAL_EXTREMIZER_AND_FINITE_PAIR_APPROACH_PASS')
print('ALL_ROOTED_TREE_RADIAL_BV_DIAGNOSTICS_PASS')
