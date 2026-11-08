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

Run `python3 verify.py` using the Python standard library. The script checks all attachment histories through seven vertices, all possible next parents and all existing vertices, verifying exact drift and variance inequalities. It also checks exact expected degree-square sums, five rising-factorial moments and seeded finite simulations. A completed run reports `PASS: 53992 finite exact-rational and seeded diagnostic checks`.

The theorem beyond finite tree sizes is established by the proof in `RESULT.md`; no finite enumeration, simulation, timeout or numerical convergence is treated as an infinite proof. The first-order maximum-degree lower scale is proved independently through moments, rather than inferred from simulations. The proof's quantitative logarithmic factors are safe bounds, not optimality certificates. The public package is not an independent validation or certification.
