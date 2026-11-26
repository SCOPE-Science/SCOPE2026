---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The product of two ordinary Laguerre generating functions is the associated Laguerre generating function at the sum of the arguments. With the orthonormal Laguerre functions this gives M=RB/2, B=I−τS; the complement of those m basis vectors is in the kernel. The determinant is (−1)^(m(m−1)/2)2^−m, and deformation to reversal gives the claimed inertia for all m≥1, including m=1. The singular-value square is B*B/4 with the one-end correction to a tridiagonal Toeplitz matrix. Rank-one interlacing gives its limiting magnitude distribution; odd signed traces are O(1) before normalization since a fixed reverse-band intersects only O(1) diagonal entries. This gives the signed law and the arcsine normalization at τ=1. The reverse triangle inequality and constant-vector Rayleigh bound give the subcritical endpoint. At τ=1 the boundary conditions are v_(−1)=0 and v_m=v_(m−1); the sine vectors in the finding satisfy both. Reversing the difference vector evaluates its sign as (−1)^(k−1), yielding the exact eigenfunctions, extreme magnitudes and determinant product. For τ>1 the reversed, τ^−m scaled inverse of B has truncated kernel τ^(−1−i−j) on i+j≤m−1; its Hilbert–Schmidt limit has norm τ/(τ²−1), giving the full prefactor. Interlacing places at most one singular value below (τ−1)/2, and the computed one is eventually below it. All limits hold for fixed τ. The packaged finite-dimensional checker was inspected, not run; it is not needed to establish the limits.

## originality

FAIL

The key trichotomy and the supercritical count are covered by the exact uniform finite open SSH problem after an explicit block reduction; the signed empirical law is a direct substitution into a general flipped-Toeplitz theorem, and the critical magnitudes are also in an earlier indexed nilpotent-shift record. The signed critical vector conversion is elementary in the reflection sector of a homogeneous path. Applying known spectral results to this kernel with the Laguerre addition identity does not support the frozen novelty claim.

## value

FAIL

The example illustrates bulk versus extremal invertibility, but the frozen contribution is a repackaging of the same already quantified SSH edge problem and flipped-Toeplitz bulk law by a standard orthonormal Laguerre expansion. No additional spectral behavior, inversion estimate outside the existing parameter/boundary setting, or mathematically motivated new consequence of the Hankel realization is established. The clean alternate derivation has expository utility but is insufficient as the asserted scientific finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
