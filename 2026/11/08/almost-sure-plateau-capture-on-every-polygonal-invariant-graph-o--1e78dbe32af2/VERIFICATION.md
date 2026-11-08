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

`check_branch_expansion.py` is a standalone exact-integer/rational test of all 16 combinations of four quadrant matrices and four allowable tangent directions, of the two collapsed cases, and of the possible nonzero squared arclength multipliers \(2\) and \(4\). It runs with Python's standard library only.

To reproduce, run `python check_branch_expansion.py` in the directory containing the extracted files. The recorded local execution printed 16 branch results and finished with `PASS: all 16 matrix-direction identities, two plateaus, nonzero length ratios 2 or 4.`

The density theorem relies on the written proof of the finite-branch BV contraction, L1 compactness, and the source's all-parameter open-density result, none of which is certified solely by script output. Independent mathematical audit has not been performed.
