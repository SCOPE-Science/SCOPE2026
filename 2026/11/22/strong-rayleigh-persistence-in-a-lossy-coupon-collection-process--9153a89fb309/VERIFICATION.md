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

# Reproducible verification

Execute `python checker.py` with Python 3 and SymPy installed. The program uses exact rational numbers (`fractions.Fraction`) to build the count polynomial recurrence and, independently, to evolve every subset state under a uniform draw and independent per-label post-draw erasures. SymPy counts the real nonpositive roots of rational-coefficient polynomials exactly.

The completed execution reported `PASS: 3960 exact finite-state / polynomial / real-root assertions`. Coverage: all alphabet sizes \(1\le n\le6\); four changing loss schedules per size, including zero, unit, and nontrivial rational loss rates; up to seven steps. Assertions compare complete state distributions, normalization, count-polynomial coefficients, exchangeability of each subset probability, and all polynomial roots. The exact check is finite and cannot establish the universal theorem; the polynomial interlacing proof in `RESULT.md` establishes all \(n\) and all finite \(t\).

The formula is contingent on uniform arrivals, independent losses of every held coupon, a common probability across labels within each step, and observation after loss. The Bernoulli variables in the count-law factorization are auxiliary and are not the individual physical coupon indicators. Mathematical priority remains subject to independent assessment.
