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

# Finite reproducibility checks and exact proof boundaries

Run the public script as `python3 verify_gcd_snf.py`. Its standard-library path builds the actual \(N\)-by-\(N\) integer matrices with entries \(\gcd(a-b,N)\), checks the local-tensor Smith prediction and determinant by independent exact fraction-free elimination, and computes modular ranks by independent finite-field Gaussian elimination. For \(N\in\{2,3,5,6\}\), it checks all determinantal divisors by an exhaustive calculation of **all** minors at every size, proving the small-instance Smith factors without using the proposed tensor formula. If SymPy is installed, it additionally checks full integer Smith forms at \(N\in\{10,14,15,21,22\}\).

Actual replay from the embedded script before packaging: `PASS 542 exact assertions; stdlib direct minors for 2,3,5,6; direct determinants and modular ranks: [2,3,5,6,7,10,14,15,21,22,30]; optional independent Smith forms: [10,14,15,21,22]; example G_6: [1,1,2,6,30,30]`.

These finite tests do not establish the all-modulus theorem. Its infinite content is justified by the symbolic determinantal-divisor calculation for each prime, the exact CRT tensor identity, and the integer invariant-factor uniqueness argument in RESULT.md. Independent auditing and external mathematical validation have not been performed.
