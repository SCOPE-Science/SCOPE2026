"""Exact rational checks for two grounded leaders in a diamond bouquet.

The finite checks corroborate but do not replace the all-m analytical proof.
Run: python verify.py (Python 3.9+; standard library only).
"""
from fractions import Fraction as Q
from itertools import combinations


def prediction(m, leaders):
    assert m >= 1 and len(leaders) == 2
    a, b = sorted(leaders)
    assert a != b and 0 <= a < 3*m+1 and 0 <= b < 3*m+1
    # Vertex 0 is the common hub. Each consecutive module is end,centre,end.
    if a == 0:
        return Q(7*m-3, 4), 'hub and outer'
    module_a, pos_a = divmod(a-1, 3)
    module_b, pos_b = divmod(b-1, 3)
    ca, cb = (pos_a == 1), (pos_b == 1)
    if module_a == module_b:
        if ca or cb:
            return Q(59*m-39, 20), 'same module end-centre'
        return Q(23*m-17, 8), 'same module end-end'
    if ca and cb:
        return Q(5*m-5, 2), 'different modules centre-centre'
    if ca or cb:
        return Q(93*m-89, 36), 'different modules end-centre'
    return Q(43*m-39, 16), 'different modules end-end'


def graph_laplacian(m):
    n = 3*m+1
    lap = [[0]*n for _ in range(n)]
    for t in range(m):
        a, b, c = 3*t+1, 3*t+2, 3*t+3
        for u,v in [(0,a),(0,b),(0,c),(a,b),(b,c)]:
            lap[u][u] += 1
            lap[v][v] += 1
            lap[u][v] -= 1
            lap[v][u] -= 1
    return lap


def trace_inverse(matrix):
    n = len(matrix)
    A = [[Q(v) for v in row]+[Q(i == j) for j in range(n)]
         for i, row in enumerate(matrix)]
    for c in range(n):
        pivot = next((r for r in range(c, n) if A[r][c]), None)
        assert pivot is not None, 'not invertible'
        A[c], A[pivot] = A[pivot], A[c]
        factor = A[c][c]
        A[c] = [v/factor for v in A[c]]
        for r in range(n):
            if r == c or not A[r][c]:
                continue
            factor = A[r][c]
            A[r] = [x-factor*y for x,y in zip(A[r], A[c])]
    return sum(A[i][n+i] for i in range(n))


def direct(m, leaders, lap=None):
    if lap is None:
        lap = graph_laplacian(m)
    keep = [j for j in range(3*m+1) if j not in leaders]
    return trace_inverse([[lap[i][j] for j in keep] for i in keep])


def block_values(m):
    """Independent Schur-complement evaluation via module summary triples.

    The hub-leader calculation uses individual diagonal blocks, whereas
    all other cases use the scalar Schur complement of the hub.
    """
    intact = (Q(7,4), Q(3), Q(3))  # trace A^-1, 1'A^-1 1, 1'A^-2 1
    removed_end = (Q(1), Q(7,5), Q(1))
    removed_centre = (Q(1), Q(1), Q(1,2))
    removed_two_end = (Q(1,3), Q(1,3), Q(1,9))
    removed_end_centre = (Q(1,2), Q(1,2), Q(1,4))
    def join(parts):
        s = 3*m - sum(x[1] for x in parts)
        assert s > 0
        return sum(x[0] for x in parts)+(1+sum(x[2] for x in parts))/s
    scores = {
        'same module end-end': join([intact]*(m-1)+[removed_two_end]),
        'same module end-centre': join([intact]*(m-1)+[removed_end_centre]),
        'hub and outer': (m-1)*intact[0]+1,
    }
    if m >= 2:
        scores.update({
            'different modules end-end': join([intact]*(m-2)+[removed_end]*2),
            'different modules end-centre': join([intact]*(m-2)+[removed_end,removed_centre]),
            'different modules centre-centre': join([intact]*(m-2)+[removed_centre]*2),
        })
    return scores


def optimal_set(m):
    if m == 1:
        return {(1,3)}, Q(3,4)
    if m == 2:
        return {(2,5)}, Q(5,2)
    return {(0,v) for v in range(1,3*m+1)}, Q(7*m-3,4)


def main():
    validations=0
    for m in range(1,26):
        all_leaders=list(combinations(range(3*m+1),2)) if m<=7 else [
            (0,1),(0,2),(1,2),(1,3),(1,4),(1,5),(2,5)]
        lap=graph_laplacian(m) if m<=7 else None
        block=block_values(m)
        winner, optimum=optimal_set(m)
        observed=set()
        for leader_set in all_leaders:
            value,cl=prediction(m,leader_set)
            assert value == block[cl], (m,leader_set,value,block[cl])
            assert value >= optimum,(m,leader_set,value,optimum)
            if value == optimum:
                observed.add(leader_set)
            if m<=7 or (m<=13 and leader_set in [(0,1),(1,3),(2,5)]):
                d=direct(m,leader_set,lap)
                assert d==value,(m,leader_set,d,value)
            validations += 1
        if m<=7:
            assert observed==winner,(m,observed,winner)
        else:
            assert observed=={x for x in winner if x in all_leaders}
    # General comparison gaps reduce to these positive affine forms.
    for m in range(2,301):
        b=block_values(m)
        cc=b['different modules centre-centre']
        for cl in ['different modules end-end','different modules end-centre',
                   'same module end-end','same module end-centre']:
            assert b[cl]>cc,(m,cl)
        if m==2:
            assert cc<b['hub and outer']
        if m>=3:
            assert b['hub and outer']<cc
        validations+=5
    print('VERIFY_OK',validations,'exact objective/class and sign checks')


if __name__=='__main__':
    main()
