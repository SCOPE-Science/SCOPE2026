---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The third-root Fourier filter gives U=(w−1)P_r+3P_(r³)(3t). For 0<t<π the derivative is negative outside |cos t|<1/2. Inside, its sign is the opposite of w−1−H_r(x), x=cos t; the positive denominator is the product of the two shifted Poisson denominators. Expanding the numerator of dH_r/dx gives the stated factor (r+2x)(1+2rx)(1+r²−2rx), with negative prefactor and the last two factors strictly positive. Hence H_r has one strictly quadratic maximum at −r/2, of height F(r); it is zero at both endpoints. Two interior roots give derivative signs −,+,− as t increases: the larger cosine gives the minimum and the smaller cosine the lateral maximum. At equality the quadratic zero of the derivative gives a shoulder on each side, not an extremum. The sine factor has simple zeros at 0,π with bracket strictly positive there, so the central maximum and antipodal minimum persist nondegenerately, including at equality. F increases from zero to infinity. The curvature H_xx<0 and F′>0 give nondegenerate folds. Taylor expansion in y=x+r/2, using sqrt(r−r*) as the small parameter, gives the stated coefficient sqrt(2F′/−H_xx) and O(r−r*) remainder. Setting w=2 gives the cubic 10q³+6q²+12q−1, increasing on [0,1] and changing sign.

## originality

PASS

The bounded comparison found no equivalent all-weight periodic threshold and fold law. The exact periodic Resultary hit is the frozen record itself. The most similar distinct hits concern real-line positive Poisson mixtures; the available circular wrapped-Cauchy literature establishes the estimation method, not this mode classification. This is a best-of-knowledge comparison, not a historical priority claim.

## value

PASS

The family is a natural first asymmetric three-site circular smoothing model. A sharp criterion for resolving the satellites is useful in its own right: the weight and bandwidth jointly determine when off-center maxima appear, exclude an intermediate two-mode regime, and identify the non-extremal shoulders at the boundary. The fold law quantifies the onset; w=2 makes it concrete for the smallest repeated-central sample of this form.

The dated certificate retains the supplied scientific assessment, sources and limitations.
