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

# Reproducible finite checks

Run `python3 verify.py` using a Python 3 interpreter. The deterministic script requires only the standard library. It computes the actual cyclic Boolean update for Rule 154 and independently peels the in-degree-zero vertices from the full functional graph for eight even ring sizes, checking 87,380 possible initial configurations. It compares each state's periodicity with the residue-parity criterion in the theorem, checks 36 ranks of actual iterate images, and separately uses binary Gaussian elimination for 176 half-ring operator-power cases. Finally, it reconstructs all 13 edges of the collision-pair transition graph from the local rule.

Expected successful output:

`VERIFY_OK ring_sizes=8 state_cases=87380 power_ranks=36 binary_matrix_cases=176 pair_graph_edges=13`

The proof covers all even ring sizes analytically. Finite enumeration neither proves the infinite family nor independently validates the literature-priority comparison. No independent scientific audit has been performed.
