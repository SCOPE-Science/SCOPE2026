---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

FAIL

The marginal ratio laws and gamma moments at RESULT.md:22–46 are correct. In row-space coordinates G=[A;B], z=A†a and an orthonormal basis K of ker A give independent standard Gaussian Bz/||z|| and BK conditional on A, since z is orthogonal to K. The physical minimum projects Bz onto the orthogonal complement of range(BK), of dimension d−ℓ, while the raw rule keeps all d−r coordinates. The common scale is ||z||²/||a||², the inverse of a chi-square of dimension ℓ−r+1 by Schur complement; the numerator laws are independent of this scale. Integrating at zero gives the stated moment threshold. However, line 48 claims an improvement by a factor of expected nullspace squared error for all ℓ>r. For ℓ=r+1 both expectations are infinite, e.g. r=1, ℓ=2, d=3, so there is no such finite-factor reduction in expected error. The claim would require ℓ≥r+2; the samplewise ordering survives. When describing exact feasible corrections for individual sketches, G having full column rank is also not enough on its own: e.g. J=(1,0), G=(0,1)ᵀ makes JG zero. The full-row-rank property holds almost surely for the random sketch. The rational witness gives 7/2 versus 19/10 by minimizing z₁²+z₂² versus 1+9z₁²+z₂² subject to z₁+z₂=1. The supplied verification/check.py was inspected, not run; its reported 1,742 finite checks cannot validate moment divergence. No repair is delivered because correcting the finite-factor claim leaves the already covered comparison below.

## originality

FAIL

A distinct public record directly covers both same-span physical-error marginals, their moment range and their squared expectations; it additionally gives a full-span case and a tail constant. Whitening the row equations reduces the entire assigned model to its orthonormal-row formulation without changing the coefficient minimizer, the physical minimizer or the comparison. The matching record is dated later than the frozen result; this is verified equivalent public coverage at review, not a determination of earlier discovery, attribution, or provenance.

## value

FAIL

Physical tie-breaking within an unchanged span is a worthwhile question, and the moment blow-up is substantively relevant. But the exact invariant and the threshold—the claimed contribution—are already available in the matching public comparison. Whitening and adding the row-space norm do not supply a new invariant or consequence, and the small rational example illustrates the very same minimization without an independent gap to resolve.

The dated certificate retains the supplied scientific assessment, sources and limitations.
