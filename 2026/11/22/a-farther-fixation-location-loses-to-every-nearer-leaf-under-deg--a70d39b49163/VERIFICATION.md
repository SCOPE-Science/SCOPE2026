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

Execute `python3 check.py` in the directory containing the science files.

The checker independently compares (1) an exact gamma-Laplace coefficient formula and (2) dynamic-programming absorption probabilities from a monotone colonization Markov chain for 17 choices of the number of short branches. It also verifies all three displayed exact fractions for the nine-vertex witness, the strict difference, and the elementary moment bound at three additional values. All calculations are carried out using Python `fractions.Fraction` integers without numerical approximation.

The proof of the all-family statement is mathematical: rate-one mutant reproduction and independent directed-edge Poisson thinning, followed by an exact conditional integral and the inequality \(1-e^{-x}\le x\). Finite checks are sanity tests, not a substitute for this proof. The comparison has not been independently reviewed or empirically validated.
