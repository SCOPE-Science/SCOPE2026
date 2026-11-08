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
# Verification instructions and scope

Run `python3 VERIFY.py` with SymPy installed. The verifier expands the quartic tangency identity exactly, reduces the quartic coefficientwise modulo two, verifies the characteristic-two hypersurface derivatives, and enumerates all projective points and tangent-incidence images over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_5\). It compares **rank-two loci** of the defining equation and of the tangent parametrization; these are the dense loci used in the proof. The expected output is included in `VERIFY_OUTPUT.txt` and ends with `ALL_CHECKS_PASSED`.

The finite-field comparisons are not proofs of set-theoretic equality over algebraically closed infinite fields. The actual proof uses the dual conic and density of rank-two matrices. The generic degree-two purely inseparable function-field extension is proved by valuation at the prime \((A_0)\) on a rational affine chart, not by counting rational points. The normality conclusion uses the exact Jacobian and Serre's criterion, not enumeration. No independent audit was performed.
