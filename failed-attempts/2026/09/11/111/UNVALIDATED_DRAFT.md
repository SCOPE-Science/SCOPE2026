# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Corner singularity at 90-degree transmission vertices in the proved contrast range

## Result
Let `sigma(theta) = k` on `|theta| < pi/4` and `1` elsewhere on `S^1`
(a straight 90-degree corner with interior conductivity ratio `k`).
The first angular transmission exponent `lambda_1` (least positive eigenvalue of
`-(1/sigma)(sigma v')' = lambda^2 v`) satisfies `lambda_1 < 1`
for all `k < 1` and all `1 < k < K*` with `K* := (3pi+4)/(4-pi) > 15.6`
(using only the hand-checkable bound `pi > 3.141`).
Contrasts `k >= K*` are explicitly open (no claim is made there).

Quantitative variational upper bounds (`lambda_1 <= sqrt(Q)`, `Q < 1`),
proved in closed form by elementary one-parameter Rayleigh quotients:
`W = pi(k+3)/2`, `A = (W+k-1)/2`, `B = (W-k+1)/2`.
- `k < 1`: trial `v = sin theta` gives quotient `Q = A/B =
  ((k-1) + pi(k+3)/2) / (-(k-1) + pi(k+3)/2) < 1` since `k - 1 < 0`.
- `1 < k < K*`: trial `v = cos theta - m` with `m = (k-1) sqrt(2)/W` gives
  quotient `Q = B/(A - W m^2) < 1` iff `k < K*` as above.
  In particular the bound holds for the six admissible contrasts
  `k in {0.2, 0.5, 2, 3, 4, 10}` of the target class.

Numerical values (replayed by `output/artifacts/corner_certificate.py`):

| k    | trial | lambda_1 upper bound |
|------|-------|----------------------|
| 0.2  | sin   | 0.851701             |
| 0.5  | sin   | 0.912837             |
| 2.0  | cos-m | 0.906289             |
| 3.0  | cos-m | 0.873674             |
| 4.0  | cos-m | 0.863568             |
| 10.0 | cos-m | 0.917928             |

Independent two-mesh angular finite-difference eigenvalues
(`output/artifacts/compute_ingredients.py`, N = 300/600 agreeing to ~2e-3,
values 0.73-0.90) are non-load-bearing consistency evidence only: each bound
sits above the corresponding FD value, but the proof does not depend on them.

## Proof sketch (self-contained; ~1 page)
The separated corner mode `u = r^lambda v(theta)` solves
`div(sigma grad u) = 0` near the vertex iff `v` is an eigenfunction as above
with periodic boundary conditions. `lambda^2` is the least positive eigenvalue =
`inf` of the Rayleigh quotient over trial functions orthogonal to constants in
the `sigma`-weighted inner product, so any admissible trial gives an upper bound.
`int sigma = W` and `int sigma cos 2theta = k-1` are elementary (each line is a
one-line integral over the sector and its complement). Substituting `v = sin`
(resp. `v = cos - m` with orthogonality-fixing `m`) yields the quotients above;
`Q < 1` is then a hand-checkable rational inequality in `k` (and `pi > 3.141`
for the `K*` threshold). Hence `lambda_1 <= sqrt(Q) < 1` in the proved range.
IF the singular coefficient `A != 0`, the corner expansion then contains a
genuinely singular `r^{lambda_1}` term at leading order; a uniform positive
lower bound on the coefficient remains open (per `output/target_exit.json`).
This complements SCOPE047, which treats the 270-degree 4:1 vertex only.

## Limitations (scope boundaries)
- Straight 90-degree vertices only; other opening angles and anisotropic tensor
  vertices need further analysis.
- The analytic `Q < 1` proof covers all `k < 1` and `1 < k < K* ≈ 15.64`
  (hence the six admissible contrasts `k in {0.2, 0.5, 2, 3, 4, 10}` with
  margin); contrasts `k >= K*` are explicitly open (numerics suggest singularity
  persists, but no trial is proved there).
- The singular-expansion conclusion is conditional: it holds IF the singular
  coefficient `A != 0`; no uniform positive lower bound on `|A|` is claimed.

## Relation to target
Proves ingredient (b) of the admitted feasibility plan within the stated
contrast range: each 90-degree corner of the nested class in the proved range (`k < 1` or `1 < k < K*`) (in particular the full admissible band used in the target work)
is singular at leading order, subject to the `A != 0` proviso. The
full logarithmic modulus remains open (uniform singular-coefficient lower bound
and reflected-CGO propagation are the identified blockers); this certificate is
submitted as an EMERGENT_FINDING because it is a complete, original,
independently valuable local theorem.
