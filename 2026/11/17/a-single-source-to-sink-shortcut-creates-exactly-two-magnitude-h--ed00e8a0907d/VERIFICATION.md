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

`python3 check_shortcut.py` reproduces `check_shortcut.out` in this package. It constructs 29 small layered source-to-sink digraph configurations (some missing between-layer arcs), adds the direct source-to-sink shortcut, enumerates all magnitude tuples from directed distances, computes the signed internal-face boundary matrices and reduces their ranks over \(\mathbb F_2\) and \(\mathbb F_3\). The recorded 56 comparisons passed: only the two predicted bigraded ranks increase, both by one.

The checker is a finite error-detection aid, **not** a proof for arbitrary graphs and **not** a certificate excluding integral torsion. The integral correctness argument compares actual chain groups and differentials over \(\mathbb Z\); its decisive steps are that the changed arc affects only distance \(d(s,t)\), the other endpoint complexes remain identical, and the old terminal augmentation is replaced by the unaugmented complex. Those steps are proved in `RESULT.md`. Independent mathematical audit has not been performed.
