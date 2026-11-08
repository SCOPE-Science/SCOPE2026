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

The proof is self-contained apart from standard linear algebra of finite-dimensional vector spaces. The checker uses only Python's standard library and can be run with `python checker.py` from the package directory. It enumerates every pair of idempotent maps for carriers of size at most four; it also constructs the optimal examples for \(1\le r\le6\). Its printed terminal line is `BUNDLED_DISAGREEMENT_DYADIC_PERIODS_OK`.

The decisive infinite steps are: (i) the constant-one valuation lies in the kernel of disagreement; (ii) a stable-image automorphism of exact order \(2^r\) has nilpotent \(S+I\) of index exceeding \(2^{r-1}\); (iii) the explicit alternating-retraction frame induces a single Jordan shift of length \(2^{r-1}+1\). These facts prove the result for all \(r\), beyond the finite checker range.

The directly relevant 2018 primary literature has not been read in full. No independent mathematical audit has been performed. Computational enumeration does not independently prove originality.
