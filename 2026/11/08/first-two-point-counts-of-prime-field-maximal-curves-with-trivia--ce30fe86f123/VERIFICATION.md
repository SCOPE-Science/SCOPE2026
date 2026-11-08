---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification and scope

The argument is universal for every odd prime \(p\) and integer \(n\ge2\). The key independent mathematical checks are: identification of both rational off-chart places; the \(\mathbb F_p\)-fiber at \(u=-1\); the kernel and image of the \(\mathbb F_p\)-linear map \(v\mapsto uv^p+v\) on \(\mathbb F_{p^2}\); the norm-one dichotomy \(u^{(p+1)/2}=\pm1\); and the counting formulas.

The standalone script `verify_point_counts.py` exhaustively enumerates finite fields, using nonsquare quadratic presentations in odd characteristic, for nine parameter pairs \((p,n)\). Its successful terminal line is `ALL_EXACT_FIELD_CHECKS_OK`. The implementation includes the two off-chart places explicitly; it does not infer their existence from computation. Exact enumeration for finite examples does not certify the all-prime theorem, which is established by the proof in RESULT.md.

No computer algebra package, network access, specialized theorem prover or external certificate is necessary to replay the code. No independent mathematical audit has been conducted.
