#!/usr/bin/env python3
"""Exact modular recurrence and independent generating-series checks (stdlib)."""
OFFSETS = {0: 7, 1: 16, 2: 9, 3: 6, 4: 6, 5: 7}
EXCEPTIONS = {3: 11, 4: 10, 5: 12, 6: 13, 7: 24,
              8: 17, 9: 15, 10: 16, 11: 18, 12: 19, 13: 35}

def residues(k, size):
    # Independent linear-time sliding evaluation of the order-k recurrence.
    vals = [0, 1]
    tail_sum = 0
    for n in range(2, size + 1):
        tail_sum += vals[n - 2]
        if n - k - 1 >= 0:
            tail_sum -= vals[n - k - 1]
        vals.append((2 * vals[-1] + tail_sum) % 8)
    return vals

def first3(vals):
    return next((i for i in range(1, len(vals)) if vals[i] == 3), None)

def gf_coefficients(size):
    # Formal series A(z)=z(1-z)/B(z) and E(z)=z(1-z)/B(z)^2,
    # B(z)=1-3z+z^2, calculated using convolution.
    inverse = [1, 3]
    for n in range(2, size + 1):
        inverse.append((3 * inverse[-1] - inverse[-2]) % 8)
    aa = [0] + [(inverse[t-1] - (inverse[t-2] if t >= 2 else 0)) % 8
                for t in range(1, size + 1)]
    ee = [sum(aa[j] * inverse[t-j] for j in range(t+1)) % 8
          for t in range(size + 1)]
    return aa, ee

def check():
    aa, ee = gf_coefficients(25)
    assert aa[1:7] == [1, 2, 5, 5, 2, 1]
    assert ee[:16] == [0, 1, 5, 3, 1, 2, 6, 1, 7, 1, 1, 4, 4, 1, 1, 7]
    rows = []
    for r in range(6):
        row = [(aa[(r+s-1)%6+1] - ee[s-1])%8 for s in range(1,17)]
        rows.append(row)
        assert row.index(3)+1 == OFFSETS[r]
    for k in range(2, 2001):
        n = (k+17) if k >= 14 else (40 if k >= 3 else 200)
        vals = residues(k, n)
        expected = (k + OFFSETS[k%6] if k >=14 else EXCEPTIONS.get(k))
        if k == 2:
            assert vals[0:9] == [0,1,2,5,4,5,6,1,0]
            assert first3(vals) is None
        else:
            assert first3(vals) == expected, (k, expected, first3(vals))
        if k >=14:
            for s in range(1,17):
                assert vals[k+s] == rows[k%6][s-1], (k,s)
    print('PASS: 1999 recurrence instances k=2..2000; six symbolic coefficient rows; all eleven finite exceptional k cases')

if __name__ == '__main__':
    check()
