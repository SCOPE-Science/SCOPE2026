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

# Reproducibility

Run `python3 check_factors.py`. The checker uses only the standard library, enumerates the complete digit-reachable state graph, proves strong connectivity by a reverse traversal, finds a self-loop, solves stationary weights with exact rational elimination and checks the original balance equations. It enumerates all state/residue/even-length combinations through the first empty length and verifies the claimed factor families, the individual rational densities, the total numbers of distinct factors and the exact occurrence states for the longest words.

The bounded direct checks of the first 512 parent values are regression checks only; the exhaustive finite-state reduction, proved in `RESULT.md`, is what connects the checker to all positions in the infinite words. The reviewer status is not independent certification.
