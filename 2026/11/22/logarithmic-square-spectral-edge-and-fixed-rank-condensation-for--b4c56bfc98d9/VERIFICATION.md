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

On positive Hardy monomials T e_{pk}=ρ^{(p+q)k}e_{qk}; coprimality excludes other nonzero actions. The source and target indices are separately injective, so the singular values are summable and the symmetrization is compact self-adjoint. An oriented path requires progressively higher powers of p in its initial index; backwards indices decrease. The resulting finite path blocks admit a diagonal phase rotation conjugating T to e^{iθ}T. This makes the numerical range a disk (including its extremal point by the positive compact eigenvalue of the Hermitian part) and gives w=λ₁/2. To check the edge, use ℓ=log(1/(−log ρ)). Dropping weights ≤ℓ⁻⁴ costs at most 2ℓ⁻⁴ in norm. A retained length-L run has final source parameter at least q^{L−1} by the successive integrality constraint, and all retained parameters are <4 log ℓ/[(p+q)(−log ρ)]. Hence runs have at most ℓ/log q+O(log ℓ) edges and their top eigenvalues are bounded by those of the corresponding unit paths. Conversely, length floor((ℓ−5 log ℓ)/log q) paths with J distinct cofactors coprime to pq have weights 1−O_{p,q,J}(ℓ⁻⁵); the cofactors separate the components. Their unit-path sine vectors give the lower bound by min–max. The gap of a unit path of m edges is 2−2 cos(π/(m+2)); with these two lengths it has the same scaled constant on both sides. Infinitely many separated one-edge paths give infinitely many positive eigenvalues even away from the limit. Finally ℓ=log(1/(1−ρ))+o(1). The frozen checker was inspected, not executed; finite sections in the checker are not the assertion about the compact operator.

## originality

PASS

Qualified to the sharp genuine radial limit of the compact symmetrization, including each fixed positive rank. The arithmetic decomposition, sine eigenvalues, hard-cutoff gap constant, and qualitative numerical-range information are prior material. The close hard-cutoff overlap also supplies the hard-cutoff analogue at each fixed rank via its exact block counts; fixed-rank enumeration by itself is not the novelty. Quantitative transfer requires controlling the whole discarded weighted tail and attaining near-unit weights at a slightly shorter scale; the earlier finite-section result does not itself assert such comparison for the radial family.

## value

PASS

The actual compact radial family, rather than degree sections, is the Hardy operator of interest. Controlling its spectral tail in norm at the gap scale yields a sharp quantitative approach to the boundary and shows that every fixed number of top modes shares that scale. This is useful even given the close and comparatively simple hard-to-soft transfer, without claiming a new coefficient for the undamped problem or a full edge distribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
