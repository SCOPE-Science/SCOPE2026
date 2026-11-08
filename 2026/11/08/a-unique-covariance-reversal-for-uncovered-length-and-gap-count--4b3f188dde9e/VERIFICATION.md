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

The argument uses exact Dirichlet-simplex one- and two-coordinate tails, a layer-cake integral, a one-turn derivative test, and a first-order asymptotic expansion. Each is provided explicitly in RESULT.md.

The included standalone `checker.py` uses only Python's standard library. Run `python3 checker.py` next to this file; it passed 5,657 finite exact-rational and numerical checks, including separate polynomial integration for the cross-spacing expectation. The finite sign grids and asymptotic checks corroborate, but cannot establish, the infinite classifications. The mathematical proof carries those classifications.

The full Holst–Hüsler (1984) article was not accessible for a definitive claim-to-claim comparison. Its abstract explicitly concerns joint limit distributions of these observables, so the asymptotic novelty has an unresolved precedence risk. The self-contained exact finite-parameter sign theorem is the main claim. Independent verification has not been performed.
