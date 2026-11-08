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

# Mathematical verification

The theorem's key chain is: Pareto extreme-point convergence; deterministic edges within any fixed rescaled hub set; a vanishing fraction of vertices touching smaller neighbors; conditional empirical concentration for fixed hub cutoffs; passage to the limiting Poisson-environment functional; Poisson thinning and exact endpoint event.

Run `python verify_local_clustering.py`. The checker independently evaluates deterministic finite identities and integrations (without external data). Its calculations support the normalization, the mean parameter and the exact Poisson endpoint probability. The script does not prove convergence in law; that is established by the arguments in `RESULT.md`.

The claim uses the convention that local clustering is zero when the degree is zero or one; this convention matters for the random limiting law. The unit atom is a statement about the *limiting distribution* and is not an assertion that the finite graph is complete with positive probability. The analogous soft exponential kernel does not have the unit atom, although its qualitative non-self-averaging and local clustering are established in the cited literature.

Independent audit has not been performed.
