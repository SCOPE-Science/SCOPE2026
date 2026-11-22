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

Run `python3 VERIFY.py` with Python 3.10+ and no dependencies. The checker enumerates all leading matrices, all left/right translation images and all actual second-coordinate cosets for \((m,q)=(1,2),(1,3),(2,2),(2,3)\). It checks the finite-field rank formula independently of the orbit construction, including the zero and full-rank cases. For \((m,q)=(3,2)\), it enumerates all \(512\) leading matrices and uses independent binary linear-generator ranks to verify every orbit-fiber dimension and all rank-stratum counts.

Exact count results: for \((m,q)=(2,2)\), the numbers of left and double orbits are \(58\) and \(40\); for \((2,3)\), \(417\) and \(225\); for \((3,2)\), \(6168\) and \(2052\). A finite numerical check at \((q,m)=(2,60)\) gives two-sided total variation approximately \(0.056517\) from uniform rank and left-orbit total variation approximately \(4\cdot10^{-10}\) from the corresponding discrete theta reference law. These are finite numerical checks, not proofs of the stated asymptotic rates.

The unrestricted field/order and asymptotic assertions rest on the exact affine translation-space proof, the classical rank-\(r\) matrix count, uniform finite-product estimates, and the subspace union bound. The checker covers prime fields only; this does not limit the symbolic theorem, which applies to every prime-power field.

The program prints `MATRIX_RADICAL_TWO_SIDED_ORBIT_SPECTRA_VERIFIED` upon completing all tests. This document does not assert independent expert validation or formal proof certification.
