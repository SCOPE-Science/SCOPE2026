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

The included `certificate.json` contains the integer coefficients of the proposed numerator, denominator, and sixteen polynomial solution coordinates. `verify.py` recomputes every polynomial identity in \((I-T(z))H(z)=Q(z)e\) and \(ze^{\mathsf T}H(z)=P(z)\) using integer convolution, then verifies the first forty-five power-series coefficients and exhaustive direct subsequence membership/deletion conditions in fifteen finite cases. The rational identity plus the mathematical transfer correspondence proves the exact infinite formula; exhaustive finite checks do not substitute for this argument. The source paper's unrelated claims are not being independently re-certified.
