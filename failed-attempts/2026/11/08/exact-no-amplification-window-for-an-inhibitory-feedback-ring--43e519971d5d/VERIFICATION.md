---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Differentiating the squared Euclidean norm shows contractivity for all t≥0 iff H=(J+Jᵀ)/2 is negative semidefinite. At b=a the signed cyclic shift is orthogonal with Q^n=−I, and the top symmetric eigenspace is the real cosine/sine pair at θ=π/n. Compressing the symmetric corner perturbation to this pair gives eigenvalues (cosθ+1)/n and (cosθ−1)/n, yielding the strict two-sided lower bound away from b=a. For z=μ/a>cosθ the interior path block of −H is positive definite. Its Chebyshev inverse entries give a two-dimensional complement with diagonal (a/2)U_(n−1)/U_(n−2) and off-diagonal (a/2)(b/a−1/U_(n−2)); the scalar PSD condition and b≥0 give the exact interval, including n=3. At the minimum damping only b=a works and the neutral modes are an undamped conjugate pair. The open-chain eigenvalues are −μ, but its top symmetric eigenvalue is −μ+a cos(π/(n+1)); the balanced closure has top real part −μ+a cos(π/n), giving the stated strict separation. The example reduces to U₁=6/5 and U₂=11/25. Independent replay: OPENBLAS_NUM_THREADS=1 python3 -B /workspace/branches/independent_checks.py 3; 768 spectral comparisons for n=3–18, including damping below/at/above threshold and intervals clipped at zero. These are finite numerical corroboration only.

## originality

FAIL

Grudsky–Maximenko–Soto-González (2020 preprint/2021 publication) treat exactly the shifted and scaled symmetric matrix, under a more general complex corner parameter. Their Proposition 1 gives the all-order Chebyshev determinant, from which the fixed-Euclidean window and unique optimizer follow by a positive path pivot and a square completion. Their Proposition 12 gives the precise double extremal eigenspace, whose two-by-two Rayleigh restriction gives the stated slopes. The paper need not use the ecological wording; the main claims are routine consequences of exact results for the same matrix. This is not a claim that Snyder or the secant criterion itself gives the Euclidean window.

## value

FAIL

The distinction between transient amplification and stability is useful, and the fixed-Euclidean question is well motivated. But here the exact window, feedback minimizer, slopes and open/closed comparison require only standard transformations of already available spectrum data for the same matrix. The frozen ecological interpretation does not supply a separate nonroutine result; no repair is warranted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
