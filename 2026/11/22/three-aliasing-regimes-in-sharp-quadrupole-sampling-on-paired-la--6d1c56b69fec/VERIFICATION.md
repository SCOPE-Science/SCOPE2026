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

# Verification and limitations

The exact proof establishes the complete spectrum by discrete Fourier root-of-unity selection rules and two explicit aliasing block diagonalizations. Elementary inequalities against the sector values \(A,B,C\) establish both sharp optimizations globally for every real \(0<t<1\) and \(\delta\), and every integer ring size at least three. The proof does not use numerical sampling for universal quantifiers.

Run `python3 verify.py` alongside this file. It evaluates five normalized harmonics directly at every sampled sphere point, independently assembles full symmetric Gram matrices, diagonalizes with a standalone Jacobi eigensolver, and compares all predicted eigenvalues for 512 configurations. It also checks identities with rational arithmetic, degeneracy cases, the extremal latitude and the plateau threshold. The command completed successfully in the package working directory. Floating-point tolerances cover only corroborative experiments. No independent audit has been performed.
