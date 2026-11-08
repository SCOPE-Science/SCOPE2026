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

# Verification of finite calculations and scope

The analytic result is proved by the four-pair stability partition and exact binomial enumeration in `RESULT.md`. Run `python3 verify_crown.py` with Python 3.9 or newer; no third-party modules are required. The script separately evaluates the complete edge-sum Hamiltonian after every possible single spin flip for small graphs, and checks the prediction against a multinomial-orbit enumeration for larger finite cases. The check produces `PASS 240 comparisons: full graph energies and four-pair orbit counts`.

Finite enumeration alone proves only the checked cases. The all-\(n\) result depends on the symbolic classification, whose critical assumptions are homogeneous positive antiferromagnetic coupling, an edge-deleted matching, positive uniform field, and weak single-flip stability. Marginal integer-field configurations may have zero-energy moves and should not be called absorbing under dynamics that allow such moves. No independent audit or expert certification has been undertaken.
