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

# Reproduction
Run `python3 check.py` using Python 3.10 or later, with only the standard library. The script independently builds the full signed projection kernel at each vertex and exactly sums over the entire \(2^d\)-point input space for the tested dimensions; it does not reuse the claimed closed formula in those kernel calculations.

# Checks completed
Exact finite-rational evaluation of 364 corner/dimension/bias combinations across dimensions 2–9 and seven rational biases, including resonant examples. Separate exact-rational spot checks of the piecewise conditional kernel increment. Numerical binomial-to-Poisson and central-limit corroboration samples in large dimensions. The universal all-dimensional conclusions follow from the written algebraic and probabilistic proof, not from those finite tests.

# Scientific limits
A finite batch of exact checks cannot certify all \(d\), all real biases or every limiting sequence; proof of those statements is analytic. External peer review and independent audit remain unperformed.
