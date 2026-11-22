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

The full proof uses the published Type-A alternating-interval theorem for distinct single-deletion descendants and an explicit formal-language decomposition of the two boundary contexts. The scripts provide corroboration, not a replacement for that general proof.

`python3 verifier_bruteforce.py` directly constructs deletion-output sets and checks every unordered pair for the listed finite parameter ranges; the run log is `bruteforce_run.txt`. `python3 verifier_recurrence.py` independently counts admissible contexts by terminal-run-state dynamic programming and checks the rational series using integer polynomial recurrences; it examines all lengths through 100 for 64 alphabet/run-cap pairs.

All included programs are Python 3 standard-library scripts. The limiting distribution and the mean-degree asymptotic are proved by a simple, unique dominant pole, rather than inferred from finite numerical samples. No optimal code size, external certification, or independent audit is asserted.
