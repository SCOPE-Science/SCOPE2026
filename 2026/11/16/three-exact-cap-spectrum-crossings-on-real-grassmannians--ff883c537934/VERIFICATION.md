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

# Verification and limits

Run `python3 VERIFY.py` with packages listed in `requirements.txt`. Exact symbolic checks establish the beta-density normalization of the three sectors, the conditional tensor moment, the three analytic spectral-gap polynomial identities, their crossing-height spacings, and the simple-pole thin-cap constant. The test also verifies the midpoint symmetry in even ambient dimension. Seeded independent Gaussian-QR Haar draws test the **whole** Gram spectrum, rather than one chosen observable, for three small parameter combinations.

Numerical samples are finite and probabilistic; they do not prove the universal theorem. The universal assertions rely on the analytic conditional-moment and beta-integration argument in `RESULT.md`. Historical novelty checks compare actual statements of related literature, without claiming an exhaustive search or independent certification. Independent audit has not been performed.
