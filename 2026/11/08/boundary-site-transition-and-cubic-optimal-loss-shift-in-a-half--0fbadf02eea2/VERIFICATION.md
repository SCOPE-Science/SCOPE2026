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

The integral representation was checked against the published latest full-text version, arXiv:2605.08056v4, Eq. (15) and Appendix D.2. The proof independently differentiates and bounds its two pieces and verifies the beta-integral coefficient. Run `python3 CHECK.py` (requires numpy and scipy) for the 285 deterministic numerical cross-checks and independent finite-chain propagation examples. Numerical tests are not exhaustive, and no independent audit has been performed.
