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
# Verification

Run `python verify.py` from the same directory after installing the SymPy dependency. The checker expands the complete homogeneous polynomial \(h_6\), verifies its equality to the independent power-sum/product expression after centering, evaluates both sharp endpoints exactly and reconstructs both additive deficit formulas. It confirms Dirichlet mixed-moment coefficient normalization using exact rational arithmetic. These finite symbolic checks are sufficient for the displayed algebraic identities but are not a substitute for the analytical global inequalities over all coefficients, whose proofs appear in `RESULT.md`.

The result has no independent audit or external certification. The theorem does not cover nonuniform simplex measures, nonlinear polynomials, other dimensions or arbitrary real exponents.
