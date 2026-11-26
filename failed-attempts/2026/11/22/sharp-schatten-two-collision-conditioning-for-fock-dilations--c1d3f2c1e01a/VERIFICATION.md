---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

On the orthonormal Gaussian Fock monomials the numerator is Σ_{n≥0}|Σ_j c_j b_j^n|² and the denominator is Σ_j |c_j|²/(1−|b_j|²). Thus the optimum is the least eigenvalue of G_{ij}=√[(1−|b_i|²)(1−|b_j|²)]/(1−conj(b_i)b_j); the first N coordinates make it positive definite. Write σ_j=∏_{k≠j}(b_j−b_k)/(1−conj(b_k)b_j), and E=diag(1/σ_j). Independently, the exact normalized Cauchy inverse is G⁻¹=E Gᵀ E*. A conjugation check: normalized Hardy functions u_j=√(1−|b_j|²)k_{b_j} have Gram Gᵀ in the conjugate-first convention; their biorthogonal functions are σ_j⁻¹ B(z) conj(z) conj(u_j(z)) on the circle, with B the finite Blaschke product of all slopes. These are analytic since B(z)/(z−b_j) is analytic, and their normalized evaluations give the identity. The boundary conjugation is anti-isometric; transposing the dual Gram gives the stated G⁻¹. At the collision, ε^(N−1)/σ_j→(1−|a|²)^(N−1)w_j and Gᵀ→11ᵀ. This yields the claimed positive rank-one inverse limit, eigenvalue coefficient and line. Alternatively, the O(ε^(N−1)) operator norm on unit minimizing coefficients forces Σ_j c_j ζ_j^m=O(ε^(N−1−m)) for m≤N−2 by the binomial identity on (b_j−a)^m. The limiting nullspace is the barycentric line by the Vandermonde interpolation identity. For regular slopes discrete Fourier modes retain the coordinates n in a single residue class, yielding eigenvalues N(1−ε²)ε^(2s)/(1−ε^(2N)), s=0,…,N−1. The smallest is s=N−1. The actual fixed interior-center hypotheses and separate center-zero identity are valid. The supplied script was inspected, not run.

## originality

FAIL

This is mechanically covered by exact classical Cauchy inversion on the very same matrix, not just analogous to earlier cluster conditioning. Fock simultaneous diagonalization gives a normalized multiplicative Cauchy matrix, and Cauchy double alternants on all minors plus the adjugate give its full inverse, equivalently G⁻¹=E Gᵀ E* above. To see coverage even without phases, det G=∏_{i<j}|(b_i−b_j)/(1−conj(b_i)b_j)|². Thus tr G⁻¹=Σ_j |σ_j|⁻² by the principal minors. The order-two principal minors of G⁻¹ are complementary determinants divided by det G, so each is O(ε^(−4N+6)), while (tr G⁻¹)² has order ε^(−4N+4). One inverse eigenvalue therefore carries the full leading trace; the exact inverse also gives its line directly, or that line follows from the vanishing Vandermonde moments. The regular-polygon identity is the elementary geometric series in each discrete Fourier residue class. There is no additional calculation beyond these standard exact implications. This fail is not a claim that a fixed-symbol Fock paper prints the collision limit, nor that the overlapping same-day catalogue record takes priority.

## value

FAIL

The conditioning question is naturally motivated, and the constant is correct, but the proposed narrow invariant is directly read from a stronger classical exact inverse on the same Gram matrix. The eigenline is the usual nullspace of the lower Vandermonde moments, and the symmetric check is routine Fourier summation. The present scope supplies no separate new mathematical obstruction or quantitative case not resolved by those identities.

The dated certificate retains the supplied scientific assessment, sources and limitations.
