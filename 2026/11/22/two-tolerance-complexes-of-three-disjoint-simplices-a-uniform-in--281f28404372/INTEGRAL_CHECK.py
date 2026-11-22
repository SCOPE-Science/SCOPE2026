"""Optional exact integer Smith test; requires SymPy >= 1.12.

Reconstructs two complete signed integer boundary complexes. This is a
finite integrity check, not a proof of the infinite-family theorem.
"""
from sympy import zeros
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ


def face_complex(block_sizes):
    blocks = []
    start = 0
    for n in block_sizes:
        blocks.append(((1 << n) - 1) << start)
        start += n
    faces = {}
    for mask in range(1, 1 << start):
        if min((mask & ~block).bit_count() for block in blocks) <= 2:
            faces.setdefault(mask.bit_count() - 1, []).append(mask)
    return faces


def signed_boundary(lower, upper):
    low = {mask: r for r, mask in enumerate(lower)}
    M = zeros(len(lower), len(upper))
    for c, mask in enumerate(upper):
        selected = [i for i in range(mask.bit_length()) if mask & (1 << i)]
        for j, i in enumerate(selected):
            M[low[mask ^ (1 << i)], c] = 1 if j % 2 == 0 else -1
    return M


def check(sizes, ranks):
    by = face_complex(sizes)
    nmax = max(by)
    observed = []
    for d in range(1, nmax + 1):
        S = smith_normal_form(signed_boundary(by[d-1], by[d]), domain=ZZ)
        entries = [int(abs(S[i, i])) for i in range(min(S.rows, S.cols)) if S[i, i] != 0]
        assert all(x == 1 for x in entries), (sizes, d, 'nonunit Smith invariant')
        observed.append(len(entries))
    assert tuple(observed) == ranks, (sizes, observed, ranks)
    print('PASS', sizes, 'fvector', tuple(len(by[d]) for d in range(nmax+1)),
          'Smith ranks', tuple(observed), 'all nonzero invariant factors 1')


if __name__ == '__main__':
    check((2, 3, 3), (7, 21, 35, 19))
    check((3, 3, 3), (8, 28, 56, 42))
    print('ALL OPTIONAL INTEGER SMITH CHECKS PASS (finite only).')
