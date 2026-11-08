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

The analytic proof derives stationary Fourier and conditional-generator moment equations and differentiates the resulting inverse-rate moments. Its first and second shape derivatives are explicit strictly signed expectations for every nondegenerate intensity law, not estimated numerical derivatives. The sharp upper envelope is proved through a bounded-variable quadratic inequality with an explicitly characterized equality law.

Reproduction: run `python verify.py` from the same directory. The recorded run passed 228 exact-arithmetic evaluations and all generator, shape-derivative, extremal-envelope and two-point identities. The code uses only Python's standard library. Diagnostic computations cover finitely supported rates, not the full family; the proof covers arbitrary finite, nonnegative rates with positive probability of a nonzero intensity.

The full one-time stationary Fourier transform is already available in Arutkin and Reuveni (2025). No claim of novelty is made for that transform, the Brownian Laplace limit, or the unnormalized second/fourth moment expressions as immediate consequences. Inaccessible or unindexed independent analyses might contain the strict normalized-shape comparison. The results do not establish search-time or dynamical-stability properties.
