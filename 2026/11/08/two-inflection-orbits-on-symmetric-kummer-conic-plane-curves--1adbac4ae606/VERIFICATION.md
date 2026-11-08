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

Run `python verify_flex.py` with SymPy available. The script checks the general determinant formula (with symbolic integer parameter \(n\)), the residual cubic's discriminant, and the conic's nonsingularity and coordinate-axis transversality. It then directly expands and compares the full plane-curve Hessian for \(n=3,4,5\), and checks simplicity of residual roots at \(n=3,4,5,6,10,20\). Its complete recorded output is `verify_output.txt`. The run terminated in `ALL_CHECKS_PASSED`.

The characteristic-zero projective flex criterion, Bézout's theorem, the analytic restriction to each tangent, and the transversality argument are mathematical proofs in `RESULT.md`; a finite list of software tests is not taken as an exhaustive proof for every \(n\). No independent audit was performed.
