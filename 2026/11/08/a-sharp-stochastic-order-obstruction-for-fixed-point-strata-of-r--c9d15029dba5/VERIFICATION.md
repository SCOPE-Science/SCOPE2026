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

# Verification of the stated distributional comparison

The exact proof in `RESULT.md` consists of the one-descent adjacent-block classification, local descent expectation by partner cases, the ratio of class sizes, and a direct check of the three smallest even comparison pairs. The full stochastic incomparability claim is deduced symbolically and is not extrapolated from experiments.

Run `python3 check_involutions.py` in the extracted directory. The standard-library checker independently builds all involutions through size twelve, groups them by fixed points and descents, computes the class means and first-tail counts exactly, and compares the cumulative distribution functions in the finite edge cases. It also checks algebraic quadratic sign boundaries for all admissible parameter pairs below one hundred. Observed result: `PASS: 4893 exact assertions`.

The finite verification is not a proof at unbounded sizes. Prior full generating functions determine all fixed-point-conditioned descent counts, and possible implicit historical coverage remains unresolved. Independent audit not performed.
