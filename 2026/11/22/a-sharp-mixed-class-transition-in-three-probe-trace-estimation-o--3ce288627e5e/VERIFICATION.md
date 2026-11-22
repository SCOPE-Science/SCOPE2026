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

The analytic argument in `RESULT.md` establishes the universal claim for all integers \(n\ge3\) and all real \(\mu>0\). The supplied Python standard-library checker is supplementary, not a substitute for the uncrossing proof, the exact gain formula, or the strict classification of equality cases.

Run `python verify.py` from the directory containing this document. `VERIFY_OUTPUT.txt` records a successful execution with 35,610 assertions. The tests use exact rational arithmetic: exhaustive unlabeled three-class partition comparisons for \(3\le n\le6\) at nine rational weight ratios; independent full-matrix Green inversion and matrix-based variance checks for \(3\le n\le5\) at three rational shifts; and discrete gain checks over further integer sizes. Exhaustive enumeration applies only to those finite dimensions and test parameters. The exact threshold for general real screening is established in the written proof.

No external independent audit has been performed. The originality comparison is limited to accessible full mathematical statements and indexed searches described in `REVIEW.md` and `AUDIT.json`.
