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

Execute `python checker.py` with a standard Python 3 interpreter. Only the Python standard library is required. Exact `fractions.Fraction` operations represent each single-edge exponential by its transfer probability \(u\); consequently no numerical approximation to an exponential is involved in checking the algebra.

The checker verifies the claimed stationary vector by multiplying it by an independently constructed sweep matrix; the corresponding exact total variation; stochastic row sums; all ascent values; the stationary uniform law for cyclically randomized origins; specific five-state rational examples; and a dimension-free bound example with \(u=3/4\). `check_output.txt` is the recorded output of the actual checker. It performs more than 21,000 exact rational assertions.

A rational transfer probability corresponds to a positive physical step \(h=-\log(1-u)\). The all-dimension proof is algebraic and analytic and does not depend on finite searches. The checker does not establish novelty, general-purpose Markov generator properties, or independent scientific validation.
