"""Finite checks for local triangle incidence and removable-subgraph barriers.

Run with Python 3.10+; no third-party dependencies.
"""
from itertools import combinations


def graph(vertices, edges):
    a = [0] * vertices
    for i, j in edges:
        assert 0 <= i < vertices and 0 <= j < vertices and i != j
        a[i] |= 1 << j
        a[j] |= 1 << i
    return a


def icosahedron():
    # 0,11 are poles, the two pentagonal rings are 1..5 and 6..10.
    e = set()
    def add(i, j): e.add(tuple(sorted((i,j))))
    for i in range(5):
        j = (i + 1) % 5
        add(0, 1+i)
        add(11, 6+i)
        add(1+i, 1+j)
        add(6+i, 6+j)
        add(1+i, 6+i)
        add(1+j, 6+i)
    return graph(12, e)


def triangular_torus(m):
    assert m >= 6
    def p(x, y): return (x % m) * m + (y % m)
    e = set()
    for x in range(m):
        for y in range(m):
            for a,b in ((1,0),(0,1),(1,-1)):
                e.add(tuple(sorted((p(x,y),p(x+a,y+b)))))
    return graph(m*m, e)


def removable(subset, a):
    bits = sum(1 << v for v in subset)
    for v in subset:
        nbr = a[v] & bits
        d = nbr.bit_count()
        if d <= 1:
            return True
        if d == 2:
            w = [u for u in subset if nbr & (1 << u)]
            if (a[w[0]] >> w[1]) & 1:
                return True
    return False


def psi(a, k):
    checked = 0
    for size in range(1, k+1):
        for ss in combinations(range(len(a)), size):
            checked += 1
            if not removable(ss, a):
                return False, size, ss, checked
    return True, None, None, checked


def phi0(a):
    n=len(a)
    degrees = [u.bit_count() for u in a]
    if min(degrees) < 3:
        return False, ('degree', degrees)
    for i in range(n):
        for j in range(i+1,n):
            if (a[i] >> j) & 1 and (a[i] & a[j]).bit_count() != 2:
                return False, ('edge', i, j, (a[i]&a[j]).bit_count())
    return True, None


def no_clique4_or_induced_cycles4_5(a, check_five=True):
    n=len(a)
    def adjacent(x,y): return (a[x] >> y) & 1
    for ss in combinations(range(n), 4):
        e=sum(adjacent(u,v) for u,v in combinations(ss,2))
        if e == 6 or (e == 4 and all((a[v] & sum(1<<w for w in ss)).bit_count() == 2 for v in ss)):
            return False, ('K4/C4',ss)
    if not check_five:
        return True, None
    # Search induced 5-cycles through vertex 0; graph constructions are vertex transitive.
    origin=0
    def dfs(path):
        if len(path)==5:
            vset=path
            edges=sum(adjacent(u,v) for u,v in combinations(vset,2))
            if adjacent(path[-1], origin) and edges == 5:
                return path
            return None
        last=path[-1]
        for v in range(n):
            if v not in path and adjacent(last,v):
                result=dfs(path+[v])
                if result:
                    return result
        return None
    result=dfs([origin])
    return result is None, result


def check():
    I = icosahedron()
    T = triangular_torus(6)
    assert len(I)==12 and sum(x.bit_count() for x in I)//2==30
    assert len(T)==36 and sum(x.bit_count() for x in T)//2==108
    for name,a,d in [('icosahedron',I,5),('triangular_torus',T,6)]:
        assert set(x.bit_count() for x in a)=={d},name
        assert phi0(a)==(True,None),(name,phi0(a))
        five=(name == 'triangular_torus')
        assert no_clique4_or_induced_cycles4_5(a, five)[0],(name,no_clique4_or_induced_cycles4_5(a, five))
        for v in range(len(a)):
            nbr=[w for w in range(len(a)) if (a[v]>>w)&1]
            assert all((a[w]&a[v]).bit_count()==2 for w in nbr),name
    ok,size,witness,checked=psi(I,4)
    assert ok and checked==793,('icosa ψ4',ok,checked)
    ok,size,witness,checked=psi(I,5)
    assert not ok and size==5,('icosa ψ5',ok,size,witness)
    ok,size,witness,checked=psi(T,5)
    assert ok,('torus ψ5',size,witness)
    # Each toroidal vertex has an induced six-cycle in its open neighborhood.
    nset=[w for w in range(len(T)) if (T[0]>>w)&1]
    assert len(nset)==6
    assert not removable(nset,T)
    assert sum(T[w].bit_count() for w in range(len(T)))//2==3*len(T)
    print('ALL_FAREY_BOUNDARY_CHECKS_OK')
    print('icosahedral_vertices=12 edges=30 psi4_subsets=793')
    print('toroidal_vertices=36 edges=108 psi5_subsets=',checked)

if __name__=='__main__': check()
