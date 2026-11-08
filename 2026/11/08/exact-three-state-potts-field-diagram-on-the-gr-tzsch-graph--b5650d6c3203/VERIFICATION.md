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

# Reproduction and limits

The self-contained `verify_groetzsch.py` checks all \(177147\) labeled three-state assignments and independently extracts the full bivariate generating polynomial by eliminating the five shadow vertices. No random testing is used. It checks all occupancy-sector minima and counts, the exact rational coexistence fields and multiplicities, and the defect-edge orbit totals. Execute `python3 verify_groetzsch.py` using Python 3 and its standard library.

These complete finite computations, together with the exact combinatorial identity proved in `RESULT.md`, certify the finite mathematical claim. They do not prove any statement about larger graph families, finite-temperature thermodynamics, or historical uniqueness. Independent audit has not been performed.
