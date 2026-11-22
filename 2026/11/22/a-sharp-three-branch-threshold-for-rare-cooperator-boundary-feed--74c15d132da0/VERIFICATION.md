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

# Verification of the boundary fixed-point classification

Run `python3 verify.py` with Python 3 and no third-party packages. The program uses exact rational arithmetic to check that the rational witness satisfies the switching and game inequalities, that the reduction parameters are as stated, and that the three-branch condition and exact middle-root derivative hold. It also verifies the exact auxiliary eigenvalue \(459/475\), numerically isolates the other two fixed points, and checks their environmental-stability and transverse-invasion signs.

The proof in `RESULT.md` establishes a strict one-to-one reduction, classifies every root by the derivative of the logit function minus a fractional-linear response, and analyzes all multiplicities. Numerical bisection does not prove exhaustiveness; the analytic derivative argument does. The boundary is the model's formal conditional-environment extension, not a guarantee about finite-population invasion or original-model basin selection. Historical-priority checks are literature-bounded, and no independent scientific audit has taken place.
