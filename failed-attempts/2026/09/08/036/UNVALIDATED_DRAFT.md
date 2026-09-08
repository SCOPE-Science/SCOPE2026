# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Certified census of 3-point lattice tetrahedra of normalized volume ≤ 144

## Status
Replayable computational census with exact integer-arithmetic certificates.
Scope: conjectures BK-Conj-1.5 / BK-Conj-6.1 at (d,k) = (3,3),
i.e. comparators Vol ≤ 144, δ₁ ≤ 67, δ₂ ≤ 73.

## 1. Objects and normalization
- A lattice tetrahedron is `conv(v₀,v₁,v₂,v₃)`, vᵢ ∈ ℤ³ affinely independent.
- Normalized volume V = |det(v₁−v₀, v₂−v₀, v₃−v₀)| ∈ ℤ_{>0}.
- Unimodular-affine equivalence: v ↦ Uv + t, U ∈ GL(3,ℤ), t ∈ ℤ³.
- δ-vector (h\*-vector): Ehrhart series Σ_{t≥0}|tP ∩ ℤ³|xᵗ = (1+δ₁x+δ₂x²+δ₃x³)/(1−x)⁴;
  δ₃ equals the number of interior lattice points; V = 1+δ₁+δ₂+δ₃.

## 2. Enumeration (certified complete for V ≤ 144)
Every lattice tetrahedron is unimodular-affine equivalent to one with
v₀ = 0, v₁ = (a,0,0), v₂ = (b,c,0), v₃ = (d,e,f) with a,c,f ≥ 1 and V = acf.
(Translate a vertex to 0; rotate shortest lattice direction of the edge lattice
to the x-axis; rotate the face lattice into the xy-plane. This is the standard
triangular presentation; the run uses the superset 0 ≤ b < c, 0 ≤ d,e < f,
which contains every triangular presentation, hence every class.)
So enumerating all (a,b,c,d,e,f) with acf ≤ 144 and 0 ≤ b < c, 0 ≤ d,e < f
(a finite list of 2,002,829 raw 6-tuples) meets every unimodular class with V ≤ 144.
Deduplication is by an exact canonical key: the minimum, over all 24 vertex
repositionings (4 choices of origin × 6 permutations), of the column-Hermite
normal form of the positioned edge matrix (invariant under right GL(3,ℤ) action,
minimized over the left repositioning action; self-tested against random
unimodular maps, reflections, and translations in `canon.py`).
Result: 94,278 canonical classes met by the V ≤ 144 superset.

## 3. Interior-point counting (exact)
For a tetrahedron with edge matrix E (det ±V) and adjugate adj(E):
a lattice point p is inside iff nᵢ = (adj(E)·(p−v₀))ᵢ ≥ 0 and Σnᵢ ≤ V,
strictly interior iff all inequalities are strict. All integer arithmetic.
Per class the minimum interior count over its appearances is the true count
(any appearance scans a superset box of the translated tetrahedron, so extra
appearances can only confirm, never inflate, the minimum).

## 4. Calibration (matches the published record exactly)
- i = 1: 225 classes (cf. 225 in Kasprzyk's MG database / AKN).
- i = 2: 471 classes (cf. 471 in Balletti–Kasprzyk).
Both counts agree with the published classifications, validating the
enumerate → canonicalize → count pipeline end to end.

## 5. The 3-point slice (new data)
- 741 unimodular classes with exactly 3 interior points and V ≤ 144.
- Max V = 144, unique maximizer class = S³₃ (key ((1,0,0),(3,6,0),(3,6,24))),
  witnessed e.g. by conv{(0,0,0),(1,0,0),(3,6,0),(3,6,24)} and containing the
  Zaks–Perles–Wills simplex conv{(0,0,0),(2,0,0),(0,3,0),(0,0,24)}.
- Independent audit (`stage2.py`, separate adjugate/Ehrhart code path) recomputed
  for all 741 witnesses: V, L(1), L(2), δ-vectors; all satisfy V ≤ 144,
  δ₁ ≤ 67, δ₂ ≤ 73, δ₃ = 3 = interior recount, with 0 reciprocity failures.
- Max δ₁ = 67, max δ₂ = 73, both uniquely attained at the S³₃ class
  (δ = (1,67,73,3)); next-largest V are 138, 132, 132, 128, 128, 128.

## 6. What is NOT claimed
- Completeness of the i = 3 census among V ≤ 144 classes is established only
  modulo the standard triangular-presentation lemma (§2); no independent
  second enumeration (e.g. Kreuzer–Skarke-style normal forms) was run.
- Nothing is claimed about V > 144: the planned violator sweep (145–200) was
  started but killed at the consolidation deadline with no output, so the
  census supports Conjectures 1.5/6.1 at k = 3 only in the bounded range V ≤ 144
  (which contains the conjectured maximizer and all cases where equality could
  hold, but a large-volume violator remains logically possible).
- Weight data W(3,3) and the full per-class witness table are in the artifacts;
  only extremal witnesses are printed here.

## 7. Reproduction
- `canon.py`: exact canonical key + self-test (`python3 canon.py`).
- `stage1.py`: full enumeration → census (`stage1.json`: VMAX, n_raw,
  depth distribution, classes with i ≤ 3 witnesses).
- `stage2.py`: independent audit of the 741 classes (`stage2.json`:
  per-class V, L1, L2, δ-vector, witness; reciprocity-failure list, empty).
- `stage3.py`: (incomplete, no output) violator-sweep scaffold for V > 144.
- Timings: stage 1 ≈ 1364 s on 32 cores; stage 2 ≈ 2 s.
- Requirements: Python 3.12 + numpy only.
