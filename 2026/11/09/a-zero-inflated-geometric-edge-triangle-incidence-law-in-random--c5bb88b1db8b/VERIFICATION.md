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

# Verification and reproducibility

Run `python3 check_edge_incidence.py` using the Python 3 standard library. The checker enumerates all reachable labeled graphs through seven vertices. In each state it enumerates all currently eligible old vertices and edges and validates the exact integer conditional-drift numerators for each edge triangle-incidence class. It verifies the exact relation between edges and triangular 2-faces, checks closed-form limiting identities, and runs a seeded diagnostic at 150000 vertices.

Observed replay: `PASSED 525916 checks`. The checks establish only finite transition identities and numerical consistency; they do not alone prove asymptotic convergence or historical priority. The analytical argument proving almost-sure and total-variation convergence is in RESULT.md. The result has undergone self-review; independent audit has not been performed.
