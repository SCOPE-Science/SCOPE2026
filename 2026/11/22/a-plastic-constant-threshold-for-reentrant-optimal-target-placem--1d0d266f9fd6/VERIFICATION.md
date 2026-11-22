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

# Verification of the mathematical claim

The signed derivative is the quartic \(P(u,S)\) divided by a strictly positive factor. Its derivative with respect to \(u>1\) is strictly positive for \(S>0\), which independently proves existence and uniqueness of the optimum. Substitution \(u=e^{b/3}\) gives the fully factored polynomial whose sign is that of \(y^3-y-1\) on \(y>1\). The small- and large-distance limits follow by balances in the same exact equation. No finite sampling is used as a proof of an infinite-parameter classification.

Run `python verify.py`; dependencies are SymPy and SciPy. The checker tests symbolic factorizations, representative parameter signs, finite differences of the original mean objective, and both asymptotic expansions. The computed crossover is approximately 0.42179936148444286 in dimensionless distance and the ratio at \(b=2\) is approximately 0.2709653024650326. These decimals are diagnostic only.

The exact location and uniqueness of the global minimum of \(x_*(L)/L\) are not proved; only that at least one finite global minimum occurs after the sharp one-third crossing. Independent scientific audit is not performed.
