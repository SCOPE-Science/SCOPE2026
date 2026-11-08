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

# Reproducibility

Run `python3 verify.py` from a directory containing the standalone source. It uses only the Python 3 standard library. Each tested colouring is checked directly against all missing matched pairs, with a rainbow two-edge path required for each pair.

## Actual checks

- Exhaustive original-definition evaluation of all \(2^4\) and \(2^{12}\) named edge-colourings for \(m=2\) and \(m=3\); comparison of *all coefficients* of the polynomial.
- Independently constructed histograms for every simultaneous bad-event intersection at those orders; these must equal the blockwise product generating functions.
- Exact rational arithmetic checks of the Bernoulli-weighted formula at red-edge probabilities \(1/4,1/2,3/4\).
- Polynomial computations at \(m=2,3,4\), including nonnegativity, red/blue reciprocal symmetry and total counts \(10,3416,15775808\).

A successful replay ends with `VERIFY_OK`.

## Limits

The exhaustive examples are small and are not a substitute for the general proof. No numerical experiment alone establishes the infinite sum or asymptotic limit. The proof uses block factorization, inclusion–exclusion, fixed-order event intersections, and Bonferroni truncation. Independent audit has not been performed.
