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

The standalone standard-library checker `verify.py` is run as `python verify.py`. It checks the sample formulas by exact rational arithmetic for 3,900 explicitly enumerated nonzero sample vectors, four positive stepsizes, scaling identities, and rational risk integrals. The expected output is `VERIFY_OK 78095 exact checks on 3900 finite vectors`.

The universal proof is independent of these tests: the chi-square near-zero density gives a necessary and sufficient inverse-moment condition, while the bounded angular factor establishes that no singularity is hidden by sample direction. Regular variation of the squared-risk polynomial gives the stated Pareto constants. Finite tests do not constitute a proof of these asymptotics. Independent mathematical audit has not been performed.
