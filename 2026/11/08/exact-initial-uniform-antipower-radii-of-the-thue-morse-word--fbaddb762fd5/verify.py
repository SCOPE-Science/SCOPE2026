#!/usr/bin/env python3
"""Exact finite-prefix checker for the uniform Thue--Morse antipower radii.

Mathematical completeness argument: all factors of length L <= 130 in the
infinite Thue--Morse fixed point occur in the first 2048 symbols, because
L <= 256 and the 256-uniform blocks are mu^8(a).  Every length-L factor
is contained in mu^8(ab) for an adjacent letter pair ab. All four binary
pairs occur in mu^3(0)=01101001; their expansions appear in mu^11(0),
which is exactly the 2048-symbol prefix used here.
"""
RADII = {3: 5, 4: 7, 5: 9, 6: 11, 7: 11, 8: 11, 9: 13, 10: 13}
WITNESSES = {3: 0, 4: 16, 5: 16, 6: 10, 7: 0, 8: 0, 9: 64, 10: 53}
EXPECTED_FACTORS = {3: 44, 4: 86, 5: 144, 6: 196, 7: 240, 8: 284, 9: 360, 10: 388}

def is_antipower(s, k, m):
    return len({s[r*m:(r+1)*m] for r in range(k)}) == k

def main():
    s = ''.join('1' if (j.bit_count() & 1) else '0' for j in range(2048))
    assert s.startswith('01101001')
    for k, radius in RADII.items():
        L = k*radius
        factors = {s[j:j+L] for j in range(len(s)-L+1)}
        assert len(factors) == EXPECTED_FACTORS[k], (k, len(factors))
        assert all(any(is_antipower(f, k, m) for m in range(1, radius+1)) for f in factors), k
        j = WITNESSES[k]
        witness = s[j:j+k*(radius-1)]
        assert len(witness) == k*(radius-1)
        assert not any(is_antipower(witness, k, m) for m in range(1, radius)), (k, j)
        print(f'k={k}: exact radius={radius}, factors={len(factors)}, lower witness start={j}')
    print('VERIFY_OK')

if __name__ == '__main__':main()
