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

# Reproducibility and checks

Run `python check_tail.py` with Python 3 and SciPy. The program uses exact `fractions.Fraction` binomial probabilities, normalizes the mixture over sampling budgets \(1\le m\le14\), compares the far-tail identity against the exact Cauchy tail at multiple thresholds, and independently integrates the conditional density using endpoint regularization for seven values of \(\rho\). The code reports **PASS: 105 finite arithmetic checks**, with additional exact-fraction normalization assertions.

The all-integer result is analytical: it requires the independence of the sampled Hadamard sign products, the Gaussian quotient identity in the two collisions, and uniform boundedness of the finitely many noncollision conditional supports at each fixed \(m\). No finite checker establishes moment divergence, novelty, global generality, or priority.

The main source's printed Gaussian-diagonal ratio is reused with attribution. Its Section 3 constant-probability failure statement is not treated as a proof of the exact moment law. No independent mathematical audit or independent validation is represented here.
