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

# Reproducible checks and scope

Run `python3 verify.py` with a standard Python 3 installation. The script independently constructs the adjacency relation, enumerates forts, computes minimality by inclusion, calculates maximum disjoint packings by recursive search, and checks fractional-cover feasibility and parameterized optimizer-face conditions. It exhausts all 66 ordered clique-size profiles meeting the stated small-profile bounds and prints `VERIFY_OK` on success.

These finite checks are not a substitute for proof. The unrestricted disjoint-packing formula follows from the hub/no-hub decomposition; the fractional bound and all optimizers follow by summing pair inequalities and examining equality; the ordinary zero forcing number follows from transversal duality. No external mathematical audit has been performed.
