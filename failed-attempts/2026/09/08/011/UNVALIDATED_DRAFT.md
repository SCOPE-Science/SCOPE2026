# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Replayable Jones Census of Prime Knots Through 10 Crossings from PD Codes, with Volume/Width Cross-Check Columns and Separation Witnesses

**Status.** Partial theorem per the registered fallback claim: the from-scratch,
double-checked Jones column is complete (249/249); the volume and delta-width
columns are script-parsed cross-check columns from published KnotAtlas tables
(triangulation solve and Bar-Natan complex NOT re-implemented here), with exact
provenance and one-command replay. No originality is claimed for any single
invariant value; the contribution is the joint, replayable distinguishing table
plus explicit, computed separation witnesses.

## 1. What was proved / computed

**Theorem (Jones census, verified).** For every prime knot with crossing number
3..10 (249 labels: 3_1..10_165), let PD be the KnotAtlas planar-diagram
presentation. Then:

1. The Kauffman-bracket state sum
   `<D> = sum_states A^{a-b} (-A^2-A^{-2})^{c(s)-1}` with `f = (-A^3)^{-w}<D>`
   and `V(q) = f|_{A=q^{-1/4}}` yields the Jones polynomial in the table
   (`output/artifacts/full_table.json`, `jones_table.json`).
2. Two independent implementations agree exactly on all 249 diagrams:
   (A) direct 2^n state enumeration with a union-find circle counter;
   (B) memoized skein recursion with an independent walk-based circle counter.
3. All 249 computed polynomials agree exactly with the KnotAtlas-published
   Jones values (term-by-term, parsed robustly incl. bare constants).
4. Calibration: 3_1 (PD X1425 X3641 X5263) gives writhe -3, bracket
   `A^7-A^3-A^-5`, `V = -q^-4+q^-3+q^-1`, matching the atlas.

Conventions (fixed jointly by the 3_1 calibration, documented in
`jones_engine.py`): PD `X[i,j,k,l]` CCW from incoming under-edge, under
`i->k`; sign `+1` iff over runs `j->l`; A-smoothing pairs `(i,j)+(k,l)`.

**Cross-check columns (NOT from-scratch; provenance logged).**

5. Volume column: KnotAtlas-published hyperbolic volume (6-decimal string) or
   `Not hyperbolic`. Non-hyperbolic labels are exactly
   `{3_1, 5_1, 7_1, 8_19, 9_1, 10_124}` (+ unknot 0_1 by definition),
   matching the required torus-knot control set. 243/249 knots carry numeric
   volumes.
6. Width column: from the KnotAtlas-published (unreduced, integral) Khovanov
   `(r,j)` support table per knot, parsed by script (`build_table.py`), with
   `delta = j-2r` and the literal topic formula `w = max-min+1`:
   237 knots have `w=3` (two diagonals = thin), 12 have `w=5`
   (8_19, 9_42, 10_124, 10_128, 10_132, 10_136, 10_139, 10_145, 10_152,
   10_153, 10_154, 10_161).
   *Convention note:* the topic formula gives `w=3` for thin alternating
   knots (diagonals spaced by 2), whereas some literature calls these
   "width 2". We follow the formula literally and also publish
   `width_diagonals = (max-min)/2+1` (2 vs 3). Torsion is invisible in the
   parsed integral tables; the column is a support-width proxy, so labeled.

## 2. Separation witnesses (all computed from the table)

**(i) Chirality.** 3_1: `V(q) = -q^-4+q^-3+q^-1 != V(q^-1)` (chiral, Jones
detects); mirror volume equality holds trivially (both non-hyperbolic tags).
5_2 vs mirror: same asymmetry
(`-q^-6+q^-5-q^-4+2q^-3-q^-2+q^-1`, 6 terms, asymmetric). Controls:
amphicheiral 4_1, 6_3, 8_3, 8_9, 10_99 have exactly symmetric `V`
(e.g. 4_1: `q^2-q+1-q^-1+q^-2`).

**(ii) Same-Jones separation (in-census).** Seven collision classes found
(14 knots). Star witness: **5_1 vs 10_132**, identical
`V = -q^-7+q^-6-q^-5+q^-4+q^-2`, separated *both* by volume
(`Not hyperbolic` vs `4.05686`) *and* by width (`w=3`, deltas `{-5,-3}`
vs `w=5`, deltas `{-3,-1,+1}`). Six further pairs separated by volume
(10_22/10_35, 10_43/10_91, 10_59/10_106, 10_71/10_104, 10_81/10_109,
8_16/10_156; same width, distinct volumes — volume does the separating work).

**Conway 11n34 / Kinoshita-Terasaka 11n42 extension: NOT computed here**
(outside the <=10 census range; no PD fetched, no Khovanov engine built).
Cited only as motivation (Wehrli; Morton-Ryder). No claim is made on it.

## 3. Reproduction

- `python3 output/artifacts/verify_offline.py` — offline recompute of all 249 Jones
  polynomials by both methods from `replay_inputs.json` + atlas re-check.
  PASS at submission (249/249, ~11 s).
- `python3 witnesses.py` — re-derives the 7 collision classes.
- `python3 build_table.py` — rebuilds `full_table.json` (Jones + DT +
  volume + (r,j) support + widths).
- Raw inputs: `output/artifacts/replay_inputs.json` (249 PD strings + atlas Jones,
  distilled 2026-09-08 from KnotAtlas pages); engine: `jones_engine.py`; diagrams:
  `output/artifacts/diagrams/*.png` (Gauss schematics from DT codes for the
  9 witness knots — traversal circle + chord per crossing — plus PD strings
  in `full_table.json`).

## 4. Limitations (explicit)

- Volumes are cross-checked published values, not an independent
  triangulation solve (no SnapPy in this environment); agreement-with-oracle
  is the check, with the 6-label non-hyperbolic control set exact.
- Widths derive from published integral `(r,j)` support, not a rebuilt
  Bar-Natan complex; torsion and differentials are not verified; reduced-vs-
  unreduced and the `w=3`-vs-`2` convention are documented above.
- Diagrams are Gauss schematics (auditable, chord-exact), not planar
  projections with over/under rendering.
- Unknot 0_1 has no KnotAtlas page; `V=1`, non-hyperbolic by definition
  (not computed).
- Khovanov "chain dimensions" could not be logged (no complex built); the
  `(r,j)` support per knot IS logged in `full_table.json`.

## 5. Prior-art separation

Values: KnotAtlas/KnotInfo/Hoste-Thistlethwaite-Weeks (used as oracle, not
source of the Jones column). Phenomena: Wehrli (mutant, same-Jones/different-
Khovanov), Morton-Ryder (genus-2 mutants). Delta claimed here: the joint
replayable table with two-method Jones proofs and named in-census separation
witnesses, with machine-checked logs — not new invariant values.
