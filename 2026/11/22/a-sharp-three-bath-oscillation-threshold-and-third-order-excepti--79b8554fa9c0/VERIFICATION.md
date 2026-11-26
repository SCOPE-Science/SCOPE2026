---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Only a flip at i changes σᵢ, so applying the physical generator gives exactly −σᵢ+(γᵢ/2)(σᵢ₋₁+σᵢ₊₁). The mean-spin Fourier matrix (the corresponding observable matrix may be transposed) has the same spectrum and Jordan orders. In the three-cell characteristic polynomial the linear term comes from the sum of the three reciprocal-bond products and the constant term from the two directed three-cycles. They give p=−g²(1−2u)/4 and q=g³u cos(k)/4, hence −4p³−27q² is exactly the displayed discriminant. Its minimum over the mesh is at k=0, where the sign factors as (1+u)²(1−8u). At equality k=π is also critical if present, and the 2×2 principal minor at μ=±g/4 is −3g²/16, so each repeated root has geometric multiplicity one. The discriminant sign gives the mixed-regime cutoff and, at u=1/2, all blocks are still nonreal-paired except those with cos(k)=0. At these two momenta Cayley–Hamilton gives B³=0 while (B²)₃₁=−g²/8, proving a size-three Jordan block. They are in the mesh precisely when 4 divides m. A nonzero real combination of conjugate Fourier data can be scaled to admissible spin means to realize the quadratic transient. At k=0 the positive-bath-equal sector, shifted by −1+g/4, squares to g(g−8h)I/16; its exponential gives the stated damped sinusoid, frequency and linear-in-time limit at the first threshold. These are one-spin statements, not the full Markov spectrum. The supplied verify.py was inspected, not executed. It has a hard-coded symbolic count of 10 despite 12 assert evaluations in that function; the numeric list also includes (.6,.075), nominally the first exceptional ratio, despite the verification note describing nonexceptional samples. Neither reporting issue affects the symbolic Jordan argument.

## originality

PASS

The known exact one-spin closure, Floquet method and existence of opposite-sign oscillations in a two-bath chain are not new. The distinct supported result is the nonzero sharp onset, wavenumber-resolved real/nonreal classification and mesh-dependent size-three Jordan block for this sign-frustrated three-site unit cell. The strongest inspected periodic relaxation framework has a common bath and variable site relaxation times, so its eigenproblem does not give these sign-frustrated eigenvalues. Priority beyond the inspected material is not certified.

## value

PASS

A negative bath no longer suffices for all or even any oscillatory one-spin modes, in contrast to the elementary two-alternating-bath case. The result provides the exact nonzero onset on every allowed ring, predicts which discrete modes oscillate beyond it, and exhibits a third-order defect with an observable quadratic transient only at specified lengths. This is a sharp, testable spectral boundary in a natural Markov model, not merely diagonalization at one parameter point.

The dated certificate retains the supplied scientific assessment, sources and limitations.
