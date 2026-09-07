#!/usr/bin/env python3
"""Independent verifier for lane-08 degree-28 Littlewood witness.

Recomputes from scratch (trusts only the bitstring):
 1. Parses witness bitstring, checks a0=+1, length 29, reciprocal-canonical
    (numeric lex-min with -1<+1 over the {P,-P,P*,-P*} orbit representatives
    having constant term +1), and skew-symmetry.
 2. Exact integer autocorrelations C_k and merit F = 841/124 as Fraction.
 3. Exact integer lower bound |P(i)|^2 = 45 -> M >= sqrt(45).
 4. FFT dense-grid max at N (default 262144) + Lipschitz remainder L*pi/N
    (L=406, proved in DRAFT.md) + 1e-6 float margin -> rigorous M upper bound.
 5. Exact exhaustive merit scan of the skew-symmetric subspace (2^14 with
    a0=+1) in Python integers -> confirms 841/124 is the subspace maximum.
 6. 1-flip local-optimality check of sup grid around witness (optional, fast).

Usage: python3 verify.py --degree 28 [--grid 262144] [--full-skew] [--no-skew]
Replayable in <5 min on a laptop CPU (numpy only; integers for exact part).
"""
import argparse
import math
import sys
from fractions import Fraction

try:
    import numpy as np
except ImportError:
    print("numpy required", file=sys.stderr)
    sys.exit(2)

WITNESS = "+---++++---+---+---+--+-++-++"
N_DEFAULT = 262144
L_LIP = sum(range(29))  # 406
FLOAT_MARGIN = 1e-6


def parse_bits(s):
    s = s.strip().replace(" ", "").replace("\n", "")
    assert len(s) == 29, f"length {len(s)} != 29"
    c = [1 if ch == "+" else (-1 if ch == "-" else None) for ch in s]
    assert all(v is not None for v in c), "alphabet must be +,-"
    assert c[0] == 1, "a0 must be +1"
    return c


def autocorrs(c):
    n = len(c)
    out = []
    for k in range(1, n):
        out.append(sum(c[i] * c[i + k] for i in range(n - k)))
    return out


def grid_max(c, N):
    a = np.array(c, dtype=float)
    F = np.fft.fft(a, n=N)
    return float(np.max(np.abs(F)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--degree", type=int, default=28)
    ap.add_argument("--grid", type=int, default=N_DEFAULT)
    ap.add_argument("--no-skew", action="store_true",
                    help="skip exhaustive skew merit scan")
    args = ap.parse_args()
    assert args.degree == 28, "this verifier covers degree 28 only"
    N = args.grid

    c = parse_bits(WITNESS)
    print(f"witness: {WITNESS}")
    print(f"length {len(c)}, a0=+{c[0]}")

    # 1. reciprocal-canonical: orbit reps with constant term +1 are c and cr
    cr = c[::-1]
    if cr[0] == -1:
        cr = [-x for x in cr]
    # numeric lex compare on (a1..a28) with -1<+1
    def key(v):
        return tuple(v[1:])
    assert c[0] == 1 and cr[0] == 1
    is_canon = key(c) <= key(cr)
    print(f"reciprocal: {''.join('+' if x == 1 else '-' for x in (c[::-1]))}")
    print(f"canonical (numeric lex-min, -1<+1): {is_canon}")
    assert is_canon, "witness must be canonical representative"

    # skew-symmetry check
    skew = all(c[14 + k] == ((1 if k % 2 == 0 else -1) * c[14 - k])
               for k in range(1, 15))
    print(f"skew-symmetric: {skew}")
    assert skew

    # 2. exact merit
    cks = autocorrs(c)
    sumsq = sum(x * x for x in cks)
    F = Fraction(29 * 29, 2 * sumsq)
    print(f"C_k: {cks}")
    print(f"sumsq: {sumsq}")
    print(f"merit: {F} = {float(F):.12f}")
    assert sumsq == 62, f"sumsq {sumsq} != 62"
    assert F == Fraction(841, 124), f"merit {F} != 841/124"

    # 3. exact lower bound at z=i
    A = sum(c[2 * j] * ((-1) ** j) for j in range(15) if 2 * j < 29)
    B = sum(c[2 * j + 1] * ((-1) ** j) for j in range(14) if 2 * j + 1 < 29)
    print(f"P(i) = {A} + {B}i, |P(i)|^2 = {A*A+B*B}")
    assert A * A + B * B == 45
    m_low = math.sqrt(45)
    print(f"lower bound M >= sqrt(45) = {m_low:.12f}")

    # 4. grid upper bound
    g = grid_max(c, N)
    rem = L_LIP * math.pi / N
    upper = g + rem + FLOAT_MARGIN
    print(f"grid N={N}: max = {g:.12f}")
    print(f"Lipschitz L={L_LIP}, remainder L*pi/N = {rem:.9f}")
    print(f"upper bound M <= {upper:.9f} (incl. {FLOAT_MARGIN} float margin)")
    assert g >= m_low - 1e-6, "grid max must nearly attain lower bound"
    assert upper < m_low + 0.02, "certificate must beat 0.02 remainder class"
    print(f"CERTIFIED INTERVAL: sqrt(45) <= M <= {upper:.6f}")

    # 5. exhaustive skew-subspace merit maximum (exact integers)
    if not args.no_skew:
        best_num = -1
        best_list = []
        count = 0
        for mask in range(2 ** 14):
            cc = [0] * 29
            cc[0] = 1
            for i in range(1, 15):
                cc[i] = 1 if (mask >> (i - 1)) & 1 else -1
            for k in range(1, 15):
                cc[14 + k] = (1 if k % 2 == 0 else -1) * cc[14 - k]
            ss = sum(sum(cc[i] * cc[i + k] for i in range(29 - k)) ** 2
                     for k in range(1, 29))
            # merit = 841/(2 ss); maximizing merit = minimizing ss
            if best_num == -1 or ss < best_num:
                best_num = ss
                best_list = [mask]
            elif ss == best_num:
                best_list.append(mask)
            count += 1
        print(f"skew scan: {count} sequences, min sumsq = {best_num}, "
              f"max merit = {Fraction(841, 2*best_num)}")
        print(f"num attainers: {len(best_list)}, e.g. masks {best_list[:8]}")
        assert count == 16384
        assert best_num == 62, "subspace max merit must be 841/124"
        assert Fraction(841, 2 * best_num) == F
        print("SUBSPACE MAX-MERIT CONFIRMED: 841/124")
    else:
        print("(skew scan skipped)")

    # 6. 1-flip sup local optimality (grid N=8192, fast)
    g8 = grid_max(c, 8192)
    local_opt = True
    for j in range(1, 29):
        cc = list(c)
        cc[j] *= -1
        if grid_max(cc, 8192) < g8 - 1e-9:
            local_opt = False
            print(f"1-flip improvement at {j}")
            break
    print(f"1-flip sup-grid locally optimal (N=8192): {local_opt}")
    assert local_opt

    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    main()
