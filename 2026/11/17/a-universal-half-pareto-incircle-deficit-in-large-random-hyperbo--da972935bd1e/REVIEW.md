# Self-review

## Correctness — PASS

The exact inradius formula is independently confirmed by the Lorentz normal-equidistance computation in `check_hyperbolic_inradius.py`. For fixed nondegenerate angular gaps, hyperbolic chord lengths have the required \(2R+2\log\sin u\) expansion. The proof controls all gap-boundary regions by \(Z\le4/m^2\), then uses a bounded-coordinate blow-up and dominated convergence to compute the exact \(t^{-1/2}\) tail coefficient. The cyclic gaps are anchored at the first sampled vertex, which yields the exact uniform Dirichlet density (unlike anchoring at the smallest absolute polar angle). The same convergent chart densities yield the marked limit in total variation (rather than only weak convergence). The moment threshold follows from layer-cake integration. The proof deliberately does not interchange the large-\(R\) and large-\(t\) limits.

## Originality — PASS (provisional historical priority)

The hyperbolic semiperimeter incircle formula is classical and not claimed. Brody–Schettler [1] classify deterministic equal-inradius/perimeter triangles; Biró–Powers [2] use a different uniform-angle stochastic model. Closest fully inspected published public research results provide either the exact acuteness probability for this **same** hyperbolic circumcircle sampling law, the inradius distribution for **Euclidean** cyclic triangles, or the **area** deficit for volume-uniform large-hyperbolic-ball triangles. Those results have different observables or measures and do not state or imply the cotangent incircle-deficit law and its conditional single-collision limit. Searches using inradius, incircle, ideal-triangle deficit, near-collision and half-Pareto equivalents did not uncover a direct match. A previously unindexed equivalent treatment remains possible and historical priority cannot be certified by search alone.

## Value — PASS

The inradius is a canonical triangle invariant. The exponential approach to the ideal-triangle radius is a natural curvature-driven geometric limit. A previously unevaluated sharp half-Pareto exponent, exact tail constant, integrability threshold and total-variation conditional mark illuminate the role of nearly colliding random boundary directions. The tail exponent and marked mechanism are not algebraic relabelings of the deterministic inradius formula.

## Verification and limits

Run `python check_hyperbolic_inradius.py` with `numpy>=1.24`. Its two independently formulated inradius algorithms agree on nondegenerate random configurations, and seeded angular-gap simulation reproduces the predicted tail coefficient and marked means. These are tests, not infinite-dimensional proofs. Historical priority is provisional and independent mathematical review has not been performed. The theorem concerns the limiting variable only; no convergence of its finite-radius moments is asserted.

## Closest literature

[1] N. Brody and J. Schettler, *Rational Hyperbolic Triangles and a Quartic Model of Elliptic Curves*, arXiv:1406.0467 (2014-06-02).

[2] C. Biró and R. C. Powers, *A strong triangle inequality in hyperbolic geometry*, arXiv:1507.04033 (2015-07-14).

[3] *Exact dilogarithmic acuteness law for random triangles on hyperbolic circles*, public research record (2026).

[4] *The full inradius law and two contrasting tails of random cyclic triangles*, public research record (2026).

[5] *Pareto limit law and sharp moment threshold for areas of large random hyperbolic triangles*, public research record (2026).

Self-review: passed. Independent audit: not yet performed.
