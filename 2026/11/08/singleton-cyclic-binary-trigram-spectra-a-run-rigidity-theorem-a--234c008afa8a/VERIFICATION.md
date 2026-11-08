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

# Reproduction and scope

The complete proof is in `RESULT.md`; run `python3 verify.py` from this directory to replay the finite computational checks using Python 3's standard library. The checker generates all binary words of lengths \(1\) to \(19\), retains a lexicographically least representative per cyclic rotation class, groups these necklaces by their actual eight-component cyclic trigram count, and compares each computed fibre with the predicted run-type singleton condition. It separately derives generating function coefficients by summing allowed run types and checks the rational recurrence through degree \(120\) and verifies the exact formal rational identity by polynomial arithmetic.

The checks passed for \(1{,}048{,}574\) linear words and \(58{,}833\) cyclic classes; complete computation output is reproducible by executing the embedded source. Enumeration of bounded lengths is not claimed to prove the infinite theorem; the proof comes from the run-statistics identity, the weak-composition classification, and the cyclic group orbit count. The status in the front matter records absence of independent review, not a completed external validation.
