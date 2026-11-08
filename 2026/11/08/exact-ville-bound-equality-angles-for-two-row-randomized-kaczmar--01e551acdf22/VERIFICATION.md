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

The analytical proof in RESULT.md is the verification basis for the infinite-time statement. It proves the exact switched-projection identity, independence of the switch indicators, a mean-one martingale, almost-sure decay, bounded optional stopping, an equality-if-and-only-if overshoot criterion, and uniqueness of the interior polynomial root.

Running `python3 verify_exact.py` verifies exact algebra in the field \(\mathbb Q(\sqrt5)\) for the first algebraic angle, checks all row-selection strings through length ten at three specified angles, checks the binomial histograms at those lengths, isolates additional algebraic roots numerically, and bounds finite-horizon crossing probabilities by their analytic limits. The script makes no claim to verify infinitely many times or a general proof of uniqueness by enumeration.

Independent audit: not performed.
