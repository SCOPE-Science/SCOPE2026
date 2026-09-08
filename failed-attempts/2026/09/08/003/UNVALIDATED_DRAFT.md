# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Certified Ehrhart audit of the 4319 Kreuzer–Skarke reflexive 3-polytopes

**Status: CLAIMED — complete checkable census (from-scratch enumeration + independent triangulation cross-check + replay).**

## 1. Input provenance (frozen)

- Source: Kreuzer–Skarke K3/3D page `http://hep.itp.tuwien.ac.at/~kreuzer/CY/CYk3.html`
  linking `http://hep.itp.tuwien.ac.at/~kreuzer/pub/K3/RefPoly.d3`
  ("list of all 4319 reflexive polyhedra in 3 dimensions", PALP matrix format:
  header `3 nv M:# # N:# # Pic:# Cor:#` + 3 rows of vertex coordinates).
- Frozen copy: `output/artifacts/KS3_RefPoly.d3`
- SHA-256: `a6cf627828bfdbbd1a517ff87b3811232bf8da9360a65219de619fd9ff5dde5b`
- Parsed: **4319** polytopes; vertex-count histogram
  4:48, 5:250, 6:611, 7:964, 8:1051, 9:801, 10:405, 11:143, 12:37, 13:8, 14:1.

## 2. Method (exact, stdlib + numpy only)

For each polytope P with vertex list V:

1. **Facets (exact integers).** For every vertex triple, normal
   `n = (v_j − v_i) × (v_k − v_i)`, divide by `gcd`, keep supporting planes
   with all vertices on one side. Facet = primitive `(n, c)`, `n·x ≤ c`.
2. **Reflexivity certificate.** Assert every facet offset `c = 1`
   (origin = unique interior lattice point). Passed **4319/4319**.
3. **Header cross-check.** Assert `#facets == Nvert` (dual vertex count from the
   KS header). Passed **4319/4319**. Also `L(1) == Mpts` (see 4). Passed **4319/4319**.
4. **Dilate counts.** `L(t) = |tP ∩ ℤ³|` for `t = 0, 1, 2, 3` by exact box
   enumeration over `t·[min V, max V]` with numpy masks (worst 3P box ≈ 68k cells).
5. **Ehrhart interpolation (exact).** Solve `L(t) = Σ_k h_k·C(t+3−k,3)` over
   `Fraction`s; assert integral `h*`. Normalized volume two ways:
   `V = L(3) − 3L(2) + 3L(1) − L(0)` (third finite difference) and `V = Σh`.
6. **Independent triangulation volume.** Placing fan at origin: per facet, sort
   facet vertices angularly about the facet centroid in the facet plane
   (convex facet ⇒ boundary order), fan-triangulate, cone each triangle with
   the origin, sum `|det|`. Assert equals `V`. Passed **4319/4319**.
7. **Unimodality.** Exact peak test on length-4 `h*`. **0 non-unimodal** (all
   `h* = (1, a, a, 1)`, trivially unimodal).
8. **Decomposition tests.** Exhaustive: every `q ∈ 2P` writes `q = p + (q−p)`
   with `p, q−p ∈ P ∩ ℤ³` (**4319/4319 pass, zero witnesses**); hierarchical
   `3P = P + 2P` (**4319/4319 pass**). Full IDP for all `k` is *not* tested —
   reported as hierarchical evidence only (see §5).

## 3. Results

### 3.1 h*-distribution (33 distinct vectors; all palindromic `(1,a,a,1)`, `V = 2a + 2`)

| h* | count | V | | h* | count | V |
|---|---|---|---|---|---|
| (1,1,1,1) | 1 | 4 | | (1,17,17,1) | 151 | 36 |
| (1,2,2,1) | 7 | 6 | | (1,18,18,1) | 117 | 38 |
| (1,3,3,1) | 23 | 8 | | (1,19,19,1) | 87 | 40 |
| (1,4,4,1) | 54 | 10 | | (1,20,20,1) | 66 | 42 |
| (1,5,5,1) | 135 | 12 | | (1,21,21,1) | 40 | 44 |
| (1,6,6,1) | 207 | 14 | | (1,22,22,1) | 42 | 46 |
| (1,7,7,1) | 314 | 16 | | (1,23,23,1) | 27 | 48 |
| (1,8,8,1) | 373 | 18 | | (1,24,24,1) | 18 | 50 |
| (1,9,9,1) | 416 | 20 | | (1,25,25,1) | 8 | 52 |
| (1,10,10,1) | 413 | 22 | | (1,26,26,1) | 13 | 54 |
| (1,11,11,1) | 413 | 24 | | (1,27,27,1) | 9 | 56 |
| (1,12,12,1) | 348 | 26 | | (1,28,28,1) | 4 | 58 |
| (1,13,13,1) | 334 | 28 | | (1,29,29,1) | 2 | 60 |
| (1,14,14,1) | 274 | 30 | | (1,30,30,1) | 2 | 62 |
| (1,15,15,1) | 234 | 32 | | (1,31,31,1) | 5 | 64 |
| (1,16,16,1) | 179 | 34 | | (1,32,32,1) | 1 | 66 |
| | | | | (1,35,35,1) | 2 | 72 |

Missing rungs: `a ∈ {33, 34}` absent (hence `V ∈ {68, 70}` absent); all other
`a = 1..32, 35` occur. Mode: `a = 9` (416 polytopes, `V = 20`).

### 3.2 Volume range and extremal witnesses

- `V ∈ {4, 6, …, 66, 72}` (33 values, all even); min `V = 4` (id 0),
  max `V = 72` attained by exactly two tetrahedra, which also maximize
  `|P ∩ ℤ³| = 39`:
- **Witness E1 = KS id 7.** Vertices (columns of PALP matrix)
  `(1,0,0)`, `(1,2,0)`, `(1,2,6)`, `(−5,−4,−6)`.
  Facets (primitive outward `n·x ≤ 1`):
  `(1,0,0)≤1`, `(1,0,−1)≤1`, `(1,−3,1)≤1`, `(−1,1,0)≤1`.
  `L = (1, 39, 185, 511)`, `h* = (1,35,35,1)`, `V = 72`.
  Fan-from-origin triangulation: 4 cones (one per triangular facet), determinants
  `|det|`: 12, 12, 12, 36 (sum 72 — recompute via replay script).
  Header `M:39 4 N:6 4 Pic:1 Cor:0` matches (`L(1) = 39`, 4 facets).
- **Witness E2 = KS id 11.** Vertices `(1,0,0)`, `(0,1,0)`, `(3,4,6)`, `(−9,−8,−6)`.
  Facets: `(1,1,−1)≤1`, `(1,1,−3)≤1`, `(1,−2,1)≤1`, `(−1,1,0)≤1`.
  Same `L`, `h*`, `V = 72`, `|P ∩ ℤ³| = 39`.
  Header `M:39 4 N:9 4 Pic:2 Cor:0` matches.
- **Minimum witness = KS id 0** (standard simplex + opposite corner):
  vertices `(1,0,0)`, `(0,1,0)`, `(0,0,1)`, `(−1,−1,−1)`;
  `L = (1,5,15,35)`, `h* = (1,1,1,1)`, `V = 4`.

### 3.3 Unimodality / decomposition verdicts (certified absence at tested levels)

- Non-unimodal `h*` list: **empty** (all 4319 vectors `(1,a,a,1)`).
- 2P decomposition-failure list: **empty**; 3P hierarchical (`3P = P + 2P`) failure
  list: **empty**. Logs: per-polytope table asserts both; replay re-checks both.

## 4. Reproducibility

- `output/artifacts/replay.py` (stdlib + numpy): re-parses the frozen file,
  re-runs §§2.1–2.8 end-to-end, re-derives both distribution tables.
  Full replay: **≈ 3 s**, exits `REPLAY OK: 4319 polys … V range 4..72`.
- `output/artifacts/per_polytope_table.json`: per-id `{L, h*, V, Vtri, #facets}`.
- `output/artifacts/distributions.json`: frequency tables.
- File hashes (SHA-256):
  `KS3_RefPoly.d3 a6cf6278…5dde5b`, `replay.py 95edbc09…fa922`, see `research_report.json`.

## 5. Limitations (read before citing)

1. **IDP ≠ proved.** Exhaustive `2P` and hierarchical `3P = P + 2P` decomposition
   are necessary but not sufficient for the integer decomposition property
   (`kP = P + ⋯ + P ∀k ≥ 1`). The report claims *tested-level* absence of
   witnesses, not a theorem that all 4319 polytopes are IDP/normal. (Known
   literature strongly suggests all 3D reflexive polytopes are normal; this audit
   supplies the `k = 2, 3` computational leg, not a proof for all `k`.)
2. **Triangulation is a fan at the origin**, valid because reflexivity
   (`0` interior) is certified first; the angular-sort fan uses convexity of each
   facet. It is an *independent* volume route (no Ehrhart input) but not a
   full regular-triangulation classification.
3. **Enumeration correctness** rests on exact integer facet planes + exhaustive
   box search; boxes are derived from vertex bounds, so containment is exact.
   Header agreement (`L(1) = Mpts`, `#facets = Nvert`, 4319/4319) is a strong
   external cross-check but the KS header values themselves are taken as
   published, not re-derived from scratch.
4. **No new classification theorem.** The 4319-list is Kreuzer–Skarke's;
   the contribution is the frozen from-scratch verification dataset
   (counts + cross-checks + extremal certificates + replay), including the
   gaps `a ∈ {33,34}` / `V ∈ {68,70}` as observed distribution facts.

## 6. References

- M. Kreuzer, H. Skarke, "Classification of reflexive polyhedra in three
  dimensions", Adv. Theor. Math. Phys. 2 (1998), hep-th/9805190 — the 4319 census.
- K3/3D data page + `RefPoly.d3` file (frozen above).
- A. Higashitani et al., Ehrhart roots of reflexive polytopes (arXiv:1503.05739);
  Braun–Davis–Solus on IDP vs unimodality in reflexive simplices (arXiv:1608.01614).
