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

## Exact computations
The embedded `verify_wiman5.py` uses exact integer coefficient arithmetic and explicit finite-field arithmetic. It asserts that the classical sextic reduces to \(2S^3+(XYZ)^2\) modulo five, checks all ten proposed singular points, checks the local Hessian discriminant at four nodes, and counts projective points over \(\mathbb F_5\) and \(\mathbb F_{25}\). Run with `python verify_wiman5.py`; see `verification_output.txt` for the actual run.

## Mathematical checks and limits
The published characteristic-five rationality theorem [Giulietti--Kawakita--Lia--Montanucci, arXiv:1805.06317] is used as a geometric integrality/normalization premise. The derivative classification and local étale-coordinate normal forms are proved in RESULT.md independently of finite enumeration. The all-extension point counts and generalized Jacobian follow from the normalization exact sequence; no finite sampling is presented as an infinite proof. The originality judgment is based on accessible primary literature and is not an independent priority certificate.
