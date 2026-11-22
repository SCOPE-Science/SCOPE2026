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

# Reproducibility and limits

Execute `python3 check_fibonacci_curves.py` with Python 3 and no third-party dependencies. The checker prints counts and the exact genus/ramification fixtures and raises an exception on a mismatch. The verification run completed successfully with 192 Fibonacci–Lucas Binet identities, 100 infinity-divisor cancellations, 98 full genus-and-inertia comparisons, and six exact numerical fixtures. The script independently computes the binomial gcd sum and the five-adic sum for each tested exponent.

The mathematical argument for all exponents is given in `RESULT.md`. No finite test is proof of the unbounded assertions or of historical priority. Source arXiv:2611.16283v1 establishes the rational-power relation; the rest is derived via classical Kummer ramification, Riemann–Hurwitz, Lucas congruences, and base-five carries. Arithmetic Galois closure is proved algebraically, not computationally certified. Independent audit has not been performed.
