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

# Reproducibility and limits

Run `python verify_dgt.py` under Python 3 with SymPy. The checker recomputes the four-dimensional exact transition and factors the invariant unit root; compares the exact cubic coefficients, finite Schur signs and limiting factorizations; verifies the first-order negative-network expansions and the rational stable/unstable witness; tests irreducibility modulo seven; and runs a supplementary exact-rational grid of stable test cases. It does not replace the proof that all possible stable steps obey the asymptotic upper bound.

The analytical argument uses the classical necessary-and-sufficient Jury/Schur criterion for a real monic cubic and polynomial continuity. Strict inequalities apply only in the domains specified in the result. Statistical or experimental conclusions, high-dimensional graphs and time-varying parameter rules are not addressed. There is no independent mathematical audit.
