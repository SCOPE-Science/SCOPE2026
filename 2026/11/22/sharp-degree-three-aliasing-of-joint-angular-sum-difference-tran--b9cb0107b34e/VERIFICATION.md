---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

The torus map has kernel {0,(1/2,1/2)}, is surjective, and has absolute Jacobian two. The area formula gives half the sum of the sheet densities almost everywhere; normalized Haar is attained exactly when the sum is two. Equivalently the dual pulls back (k,ℓ) to (k+ℓ,k−ℓ), the full same-parity lattice. Copula marginals kill nonconstant axis modes. The only remaining modes of total degree at most two are (±1,±1), so there is no lower-degree nonconstant witness. At degree three, f(u)g(v)=sin(2πu)sin(4πv) cancels between the sheets, has both marginal integrals zero, and with 0<ε<1 gives strict positivity. Its CDF perturbation is ε times the product of the nonnegative primitives F and G, and swapping (1/4,1/8) distinguishes the density from its transpose. The first moments of the sines are −1/(2π) and −1/(4π), giving Spearman 3ε/(2π²). In the Kendall integral the two linear terms are each ε/(8π²) and the quadratic term vanishes since ∫Ff=∫Gg=0. The half-L¹ distance equals 2ε/π². The retained moment cos(2π(−U+2S)) has mean −ε/4 by expanding cos(2π(U+2V)). Identical oracle image laws give identical product laws and rejection probabilities, with no claim about ranks.

## originality

PASS

The supported distinct claim is the sharp total-degree onset for smooth PQD copula aliasing of the joint oracle pair, with an explicit nonexchangeable witness and exact indistinguishability. The two-sheet averaging and dual-lattice argument are standard torus facts applied to this map, not new general results. The strongest inspected APIT and indexed statements do not supply the sharp joint witness, and ordinary unwrapped sum–difference independence is a different constraint.

## value

PASS

The paired observable appears to carry more information than either of the summaries used for angular independence testing. A strictly positive analytic and positively quadrant-dependent counterexample shows the information loss persists even when both summary values are retained and dependence is positive by multiple criteria. The sharp first Fourier degree pinpoints that loss, and the oracle qualification prevents overreading it as a result on rank-based power.

The dated certificate retains the supplied scientific assessment, sources and limitations.
