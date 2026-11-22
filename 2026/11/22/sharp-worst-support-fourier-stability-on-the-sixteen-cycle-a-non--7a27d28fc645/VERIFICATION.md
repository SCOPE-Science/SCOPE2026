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

# Exact verification instructions

**Files.** `certificate.py` and `certificate_output.txt` are the exact proof-checking artifact and its captured output. `numeric_crosscheck.py` and `numeric_output.txt` are a separately implemented floating-point diagnostic; they are never used as exact certificates.

**Replay.** Run `python3 certificate.py` from a directory containing this file. Its standard-library implementation represents every sixteenth root as an eight-integer coefficient tuple modulo \(t^8+1\), computes determinant coefficients exactly, checks algebraic reality, and uses integer-square-root radical intervals at scale \(10^{25}\) to obtain strict signs. It exhausts all \(\binom{16}{4}=1820\) four-frequency supports, checking all four Sylvester leading minors of \(1000F[R,C]^*F[R,C]-I\) for the proposed optimum, and checks an explicit negative determinant for one frequency support in each competing full-spark orbit. It also exhausts all 256 full-spark row sets and verifies their three-orbit partition. Success terminates with the line beginning `PASS:`. Thus the exact proof covers every relevant configuration, not sampled configurations.

**Cross-check.** Run `python3 numeric_crosscheck.py`. It builds \(F\) independently with complex exponentials, then diagonalizes a real representation of the Hermitian Gram matrix by Jacobi rotations. It enumerates every frequency support separately for each of three affine row representatives. Floating-point comparisons support the exact result but cannot prove strict bounds.

**Proof boundaries.** The complete scientific statement is only that the global maximizers are the 64 affine images of \(\{0,1,3,14\}\) and that the strict separator \(1/1000\) distinguishes them from every other row set. The decimal values reported by the diagnostic are approximate, and no closed form is claimed for the optimum itself. The full-spark classification uses the published prime-power theorem. Historical priority is not independently certified.
