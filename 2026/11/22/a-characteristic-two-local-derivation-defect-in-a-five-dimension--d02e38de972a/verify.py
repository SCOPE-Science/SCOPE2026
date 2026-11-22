#!/usr/bin/env python3
"""Independent finite linear-algebra checks of a five-dimensional Zinbiel example.
No external dependencies. Run: python3 verify.py
"""
from itertools import product

N = 5
# Zero-based basis indices; integer structure constants, before reduction.
MULT = {
    (0, 0): {3: 1}, (0, 1): {2: 1}, (1, 0): {2: -1},
    (1, 1): {3: 1}, (0, 2): {4: 1}, (1, 2): {3: 1},
}

def c(i, j, k):
    return MULT.get((i, j), {}).get(k, 0)

def multiplied_basis(i, j):
    return [c(i, j, k) for k in range(N)]

def product_int(a, b):
    return [sum(a[i] * b[j] * c(i, j, k)
                for i in range(N) for j in range(N)) for k in range(N)]

def basis(i):
    a = [0] * N
    a[i] = 1
    return a

def derivation_matrix():
    out = []
    for i in range(N):
        for j in range(N):
            for k in range(N):
                row = [0] * (N * N)
                for ell in range(N):
                    row[N * ell + k] += c(i, j, ell)
                for ell in range(N):
                    row[N * i + ell] -= c(ell, j, k)
                    row[N * j + ell] -= c(i, ell, k)
                out.append(row)
    return out

def determinant_exact(a):
    """Fraction-free Bareiss elimination with integer pivoting."""
    a = [r[:] for r in a]
    n = len(a)
    sign, prev = 1, 1
    for k in range(n - 1):
        pivot_row = next((i for i in range(k, n) if a[i][k]), None)
        if pivot_row is None:
            return 0
        if pivot_row != k:
            a[k], a[pivot_row] = a[pivot_row], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numer = a[i][j] * pivot - a[i][k] * a[k][j]
                assert numer % prev == 0
                a[i][j] = numer // prev
            a[i][k] = 0
        prev = pivot
    return sign * a[n - 1][n - 1]

class Field:
    def __init__(self, q):
        assert q in (2, 3, 4, 5)
        self.q = q
    def add(self, a, b):
        return a ^ b if self.q == 4 else (a + b) % self.q
    def neg(self, a):
        return a if self.q == 4 else (-a) % self.q
    def sub(self, a, b):
        return self.add(a, self.neg(b))
    def mul(self, a, b):
        if self.q != 4:
            return a * b % self.q
        r = 0
        for i in range(2):
            for j in range(2):
                if ((a >> i) & 1) and ((b >> j) & 1):
                    r ^= 1 << (i+j)
        # In F4 = F2[t]/(t^2+t+1), t^2 = t + 1.
        if r & 8:
            r ^= 8 ^ 4 ^ 2
        if r & 4:
            r ^= 4 ^ 2 ^ 1
        return r
    def inv(self, a):
        assert a != 0
        return next(b for b in range(1, self.q) if self.mul(a, b) == 1)
    def scalar(self, z):
        if self.q == 4:
            return z & 1
        return z % self.q

def nullspace(rows, fld, cols):
    a = [[fld.scalar(x) for x in r] for r in rows]
    # rows already field elements if q=4; scalar(x) only correct for 0,1 in F4.
    piv = []
    h = 0
    for j in range(cols):
        k = next((i for i in range(h, len(a)) if a[i][j]), None)
        if k is None:
            continue
        a[h], a[k] = a[k], a[h]
        z = fld.inv(a[h][j])
        a[h] = [fld.mul(v, z) for v in a[h]]
        for i in range(len(a)):
            if i != h and a[i][j]:
                f = a[i][j]
                a[i] = [fld.sub(u, fld.mul(f, v)) for u, v in zip(a[i], a[h])]
        piv.append(j)
        h += 1
        if h == len(a):
            break
    free = [j for j in range(cols) if j not in piv]
    ans = []
    for j in free:
        v = [0] * cols
        v[j] = 1
        for k, col in enumerate(piv):
            v[col] = fld.neg(a[k][j])
        ans.append(v)
    return ans

def nullspace_field(rows, fld, cols):
    # For field matrices we must not convert the representation of F4 again.
    a = [r[:] for r in rows]
    piv = []
    h = 0
    for j in range(cols):
        k = next((i for i in range(h, len(a)) if a[i][j]), None)
        if k is None: continue
        a[h], a[k] = a[k], a[h]
        z = fld.inv(a[h][j])
        a[h] = [fld.mul(v, z) for v in a[h]]
        for i in range(len(a)):
            if i != h and a[i][j]:
                f = a[i][j]
                a[i] = [fld.sub(u, fld.mul(f, v)) for u, v in zip(a[i], a[h])]
        piv.append(j)
        h += 1
        if h == len(a): break
    out = []
    for f in range(cols):
        if f not in piv:
            v = [0] * cols;v[f] = 1
            for k,c0 in enumerate(piv):v[c0] = fld.neg(a[k][f])
            out.append(v)
    return out

def local_dimension(M, fld):
    der = nullspace(M, fld, 25)
    constraints = []
    for x in product(range(fld.q), repeat=N):
        if not any(x): continue
        image_rows = []
        for D in der:
            image_rows.append([
                sum_mod(fld, [fld.mul(x[i], D[5*i+k]) for i in range(N)])
                for k in range(N)])
        annih = nullspace_field(image_rows, fld, N)
        for z in annih:
            constraints.append([fld.mul(x[i], z[k]) for i in range(N) for k in range(N)])
    return len(der), 25 - (25 - len(nullspace_field(constraints, fld, 25)))

def sum_mod(fld, items):
    v = 0
    for x in items:v = fld.add(v, x)
    return v

def check():
    E = [basis(i) for i in range(N)]
    # Exact integral Zinbiel identity: (xy)z = x(yz) + x(zy).
    for x,y,z in product(E, repeat=3):
        lhs = product_int(product_int(x,y),z)
        rhs = [u+v for u,v in zip(product_int(x,product_int(y,z)),product_int(x,product_int(z,y)))]
        assert lhs == rhs
    M = derivation_matrix()
    rows21 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,28,29,33,34,38,39]
    cols21 = [0,1,2,5,6,7,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
    rows19 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,28,29,38,39]
    cols19 = [0,1,2,5,6,7,10,11,12,13,14,15,16,17,18,19,20,21,22]
    d21 = determinant_exact([[M[i][j] for j in cols21] for i in rows21])
    d19 = determinant_exact([[M[i][j] for j in cols19] for i in rows19])
    assert (d21,d19) == (-4,-15), (d21,d19)
    for q in (2,3,4,5):
        fld = Field(q)
        d,l = local_dimension(M,fld)
        want = (6,7) if q in (2,4) else (4,4)
        assert (d,l) == want, (q,d,l)
        print('FIELD',q,'DER',d,'LOCAL',l)
    # The explicit extra map P(e1)=e2 fails the Leibniz rule at e1*e2=e3.
    P = [0] * 25
    P[1] = 1
    assert any(sum(M[i][j]*P[j] for j in range(25)) % 2 for i in range(125))
    print('ZINBIEL_LOCAL_MODULAR_OK')

if __name__ == '__main__':check()
