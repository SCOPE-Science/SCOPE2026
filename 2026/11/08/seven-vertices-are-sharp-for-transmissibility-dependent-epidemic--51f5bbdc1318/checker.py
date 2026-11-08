"""Exact finite check for the minimum seven-vertex outbreak-influence reversal.
Run: python3 checker.py; Python 3 standard library only.
All comparisons are rational and all trees through seven vertices are covered.
"""
from fractions import Fraction as F
from itertools import product, combinations
from heapq import heapify, heappop, heappush
from collections import Counter, deque


def prufer_tree(code, n):
    degree = [1] * n
    for x in code:
        degree[x] += 1
    leaves = [i for i in range(n) if degree[i] == 1]
    heapify(leaves)
    edges = []
    for x in code:
        u = heappop(leaves)
        edges.append(tuple(sorted((u, x))))
        degree[u] -= 1
        degree[x] -= 1
        if degree[x] == 1:
            heappush(leaves, x)
    a, b = [i for i in range(n) if degree[i] == 1]
    edges.append(tuple(sorted((a, b))))
    return tuple(sorted(edges))


def adj(edges, n):
    a = [set() for _ in range(n)]
    for u, v in edges:
        a[u].add(v)
        a[v].add(u)
    return a


def rooted_code(a, v, parent=-1):
    return '(' + ''.join(sorted(rooted_code(a, z, v) for z in a[v] if z != parent)) + ')'


def tree_code(a):
    return min(rooted_code(a, v) for v in range(len(a)))


def edge_code(a, u, v):
    x, y = rooted_code(a, u, v), rooted_code(a, v, u)
    return tuple(sorted((x, y)))


def profiles(a):
    n = len(a)
    res = []
    for v in range(n):
        dist = [-1] * n
        dist[v] = 0
        Q = deque([v])
        while Q:
            x = Q.popleft()
            for y in a[x]:
                if dist[y] < 0:
                    dist[y] = dist[x] + 1
                    Q.append(y)
        assert all(d >= 0 for d in dist)
        res.append([sum(d == j for d in dist) for j in range(1, n)])
    return res


def trim(p):
    p = list(p)
    while p and p[-1] == 0:
        p.pop()
    return p


def deriv(p):
    return trim([j * p[j] for j in range(1, len(p))])


def divmod_poly(a, b):
    a, b = trim(map(F, a)), trim(map(F, b))
    assert b
    q = [F(0)] * max(0, len(a)-len(b)+1)
    while len(a) >= len(b):
        d = len(a) - len(b)
        c = a[-1]/b[-1]
        q[d] += c
        for j, z in enumerate(b):
            a[d+j] -= c*z
        a = trim(a)
    return trim(q), a


def root_count(poly):
    p = trim(poly)
    if len(p) <= 1:
        return 0
    a, b = list(map(F,p)), list(map(F,deriv(p)))
    while b:
        _, rem = divmod_poly(a,b)
        a,b = b,rem
    squarefree,rem = divmod_poly(p,a)
    assert not rem
    s = [squarefree, deriv(squarefree)]
    while s[-1]:
        _, rem = divmod_poly(s[-2],s[-1])
        if not rem:
            break
        s.append([-v for v in rem])
    def side_sign(coef, right):
        c = list(coef)
        for k in range(len(coef)):
            val = sum(c) if right else c[0]
            if val:
                if right and k%2:
                    val = -val
                return 1 if val > 0 else -1
            c = deriv(c)
        raise AssertionError('zero polynomial in Sturm sequence')
    def variations(right):
        signs = [side_sign(z, right) for z in s]
        return sum(signs[i] != signs[i+1] for i in range(len(signs)-1))
    out = variations(False) - variations(True)
    assert out >= 0, (p, s, out)
    return out


def q_diff(profile_u, profile_v):
    # E_u-E_v = p(1-p)Q(p). Polynomial coefficients in increasing order.
    d = [x-y for x,y in zip(profile_u,profile_v)]
    q = []
    cur = 0
    for x in d:
        cur += x
        q.append(cur)
    assert cur == 0, d  # same total other-vertex count
    return trim(q)


def value_q(q,p):
    return sum(F(z)*p**j for j,z in enumerate(q))


def direct_diff(edges, n, u, v, p):
    out = []
    for root in (u,v):
        expected = F(0)
        for bits in product((0,1), repeat=len(edges)):
            aa = [set() for _ in range(n)]
            for bit,(x,y) in zip(bits,edges):
                if bit:
                    aa[x].add(y);aa[y].add(x)
            seen = {root}; queue = [root]
            for x in queue:
                for y in aa[x]:
                    if y not in seen:
                        seen.add(y);queue.append(y)
            expected += len(seen) * p**sum(bits) * (1-p)**(len(edges)-sum(bits))
        out.append(expected)
    return out[0]-out[1]


def main():
    tree_counts=[]
    witnesses=[]
    for n in range(2,8):
        trees={}
        total=0
        for seq in product(range(n),repeat=n-2):
            edges=prufer_tree(seq,n)
            a=adj(edges,n)
            code=tree_code(a)
            trees.setdefault(code,edges)
            total+=1
        assert total == n**(n-2)
        tree_counts.append((n,len(trees),total))
        for shape,edges in trees.items():
            a=adj(edges,n)
            ps=profiles(a)
            for u,v in combinations(range(n),2):
                q=q_diff(ps[u],ps[v])
                crossings=root_count(q)
                if crossings:
                    assert n == 7
                    assert crossings == 1
                    assert v in a[u]
                    witnesses.append({'shape':shape,'pair_code':edge_code(a,u,v),'edges':edges,'u':u,'v':v,'q':q})
    assert [x[1] for x in tree_counts] == [1,1,2,3,6,11]
    assert len(witnesses) == 3, witnesses
    classes={(w['shape'],w['pair_code']) for w in witnesses}
    assert len(classes)==2, classes
    differences=Counter(tuple(w['q']) for w in witnesses)
    assert set(differences)=={(1,-2),(-1,2),(1,-1,-1)}, differences
    for w in witnesses:
        for p in [F(1,4),F(3,4)]:
            expected = p*(1-p)*value_q(w['q'],p)
            independent = direct_diff(w['edges'],7,w['u'],w['v'],p)
            assert expected==independent,(w,p,expected,independent)
        assert (value_q(w['q'],F(1,4))*value_q(w['q'],F(3,4)))<0
    print('EXACT_CHECK_PASS')
    print('tree_counts[n,nonisomorphic,labeled]',tree_counts)
    print('reversal_pairs_representatives',len(witnesses))
    print('tree_and_unordered_vertex_pair_isomorphism_classes',len(classes))
    for w in witnesses:
        print('WITNESS', 'edges=',w['edges'],'pair=',(w['u'],w['v']),'Q_coefficients=',w['q'],'edge_orbit=',w['pair_code'])

if __name__ == '__main__':
    main()
