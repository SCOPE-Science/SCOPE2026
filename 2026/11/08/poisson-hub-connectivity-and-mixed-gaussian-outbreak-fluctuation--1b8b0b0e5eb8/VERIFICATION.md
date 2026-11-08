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

# Verification details

Run `python verify.py` using Python 3. The script enumerates exactly all three-hub incidence patterns on networks with one through four ordinary vertices for three independent rational probability parameter sets; it checks exact source-component probability identities and normalization. It also confirms the exact pair/triple cell decomposition and numerically bounds the finite-size discrepancy between source-component probabilities and their independent-edge limits for three large sizes. The observed result was `PASS: 96 deterministic exact/arithmetic checks`.

The all-size proof is contained in RESULT.md. Its decisive steps are the one-vertex incidence pattern law, union bound excluding triple hubs, mixed Gaussian/Poisson moment-generating-function limit, and component mapping; finite enumeration is not an infinite proof. A total variation rate is proved by a rare-cell multinomial-to-independent-Poisson coupling.

No independent audit has been performed. Historical-priority equivalence in other terminology remains possible.
