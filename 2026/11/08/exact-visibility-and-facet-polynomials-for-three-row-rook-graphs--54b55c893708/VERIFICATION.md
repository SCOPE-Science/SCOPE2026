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

# Reproducibility checks

`verify.py` is a self-contained Python 3 verifier. Execute `python3 verify.py`; it should end with `VERIFY_OK`. It builds the labelled graph directly from the Cartesian adjacency rule, checks the actual shortest-path definition for each selected pair, tests maximality by trying each absent vertex, and compares all coefficients with the proposed formulas. The checked orders are \(n=2,3,4,5,6\), exhausting \(64+512+4096+32768+262144=299584\) subsets. Formula arithmetic is checked separately for \(n=2\) through \(90\).

Observed facet counts (by set size): \(n=2\): \(\{4:12\}\); \(n=3\): \(\{5:45,6:6\}\); \(n=4\): \(\{6:144,7:72\}\); \(n=5\): \(\{7:465,8:540\}\); \(n=6\): \(\{8:1548,9:3240\}\).

This is a finite computational cross-check, not a proof of all parameter values. The unrestricted proof is the complete column-support classification in RESULT.md. The originality assessment is literature-dependent and is not experimentally certified; the full text of Bryant–Fu (2002) was not available for comparison.
