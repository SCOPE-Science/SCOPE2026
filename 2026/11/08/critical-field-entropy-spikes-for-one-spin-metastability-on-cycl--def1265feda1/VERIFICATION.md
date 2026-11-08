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

# Verification of the circular-ladder one-spin-stability formula

The proof is analytic: each spin has exactly three neighbors, the local stability inequalities determine a sixteen-state transfer matrix, and labeled cyclic stable configurations correspond bijectively to closed walks. The five exact characteristic-polynomial identities and all derived counts can be reconstructed using `python3 verify.py` without external dependencies.

The verifier uses exact integer arithmetic for all matrix operations and characteristic polynomials. As a second implementation, it enumerates labeled rung words for \(3\le n\le8\), and as a genuinely different energy check it independently evaluates the full Ising Hamiltonian and flips each spin for \(3\le n\le6\). It also tests recurrence formulas up to \(n=13\), the field-sign symmetry, and the eleven-state primitive component responsible for the dominant critical-field eigenvalue. These checks completed without assertion failures on the package's source code.

Computations at finitely many sizes do not prove infinite-size statements. Those depend on the explicit matrix-to-configuration bijection, the exact characteristic polynomials and the Perron–Frobenius argument in `RESULT.md`. No independent scientific audit has been performed.
