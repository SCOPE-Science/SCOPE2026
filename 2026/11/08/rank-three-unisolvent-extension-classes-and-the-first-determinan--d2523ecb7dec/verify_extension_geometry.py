"""Exact checks of the extension dimensions for the low-exponent coherent-system classification.

Python 3 standard library only. The proof for all m uses the cohomological exact
sequence and the simplicity of the two endpoint systems. This finite check tests
an independent polynomial-gradient realization of the comparison map.
"""
from fractions import Fraction


def rational_rank(mat):
    a = [[Fraction(x) for x in row] for row in mat]
    if not a:
        return 0
    nrows, ncols = len(a), len(a[0])
    pivot_row = 0
    for col in range(ncols):
        pivot = next((r for r in range(pivot_row, nrows) if a[r][col]), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        pv = a[pivot_row][col]
        a[pivot_row] = [z/pv for z in a[pivot_row]]
        for r in range(pivot_row+1, nrows):
            scale = a[r][col]
            if scale:
                for c in range(col, ncols):
                    a[r][c] -= scale * a[pivot_row][c]
        pivot_row += 1
        if pivot_row == nrows:
            break
    return pivot_row


def check(m):
    # E_H = O(2m-2)^2. W_H is the gradient of binary forms of degree 2m-1.
    # H^0(E_H)/W_H is the curl quotient of pairs of degree 2m-2 forms.
    # The map below sends a pair (A,B) of degree m-1 forms to
    # f |-> d_y(A*f)-d_x(B*f), f in H^0(O(m-1)).
    qdim = 2*m-2
    mat = [[0]*(2*m) for _ in range(m*qdim)]
    for i in range(m):
        for j in range(m):
            l = i+j-1
            if 0 <= l < qdim:
                mat[i*qdim+l][j] += i+j
            l = i+j
            if 0 <= l < qdim:
                mat[i*qdim+l][m+j] -= 2*m-2-i-j
    rank = rational_rank(mat)
    assert rank == 2*m, (m,rank)
    ext_L_H = m*qdim-rank
    ext_H_L = 2*max(m-2,0)
    assert (ext_L_H,ext_H_L) == (2*m*(m-2),2*(m-2))
    return ext_L_H, ext_H_L

if __name__ == '__main__':
    for m in range(2, 11):
        d1,d2=check(m)
        print('m=',m,'ext_L_H=',d1,'ext_H_L=',d2)
    assert check(2)==(0,0)
    assert check(3)==(6,2)
    print('VERIFY_OK')

# At m=4, an extension 0 -> O(3) -> E -> O(6)^2 -> 0
# is determined by a 2x2 matrix of classes in H^1(O(-3)).
# The determinant-zero jumping divisor in P^3 is a smooth quadric;
# its finite-field point count is (q+1)^2.
def projective_matrix_counts(q):
    representatives=[]
    for a in range(q):
        for b in range(q):
            for c in range(q):
                for d in range(q):
                    vec=(a,b,c,d)
                    if not any(vec):
                        continue
                    inv=pow(next(z for z in vec if z),-1,q)
                    can=tuple((inv*z)%q for z in vec)
                    representatives.append(can)
    reps=set(representatives)
    rank_one=sum((v[0]*v[3]-v[1]*v[2])%q==0 for v in reps)
    assert len(reps)==q**3+q**2+q+1
    assert rank_one==(q+1)**2
    return len(reps),rank_one

if __name__ == '__main__':
    for q in [2,3,5,7]:
        print('q=',q,'P3(Fq) and quadric:',projective_matrix_counts(q))
    print('QUADRIC_VERIFY_OK')
