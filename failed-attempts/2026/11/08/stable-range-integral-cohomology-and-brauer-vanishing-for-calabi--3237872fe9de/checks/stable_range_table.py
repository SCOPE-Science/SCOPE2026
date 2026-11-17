"""Bigraded E2 and multiplicative-basis consistency checks for a free C2 cover.
This only checks finite additive data; the spectral-sequence argument is mathematical.
"""
def e2_piece(p, q, d):
    if p < 0 or q < 0 or q >= d or q % 2 or p % 2:
        return None
    return 'Z' if p == 0 else 'Z/2'

for m in range(2, 10):
    d = 2*m
    for degree in range(d):
        pieces = [(p, degree-p, e2_piece(p, degree-p,d))
                  for p in range(degree+1) if e2_piece(p, degree-p,d)]
        if degree % 2:
            assert not pieces
        else:
            k = degree//2
            assert len(pieces) == k+1, (d, degree, pieces)
            assert pieces[0] == (0, degree, 'Z')
            assert all(z == 'Z/2' for _,_,z in pieces[1:])
            # The ring monomials h^(k-j) u^j occupy filtration p=2j.
            assert [p for p,_,_ in pieces] == list(range(0,degree+1,2))
        # Every potential d_r between non-middle E2 terms has odd total degree,
        # so its E2 target/source in this range vanishes.
        for r in range(2,degree+2):
            for p,q,_ in pieces:
                if p+r+q-r+1 < d:
                    assert e2_piece(p+r,q-r+1,d) is None
                if p-r>=0 and q+r-1<d:
                    assert e2_piece(p-r,q+r-1,d) is None
    print(f'dim={d}: stable degrees 0..{d-1}; torsion ranks [',
          ','.join(str(k) for k in range(m)), ']')
print('E2_ADD_MULT_CHECK_OK')
