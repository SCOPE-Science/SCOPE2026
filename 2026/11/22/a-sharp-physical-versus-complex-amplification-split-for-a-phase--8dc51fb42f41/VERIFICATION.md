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

# Mathematical verification and limits

**Reproduction:** Run `python3 verify.py` using Python 3 and no third-party dependencies. Expected lines begin `VERIFY_OK`. The checker symbolically verifies the degree-four polynomial identity \(A^2+\rho|B|^2=1\) and the real and imaginary polynomial parts of \(C=-\rho\overline B\) with exact rational coefficients. This validates the only critical coefficient reduction used to construct the Hermitian invariant.

It then verifies the complex and projected weighted-energy identities at representative parameters and multiple powers, the physical-output notch at \(q^2=8\), and convergence of the two near-endpoint rescaled gains on a real unit input. The original scalar modal matrix is specified explicitly in RESULT.md and derived by substituting the given phase-optimized coefficient into the primary article's polynomial formulas.

**Logical scope:** The positivity interval follows from \(\rho=1-q^2/12\) and \(|A|<1\) when \(0<q^2<12\). The formula for every matrix power follows from Cayley-Hamilton, and the physical-output energy identity is exact for every real input and every nonnegative integer power. Uniformity in the integer is proved by bounded sine and cosine coefficients, not inferred from finite enumeration. Sharpness uses the integer nearest to a quarter of the numerical period as the CFL edge is approached. No experiment or checker run can establish historical priority, an independent audit, an unrestricted mesh-independent bound, or physical electromagnetic energy conservation.
