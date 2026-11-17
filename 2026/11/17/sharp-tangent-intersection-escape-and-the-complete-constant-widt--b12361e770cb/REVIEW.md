# Scientific review — Sharp tangent-intersection escape and the complete constant-width stability law

## Correctness — PASS
The complete proof is in RESULT.md. The support-line intersection formula has a uniformly removable singularity for coincident normals, and an antipodal pole with coefficient equal to geometric width. The probability is integrated against the correct arclength-induced angular densities, leading to the exact \(R^{-1}\) coefficient. A monotone inverse map provides the marked total-variation law without confusing it with the weak directional limit. Under constant width, the nonnegative square identity is exact, the disk is the unique equality case, and threefold smooth curvature-radius families establish all attainable values. Numeric checker tests corroborate the circle formula and harmonic examples, but do not replace the proof.

## Originality — PASS, provisional
The full Fodor–Hug–Ziebarth 2014 paper treats increasing numbers of containing halfspaces and truncated geometric functionals. The nearest published tangent-polygon result treats a *bounded polygon area* for \(n\ge3\) and therefore has a width-squared coefficient and semicircle-occupancy factor, rather than the present distance law for exactly two tangents. Another published tangent-polygon paper concerns Poisson high-intensity covariance. The closest two-line comparison concerns *normal* intersections, whose constant-width behavior is opposite. The exact complete curvature-defect/range statement was not identified in the inspected sources. Xu's 2015 full paper was inaccessible and definitive historical priority is not claimed.

## Value — PASS
The two-tangent intersection is a natural observable of convex-boundary geometry. Its tail detects curvature-radius asymmetry among all curves sharing constant width and perimeter, the exact defect quantitatively characterizes disk rigidity, and the complete sharp attainable range is supplied. The conditional marked law accounts for the mechanism of very distant intersections.

## Verification and residual limitations
`python verify_tangent_intersections.py` tests the formulas for circle radius one and smooth constant-width harmonic perturbations and constructs increasingly small positive coefficients. The proof requires strictly positive smooth curvature, and no uniform family-wise remainder or finite-radius formula for general ovals is claimed. Historical priority and mathematical validity are not independently certified.

Self-review: passed. Independent audit: not yet performed.
