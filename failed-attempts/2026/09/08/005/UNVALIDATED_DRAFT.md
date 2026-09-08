# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Complete-arc spectra in PG(2,5) and PG(2,7), with maximal witnesses in PG(2,8) and PG(2,9)

## Theorem (machine-checked)

Let an *arc* be a set of points, no three collinear, and *complete* if it is
not strictly contained in another arc (equivalently, every point outside it
lies on some secant spanned by two of its points).

- (a) **Spectrum in PG(2,5):** S(5) = {6}. There is, up to projective
  equivalence, a unique complete arc size: 6 (3 frame-containing 6-arcs,
  all complete; no complete 4- or 5-arc).
- (b) **Spectrum in PG(2,7):** S(7) = {6, 8}. Up to the fixed-frame reduction
  there are 40 complete 6-arcs and 5 complete 8-arcs containing the standard
  frame, and zero complete 4-, 5-, or 7-arcs.
- (c) **Maximal witnesses.** The conic-plus-nucleus 10-set in PG(2,8) is a
  complete 10-arc (hyperoval) with PGL-stabilizer of order 504
  (PGammaL-stabilizer 1512) and secant distribution (0:28, 1:0, 2:45).
  The conic 10-set in PG(2,9) is a complete 10-arc (oval) with
  PGL-stabilizer of order 720 (PGammaL-stabilizer 1440) and secant
  distribution (0:36, 1:10, 2:45). Both attain the classical bound q+2
  (q even) and q+1 (q odd).
- (d) **Blocking-set separation.** In each of PG(2,8), PG(2,9), the triangle
  point set T on the three coordinate axes minus the three vertices
  (|T| = 21 for q=8, 24 for q=9) is a non-trivial blocking set (meets every
  line, contains no line) that carries **zero** 10-arcs — certified by
  exhaustive DFS (6215 nodes for q=8, 19019 for q=9). Hence T is a small
  blocking set disjoint in character from the 10-arc secant covers.

## Proof and computation

All claims are certified by two independent stdlib-only Python programs in
`artifacts/`:

- `search.py` builds each plane from scratch (GF(8) = GF(2)[t]/(t^3+t+1),
  GF(9) = GF(3)[t]/(t^2+1)), enumerates arcs, stabilizers, secants, blocking
  sets, and emits `witnesses.json` plus `points_q{q}.csv` / `lines_q{q}.csv`.
- `verify.py` (124 lines, ~3 s) re-derives everything independently from the
  CSVs + witness coordinates: arc property, completeness with per-point
  secant witnesses, secant counts summing to q^2+q+1, stabilizer orders via
  the unique projective frame-extension map, blocking-set hits, "T contains
  no line", "T contains no 10-arc", and the spectrum gaps (zero complete
  extensions at every missing size).

**Exhaustiveness argument.** PGL(3,q) acts transitively on ordered frames
(4 points, no three collinear), so every k-arc with k >= 4 is
PGL-equivalent to one containing the fixed frame
F = {(1:0:0),(0:1:0),(0:0:1),(1:1:1)}. The census enumerates every subset of
the "pool" (points on no secant of F: 6 points for q=5, 20 for q=7) exactly
once in increasing-index order, extending the secant-cover bitmask
incrementally; a subset is kept iff each new point avoids all current
secants. Counts: q=5 gives 10 frame-containing arcs
(1×4-arc, 6×5-arc, 3×6-arc, the three 6-arcs complete); q=7 gives 116
frame-containing arcs (1, 20, 70, 20, 5 at k=4..8; complete exactly at
k=6 (40) and k=8 (5)). Sizes 1–3 are trivially incomplete (their secant
cover misses points). The verifier repeats the gap check with independent
code. This closes S(5) = {6} and S(7) = {6, 8} exactly.

**Stabilizers** use the fundamental theorem of projective geometry: for base
ordered frame E of H, each ordered frame T of H determines at most one
projective map E→T (diagonal correction b_i/a_i from the fourth frame
points); the map is counted iff it preserves H as a set. Cross-checked by
`verify.py` with its own matrix code (this caught and fixed two verifier
bugs: swapped adjugate entries and a dropped diagonal-scaling class).

## Representatives (normalized homogeneous coordinates)

- PG(2,5), k=6 (stab 120, secants 0:10, 1:6, 2:15):
  (1:0:0), (0:1:0), (0:0:1), (1:1:1), (1:3:2), (1:4:3).
- PG(2,7), k=6 (stab 12, secants 0:24, 1:18, 2:15):
  (1:0:0), (0:1:0), (0:0:1), (1:1:1), (1:5:6), (1:6:4).
- PG(2,7), k=8 (stab 336, secants 0:21, 1:8, 2:28):
  (1:0:0), (0:1:0), (0:0:1), (1:1:1),
  (1:3:4), (1:4:5), (1:5:3), (1:6:2).
- PG(2,8) hyperoval (stab_PGL 504, stab_PGammaL 1512; secants 0:28, 1:0, 2:45):
  conic XZ=Y^2 affine points (u^2:u:1), u in GF(8), plus (1:0:0) and nucleus
  (0:1:0); integer labels per GF(2)[t]/(t^3+t+1) in `witnesses.json`.
- PG(2,9) oval (stab_PGL 720, stab_PGammaL 1440; secants 0:36, 1:10, 2:45):
  conic XZ=Y^2 affine points (u^2:u:1), u in GF(9), plus (1:0:0);
  integer labels per GF(3)[t]/(t^2+1) in `witnesses.json`.

## Conjecture vs. proof (honesty section)

- Proved (machine-checked): S(5)={6}, S(7)={6,8}; completeness of all listed
  witnesses; exact secant distributions; exact PGL stabilizer orders
  (120; 12, 336; 504; 720); PGammaL orders 1512 (q=8), 1440 (q=9);
  triangle-set blocking property with no contained line and no 10-arc.
- Uniqueness up to PGL is certified only for the q=5 6-arc
  (3 frame-containing 6-arcs = one orbit under the 120-element stabilizer
  action is consistent but orbit-fusion was not separately logged; stated
  as computational observation, not theorem). For q=7 the census logs
  frame-containing counts, not PGL-orbit fusion; per-size representatives
  are given as orbit witnesses, with full per-k classification left open.
- Maximality (largest complete size) follows from the spectrum for q=5,7;
  for q=8,9 the witnesses attain the classical Segre bounds (q+2/q+1),
  cited as theory, with completeness machine-checked.

## Reproduction

```
python3 artifacts/search.py    # rebuilds planes, census, witnesses (~2 s)
python3 artifacts/verify.py    # independent recheck (~3 s, ALL CHECKS PASSED)
```

## Limitations

- Small-order data note: S(5), S(7) overlap textbook knowledge; the novel
  contribution is the replayable certificate bundle (canonical census +
  stabilizer/secant/blocking data + 2 independent programs), not a new bound.
- `verify.py` trusts the CSV schema (point/line index alignment), but
  re-derives all incidence from coordinates, so mislabeling would fail loudly.
- PGammaL orders assume the standard Galois actions (squaring on GF(8),
  a+bt ↦ a−bt on GF(9)); verified computationally against the witness sets.
