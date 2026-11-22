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

# Verification and reproducibility
The proof is in `RESULT.md`. Re-run from this package with `python3 verify_reach.py`. The script uses only Python's standard library. It computes the rank of coordinate evaluations on a recurrence kernel using free initial data and modular Gaussian elimination; it does not implement the quotient-ring proof used to derive the prediction. It executes 4,326 finite exact checks. The expected line is:

`PASS: 4326 exact recurrence-matrix rank comparisons; no exhaustive infinite claim`

The explicit count is a finite test count, not an exhaustive proof for all finite fields, coefficients, spacings, and times. The universal statement is justified analytically by the invertible recurrence and by the order of vanishing of \(z^h-\zeta^h\) at \(\zeta=-a/b\). The checker tests prime fields for characteristic \(2\), \(3\) and \(5\); extension fields follow from the proof because the nonzero leading derivative criterion remains valid. The result is restricted to full bi-infinite shifts and two-term scalar rules.

The source date refers to the first public version of arXiv:2611.16746, not subsequent publications. No independent audit has been conducted.
