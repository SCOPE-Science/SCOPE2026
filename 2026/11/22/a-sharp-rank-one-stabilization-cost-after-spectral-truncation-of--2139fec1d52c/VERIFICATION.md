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

`verify.py` checks the exact scalar Riccati cancellation and squared optimal-distance ratio in the quadratic extension \(\mathbb Q(\sqrt2)\) for several values of \(K\), finite-dimensional closed-loop matrices, and candidate rank-one approximants approaching the marginal stability boundary. It is executed with `python3 verify.py`. These computations corroborate, but do not replace, the universal analytic proof and do not constitute an independent audit. The theorem allows all \(n\ge2\) and all real \(K\ge3\); the code evaluates a finite sample of integer \(K\) and dimensions.
