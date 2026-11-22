# Mathematical review

## Correctness: PASS
Euclidean normal-cone optimality yields the firm nonexpansivity ball for any pair of projected inputs. Its coordinate and weighted-sum estimates prove the universal bound. An explicit weighted hyperplane row-sum optimizer proves optimality for a tangent projector; the tangent-halfspace limit at every smooth support normal transfers sharpness to each smooth convex body. Strictly convex support makes the finite-point inequality strict. Rounded boxes are smooth parallel bodies and establish discontinuity. The supplementary standalone checker passed 4,228 assertions on ellipsoids and boxes. All universal quantifiers are discharged analytically, not computationally.

## Originality: PASS (with historical priority risk)
The previously published sharp weighted coordinate norm of **ball clipping** has exactly the same expression, and is explicitly cited rather than presented as new. Its stated scope does not cover arbitrary smooth convex bodies. The general body-invariance law, strict-convexity nonattainment, and the Hausdorff discontinuity example are not entailed merely by that ball theorem. Balestro--Martini--Teixeira (2019) provide normal geometry without this sharp two-norm formula; Leobacher--Steinicke (2021) analyze manifold projection regularity; Bednarczuk--Rutkowski (2020) treat parameter-varying polyhedral feasible sets. An older equivalent theorem under projector norm terminology remains possible. The new contribution is the full-body quantified extension, not the familiar bound or ball calculation alone.

## Mathematical value: PASS
The exact coefficient is surprisingly insensitive to all shape, scale and curvature choices within a large natural class, but drops discontinuously at a nonsmooth limit. The proof connects firm nonexpansivity, optimal tangent hyperplane geometry, the Gauss-normal range and topological sensitivity of nonlinear projector moduli. Its weighted dual-norm and nonattainment consequences offer structural robustness information for convex repair problems.

## Closest literature and limitations
- Balestro, Martini, Teixeira, *Convex analysis in normed spaces and metric projections onto convex bodies*, arXiv:1908.08742 (2019).
- *Sharp weighted coordinate sensitivity of Euclidean-ball clipping*, published-finding corpus public record (October 2026), ball-only statement with identical factor.
- Leobacher, Steinicke, *Existence, uniqueness and regularity of the projection onto differentiable manifolds* (2021).
- Bednarczuk, Rutkowski, *On Lipschitz Continuity of Projections onto Polyhedral Moving Sets* (2020 online).

The result concerns finite-dimensional real Euclidean projection to a fixed smooth compact convex region. For general nonsmooth convex regions only the universal upper bound is asserted. Independent priority analysis and independent mathematical validation remain outstanding.

Self-review: passed. Independent audit: not yet performed.
