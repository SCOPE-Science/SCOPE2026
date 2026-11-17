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

# Reproducibility and limits

Run `python3 verify.py` (standard library only) from the directory containing the files. The checker enumerates all part-count vectors for each integer scale 1 through 7 with exact binomial multiplicities, checks every one of the 65,536 labelled vertex words at size scale one using explicit graph adjacency, and directly checks all possible frozen-word occupancies through scale four. The program prints exact counts and terminates with `VERIFY_OK` when all assertions pass.

The infinite theorem is proved using exact update inequalities, a complete 16-word homogeneous-part table, a disjoint-sum uniqueness argument, and a finite-state threshold potential. Computational checks by themselves do not establish the theorem for arbitrary scale. Some historical papers were only partly accessible and independent mathematical validation has not been performed.
