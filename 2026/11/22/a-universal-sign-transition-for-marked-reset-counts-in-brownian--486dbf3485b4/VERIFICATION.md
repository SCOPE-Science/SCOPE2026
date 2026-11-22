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

The proof derives the all-rate statement analytically from Brownian first-passage transforms and marked excursion renewal; it does not infer an infinite theorem from finite enumerations. The bundled `check_reset_counts.py` runs on stock Python 3 and independently solves finite Markov-reward equations with exact rational arithmetic. It passed 184 exact rational instances and 3297 identity, moment and sign comparisons. For Brownian test settings with integer distances and resetting rate \(r=D(\log 2)^2\), one-excursion absorption probabilities are rational powers of two. Numerical bisection checks the representative pair \(x_0=4\), \(x_i=1\), \(x_j=2\), \(D=1\). Checks do not establish independent certification or priority. A self-review examined the mathematical proof, boundaries, and pertinent published literature.
