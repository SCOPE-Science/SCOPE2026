"""Exact finite verification of F-congruences of cyclic flat-semilattice action monoids.
Only Python standard library. Exhaustive closure under the multiplication and maximum map.
"""
from collections import deque
from itertools import product, permutations


def monoid(m):
    """C_m acting regularly on m atoms, with 0=0 and top=m+1."""
    E = tuple(range(m + 2))
    S = tuple(product(E, range(m)))
    loc = {x: i for i, x in enumerate(S)}
    top = m + 1

    def meet(a, b):
        if a == top:
            return b
        if b == top:
            return a
        if a == b:
            return a
        return 0

    def act(g, a):
        return a if a == 0 or a == top else ((a - 1 + g) % m + 1)

    mult = tuple(tuple(loc[(meet(e, act(g, f)), (g + h) % m)]
                       for f, h in S) for e, g in S)
    maximum = tuple(loc[(top, g)] for _, g in S)
    return S, mult, maximum


def canonical(parents):
    idx = {}
    return tuple(idx.setdefault(x, len(idx)) for x in parents)


def generated_closure(base, pair, mult, maximum):
    """Least equivalence preserving multiplication and maximum containing base and pair.
    This computes a least F-congruence by repeatedly imposing every operation.
    """
    n = len(base)
    parent = list(range(n))

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    def join(a, b):
        a, b = find(a), find(b)
        if a == b:
            return False
        parent[max(a, b)] = min(a, b)
        return True

    for i in range(n):
        for j in range(i):
            if base[i] == base[j]:
                join(i, j)
    join(*pair)
    while True:
        changed = False
        for i in range(n):
            for j in range(i):
                if find(i) != find(j):
                    continue
                changed |= join(maximum[i], maximum[j])
                for z in range(n):
                    changed |= join(mult[i][z], mult[j][z])
                    changed |= join(mult[z][i], mult[z][j])
        if not changed:
            break
    return canonical(tuple(find(i) for i in range(n)))


def enumerate_F_congruences(m):
    S, mult, maximum = monoid(m)
    n = len(S)
    identity = tuple(range(n))
    seen = {identity}
    queue = deque([identity])
    while queue:
        current = queue.popleft()
        for i in range(n):
            for j in range(i):
                if current[i] == current[j]:
                    continue
                new = generated_closure(current, (i, j), mult, maximum)
                if new not in seen:
                    seen.add(new)
                    queue.append(new)
    return S, seen


def predicted_F_congruences(m):
    S, _, _ = monoid(m)
    T = m + 1
    answer = set()
    for theta in ("identity", "collapsed_atoms", "universal"):
        for step in range(1, m+1):
            if m % step:
                continue
            if theta == "identity" and step != m:
                continue
            classes = []
            for e, g in S:
                tag = e if theta == "identity" else (0 if e != T else 1) if theta == "collapsed_atoms" else 0
                classes.append((tag, g % step))
            answer.add(canonical(classes))
    return answer



def permutation_action_example():
    """C2 swaps two of three atoms and fixes the third: a nontransitive check."""
    m=3
    top=m+1
    S=tuple(product(range(m+2), range(2)))
    loc={s:i for i,s in enumerate(S)}
    def act(g,e):
        return ({1:2,2:1}.get(e,e) if g else e)
    def meet(a,b):
        return b if a==top else a if b==top else a if a==b else 0
    table=tuple(tuple(loc[(meet(e,act(g,f)),(g+h)%2)] for f,h in S) for e,g in S)
    maximum=tuple(loc[(top,g)] for e,g in S)
    identity=tuple(range(len(S)))
    seen={identity}
    queue=deque([identity])
    while queue:
        cur=queue.popleft()
        for i in range(len(S)):
            for j in range(i):
                if cur[i]==cur[j]:continue
                part=generated_closure(cur,(i,j),table,maximum)
                if part not in seen:
                    seen.add(part);queue.append(part)
    # The invariant subsets are {}, {1,2}, {3}, {1,2,3}.
    # With theta_U, only normal subgroups contained in the pointwise
    # kernel on the noncollapsed atoms may be used.
    classified=set()
    for U in (set(),{1,2},{3},{1,2,3}):
        for step in (1,2):
            if step==1 and not {1,2}.issubset(U):continue
            classes=[((0 if e==0 or e in U else e),g%step) for e,g in S]
            classified.add(canonical(classes))
    # The only fixed atom is 3, so there is one additional top+atom
    # partition, and the universal idempotent partition: both admit N<=C2.
    for kind in ('fixed3_top','universal'):
        for step in (1,2):
            classes=[((0 if kind=='universal' else 1 if e in (top,3) else 0),g%step) for e,g in S]
            classified.add(canonical(classes))
    assert seen==classified,(len(seen),len(classified),seen-classified,classified-seen)
    assert len(seen)==10
    return len(S),len(seen)


def direct_all_congruences_on_two_atoms():
    """Independently scan all 4,140 set partitions of the eight-element example."""
    S, mult, maximum=monoid(2)
    n=len(S)
    a=[0]*n
    counts=[0,0,0]
    def rec(i, high):
        if i==n:
            counts[0]+=1
            for x in range(n):
                for y in range(x):
                    if a[x]!=a[y]:continue
                    for z in range(n):
                        if a[mult[x][z]]!=a[mult[y][z]] or a[mult[z][x]]!=a[mult[z][y]]:
                            return
            counts[1]+=1
            if all(a[maximum[x]]==a[maximum[y]] for x in range(n) for y in range(x) if a[x]==a[y]):
                counts[2]+=1
            return
        for j in range(high+2):
            a[i]=j
            rec(i+1,max(high,j))
    rec(1,0)
    assert counts==[4140,7,5], counts
    return counts


def symmetric_three_action_example():
    """Independent closure enumeration for the nonabelian faithful S3 action."""
    group=tuple(permutations(range(3)))
    index={g:i for i,g in enumerate(group)}
    ident=(0,1,2)
    invcount=lambda g: sum(g[i]>g[j] for i in range(3) for j in range(i+1,3))
    sign={g:(invcount(g)%2) for g in group}
    S=tuple(product(range(5),group))
    loc={s:i for i,s in enumerate(S)}
    def meet(e,f):
        return f if e==4 else e if f==4 else e if e==f else 0
    def act(g,e):return e if e in (0,4) else g[e-1]+1
    def comp(g,h):return tuple(g[h[i]] for i in range(3))
    table=tuple(tuple(loc[(meet(e,act(g,f)),comp(g,h))] for f,h in S) for e,g in S)
    maximum=tuple(loc[(4,g)] for e,g in S)
    identity=tuple(range(len(S)))
    seen={identity};queue=deque([identity])
    while queue:
        cur=queue.popleft()
        for i in range(len(S)):
            for j in range(i):
                if cur[i]==cur[j]:continue
                part=generated_closure(cur,(i,j),table,maximum)
                if part not in seen:
                    seen.add(part);queue.append(part)
    predicted={identity}
    for theta in ('collapsed_atoms','universal'):
        for N in ('identity','A3','S3'):
            data=[]
            for e,g in S:
                ec=0 if theta=='universal' else 1 if e==4 else 0
                gc=index[g] if N=='identity' else sign[g] if N=='A3' else 0
                data.append((ec,gc))
            predicted.add(canonical(data))
    assert seen==predicted,(len(seen),len(predicted),seen-predicted,predicted-seen)
    assert len(seen)==7
    return len(S),len(seen)

def verify():
    expected = {2: 5, 3: 5, 4: 7}
    for m in expected:
        S, actual = enumerate_F_congruences(m)
        predicted = predicted_F_congruences(m)
        assert actual == predicted, (m, len(actual), len(predicted), actual-predicted, predicted-actual)
        assert len(actual) == expected[m], (m, len(actual))
        print('m=%d, elements=%d, F_congruences=%d, all_generators_checked=%d, exact_lattice_match=True' % (m, len(S), len(actual), len(S)*(len(S)-1)//2))
    print('m=2 direct Bell-partition scan (partitions, ordinary_congruences, F_congruences)=%s' % (direct_all_congruences_on_two_atoms(),))
    n,k=permutation_action_example()
    print('nontransitive C2-action, elements=%d, F_congruences=%d, exact_lattice_match=True' % (n,k))
    n,k=symmetric_three_action_example()
    print('faithful nonabelian S3-action, elements=%d, F_congruences=%d, exact_lattice_match=True' % (n,k))
    print('FLAT_SEMIDIRECT_F_CONGRUENCES_OK')


if __name__ == '__main__':
    verify()
