"""Max absolute minor of B_l root normals (for good-prime Hadamard-type bound)."""
import itertools

def normals(l):
    N = []
    for i in range(l):
        v = [0]*l; v[i] = 1; N.append(tuple(v))
    for i in range(l):
        for j in range(i+1, l):
            v = [0]*l; v[i] = 1; v[j] = -1; N.append(tuple(v))
            w = [0]*l; w[i] = 1; w[j] = 1; N.append(tuple(w))
    return N

def det_int(M):
    # Bareiss
    n = len(M); A = [row[:] for row in M]
    prev = 1
    for k in range(n-1):
        if A[k][k] == 0:
            piv = next((i for i in range(k+1, n) if A[i][k] != 0), None)
            if piv is None: return 0
            A[k], A[piv] = A[piv], A[k]
        for i in range(k+1, n):
            for j in range(k+1, n):
                A[i][j] = (A[i][j]*A[k][k] - A[i][k]*A[k][j]) // prev
        prev = A[k][k]
    return A[n-1][n-1]

for l in [3, 4]:
    N = normals(l)
    mx = 0; arg = None
    for r in range(1, l+1):
        for cols in itertools.combinations(range(l), r):
            for rows in itertools.combinations(range(len(N)), r):
                M = [[N[i][j] for j in cols] for i in rows]
                d = abs(det_int(M))
                if d > mx: mx, arg = d, (rows, cols)
    print(f'l={l} n_normals={len(N)} max_minor={mx} e.g. {arg}')
    print(f'  cone-minor bound B(l,k) = (l+1)*k*{mx} = {l+1}*k*{mx}')
