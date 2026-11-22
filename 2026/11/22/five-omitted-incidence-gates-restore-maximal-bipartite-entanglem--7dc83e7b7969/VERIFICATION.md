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

# Verification and scientific limits

The incidence graph is completely specified by the six symbols and their two-subsets/perfect matchings. Execute `python3 VERIFY_RANK.py` and `python3 VERIFY_BINARY.py`; both require Python 3 and no third-party packages.

`VERIFY_RANK.py` uses exact integer fraction-free determinant elimination to verify the unperturbed ten-by-ten minor has determinant \(-1\), every one of the 32 subsets of the five selected deleted gates gives a unit maximal minor, and the final fifteen-by-fifteen matrix has determinant \(-1\). `VERIFY_BINARY.py` separately enumerates all 15 perfect matchings and recomputes binary rank \(10+k\) for all 32 subsets, as well as rank 11 after omitting any one of all 45 original gates. The programs passed with their embedded source text. The algebraic proof in `RESULT.md` establishes the general qudit-dimension conclusion; finite enumeration is not used as an infinite proof.

The main limitations are fixed finite incidence geometry, the specified deletion matching, the point–syntheme bipartition and ideal pure-state preparation. The checked literature does not rule out an unlocated equivalent integer-rank result. No independent audit has been performed.
