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

# Reproducibility and scope

Execute `python3 verify.py`; the script uses only the Python 3 standard library. `verification_output.txt` contains the exact expected output for all nineteen conjugacy-class representatives and the concluding success marker. The verifier independently enumerates the finite group, all its subgroups, its action on the Petersen graph's fifteen edges, the orbit-compressed fixed complexes, and every Hasse edge for checking acyclicity. It verifies a homotopy classification via complete acyclic discrete-Morse matchings, not merely homology ranks. It cannot verify absence of unindexed prior literature, claims about larger graphs, or independent mathematical review.
