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

# Verification record
The standalone `VERIFY.py` builds complete multipartite graphs from each part profile, evaluates general position using shortest-path distances, and directly enumerates the exchange graph without assuming the pure/rainbow decomposition. The all-size/all-batch counts are compared to the closed formula. The program was actually executed and returned `VERIFIED_PROFILES 1036`, `COMPONENT_COMPARISONS 2534`, `VERIFY_OK`. Mathematical soundness for unbounded input sizes comes from the proof, not from exhaustive finite testing. The manuscript was checked against three accessible primary full-text sources, and novelty remains historically provisional.
