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

Integration gives V_c e_n=(log c/log(cn))e_{cn}, bounded with weights tending to zero. The adjoint removes the factor a only from indices divisible by a. Thus the terms of K are supported respectively on a|bn and a|n, with identical output e_{bn/a} when both are present. The former condition means n=a′m; the latter then means d|m. The output is injective, so K*K is diagonal with squared absolute coefficients. The one-term weights are inverse-square logs, and for n=ak the difference is −ABF(log k). The ratio (u+A)(u+B)/(u+A+B)² is below one and increases, so F is positive and strictly decreasing. The strict lattice threshold gives ceil(X)−ceil(X/d) even at integer X, with X=e^(√(AB/t))/(ba′). Expansion of the two fractions gives C=AB(A+B), D=−AB(2A²+5AB+2B²); taking the cube root in the reversed expansion gives U=(C/t)^(1/3)+D/(3C)+O(t^(1/3)). Cubic counting is ceil(e^U)−1 for small positive t. This checks both exact branch counts, the constant exponential prefactor, the scale comparison, and the separate signed populations when a=b. Logarithmic decay gives compact infinite rank but no summability to any finite power. The uploaded verify.py and VERIFICATION.md were inspected, not executed; finite column checks do not establish the asymptotic inversion.

## originality

PASS

The supported distinct result is exact mixed-adjoint monomial spectra with a gcd-dependent branch split, sharp counting at both scales, and opposite signed scales for the diagonal self-commutator. Known non-Schatten theorems for individual operators and the similar unstarred computation are credited, but neither determines these results.

## value

PASS

Comparing two monomial Volterra operators with one adjoint tests natural relative nonnormality. The gcd decides whether the slower scale is present, while the finer scale can be recovered by exact subtraction or by a sign restriction in the self-commutator. These exact spectral and counting statements are more informative than routine compactness or ideal nonmembership, and their leading constants matter when comparing ranks at a fixed small tolerance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
