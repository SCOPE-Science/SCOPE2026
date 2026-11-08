#!/usr/bin/env python3
"""Independent bit-matrix checks of a dyadic-ladder reversible wave theorem.
Only Python standard library required. Run: python3 check_matrix.py
"""

def identity(n):
    return [1 << i for i in range(n)]

def product(a, b):
    return [xor_selected(row, b) for row in a]

def xor_selected(mask, rows):
    v = 0
    while mask:
        bit = mask & -mask
        v ^= rows[bit.bit_length()-1]
        mask ^= bit
    return v

def rank(rows, n):
    basis = {}
    for row in rows:
        while row:
            k = row.bit_length()-1
            if k in basis:
                row ^= basis[k]
            else:
                basis[k] = row
                break
    return len(basis)

def xor_matrices(a, b):
    return [x ^ y for x, y in zip(a, b)]

def ladder(n):
    v = 2*n
    a = [0]*v
    for i in range(n):
        for leg in range(2):
            pos = 2*i+leg
            neigh = [2*i+1-leg]
            if i: neigh.append(2*(i-1)+leg)
            if i+1 < n: neigh.append(2*(i+1)+leg)
            a[pos] = sum(1 << j for j in neigh)
    return a

def two_row(a):
    v = len(a)
    return [row | (1 << (v+i)) for i, row in enumerate(a)] + [1 << i for i in range(v)]

def expected_dim(n, t):
    if t % 3: return 0
    h = t & -t
    return 2*(min(n+1,h)+min(n-1,h))

def check(n):
    v = 2*n
    a=ladder(n)
    k=xor_matrices(a, identity(v))
    power=identity(v)
    for j in range(n+2):
        predicted=max(0,n+1-j)+max(0,n-1-j)
        actual=rank(power,v)
        assert actual==predicted, ('K Jordan',n,j,actual,predicted)
        power=product(power,k)
    assert power==[0]*v
    t=two_row(a)
    p=identity(2*v)
    order=3*(n+1)
    for j in range(1,order+1):
        p=product(p,t)
        actual=2*v-rank(xor_matrices(p,identity(2*v)),2*v)
        predicted=expected_dim(n,j)
        assert actual==predicted, ('wave fixed dim',n,j,actual,predicted)
        if j<order: assert p!=identity(2*v), ('order',n,j)
    assert p==identity(2*v)
    print(f'n={n} wave_dimension={2*v} exact_order={order} gf2_fixed_dimensions=verified_for_t_1_through_{order}')

if __name__=='__main__':
    for r in (2,3,4,5):
        check(2**r-1)
    print('CHECK_MATRIX_PASS')
