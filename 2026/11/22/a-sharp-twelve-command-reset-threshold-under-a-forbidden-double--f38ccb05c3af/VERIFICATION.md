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

Run `python3 verify.py` in the same directory. This is a Python 3 standard-library program with a fully deterministic exhaustive enumeration of all 65,536 labeled ordered two-letter transition tables on four states. It compares breadth-first search of the subset/last-input graph against an exact-length reachable-family recurrence on every table, with cycle detection for infinite thresholds. It checks the complete 13-bin histogram including the nonresettable bin, the unrestricted-synchronization count, the 24 conjugates of a representative, and the explicit twelve-input reset witness. Successful replay prints `VERIFY_OK` plus the counts and witness masks.

The total number of possible input transition pairs, the finite state-space termination argument, and the two recurrence invariants are specified in `RESULT.md`. These checks substantiate the finite four-state classification only; no larger-state threshold or exhaustive literature-priority check is inferred. Independent mathematical audit has not been performed.
