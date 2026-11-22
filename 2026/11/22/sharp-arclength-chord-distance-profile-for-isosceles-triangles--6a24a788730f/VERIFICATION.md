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

# Computation and proof checks

The deterministic `verify.py` computes exact rational lower bounds for the continuous positive function \(G(t)\) on every member of a 512-piece rational cover of \([1/8,15/8]\); it does **not** infer an infinite assertion from a finite sample. It uses the first 160 positive terms of the atanh power series, explicitly bounded geometric remainder tails, and fixed-point enclosures rounded outward at scale \(10^{28}\). Each range operation encloses its full interval. The least certified rational lower bound is greater than \(0.5766\); the polynomial/logarithm inequalities for both outside subintervals are proved in `RESULT.md`.

Run `python3 verify.py` using a standard Python 3 interpreter; no packages or data downloads are needed. Separately, two-dimensional numerical integration over all pairs of triangle sides agreed with the exact profile at base ratios \(0.2,0.6,1,1.5,1.95\) within \(8\times10^{-12}\) (validation only). Symbolic differentiation also reproduced the derivative identity, the endpoint asymptotic series, and \(R''(1)=4(1-\log3)/81\). The global proof still requires the written analytic integration, small/large parameter tail estimates, and interval enclosure logic.

No independent external mathematical audit has been performed. Novelty priority is best-knowledge subject to unindexed earlier literature. The theorem is restricted to independent boundary-uniform points on nondegenerate isosceles triangles.
