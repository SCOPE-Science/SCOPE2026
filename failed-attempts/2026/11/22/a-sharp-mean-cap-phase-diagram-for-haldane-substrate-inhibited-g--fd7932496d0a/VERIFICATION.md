---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The stated theorem is mathematically correct, with a local proof error in the source's minimum argument. Suppressing the positive multiplier, the second derivative has sign of c²s³−3Kcs−K, c=1/I, which changes sign once beyond M=√(KI). The cap tangency satisfies Bc(ca²−K)=K(1+2ca), with the inverse cap decreasing from infinity to R as a rises from M to R. Multiplying the tangent deficit by D(s)=K+s+cs² gives a cubic with leading coefficient c f′(a) and roots a (double) and B. The resulting nonnegative deficit makes the piecewise majorant concave, and its contact set and strict concavity up to a give unique optimizers, including at a. Inversion yields B_c(m) and the strict benefit threshold. For the minimum, RESULT.md:72 is false as printed (take s=B<1); the correct pointwise bound is s/D(s) ≥ s/D(B) = (s/B)[B/D(B)], strict for 0<s<B since D is strictly increasing. This proves the stated minimum and equality case. On the half-line the tangent at m≤M is strictly supporting away from m; for m>M the unique pointwise peak excludes attainment under the mean constraint, while mixing M with a diverging cap gives the supremum. Mixing 0 and the cap gives infimum zero, unattainable at positive mean. Inspected VERIFICATION.md and checker.py; the source-reported checks are finite diagnostics and were not executed. No claim of physical feasibility, formal verification, or attestation.

## originality

FAIL

A distinct indexed record gives the same finite-cap upper-envelope theorem for all laws, not merely the same response or a particular optimum. In dimensionless variables u=s/K, c=K/I, L=B/K and mean m/K, the objectives differ only by μ, and the unique optimizers and inflection boundary map bijectively. The shared date provides no chronological priority evidence. The mean-to-cap inverse is already implied by the matching tangency equation. The minimum and half-line limits are not claimed to be word-for-word matches, but they do not make the submitted finite-cap maximization a distinct result.

## value

FAIL

A sharp arbitrary-law envelope would be useful, but that content is already present under an invertible normalization. The remaining chord minimum, elementary unbounded supremum/infimum consequences, and rewriting the same tangency as a cap threshold do not supply a distinct worthwhile mathematical result. No repair is delivered.

The dated certificate retains the supplied scientific assessment, sources and limitations.
