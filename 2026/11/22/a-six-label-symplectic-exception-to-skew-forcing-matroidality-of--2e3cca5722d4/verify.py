"""Standalone checks for skew forcing on triangular graphs; Python 3 standard library."""
from itertools import combinations


def edges(n):
    return list(combinations(range(n), 2))


def graph(n):
    es = edges(n)
    return es, [sum(1 << j for j, f in enumerate(es) if i != j and (e[0] in f or e[1] in f)) for i, e in enumerate(es)]


def closure(neighborhoods, blue):
    allv = (1 << len(neighborhoods)) - 1
    while True:
        extra = 0
        for neighbors in neighborhoods:
            white = neighbors & (allv ^ blue)
            if white and white & (white - 1) == 0:
                extra |= white
        new = blue | extra
        if new == blue:
            return new
        blue = new


def rank(vectors):
    basis = {}
    for v in vectors:
        while v:
            b = v.bit_length() - 1
            if b in basis:
                v ^= basis[b]
            else:
                basis[b] = v
                break
    return len(basis)


def pg_rank(es, mask):
    return rank([(1 << a) | (1 << b) for i, (a, b) in enumerate(es) if mask >> i & 1] + [63]) - 1


def witness(n, W, x, y):
    es, neighbors = graph(n)
    mask = lambda Q: sum(1 << es.index(tuple(sorted(e))) for e in Q)
    white = mask(W)
    blue = ((1 << len(es)) - 1) ^ white
    outcomes = [closure(neighbors, blue | mask(Q)) for Q in [[], [x], [y]]]
    allv = (1 << len(es)) - 1
    assert allv ^ outcomes[0] == white
    assert outcomes[1] >> es.index(tuple(sorted(y))) & 1
    assert not (outcomes[2] >> es.index(tuple(sorted(x))) & 1)
    return [ [es[i] for i in range(len(es)) if ((allv ^ c) >> i) & 1] for c in outcomes ]


def run():
    for n in [3, 4, 6]:
        es, nb = graph(n)
        size = len(es)
        assert size <= 15
        closures = [closure(nb, S) for S in range(1 << size)]
        if n == 3:
            expected = lambda S: (1 << size) - 1 if S else 0
        elif n == 4:
            # The dual of a rank-two partition matroid with the three disjoint 2-element classes.
            # More straightforward: the three neighborhoods, each the complement of a perfect-matching pair.
            parts = [sum(1 << i for i,e in enumerate(es) if frozenset(e) in [frozenset(p) for p in P]) for P in [[(0,1),(2,3)], [(0,2),(1,3)], [(0,3),(1,2)]]]
            circuits = [((1 << size)-1) ^ part for part in parts]
            def expected(S):
                while True:
                    nextS = S
                    for C in circuits:
                        missing = C & ~S
                        if missing and missing & (missing - 1) == 0:
                            nextS |= missing
                    if nextS == S:return S
                    S = nextS
        else:
            # Independent dual-rank computation, not a forcing simulation:
            # r_{PG(3,2)^*}(S)=|S|-4+r_{PG(3,2)}(E\\S).
            whole=(1 << size)-1
            rp = [pg_rank(es, S) for S in range(1 << size)]
            assert rp[whole] == 4
            def expected(S):
                dualr=S.bit_count()-4+rp[whole ^ S]
                return S | sum(1 << i for i in range(size) if not(S>>i&1) and (S | (1 << i)).bit_count()-4+rp[whole ^ (S|(1<<i))] == dualr)
        for S in range(1 << size):
            if closures[S] != expected(S):
                raise AssertionError((n,S,closures[S],expected(S)))
        print(f'POSITIVE n={n} vertices={size} subsets={1<<size} closure_equal_matroid=PASS')
    W5=[(0,4),(1,4),(2,3),(2,4),(3,4)]
    W7=[(0,1),(0,2),(1,2),(3,4),(5,6)]
    print('EXCHANGE n=5 white-after [base, x, y]',witness(5,W5,(2,4),(0,4)))
    print('EXCHANGE n=7 white-after [base, x, y]',witness(7,W7,(0,1),(3,4)))
    for n in range(8,15):
        W=[(0,1)]+[(0,j) for j in (2,3,4)]+[(1,j) for j in range(5,n)]
        out=witness(n,W,(0,2),(0,1))
        assert out[1] == [] and (0,2) in out[2]
    print('DOUBLE_STAR_EXCHANGE n=8..14 PASS')
    print('VERIFY_OK')

if __name__=='__main__':
    run()
