---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

For the linear kernel, cross-MMD factors as the first-half mean difference A times the second-half mean difference B. The published studentizer reduces to \(B^2S/s^2\), so the statistic is \(\operatorname{sgn}(B)sA/\sqrt S\). Under the equal-variance Gaussian null, the first-half pooled statistic is exactly \(t_{2s-2}\), while the independent sign of B preserves symmetry, yielding \(\sqrt{s/(s-1)}t_{2s-2}\). The exact cutoff and finite-size anti-conservatism follow, and the quoted tail expansion/numerics were independently checked.

## originality

FAIL

The source paper explicitly defines cross-MMD as a sample-split inner product and its studentizer as the sample variance of projected first-half variables. Specializing those published formulas to the linear kernel immediately factors out the second-half mean difference and leaves, up to a deterministic scale and independent sign, the classical pooled equal-variance two-sample t statistic. Thus the exact finite t law and exact t cutoff are direct textbook consequences of the published statistic definition; the first-order tail correction is then a standard Student-vs-normal expansion. The absence of this special case in the source text does not overcome implication coverage.

## value

FAIL

The finite calibration warning is useful pedagogically, but the result is a direct textbook Gaussian-linear specialization of the published cross-MMD statistic. Once the reduction to pooled t is made, the exact law, cutoff, anti-conservatism and first-order tail correction require no new structural argument. Under the stated value bar this is not an independent mathematical gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
