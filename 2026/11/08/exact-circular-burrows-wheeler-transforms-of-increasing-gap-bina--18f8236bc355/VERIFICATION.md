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

Execute `python3 verify_bwt.py` with Python 3 (standard library only). The script constructs exact zero-gap words; for each, it independently sorts every complete cyclic rotation and compares the full BWT against the claimed explicit expression. Checks cover every increment vector in \(\{1,2,3,4\}^k\), for \(2\le k\le7\) (21,840 instances), plus 17 actual radix-power words. Also checked: number of ones, output length, and the run-count transition for every tested instance.

Successful execution output:

`PASS exhaustive_gap_vectors=21840; radial_prefixes=17; lengths_and_runcounts=verified`

The infinite quantifiers are justified by the structural proof, not by test coverage. This is a self-review, not independent validation or external certification.
