"""Finite exact certificate for the intersection pairing of an Abrams deleted product.
Run with Python 3.9 or later. Only the standard library is used.
"""
from itertools import combinations
from collections import Counter, defaultdict

LABELS = tuple(range(7))
CELLS = {k: [] for k in range(5)}
for a in range(1, 4):
    for A in combinations(LABELS, a):
        remain = tuple(v for v in LABELS if v not in A)
        for b in range(1, 4):
            for B in combinations(remain, b):
                CELLS[a+b-2].append((A, B))
for k in CELLS:
    CELLS[k].sort()
INDEX = {k: {cell: i for i, cell in enumerate(CELLS[k])} for k in CELLS}


def faces(cell):
    A, B = cell
    if len(A) > 1:
        for i in range(len(A)):
            yield (A[:i]+A[i+1:], B), (-1)**i
    if len(B) > 1:
        for i in range(len(B)):
            yield (A, B[:i]+B[i+1:]), (-1)**(len(A)-1+i)


def insert_reduced(v, pivots):
    """Binary row echelon: least-significant pivot, with only higher columns."""
    while v:
        k = (v & -v).bit_length()-1
        if k in pivots:
            v ^= pivots[k]
        else:
            pivots[k] = v
            return True
    return False


def rank(vectors):
    pivots = {}
    for v in vectors:
        insert_reduced(v, pivots)
    return len(pivots)


def cochain_differential(k):
    """Columns, represented as binary bit sets; delta: C^k -> C^(k+1)."""
    out = [0]*len(CELLS[k])
    for row, cell in enumerate(CELLS[k+1]):
        for face, _ in faces(cell):
            out[INDEX[k][face]] ^= 1<<row
    return out


def kernel_basis(columns, nrows):
    """Solve sum_j x_j columns[j]=0 exactly over F_2."""
    pivots = {}
    associated = {}
    answer = []
    for j, col in enumerate(columns):
        coeff = 1<<j
        while col:
            p = (col & -col).bit_length()-1
            if p in pivots:
                col ^= pivots[p]
                coeff ^= associated[p]
            else:
                pivots[p] = col
                associated[p] = coeff
                break
        else:
            answer.append(coeff)
    return answer, len(pivots)


def permutation_sign(seq):
    return (-1)**sum(a>b for i,a in enumerate(seq) for b in seq[i+1:])


def orientation(cell):
    A,B = cell
    remaining = tuple(v for v in LABELS if v not in A and v not in B)
    assert len(remaining) == 1
    return permutation_sign(A+B+remaining)


def relabel(cell, perm):
    A,B=cell
    AA=[perm[i] for i in A]
    BB=[perm[i] for i in B]
    local=permutation_sign([AA.index(x) for x in sorted(AA)])
    local*=permutation_sign([BB.index(x) for x in sorted(BB)])
    return (tuple(sorted(AA)),tuple(sorted(BB))),local


def cup_evaluation(alpha, beta, tops):
    """AW-diagonal on both simplex factors, evaluated on fundamental 4-cycle mod 2."""
    answer=0
    for A,B in tops:
        for i in (0,1,2):
            j=2-i
            left=(A[:i+1],B[:j+1])
            right=(A[i:],B[j:])
            a,b=INDEX[2][left],INDEX[2][right]
            answer ^= ((alpha>>a)&1)&((beta>>b)&1)
    return answer


def main():
    counts=tuple(len(CELLS[k]) for k in range(5))
    assert counts == (42,210,490,420,140)
    assert sum((-1)**i*counts[i] for i in range(5)) == 42
    differentials = [cochain_differential(k) for k in range(4)]
    for k in range(1, 4):
        for c in differentials[k-1]:
            image=0
            while c:
                bit=c&-c; c-=bit
                image ^= differentials[k][bit.bit_length()-1]
            assert image==0, 'differential squared nonzero'
    rk=[rank(cols) for cols in differentials]
    assert rk == [41,169,281,139], rk
    betti=[counts[i]-(rk[i-1] if i>0 else 0)-(rk[i] if i<4 else 0) for i in range(5)]
    assert betti == [1,0,40,0,1], betti

    topboundary=defaultdict(int)
    for cell in CELLS[4]:
        for f, s in faces(cell):
            topboundary[f] += orientation(cell)*s
    assert len(topboundary)==420 and all(v==0 for v in topboundary.values())
    transposition = (1,0,2,3,4,5,6)
    assert all(orientation(relabel(cell, transposition)[0])*relabel(cell, transposition)[1]
               == -orientation(cell) for cell in CELLS[4])

    cocycles,rk2=kernel_basis(differentials[2],len(CELLS[3]))
    assert rk2==281 and len(cocycles)==209
    # Checking all solutions by reduction is exact and independent of the listed Betti numbers.
    for x in cocycles:
        z=0
        while x:
            bit=x&-x; x-=bit
            z ^= differentials[2][bit.bit_length()-1]
        assert z==0

    # The cup square is linear on cocycles when evaluated on an integral top cycle mod two.
    sq=[cup_evaluation(x,x,CELLS[4]) for x in cocycles]
    assert not any(sq), 'nonzero cup square: intersection lattice could be odd'

    # Quotient Cocycles / coboundaries, an independent nondegeneracy check.
    pivots={}
    for delta in differentials[1]:
        insert_reduced(delta,pivots)
    assert len(pivots)==169
    cohomology=[]
    for x in cocycles:
        if insert_reduced(x,pivots):
            cohomology.append(x)
    assert len(cohomology)==40 and len(pivots)==209
    pairrows=[]
    for a in cohomology:
        pairrows.append(sum(cup_evaluation(a,b,CELLS[4])<<j for j,b in enumerate(cohomology)))
    assert rank(pairrows)==40
    assert all(cup_evaluation(a,b,CELLS[4])==cup_evaluation(b,a,CELLS[4])
               for a in cohomology for b in cohomology)
    assert all(cup_evaluation(a,a,CELLS[4])==0 for a in cohomology)
    print('face_counts:',counts)
    print('boundary_ranks_F2:',rk)
    print('mod2_Betti_numbers:',betti)
    print('oriented_top_cycle_140_facets: VALID')
    print('vertex_transposition_orientation_degree: -1')
    print('C2_cocycle_basis_dimension:',len(cocycles))
    print('mod2_cup_squares_nonzero:',sum(sq))
    print('H2_dimension:',len(cohomology))
    print('mod2_intersection_pairing_rank:',rank(pairrows))
    print('mod2_intersection_alternating: YES')
    print('ALL CHECKS PASSED')

if __name__=='__main__':main()
