# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Replayable Tutte Census and Fano-Minor Extremals for a Committed 3-Connected Binary Slice on 7–9 Elements

## 1. Committed objects

Work over GF(2) with ground sets $\{0,\dots,n-1\}$. The committed slice consists of nine
matroids given by the explicit matrices below (columns = elements). All are simple,
binary, and 3-connected (machine-checked, §3).

- **M1_F7** (Fano, $n=7$, $r=3$):
  `[1000111; 0101011; 0011101]`
- **M2_F7s** (dual-Fano, $n=7$, $r=4$):
  `[0111000; 1010100; 1100010; 1110001]`
- **M3_AG32** ($n=8$, $r=4$): `[I_4 | 1111; 1110; 1101; 1011]`
- **M4_S8** ($n=8$, $r=4$): `[I_4 | 0111; 1011; 1101; 1110]`
- **M5_X8a** ($n=8$, $r=4$): `[I_4 | 1011; 1101; 1100; 1110]`
- **M6_X8b** ($n=8$, $r=4$): `[I_4 | 1111; 1110; 1101; 1010]` (new variant; pairwise
  non-isomorphic to M3/M4/M5 by exhaustive $S_8$ basis-image check)
- **M7_MK33** (graphic $M(K_{3,3})$, $n=9$, $r=5$): incidence rows above
- **M8_AG32e** ($n=9$, $r=4$): M3 plus column $[0,1,1,0]^T$
- **M9_S8e** ($n=9$, $r=4$): M4 plus column $[1,1,1,1]^T$

Reference minors: F7 = M1_F7; F7\* = M2_F7s (28 bases each).

## 2. Theorems (machine-verified; replay with `python3 output/artifacts/verify.py`)

**Theorem A (dual-recomputed Tutte table).** For each of the nine matroids, the Tutte
polynomial computed by memoized deletion–contraction equals the polynomial computed by
the independent rank-oracle subset expansion; in each case $T(1,1)$ equals the
enumerated basis count and $T(2,2)=2^n$. Basis counts:
M1: 28, M2: 28, M3: 48, M4: 56, M5: 48, M6: 45, M7: 81, M8: 80, M9: 88.

**Theorem B (Fano verdicts with explicit witnesses).**
Presence/absence of F7 and F7\* minors, each presence by an explicit
(delete $D$, contract $C$, remain $R$, relabelling $\pi$) replayed against reference
bases, each absence by exhaustive replay over all $(D,C)$ with $|R|=7$:

| matroid | has F7 | has F7\* |
|---|---|---|
| M1_F7 | yes ($D=C=\varnothing$) | no |
| M2_F7s | no | yes ($D=C=\varnothing$) |
| M3_AG32 | yes | yes |
| M4_S8 | yes | yes |
| M5_X8a | yes | yes |
| M6_X8b | no | no |
| M7_MK33 | no | no |
| M8_AG32e | yes | yes |
| M9_S8e | yes ($D=\{0\},C=\{4\}$) | yes ($D=\{0,8\},C=\varnothing$) |

**Theorem C (extremals).**
(a) The largest maximal Tutte coefficient over the slice is **18**, attained uniquely
(in the slice) by **M9_S8e** at $x^1y^1$. Its Tutte coefficients $(i,j\mapsto c)$:
$(0,1){:}7$, $(0,2){:}14$, $(0,3){:}10$, $(0,4){:}4$, $(0,5){:}1$, $(1,0){:}7$,
$(1,1){:}18$, $(1,2){:}6$, $(2,0){:}11$, $(2,1){:}4$, $(3,0){:}5$, $(4,0){:}1$.
(b) The F7- and F7\*-free members are exactly {M6_X8b, M7_MK33}; the one with the most
bases is **M7_MK33 with 81 bases** (max coefficient 15 at $x^1y^1$).

## 3. Certificates and reproduction

- `output/artifacts/census.py` — builds the table with dual Tutte computation and the
  minor search; asserts agreement, $T(1,1)=\#\text{bases}$, $T(2,2)=2^n$, and
  3-connectivity (Tutte separation inequality for $k=1,2$ over all bipartitions).
- `output/artifacts/tutte_table.json` — full coefficient lists, basis counts, verdicts,
  witnesses, extremal pointers.
- `output/artifacts/verify.py` — independent replay from stored matrices only; prints
  `VERIFY_OK` (confirmed). No third-party packages; seconds-to-minutes runtime.

## 4. Scope, originality, and limits

- The slice is **committed, not exhaustive**: claims are "over this 9-member committed
  slice", not over all 3-connected binary matroids on 7–9 elements. No isomorphism
  completeness is claimed (indeed M3/M5 share a Tutte polynomial and are isomorphic).
- Separation from SCOPE026 (simple rank-3 on 8 elements, $T(2,0)$ extremal): different
  objects (binary, connectivity-filtered, multi-rank, three sizes), full polynomials with
  dual replay, F7/F7\* witnesses, and different extremals (max coefficient; most bases
  among Fano-free).
- Conjecture/uncertainty: none inside the verified table; any heuristic reading
  (e.g., unimodality) is interpretation, not claimed.
