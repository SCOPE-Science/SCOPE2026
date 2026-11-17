---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

PASS: for Y=(1/2,1] under map right branch (y-1/2)^B and subsequent left doubling, R=1+floor(B Z), Z=log_2 1/(y-1/2)≥1. For integer n, {R>n}={BZ≥n}; conditional Pareto tail is min(1,(Z/n)^kappa). Source induced stationary density bounded on Y implies P(Z>z)=O(2^-z), finite C_kappa. Layer-cake gives exact deficit and O(2^-n/n). Conditional mixed tails converge to kappa-size-biased Z independent of Pareto overshoot by dominated convergence; tower mass finiteness iff E R<∞ iff kappa>1. Independently checked exact integer returns (Z,B)=(2,2),(3,3),(4,5): R=5,10,21. Source stationary law is NOT asserted uniform and numerical uniform test only diagnostic.

## originality

PASS

PASS best-of-knowledge: original Inoue–Toyokawa supplies invariant measure and infinite-mass side but not this exact return-clock tail formula, exponential correction, stationary depth-size bias and conditional overshoot law in inspected accessible preprint; generic Breiman/Pareto product results are prior tools.

## value

PASS

PASS: provides an exact regenerative return distribution, sharp moment/finite-mass boundary, and explicit rare-excursion depth mechanism for a natural published random intermittent map; the invariant-entrance constant is meaningful despite lacking closed-form density.

The dated certificate retains the supplied scientific assessment, sources and limitations.
