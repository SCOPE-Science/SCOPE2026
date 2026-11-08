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

Reproducibility: execute `python3 verify_rook.py` and `python3 verify_words.py` with Python 3. No external packages are needed. The corresponding captured standard outputs are in `verify_rook.out` and `verify_words.out`.

The rook-board script directly tests all candidate minimal dominating vertex subsets of size at least \(n\) and checks all one-vertex exchanges for \(4\le n\le7\). The word script verifies the exact counts and all-pairs graph diameter, with exhaustive BFS for \(4\le n\le9\). Both tests passed when run independently. These finite checks are supplementary to the general proof in `RESULT.md` and do not establish historical priority or provide independent scholarly validation.
