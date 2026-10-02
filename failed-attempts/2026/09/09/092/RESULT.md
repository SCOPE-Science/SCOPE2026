# Certified non-collapse: dim_H(K0) >= 1 for the fixed irrational-rotation overlapping planar self-affine 3-cell C0

## Context

The Hausdorff dimension of overlapping planar self-affine attractors is a
recognized frontier (Falconer affinity/overlap program, Hochman self-similar
overlap program, Feng-Hu variational principle). Generic, almost-every
translation, axis-aligned carpet, and qualitative dichotomy theorems do not
give explicit thresholds for a single fixed rotation cell with overlaps.
This record fixes the first rigorous non-collapse mark (threshold 1, the
collapse-to-curve/line boundary) for one explicit dominated-splitting cell.

## Definitions

- Let `A = diag(0.7, 0.4)`, `R = rotation by 1 radian`, `M = A R`.
- Translations: `t_1 = (0,0)`, `t_2 = (1,0)`, `t_3 = (0,1)`.
- Cell C0: the three affine maps `f_i(x) = M x + t_i`, `i = 1,2,3`, on R^2.
- `K0`: the attractor of C0.
- `rho = sqrt(det M) = sqrt(0.28) = sqrt(7)/5 = 0.5291502622128...`.
- `tr(M) = 1.1 cos 1`; interval-verified `tr(M)^2 - 4 det(M)` lies in
  `[-0.76677, -0.76676] < 0`, so M has a complex-conjugate eigenvalue pair
  of modulus rho.
- Conjugacy: `M = P S P^{-1}` with `S = rho Rot(-psi)`,
  `psi = acos(tr(M)/(2 rho))`, `P = [[1,qx],[0,qy]]`,
  `qx = (rho cos psi - m11)/(rho sin psi)`,
  `qy = -m21/(rho sin psi) ~ (-0.18510828, -0.76877085)`, `det P = qy != 0`.
  With `y = P^{-1} x`, the IFS becomes the homogeneous self-similar system
  `g_i(y) = S y + u_i`, `u_i = P^{-1} t_i`, all with ratio rho.
  The norm `|y|_Y = |P y|_2` makes S-balls genuine Euclidean balls.
- `T* = max_i |u_i|_Y` (with `u_1 = 0`, `u_2 = (1,0)`), `T* <= 1.32287565553269`;
  `K0' = P^{-1}(K0)` lies in `B(0, R*)`, `R* = T*/(1-rho)` in
  `[2.8095495215727, 2.8095495215739]`.
- Level-4 centers `c_w = f_w(0)` over the 81 words; cylinder radius
  `r_4 = rho^4 R* <= 0.22026868249154` with `rho^4 = 0.0784` exactly as rationals.

## Result

**Theorem.** For the fixed overlapping self-affine cell C0 defined above,
the Hausdorff dimension of its attractor satisfies

    dim_H(K0) >= 1.

Precisely, the 16 level-4 words

    [[1,2,1,1],[1,2,2,2],[0,0,1,2],[1,0,2,0],
     [2,1,0,2],[2,0,2,2],[2,0,2,1],[1,2,0,0],
     [0,1,2,2],[1,1,0,0],[0,1,1,0],[0,0,1,1],
     [2,0,0,0],[2,2,2,0],[2,2,0,1],[2,2,0,2]]

(indexing t_1,t_2,t_3 as 0,1,2) give 16 pairwise-disjoint balls
`B(c_w, r_4)` contained in `B(0, R*)`, with `16 rho^4 = 1.2544 > 1` and

    s = ln 16 / (4 ln(1/rho)) = 1.0890272... >= 1.0890 >= 1,

so `dim_H(K0') >= s >= 1` and by bi-Lipschitz invariance `dim_H(K0) >= 1`.

## Proof / evidence

1. **Conjugacy.** Verified by exact interval arithmetic and an 80-digit
   recomputation (residual of `MP - PS` below 1e-80): M is conjugate via the
   closed-form P above to the similarity `S = rho Rot(-psi)`. Hence the
   system is homogeneous self-similar with ratio rho, and Hausdorff
   dimension is preserved under the invertible linear map P.
2. **Enclosure.** cos 1 / sin 1 by alternating Taylor intervals with
   remainder bounded by the first omitted term; rho via integer square-root
   enclosure; all remaining quantities by rational interval arithmetic
   (Python `Fraction` only for verdict inequalities). Interval widths are
   ~1e-12; final margins are ~1e-2.
3. **Separation.** Over all 120 pairs of the 16 words,
   `min |c_w - c_v|_Y^2 >= 0.20467744730049 > (2 r_4)^2 = 0.19407316994623`.
   Hence the 16 balls are pairwise disjoint (open-set condition for the
   subsystem). Distance margin ~0.0119.
4. **Containment.** For each chosen word `|c_w|_Y + r_4 <= R*`
   (worst `|c|+rN = 2.30930` versus `R = 2.80954`, margin ~0.50), so every
   cylinder-ball lies in the ball containing K0'.
5. **Dimension.** `16 rho^4 = 16 x 0.0784 = 1.2544 > 1`, so by the Moran /
   Hutchinson theorem for a homogeneous subsystem (k disjoint similar copies
   of ratio r inside a bounded set force `dim_H >= ln k / ln(1/r)`),
   `dim_H(K0') >= ln 16/(4 ln(1/rho)) >= 1.0890 >= 1`; transfer by P gives
   `dim_H(K0) >= 1`.
6. **Replay.** `python3 artifacts/certify.py` (run from the artifacts
   directory) exits 0 and writes `artifacts/fallback_certificate.json`
   with the endpoints above. Float-greedy search (`propose.py`) only
   proposes the words; the verdict uses only rigorous interval endpoints
   plus a nextafter-directed float-sound recheck.

## Limitations

- Proves only the threshold `dim_H(K0) >= 1`, not the full target equality
  `dim_H(K0) = D_LY` where `D_LY = 2 ln 3 / ln(25/7) ~ 1.7260674180653935`.
- Exponential separation for the conjugated homogeneous IFS is neither
  verified nor refuted (cylinder-proximity data `Delta_8 ~ 7.98e-4`
  inconclusive); an exact Fourier integer resonance blocks any uniform
  power-decay transversality certificate. These are logged obstructions,
  not claims.
- No exact-dimensional measure of dimension >= 1 is exhibited; the proof
  uses a Moran/OSC subsystem, which satisfies the binary success criterion
  (a proof certificate that `dim_H(K0) >= 1`).

## Reproducibility

- `artifacts/certify.py`: rigorous interval certificate; writes
  `artifacts/fallback_certificate.json`.
- `artifacts/propose.py`: float-greedy word proposal (discovery only).
- `artifacts/fallback_certificate.json`: endpoints (N=4, k=16, words, rho,
  Rstar, rNhi, min_pair_y2_lo, two_rNhi_sq, dim_ratio_16rho4_lo).
- Run `python3 artifacts/certify.py` from the artifacts directory;
  expected output ends with `CERTIFICATE WRITTEN` and exit code 0.

## References

- M. Hochman, A. Rapaport, Hausdorff dimension of planar self-affine sets
  and measures with overlaps, arXiv:1904.09812. Total irreducibility plus
  exponential separation gives Lyapunov-dimension equality; hypotheses not
  verified for C0, no numeric value for C0.
- B. Barany, M. Hochman, A. Rapaport, Hausdorff dimension of planar
  self-affine sets and measures, arXiv:1712.07353. Strong separation / strong
  open set condition case; inapplicable to overlapping C0.
- J. Fraser, P. Shmerkin, On the dimensions of a family of overlapping
  self-affine carpets, arXiv:1405.4919. Axis-aligned Bedford-McMullen family
  outside an exceptional translation set; does not imply a fixed rotation
  cell threshold.
- K. Falconer, Fractal Geometry, Theorem 9.3 (Moran / Hutchinson homogeneous
  subsystem dimension bound).
