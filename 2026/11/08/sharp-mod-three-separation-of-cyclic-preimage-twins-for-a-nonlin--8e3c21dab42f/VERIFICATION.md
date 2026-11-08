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

# Reproducing the mathematical certificate

Execute `python3 verify.py` in the directory containing this file. The executable uses only the Python standard library. Expected summary: `VERIFY_OK checks=57769 edges=128 ones=16`.

The independent mathematical ingredients are the explicit rule and involution factor, the complete finite 64-vertex pair graph with 128 edges, the given 64-entry potential, the reduced-cost check, and the exclusion of a path made exclusively of zero-cost edges from the head to the tail of each 1-cost edge. The last exclusion is a finite exact directed reachability calculation, not a sampled estimate. The program checks explicit witnesses on 200 lengths and the stability of their finite four-symbol window sets; the paper's repeating-word proof explains why that covers all positive lengths. It additionally enumerates all input fibers on cyclic rings of sizes 1 through 12 and checks the factorization against the original five-neighbor rule.

**Limits:** This is a self-reviewed proof with an exact reproducible finite graph computation, not an independent scientific audit. The short-ring enumeration alone would be insufficient for the universal statement. No search result is treated as a uniqueness certificate.
