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
# Mathematical verification

The Fock monomial basis \(e_n(z)=\alpha^{n/2}z^n/\sqrt{n!}\) reduces the operator to a diagonal sequence \(\sum_jc_jb_j^n\), proving the exact Hardy-kernel Gram representation. The cardinal functions in RESULT.md interpolate the identity matrix and have rational kernels with only the prescribed poles; their Hardy norm limit is justified on a fixed disk of radius greater than one. The unique nonzero eigenvalue of the rescaled inverse Gram limit gives both the exact sharp leading constant and the optimizing coefficient line.

The roots-of-unity formula is checked analytically by finite Fourier decomposition. A numerical supplemental script, `CHECK.py`, evaluates positive matrices at high precision, checks the exact symmetric formula for five sizes and four radii, and checks limiting trends/eigenvector alignment for four nonsymmetric sizes and four positive perturbations. Its recorded run completed 88 assertions successfully.

The analytical argument does not depend on numerical conditioning or finite sampling. Existing qualitative comparisons do not by themselves certify publication priority; the scope is solely a fixed-center, \(\mathcal S_2\), scalar-weight degeneration result. Independent audit has not been performed.
