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

The primary modal polynomials (12)–(15) give B/q=−1+(1/8−i/(8√3))q² and C=−ρ conjugate(B), ρ=1−q²/12, on substituting the stated a. In particular |B|²=q²(q⁴−12q²+48)/48, and det M=1 gives A²+ρ|B|²=1. With S=diag(√ρ,1), SMS⁻¹ is unitary (determinant one) on 0<q²<12. Using the exact power formula and real S, SP_nS⁻¹ has diagonal cos(nθ) and antisymmetric off-diagonal entries ±(Re B/|B|)sin(nθ); the Gram matrix is the scalar in the output-energy identity. At q²=8 the real coupling vanishes and A=−1/3. At q²=12−δ, A=1−δ/2+δ²/24, sinθ∼√δ, B→√3−3i and C=O(δ). Hence the rescaled diagonal and lower-left entries vanish uniformly in n, and the upper-right coefficients approach (√3−3i)sin(nθ) and √3 sin(nθ). The rank-one norms yield sharp upper bounds, and the integer nearest π/(2θ) gives the lower bounds on the same real vector e₂, without an assumption of phase-density for a fixed q. At δ=0 the nonzero shear grows linearly, including after projection. The real part is taken only after the full recurrence. The supplied verifier and metadata were inspected without executing the script; the exact algebra and uniform-in-n argument establish the limits.

## originality

PASS

The substantial distinction is the sharp all-time near-CFL norm split for this specified integrator with real output. The explicit modified energies are useful supporting identities, not a claim to have invented unitary similarity, spectral CFL, or the exact propagation formula.

## value

PASS

The sharp constants show how badly Euclidean transients can deteriorate on approaching a spectral CFL boundary, and exactly how much of that largest transient is still visible in the physical output. The separate real and complex limits, common real excitation and measurable observation time are useful for this known integrator and go beyond restating strict-CFL stability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
