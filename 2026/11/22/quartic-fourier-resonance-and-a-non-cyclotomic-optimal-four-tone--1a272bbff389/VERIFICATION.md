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

Run `python3 check.py` using the standalone Python standard library. The program reconstructs the normalized eighth moments by exact integer convolution at spacings 4, 5, 6, 7, 9 and 12 and checks them against the independently derived Laurent identities, including the four interference coefficients. It also compares the second and third convolution powers for the fourth and sixth moments, finds their first difference at the fourth power, tests an exact rational strict-improvement witness, evaluates the two analytical endpoints and performs 180 sampled Haar integral cross-checks. The present check reported all assertions passing.

The proof, not finite numerical testing, establishes the theorem for every integer spacing at least four. It uses exact binomial-block support, a monotone cubic and an algebraic-integrality argument. The numerical minimizer value is an approximation to the uniquely specified algebraic root, not an independently certified interval enclosure. Historical originality remains limited to inspected primary material and published comparison results. Independent audit has not been performed.
