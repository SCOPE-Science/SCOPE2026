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

The standalone standard-library verifier `verification/verify.py` reconstructs graph distances by two algorithms, checks the explicit edge-transitivity generators, enumerates both Čech nerves, and verifies three acyclic face-poset matching certificates. It checks the full oriented Hasse graph for each matching, including the relative matching extended by leaving the base unpaired. It independently reduces binary boundary matrices to verify the expected Betti numbers.

Expected outcomes: the intact nerve has 399 matching pairs and 48 critical two-cells; the single-edge-deleted nerve has 338 pairs and 37 critical two-cells; their relative face poset has 61 pairs and 11 critical two-cells. The verifier outputs `VERIFY_OK` upon success. These finite checks provide an exhaustive proof certificate for the specified fourteen-vertex example; they do not prove a result for larger projective planes. Independent audit has not been performed.
