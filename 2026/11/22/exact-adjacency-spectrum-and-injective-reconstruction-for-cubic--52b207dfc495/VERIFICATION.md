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

The standalone certificate `artifacts/verify_spectrum.py` was executed in Python 3 with the expected `CHECK_OK` result, integer Gram polynomial, seven exact trace values, and rational primary multiplicities. The checker uses exhaustive generation of the \(6048\) classical theta hexads and proves full symmetry transitivity, so checking a single matrix column of the invariant polynomial suffices. It uses no numerical eigenvalue approximations. All arithmetic in the decisive certificate is integral or rational. The classical geometric correspondence between odd theta characteristics and plane-quartic bitangents is cited from the literature, not reconstructed by this checker. This is a self-review, not independent audit.
