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

Rotate c into one complementary coordinate. The 2×2 core U=[[0,−k/a],[−kt,1−bt]] dominates the scalar complementary block in norm and spectral radius, including at zero coupling. For k>0 let η=k²/a<b and p_t(λ)=λ²−(1−bt)λ−ηt. The roots have opposite signs, p_t(1)=t(b−η)>0 and p_t(−1)=2−t(b+η), giving the exact convergence interval. Put r=√(η/b). Then p_t(r)=r(r−1)(1−bt) and p_t(−r)=r(r+1)(1−bt), so away from 1/b one root has magnitude strictly greater than r. At k=0 the radius is |1−bt|, with the same unique optimum. The top-left entry of I−UUᵀ is 1−q and its determinant is −q+2bt−[b²+k²(1−q)]t². For k<a the discriminant divided by four is (1−q)(b²−k⁴/a²)>0, and strict Sylvester positivity is exactly between the two roots. Its norm-one boundary includes t=0 only in the zero-coupling continuous extension. For k≥a the fixed first row rules out strict contraction. At 1/b the off-diagonal entries give norm max(k/a,k/b). Transposition preserves the residual norm. In the displayed family the core square is I/2 and the fixed row has norm R, verifying the parity and universal-in-weight lower bound.

## originality

FAIL

The asserted Euclidean frontier and selection regimes are mechanically covered by the earlier codimension-one Type-II result, not merely similar to it. Its trial-norm quadratic at z=1 is exactly the frozen determinant, and its block spectrum and exact norm at α=1/d supply the needed comparisons. Isotropy makes the higher-dimensional extension an identical two-dimensional calculation with a dominated scalar block. A second indexed result states the full safety window in dimension two explicitly, and a general earlier result already treats sharp amplification at fixed spectral enclosure. The unique spectral optimum and the fixed-rate family are checked, but follow by direct polynomial comparison and substitution into the previously analyzed block; this is not a distinct safety frontier.

## value

FAIL

This is a useful interpretation of a known Type-II tuning calculation, but it does not supply a worthwhile new exact frontier. In the stated isotropic model the extra dimensions are dominated scalar modes. Once the earlier norm quadratic and convergence interval are credited, the remaining single-weight spectral comparison and fixed-rate example are direct two-by-two deductions and do not identify a new obstruction beyond the earlier norm/amplification results. No substantively distinct repair is supported by these calculations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
