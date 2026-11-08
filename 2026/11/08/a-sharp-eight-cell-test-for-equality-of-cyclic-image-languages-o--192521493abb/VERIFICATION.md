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

The reproducible standard-library `verify.py` directly enumerates all inputs for the 256 elementary cellular automata at each ring length 1–8, partitions the rules by complete output-word sets, and separately builds the Boolean-relation word recognizers. It checks all 256 recognizers against the direct image sets through length 8 and exhaustively searches 156 synchronized finite-state product automata to establish equality for every possible output length within each identified group.

Expected terminal line: `VERIFY_OK`. The exact class table is supplied in `classes.json`. The relevant program output is the sequence of 100 classes at length 8, 99 classes at length 7, class-size distribution 8/75/10/3/4, and the length-eight distinguishing word for Rules 57 and 99. No random sampling, approximate linear algebra or unverified external certificate is used.

The program's completed finite graph reachability is an all-length proof because a distinguishing word exists if and only if some reachable synchronized state has unequal acceptance flags. It does not establish any property of nonperiodic images, longer iterations, or generalized local rules. Independent scientific auditing has not been performed.
