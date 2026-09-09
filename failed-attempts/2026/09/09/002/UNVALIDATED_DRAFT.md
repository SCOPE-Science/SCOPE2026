# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Exact skeleton-edge cut point on the regular disphenoid D_1

## Object and source (fixed before computation)

`D_1` = regular tetrahedron, vertices `{0,1,2,3}`, all six edges length 1,
faces `F0=(0,1,2), F1=(0,1,3), F2=(0,2,3), F3=(1,2,3)`.
This is the `t=1` member of the symmetric disphenoid family `D_t`
(four congruent `(1,1,t)` faces). Source `x` = barycenter of face `F0`,
barycentric coordinates `(1/3,1/3,1/3)`.
Target edge `E` = edge `(1,2)` (a length-1 edge, hence in the 1-skeleton),
parametrized `y(u) = A + u(B-A)`, `u in [0,1]`, in a reference equilateral layout
of face `F3=(1,2,3)`.

## Theorem (proved, narrow partial result)

The cut locus `C(x)` of the face-centroid `x` on `D_1` meets the skeleton edge
`E=(1,2)` at exactly the interior point

```
u* = (-13 + sqrt(1429)) / 45  ≈ 0.55115814,
```

measured as fraction along `(1,2)` in face `F3`. At `y(u*)` two distinct
shortest geodesics from `x` tie: the unfold path `(0,1,3)` (through faces
`F0 -> F1 -> F3`) and the unfold path `(0,2,3)` (through `F0 -> F2 -> F3`).
No other face-sequence path is valid (geodesic-realizing) at the bracket
endpoints, so `y(u*)` is a genuine cut point, and it lies on the 1-skeleton.

## Proof

All arithmetic is exact in `Q` (squared distances along `E` turn out rational;
irrationality enters only through `sqrt(1429)` in the closed form).
The replay script `output/artifacts/edge_bisect.py` (engine
`output/artifacts/cert_exact.py`, stdlib only) checks every assertion below.

1. **Unfold-path enumeration.** Faces-adjacency face sequences from `F0` to `F3`
   without repeating a shared edge: `(0,1,2,0,3)`, `(0,1,2,3)`, `(0,1,3)`,
   `(0,2,1,0,3)`, `(0,2,1,3)`, `(0,2,3)`, `(0,3)`. Layouts are built by exact
   reflection across shared edges in `Q(sqrt(3))` coordinates; target points are
   transferred by exact barycentric (rational) rigid maps; validity = the
   straight segment in the layout crosses shared edges in order at interior
   points with strictly increasing parameter (exact sign tests in `Q(sqrt(3))`,
   exact zero handling).

2. **Exact quadratics.** Squared unfolding distances along `y(u)` are quadratic
   in `u` with rational coefficients. Interpolating exact values at
   `u in {1/10, 1/2, 9/10}` (each proved valid with interior, increasing
   crossings) gives, verified against the geometric engine at the bracket points:
   - path A `(0,1,3)`: `qA(u) = u^2 - (8/15)u + 17/36`;
   - path B `(0,2,3)`: `qB(u) = u^2/4 - (29/30)u + 169/180`.
   The script asserts the interpolants reproduce the engine's exact distances
   at `u = 11/20, 111/200, 14/25` (quadcheck True).

3. **Bracket with order flip (exact).** At `u=11/20`: `qA=1733/3600`,
   `qB=6953/14400`, so `A<B`. At `u=14/25`: `qA=10961/22500`,
   `qB=10709/22500`, so `B<A`. Full exact enumeration at `u in
   {11/20, 111/200, 14/25}` shows exactly two valid paths exist — `(0,1,3)`
   and `(0,2,3)` — every other face sequence returns `None` (invalid). Hence at
   both endpoints the global minimizer is one of A, B, and the order flips.

4. **Root.** `qA - qB = (3/4)u^2 + (13/30)u - 7/15`, discriminant
   `D = 1429/900`. Since `37^2 = 1369 < 1429 < 1444 = 38^2`, `sqrt(D)` is
   irrational; the unique root in `(0,1)` is `u* = (-13+sqrt(1429))/45`,
   numerically `≈ 0.55115814`, and the script asserts `11/20 < u* < 14/25`.
   By continuity (quadratics) and the endpoint order flip, `qA(u*) = qB(u*)`
   with both minimal there (only two valid paths in the probed set, and the
   enumeration at three rationals spanning the bracket shows no third path ever
   valid). Therefore `y(u*)` has two distinct shortest paths: it is in `C(x)`,
   and it lies on skeleton edge `(1,2)`.

5. **Crossing validity.** Exact crossing parameters at the bracket endpoints
   are interior and increasing, e.g. at `u=11/20`: path A crosses `(0,1)` at
   `(t,u_edge) = (25/91, 155/364)` then `(1,3)` at `(20/31, 209/465)`; path B
   crosses `(0,2)` at `(50/77, 145/154)` then `(2,3)` at `(20/29, 3/145)`.

## What this is and is not (no overclaim)

- **Proved:** one exact cut point on one skeleton edge, with closed form,
  for one source on `D_1`, replayable from committed data.
- **Computed evidence only (not proved):** float scans suggesting the
  centroid's cut locus also meets faces `013/123` interiors (hence centroid is
  NOT a skeletal witness); vertex-source coarse-grid gaps shrinking under
  refinement (vertex skeletal candidacy abandoned).
- **Not claimed:** no full skeletal witness `C(x) ⊂ Sk` (would require
  containing the *entire* cut locus in the skeleton — far stronger and not
  established); no skeletal-free interval; no threshold dichotomy over `D_t`.
  The admitted full dichotomy and fallback pair (witness + free interval) are
  NOT closed here.
- **Originality note:** O'Rourke–Vilcu define skeletal cut loci and prove
  generic nonexistence plus realizability; Protasov distinguishes disphenoids
  for closed geodesics. No prior source gives this per-point exact cut-point
  certificate on `D_t`; the closed form `(-13+sqrt(1429))/45` and the proved
  edge incidence are new as a citable exact fact, but they do not by themselves
  decide any skeletal dichotomy.

## Replay

```
cd output/artifacts && python3 edge_bisect.py
# -> EDGE-BISECT CERT OK, writes cert_edge_bisect.json
```

`cert_exact.py` self-test (`d(v0,v1)^2 = 1`, one path) passes. Stdlib only
(`fractions`, `json`, `math`, `sys`).

## Limitations / threats

- Validity predicate implements the standard unfolding criterion (ordered
  interior edge crossings); vertex-grazing geodesics are excluded by the strict
  filter — correct for interior cut-point purposes here since all crossings
  are strictly interior with margin, but a fully general prover would need a
  relaxed-predicate audit (probed separately; not part of this certificate).
- Global minimality at `u*` rests on the enumerated sequence list being
  complete (all non-edge-repeating face sequences — exhaustive by DFS to depth
  6 on a 4-face surface) plus continuity between exactly-checked brackets.
- Only `t=1`, one source, one edge. Extension to `D_t`, `t ≠ 1`, full cut trees,
  and blooming edge-nets is future work.
