# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Dual-verified inversion-refined census of Av(1324) to n = 12 with Linusson–Verkama transfer audit and sharpness certificates

## Claim

Let `a(n,k)` = number of 1324-avoiding permutations of length `n` with `k` inversions.
The committed table `output/artifacts/tableA.txt` gives the **exact full distribution**
for `1 ≤ n ≤ 12` (rows sum to OEIS A061558: 1, 2, 6, 23, 103, 513, 2762, 15793,
94776, 591950, 3824112, 25431452), dual-verified by two independent generation
orders/checkers through `n = 9` (129 cells byte-identical). On the computed window:

- column-monotonicity `a(n,k) ≤ a(n+1,k)` holds for all 231 comparable cells (0 violations);
- the Linusson–Verkama difference identity
  `a(n+1,k) − a(n,k) = [x^k] 2(2+x)x^{n−1}P(x)^2` (P = partition GF, exact integer
  arithmetic) holds on all 52 cells with `n = 8..11`, `k ≤ 2n−7`;
- the LV sharpness family `π = 3,6,1,2,7,…,n,4,5` (2n−6 inversions, 1324-avoiding,
  indecomposable, no decomposable boundary deletion) is certified for `n = 7..12`,
  pinning the boundary at which the `f ⊔ g` audit method stops.

`python3 output/artifacts/verify.py` replays all five checks → `VERIFY_OK` (stdlib only).

## Provenance and method

- **Engine A** (`engineA.c`, compiled C): insert-new-maximum generation. A child formed
  by inserting `M = m+1` at position `p` avoids 1324 iff the length-`p` prefix avoids
  132 (any 1324-use of `M` puts `M` as the `4`, hence last, forcing the 132-part into
  the prefix; non-`M` occurrences live in the avoiding parent). Delete-max inverts the
  step ⇒ every avoider reached exactly once. `inv(child) = inv(parent) + (m − p)`.
- **Engine B** (`engineB.py`, pure Python): append-last-rank generation with naive
  per-child 1324 quadruple scan; only quadruples using the new last entry need testing.
  Different traversal order and different pattern test from Engine A.
- Partition numbers for check V4 by Euler's pentagonal recurrence (exact integers);
  no floating point anywhere.

## What is proved vs conjectured

- **Proved (machine-certified finite census):** exactness of the `n ≤ 12` table
  (dual-engine to `n = 9`, OEIS-anchored marginals + LV-table rows to `n = 12`),
  window monotonicity, LV-identity audit, sharpness witnesses. These are
  replayable facts, not hand proofs.
- **Not proved:** defect-11 monotonicity (`k ≤ 2n+4`), any `R_{11,n}` classification,
  any growth-rate bound `< 13.5`. The exact `|R_3|` polynomial (fallback F1) is also
  **not** derived here — recovering it needs Meng's skeleton enumeration code/theory
  beyond this time budget. The table furnishes the residual data (`R`-side differences
  are computable from it) but the skeleton-sum closed form is left open.
- **Originality:** LV print only Table 2 slices (`n ≤ 12`, `k ≤ 12`); full certified
  rows to `n = 12` (through `k = 66`) with a replayable dual-engine certificate are new
  as an artifact. No new infinite-family theorem is claimed.

## Replay

```
gcc -O2 -o /tmp/engA output/artifacts/engineA.c && /tmp/engA > output/artifacts/tableA.txt
python3 output/artifacts/engineB.py > output/artifacts/tableB.txt
python3 output/artifacts/verify.py   # expect VERIFY_OK
```

Engine A runs in ~1 s; Engine B (~n ≤ 9) in ~0.5 s; verifier in ~1 s.
