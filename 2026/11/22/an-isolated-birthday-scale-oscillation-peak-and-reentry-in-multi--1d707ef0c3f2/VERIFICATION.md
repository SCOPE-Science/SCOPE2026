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

# Verification

Execute `python3 check_plurality.py`, `python3 check_unbalanced.py`, and `python3 check_occupancy.py` from a directory containing these extracted files (Python 3 standard library only). Their expected console records are embedded in `check_output.txt`, `unbalanced_output.txt`, and `occupancy_output.txt`; the actual calculations were executed and all assertions passed. One checker exhausts each balanced colored state space up to five colors on six vertices; a separately designed checker tests the full unequal-shore five-shell identity on 27 cases; a third verifies occupancy counts against direct enumeration. The asymptotic and all-size claims depend on the mathematical proof in `RESULT.md`, not on a finite experiment. No external or independent audit has been performed.
