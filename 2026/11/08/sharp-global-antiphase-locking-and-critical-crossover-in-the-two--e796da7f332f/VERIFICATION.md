---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

For K=2h in (0,2], the error u=theta-pi satisfies |u-K sin u|<|u| for 0<|u|<pi; compact strict descent gives global attraction excluding the in-phase fixed point. At K>2 the multiplier 1-K<-1 yields local repulsion. For h=1, g(v)=2sin(v)-v=v(1-v^2/3+v^4/60+O(v^6)); independent exact Taylor expansion gives w_{n+1}-w_n=2/3+3/(10w_n)+O(w_n^-2). Summing after w_n=2n/3+O(log n) yields w_n=2n/3+(9/20)log n+C+o(1). For fixed v0 in (0,1], at h=1-eps the positive decreasing recursion and uniform affine reciprocal-square expansion give eps*w_floor(t/eps)->(exp(4t)-1)/6. Finite-hitting seeds are separately excluded. Checked RESULT.md and verify.py actual frozen blobs; numerical meshes are corroboration, not proof.

## originality

PASS

Best-of-knowledge matching theorem search found no logically dominating already published result after comparing actual statements; relevant uninspected primary literature and older methods are recorded as residual risks.

## value

PASS

The dynamics at a nonhyperbolic flip boundary is a motivated spectral endpoint problem: exact all-initial global stability, the evaluated logarithmic inverse-square correction, and the finite-time subcritical scaling give genuinely distinct critical features on the physical iteration clock. Merely reproducing the local multiplier or the known leading parabolic exponent would not suffice; the sharp endpoint and two-scale law supply value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
