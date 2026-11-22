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

# Exact verification

Run `python3 CHECKER.py` with Python 3 and no external packages. The script generates \(
ho(T)=T\otimes I+I\otimes T\) from matrices and constructs all constraints defining the pointwise algebraic reflexive hull of that action.

The exhaustive checks of every nonzero tensor in \(V\otimes V\) for generator rank two over \(\mathbb F_3\) and \(\mathbb F_5\) give hull dimensions four and four. In generator rank three over \(\mathbb F_3\), all 169 projective decomposable tensors alone force dimension nine, which matches the full image dimension of \(
ho\). The script also checks, for every nonzero \(2	imes2\) candidate mismatch \(A-S\) over \(\mathbb F_3\) and \(\mathbb F_5\), that some vector and invertible diagonal tensor violate the necessary skew-adjoint two-local matching equation, excluding respectively 80 and 624 candidates.

Successful output ends with `ASSOCIATIVE_LOCAL_DERIVATION_CHECKS_OK`.

These are separate finite-field calculations, not an exhaustive infinite-field proof or external certification. The all-field proof is in `RESULT.md`. The characteristic-two, rank-one and nonlinear two-local cases are outside the claim. No independent mathematical audit has been performed.
