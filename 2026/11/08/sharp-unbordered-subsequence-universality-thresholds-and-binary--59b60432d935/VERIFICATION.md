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

Run `python3 verify_unbordered.py` using Python 3.9 or later. It checks 1,048,564 binary words across full candidate-length and lower-bound comparisons; makes 676 independent direct universal-target comparisons; tests normalized halfwords and reversal/complement through `k=14`; and checks the nonbinary construction for alphabet sizes 3 through 8 and indices 1 through 15. These checks passed in the packaged copy.

The infinite proofs are given in `RESULT.md`, including the greedy-arch characterization and the complete characterization of potentially offending borders. Finite enumerations cannot prove the universal quantifiers. No claim about an elementary formula for the admissible-vector count, and no independent scientific audit, is made.
