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

# Verification scope

The mathematical proof is self-contained in `RESULT.md`; `checker.py` uses only Python's standard library and is intended as reproducible arithmetic cross-checking, not a substitute for proof.

The source's macroscopic equations (41) and (43) are reduced by choosing equal intrinsic prey-state reproduction and competition, normalizing the behavioral ratios, and restricting to spatially constant solutions. The positive predator nullcline is \(x=(1+y)/\lambda\) for \(\lambda>0\), after which the prey equation is exactly \(-P(y)/\lambda^2\). This equality is checked for 600 deterministic rational assignments. The exact sample's three states and Jacobian trace/determinant signs are verified using `fractions.Fraction`.

The analytical root count covers all positive parameter triples, while the bistability stability analysis covers \(\lambda_c<\lambda<1\) and \(0<a<a_f(\lambda)\). Endpoints and the double-root fold are handled explicitly in the proof. Finite tests do not establish the universal inequalities; they are proved from the quadratic and Jacobian identities.

The comparison covers the main 2026 source's derivation and stated open problems, earlier open full text with prescribed logistic growth, and a 2024 open predator–prey model with separate carrying-capacity dynamics. One closely related 2019 full text could not be examined. This remaining literature risk is not an independent validation of novelty.
