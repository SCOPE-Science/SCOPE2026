# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Maximal volume and h*-unimodality census for reflexive 3-polytopes with ≤ 14 lattice points

## 1. Statement

Let C = {reflexive lattice 3-polytopes P ⊂ R³, |P ∩ Z³| ≤ 14} up to GL(3,Z)-equivalence,
with V(P) the normalized volume (3! × Euclidean volume) and h*(P) the Ehrhart h*-vector.

**Theorem (verified census).**
(a) C contains exactly **1943** classes: 1/7/23/54/135/207/314/373/416/413 with
n = |P ∩ Z³| = 5/6/7/8/9/10/11/12/13/14.
(b) Every P ∈ C satisfies the rigid identity V(P) = 2n − 6 and
h*(P) = (1, n−4, n−4, 1), with Ehrhart counts L(k) = |kP ∩ Z³| given by the ten rows below
(k = 0..6). In particular every h* is palindromic and unimodal; the non-unimodal list is
empty (no unimodality gap anywhere in the window).
(c) The maximal normalized volume on C is **V* = 22**, attained exactly by the 413
polytopes with n = 14 (413-way tie — uniqueness is NOT claimed). Every other P ∈ C has
V(P) ≤ 20, i.e. a committed integer gap **g = 2**.
(d) A concrete maximal witness is KS archive index **167** (`3 6 M:14 6 N:16 5 …`):
vertices (−4,−3,−1), (−2,−1,1), (0,0,1), (0,1,1), (1,0,0), (1,2,0),
count 14, V = 22, h* = (1,10,10,1), L = (1,14,60,161,339,616,1014).

## 2. Census table (complete: one row per lattice-point count)

| n | #polys | V | h* | L(0..6) |
|---|---:|---:|---|---|
| 5 | 1 | 4 | (1,1,1,1) | 1,5,15,35,69,121,195 |
| 6 | 7 | 6 | (1,2,2,1) | 1,6,20,49,99,176,286 |
| 7 | 23 | 8 | (1,3,3,1) | 1,7,25,63,129,231,377 |
| 8 | 54 | 10 | (1,4,4,1) | 1,8,30,77,159,286,468 |
| 9 | 135 | 12 | (1,5,5,1) | 1,9,35,91,189,341,559 |
| 10 | 207 | 14 | (1,6,6,1) | 1,10,40,105,219,396,650 |
| 11 | 314 | 16 | (1,7,7,1) | 1,11,45,119,249,451,741 |
| 12 | 373 | 18 | (1,8,8,1) | 1,12,50,133,279,506,832 |
| 13 | 416 | 20 | (1,9,9,1) | 1,13,55,147,309,561,923 |
| 14 | 413 | 22 | (1,10,10,1) | 1,14,60,161,339,616,1014 |

## 3. Method and replay (what was actually verified)

1. Source: Kreuzer–Skarke `RefPoly.d3` (TU Wien,
   `http://hep.itp.tuwien.ac.at/~kreuzer/pub/K3/RefPoly.d3`; md5 `c9fc314d0191b7ac2d3b7d1cce24c612`,
   4319 records). Parsed all 4319 headers + vertex rows.
2. For each record: exact facet enumeration (all vertex triples, primitive outward
   normals, allConfirm via centroid orientation); bounding-box lattice-point enumeration
   for dilations k = 0..6.
3. Recount equals the KS `M:` header on all 4319 records (0 mismatches) — this anchors
   window completeness: the ≤14-point window is exactly the 1943 records with M: ≤ 14.
4. h* solved exactly (Fraction arithmetic) from L(0..3) via the binomial system
   L(k) = Σ h*_i C(k+3−i,3); integrality, prediction of L(4..6), identity sum(h*) = V
   with V = third finite difference of L, palindromicity, and unimodal-peak existence
   asserted for all 1943 — all pass.
5. An independent stdlib-only verifier (`output/artifacts/verify_window.py`, separate code
   path) replays steps 1–4 from the archive bytes plus the committed table and asserts
   window = 1943, maxvol = 22 (413×), runner-up 20, witness-167 entry. It prints
   ALL VERIFIER CHECKS PASS.
6. Full per-polytope data (vertex lists, facets, L, h*, V for all 1943):
   `output/artifacts/final_table.json`.

## 4. Limitations and honest deviations from the target
- **Triangulation leg failed, excluded.** A half-open star-triangulation h* implementation
  matched only 291/1943 cases (non-unimodular stars + float-tolerance issues); it is NOT
  part of the evidence. h* is verified by the Ehrhart-series route (exact solve +
  dilation-6 prediction + independent replay), which is rigorous for the stated identities.
- **Extremal ties 413 ways.** The "one maximal witness" exists (index 167 committed) but
  uniqueness fails; headline strength is the closed-form census + gap g = 2, not a unique
  extremal.
- **Rigidity is empirical over the window**, proved by exhaustive enumeration replay, not
  by a general theoretical argument; it is consistent with reflexive palindromicity
  (Hibi) plus the small-point regime but the proof here is the certified census itself.
- Scope is the KS archive as published (taken as the classification baseline); no
  independent proof that 4319 is complete is attempted — window-completeness is relative
  to the archive plus the recount==header check.
