# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Of the listed quasi-minimal size-7 candidates, the hollow ones are ten, all of width two

## Abstract
Let **H7** be the set of GL(3,Z)-equivalence classes of hollow lattice
3-polytopes (zero interior lattice points) with exactly 7 lattice points.
We work strictly inside the Blanco–Santos boxed/spiked/merged taxonomy and
make **no claim about the full maximum W7\*** over H7, which remains open
(it is 2 or 3, bounded above by the published overall size-7 maximum 3).
What we determine, with full negative evidence replayed, is the hollow
subset of the two quasi-minimal candidate lists at size 7:
of the **23 listed boxed candidates** (`list_boxed.tex` Size-7 section,
re-parsed byte-identically; see `output/artifacts/candidates.json`),
exactly **8** are hollow, all of lattice width exactly 2, while the other
**15** each have exactly 1 interior lattice point (and width 2);
of the **32 minimal-size-7 spiked instantiations** generated from the
parameters of Theorems spiked-minimals / spiked-quasiminimals cases
(1)–(10b), exactly **2** are hollow, both of width exactly 2, while the
other **30** are non-hollow.
The 10 hollow classes are pairwise inequivalent (all 45 exhaustive
unimodular-congruence searches rerun and stored in
`output/artifacts/inequivalence.log`, all False).
Everything is certified by a self-contained stdlib-only verifier
(`output/artifacts/verify.py` over `candidates.json`,
`certs_boxed_all.json`, `certs_spiked_all.json`) that replays all 23+32
candidates including negatives, re-asserts the totals, and recomputes its
own rigorous adjugate-box width bounds rather than trusting stored ones.

## 1. Background and scope
Blanco–Santos classified width > 1 lattice 3-polytopes of size 6
(74 of width 2, 2 of width 3; only 4 hollow) and enumerated sizes up to 11
via the boxed/spiked/merged taxonomy (size 7: 496 classes, 477 of width 2,
19 of width 3, none larger). The hollow-restricted maximum at size 7 was
never stated. Width-1 polytopes are infinite in every size, so we work
throughout modulo the width > 1 (hence finite) classification.
Candidate-list completeness (auditor-repaired, not trusted parsing):
boxed = the 23 matrices of the Size-7 section of `list_boxed.tex`
(count 23 matches Table-minimal's boxed size-7 total 4+15+4; the replay
script `generate_candidates.py` re-parses the source file with the
documented regex, asserts entry-by-entry equality with the embedded list,
and asserts the count is 23; source tarball sha256 recorded in
`candidates.json`); spiked = 32 instantiations generated from the theorem
parameters (minimal case (a,b) in {(0,0),(0,1),(1,1)}, k=2; cases
(1),(2),(4),(5),(6),(7),(8),(9),(10a),(10b) at the k forced by the stated
size formulas k+4/k+5/k+6/floor((3k+b)/2)+5 with the full finite a/b ranges
from the theorem statements), each size formula evaluating to 7 with a
7-point recount, plus neighboring-k non-7 exclusion (in particular case (3),
size k+6, would need k=1, excluded by k≥2, so it contributes no size-7
candidate). The merged branch is explicitly excluded throughout.

## 2. Results (narrowed to the replayed candidate lists)

**Theorem 1 (listed boxed candidates).**
Of the 23 listed boxed size-7 candidates (artifact pointer:
`output/artifacts/candidates.json` → `certs_boxed_all.json`, ids 0–22 in
source order), exactly 8 (ids 1, 4, 5, 6, 7, 12, 13, 19) are hollow, each of
lattice width exactly 2 with h3\* = 0. Each of the remaining 15 candidates
has exactly 1 interior lattice point (hence h3\* = 1) and lattice width
exactly 2. Per-candidate facet/point/interior/Ehrhart/width logs are stored
for all 23 (not only the hollow 8).

**Theorem 2 (generated spiked instantiations + width bound).**
Of the 32 generated minimal-size-7 spiked instantiations (artifact pointer:
`output/artifacts/candidates.json` → `certs_spiked_all.json`, keyed by
theorem/case/params/k with size-formula evaluation), exactly 2 are hollow,
both tetrahedra of width exactly 2:
- (S1) `conv{(1,-1,-1),(-1,1,1),(-1,-1,0),(0,0,3)}`
  (spiked-quasiminimals case (1), k=3, size 3+4=7), attainer `(-1,-1,0)`,
  h\* = (1,3,8,0);
- (S2) `conv{(1,-1,0),(-1,1,-1),(-1,-1,0),(0,0,2)}`
  (spiked-quasiminimals case (2), k=2, size 2+5=7), attainer `(-1,-1,0)`,
  h\* = (1,3,6,0).
The other 30 instantiations are non-hollow (1–3 interior points; includes
one width-3 non-hollow member, q4 case (4), so no hollow width-3 witness is
produced). Per-candidate hollow/width logs are stored for all 32. Hence
every hollow member of the generated spiked size-7 list has width ≤ 2
(in fact = 2).

**Theorem 3 (combined hollow-10 of the two lists).**
The hollow members of the two lists above give exactly 10 classes
(8 boxed + 2 spiked), pairwise inequivalent under GL(3,Z) ⋉ Z³ (all 45
pairs rerun by exhaustive unimodular-congruence search, stored in
`output/artifacts/inequivalence.log`, all inequivalent), each of width
exactly 2 with h3\* = 0.

**Corollary (Codenotti–Santos consistency).**
All 10 classes have lattice width 2 < 2+√2 ≈ 3.414, consistent with the
conjectured 3D hollow maximum at this stratum (no implication for the full
conjecture).

## 3. Witness tables
Boxed hollow 8 (vertex columns; attainer; h\*):
| # | vertices | point set (7) | width u | h\* |
|---|---|---|---|---|
| B1 | (0,-1,0),(0,1,0),(1,1,3),(2,0,0) | + (0,0,0),(1,0,0),(1,0,1) | (-1,0,0) | (1,3,8,0) |
| B4 | (-1,2,1),(0,0,0),(0,0,1),(1,-1,1),(1,1,-1) | + (0,1,0),(1,0,0) | (-2,-1,-1) | (1,3,3,0) |
| B5 | (0,1,0),(0,2,1),(1,0,1),(1,0,2),(2,1,0) | + (1,1,0),(1,1,1) | (-1,-1,-1) | (1,3,4,0) |
| B6 | (0,1,0),(0,1,2),(1,0,0),(1,2,0),(2,0,0) | + (0,1,1),(1,1,0) | (-1,-1,-1) | (1,3,4,0) |
| B7 | (0,0,0),(0,1,1),(0,1,2),(1,2,0),(2,0,0) | + (1,0,0),(1,1,0) | (-1,0,-1) | (1,3,5,0) |
| B12 | (0,0,1),(0,2,0),(1,0,0),(1,1,2),(2,0,0) | + (1,1,0),(1,1,1) | (-1,-1,0) | (1,3,6,0) |
| B13 | (0,0,1),(0,1,0),(0,1,2),(1,2,0),(2,0,0) | + (0,1,1),(1,1,0) | (-1,-1,-1) | (1,3,6,0) |
| B19 | (0,0,1),(0,1,0),(0,1,2),(0,2,1),(1,0,0),(2,0,0) | + (0,1,1) | (-1,-1,-1) | (1,3,5,0) |
Boxed negatives (15): ids 0,2,3,8,9,10,11,14,15,16,17,18,20,21,22, each with
exactly 1 interior point, width 2, h3\* = 1 (full logs in
`certs_boxed_all.json`).
Spiked negatives (30): all instantiations except q1,q2, with interior
counts 1–3 and stored widths (29 of width 2, q4 of width 3 non-hollow);
full logs in `certs_spiked_all.json`.

## 4. Methods (reproducible)
Candidate generation: `generate_candidates.py` (stdlib only) embeds the 23
boxed matrices, re-parses `list_boxed.tex` and asserts byte-level equality
plus count 23 and 7-point recounts; generates the 32 spiked instances from
theorem parameters and asserts count 32, size-formula = 7, and 7-point
recounts, with neighboring-k exclusion. Certificates:
`build_certs_all.py` (stdlib only) emits per-candidate facet/point/
interior/Ehrhart/width logs for all 23+32. Facets: supporting-plane scan
over vertex triples with tolerance-free integer arithmetic (interior
diagonals skipped by the two-sided test). Points: exact box enumeration;
interior = strict inequalities. Hollowness cross-checked two ways:
empty strict-interior list AND h3\* = 0 via dilate counts
L(0..3) = (1, 7, L2, L3) with reciprocity L(3) − 4L(2) + 28 − 4 = 0
(boxed negatives: exactly 1 interior point, h3\* = 1).
Width: upper bound by an explicit attaining functional; lower bound by
exhaustive scan of primitive functionals in the rigorous box
|u_i| ≤ ⌈(Σ_j|adj_ij|·W)/|det|⌉ + 1. The verifier (`verify.py`) recomputes
its own box and basis rather than trusting stored ones, replays negatives
(interior count 1 for the 15 boxed; stored interior counts for the 30
spiked rejects), re-asserts the totals (23 = 8+15; 32 = 2+30), and reruns
all 45 inequivalence searches to `inequivalence.log`.
Current run: `ALL REPLAYS PASSED: boxed 23/23, spiked 32/32,
inequivalence 45/45`.

## 5. Limitations (explicit non-claims)
(i) The **merged branch is not enumerated**, so no claim is made about the
full maximum W7\* over all of H7; it is either 2 or 3 (bounded above by the
published overall size-7 maximum 3). (ii) No width-3 hollow 7-point witness
is produced (the one width-3 spiked size-7 member, q4, is non-hollow with 2
interior points). (iii) The census is over the two listed/generated
candidate lists (artifact pointers above), up to GL(3,Z)-equivalence; vertex
representatives are not in canonical normal form. (iv) Nothing is claimed
about the Codenotti–Santos conjecture beyond consistency at this stratum.

## References
- M. Blanco, F. Santos, Lattice 3-polytopes with six lattice points,
  arXiv:1501.01055.
- M. Blanco, F. Santos, Enumeration of lattice 3-polytopes by their number
  of lattice points, arXiv:1601.02577 (source of boxed list, spiked theorems,
  width/size tables used for candidate completeness; e-print URL recorded in
  `candidates.json` with tarball/file sha256).
- G. Codenotti, F. Santos, Hollow polytopes of large width,
  arXiv:1812.00916.
