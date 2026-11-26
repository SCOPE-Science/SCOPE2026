---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For k=u+iv, divide |P_k(iy)|²−1 by y² at nonzero y to get the convex quadratic |k|²y²−2vy+1−2u. For A=ah>0 and B=bh>0 the exact endpoint constraints are disks centered at (1+iA)/A² and (1−iB)/B², with radii A^−2 and B^−2. Squared center distance minus squared sum of radii is ((A+B)²−4)/(A²B²). At A+B=2 the weighted division point is uniquely k=(2+i(A−B))/(A²+B²). Substituting gives |k|²=u and 1−2u=−uAB, hence the stated factorization and exact axis interval. In fact endpoint sufficiency for arbitrary k when both widths are positive follows from convexity of the bracket. If B=0, stability near zero gives u≥1/2, while the nonzero endpoint disk requires u≤2/A²; equality at A=2 picks its unique rightmost point (1+i)/2. Conjugation handles A=0. For real k, the nonzero radius equals sqrt(2u−1)/u when u>1/2, bounded by 1 with equality only at u=1. This verifies the example, the gain, and the zero-width boundaries. The factor and normal-matrix realizations follow by multiplication and the spectral theorem. The proof is scalar/normal and does not assert nonnormal contractivity.

## originality

FAIL

Direct theorem-level overlap: the indexed November 2 finding already gives the same mixed-sign whole-interval feasibility frontier, unique complex optimizer, factorization, real optimum and exact gain. The one-sided cases excluded by its positive-width hypotheses were separately established in George et al., Theorem 1. Combining those cases does not leave a distinct substantive mathematical claim. This is demonstrated coverage, not an inference of authorship or priority from an index date.

## value

FAIL

The exact real-versus-complex step trade-off is a useful question for asymmetric imaginary spectra. The submitted mathematical contribution, however, is the already covered positive-width trade-off with already known one-sided optima appended; the rescaling, explicit example and consolidation into a single formula do not supply a distinct valuable result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
