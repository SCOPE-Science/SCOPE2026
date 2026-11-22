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

# Reproduction and limits

Run `python3 check_rps.py` in the directory containing the supplied files. The checker uses only the Python standard library and deterministically passed 8,568 assertions. It independently calculates the published recursively normalized product and compares it with the binomial-convolution expression using exact rational arithmetic, checks interval-count geometry on finite alphabets of spacing positions, verifies the explicit \(n=2\) product, and evaluates the beta/gamma constant numerically.

The full theorem for arbitrary fixed \(n\) rests on the analytic proof in `RESULT.md`, not on those finite checks or simulation. The reported 25,000,000-draw check is an additional stochastic diagnostic and is not a reproducibility prerequisite or proof of an infinite asymptotic. The theorem makes no finite-quantile error claim, no interchange of \(n\) and tail limits, and no claim about estimated-null or dependent observations.
