"""Finite corroboration for proper three-colorings on cycles.
Run: python check_cycle.py. Requires Python 3 standard library only.
The all-order conclusions in RESULT.md follow from proofs, not these tests.
"""
from itertools import product
from functools import lru_cache

PALETTE = (0, 1, 2)


def colorings(n):
    assert n >= 3
    return [c for c in product(PALETTE, repeat=n)
            if all(c[i] != c[(i+1) % n] for i in range(n))]


def expected(n):
    return n - (n+3)//4, n-1


def test_vc_exhaustive(n, colors):
    # A shattered query set contains at most one literal per vertex.
    # Options 0,1,2 mean testing that color, 3 means no query.
    best = -1
    for selections in product(range(4), repeat=n):
        queries = [(i,a) for i,a in enumerate(selections) if a != 3]
        if len(queries) < best:
            continue
        traces = {sum((c[i] == a) << bit for bit,(i,a) in enumerate(queries))
                  for c in colors}
        if len(traces) == (1 << len(queries)):
            best = max(best, len(queries))
    return best


def test_ld_exact(n, colors):
    column = [sum((int(c[i] == a) << j) for j,c in enumerate(colors))
              for i in range(n) for a in PALETTE]
    @lru_cache(None)
    def dim(mask):
        if mask & (mask-1) == 0:
            return 0
        answer = 0
        for test in column:
            yes, no = mask & test, mask & ~test
            if yes and no:
                answer = max(answer, 1+min(dim(yes), dim(no)))
        return answer
    return dim((1 << len(colors))-1)


def prescribed_support(n):
    # Cyclic blocks of 1110, possibly followed by 0 / 10 / 110.
    sel=[]
    for start in range(0, 4*(n//4), 4):
        sel.extend([(start, 0), (start+1, 1), (start+2, 0)])
    residual = n % 4
    last = 4*(n//4)
    if residual >= 2: sel.append((last,0))
    if residual >= 3: sel.append((last+1,1))
    assert len(sel) == n-(n+3)//4
    return sel


def test_constructive_vc(n, colors):
    sel = prescribed_support(n)
    traces={sum((c[i]==a)<<j for j,(i,a) in enumerate(sel)) for c in colors}
    assert len(traces)==(1 << len(sel)), (n,len(traces),len(sel))


def realize_branch(n, bits):
    # A depth-(n-1) complete tree, with adaptive vertex-color queries.
    assert len(bits)==n-1
    c=[None]*n
    q=[(0,0)]
    c[0] = 0 if bits[0] else 1
    for i in range(1,n-1):
        allowed=[x for x in PALETTE if x!=c[i-1]]
        selected=allowed[0]
        q.append((i,selected))
        c[i]=selected if bits[i] else allowed[1]
    c[n-1]=next(x for x in PALETTE if x!=c[n-2] and x!=c[0])
    assert all(c[i]!=c[(i+1)%n] for i in range(n))
    assert all(int(c[i]==a)==bit for (i,a),bit in zip(q,bits))
    return tuple(c)


def test_constructive_online(n, colors):
    family=set(colors)
    witnesses=[]
    for bits in product((0,1),repeat=n-1):
        candidate=realize_branch(n,bits)
        assert candidate in family
        witnesses.append(candidate)
    assert len(set(witnesses)) == 2**(n-1)


def main():
    for n in range(3,9):
        colors=colorings(n)
        assert len(colors)==2**n+2*(-1)**n
        for i in range(n):
            for a in PALETTE:
                assert sum(c[i]==a for c in colors)==len(colors)//3
        test_constructive_vc(n, colors)
        test_constructive_online(n, colors)
        actual_vc=test_vc_exhaustive(n, colors)
        assert actual_vc==expected(n)[0], (n, actual_vc)
        if n<=7:
            actual_ld=test_ld_exact(n, colors)
            assert actual_ld==expected(n)[1], (n,actual_ld)
            print(f'C{n} concepts={len(colors)} VC_exact={actual_vc} Ldim_exact={actual_ld} constructive_tree_leaves={1<<(n-1)}')
        else:
            print(f'C{n} concepts={len(colors)} VC_exact={actual_vc} Ldim_from_proof={n-1} constructive_tree_leaves={1<<(n-1)}')
    for n in range(9,11):
        colors=colorings(n)
        test_constructive_vc(n,colors)
        test_constructive_online(n,colors)
        print(f'C{n} concepts={len(colors)} constructive_VC_support_size={expected(n)[0]} online_leaves={1<<(n-1)}')
    print('ALL_CYCLE_3_COLORING_SHATTERING_CHECKS_PASS')

if __name__ == '__main__': main()
