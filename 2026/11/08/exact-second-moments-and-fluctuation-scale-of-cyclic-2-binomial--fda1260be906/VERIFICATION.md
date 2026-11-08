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

The standalone verifier computes complete scattered-subsequence length-two signatures for each cyclic rotation, independently of the indicator and moment formulas. It checks the collision identity, exact first and second moments, and known boundary criteria for all coprime pairs \((m,h)\) with \(2\le m\le8\), covering 25,180 labeled words. Command: `python3 VERIFY.py`. Expected final line: `DIRECT_TYPES_AND_BOTH_MOMENTS_OK 25180`.

Exact rational arithmetic is used for the two finite moment identities. The asymptotic statements are mathematical consequences of the local hypergeometric estimates and dominated Riemann sums given in the proof, not of finite enumeration. Independent mathematical audit: not performed.
