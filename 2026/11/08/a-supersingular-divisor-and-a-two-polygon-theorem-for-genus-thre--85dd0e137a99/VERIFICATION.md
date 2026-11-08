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

`python3 verify.py` requires Python 3 and SymPy; it uses internal exact field arithmetic for GF(3), GF(9) and GF(27). The verifier reconstructs the three-by-three Hasse–Witt coefficient matrix, multiplies Frobenius-twisted matrices symbolically modulo three, checks the polynomial substitution on the exceptional divisor, and tests smoothness independently via polynomial gcd. It exhausts all triples in the first two finite fields and samples the third with a complete one-parameter special slice. The paired `verify_output.txt` records the reproducible run, ending in `ALL_CHECKS_PASSED`.

The general algebraically closed-field result uses the symbolic semilinear and geometric arguments in `RESULT.md`, not the finite enumeration. The Newton-polygon deduction depends on the standard Dieudonné slope decomposition, the order-four automorphism action, and polarization. No independent scientific audit has been carried out.
