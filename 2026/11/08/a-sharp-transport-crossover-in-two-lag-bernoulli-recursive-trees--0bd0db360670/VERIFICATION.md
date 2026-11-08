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

# Reproducibility checks

Run `python3 verify.py` with Python 3 and SymPy. The standalone checker enumerates every independent Bernoulli attachment configuration through 11 vertices and independently computes distances by breadth-first search, Wiener sums by edge cuts, the known Kemeny/Wiener relation, the deterministic depth-distance bound, and stationary-label-prefix degrees. For trees through 6 vertices it additionally solves exact rational Markov hitting-time equations. It checks every possible single-bridge location through 99 vertices, an independent three-arm polynomial identity for arm lengths up to 11, and four finite-size conditional critical curve diagnostics. The observed output was `VERIFICATION_OK assertions=20859`.

## Analytic verification and limits

The all-size identity is proved by edge-cut summation, not finite enumeration. The limiting law uses independently sampled ancestral label decrements, Hoeffding concentration, a union bound over attachment positions, and the longest-zero-run tail. The exact critical conditional result uses elementary binomial-to-Poisson convergence and a uniform single-bridge position. The full distribution with two or more bridges in the critical regime, an asymptotic error constant, and a mixing-time statement were not established; the finite checker does not prove any infinite assertion.
