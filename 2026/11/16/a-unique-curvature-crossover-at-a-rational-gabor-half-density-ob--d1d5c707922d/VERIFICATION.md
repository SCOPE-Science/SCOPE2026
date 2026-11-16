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

# Reproducibility and verification

Run `python3 CHECK.py` with the Python standard library. The checker compares derivative sums of the original Zak series with the hyperbolic closed forms at eight scales, tests the exact curvature ratio, checks rational samples of the positive derivative expression, and probes the two scale limits and the numerical crossover bracket. The saved checker reports 136 successful finite consistency assertions.

The complete quantified proof is in `RESULT.md`: the nonstandard essential step is the explicit factorization of the derivative of the rational function \(H(u)\), with an elementary positive decomposition of the resulting polynomial on \(0<u<1\). The comparison of local areas is deduced from a positive quadratic form, not finite sampling. The checks do not establish exhaustive zero-set classification, a uniform joint limit, global Gabor frame bounds, or independent certification.
