---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

Reconstructed barycentric λ_i>0 with sum1 and zero barycenter. The opposite ray from the origin to -p_i meets the opposite facet at -λ_i p_i/(1-λ_i), so ∥-p_i∥_P=(1-λ_i)/λ_i. For K=-K⊂P, ∥p_i∥_K=∥-p_i∥_K≥∥-p_i∥_P. Reciprocal Cauchy gives Σ1/λ_i≥(d+1)² and hence Σ∥p_i∥_K≥d(d+1). For centered Delta, the identity -a_i/d=(1/d)Σ_{j≠i}a_j∈Delta proves -Delta⊂dDelta and K⊂(d+1)Delta. The barycentric linear functional L_i bounded by 1 on Delta-Delta takes d at (d+1)a_i, and explicit difference-body membership gives the reverse gauge bound; each exact norm is d. Applicable all d≥2. Independent exact rational checker inspects d=2..12 but is not the universal proof.

## originality

FAIL

DECISIVE DIRECT PRIOR IMPLICATION found by reading, not merely the headline of, E. D. Gluskin and A. E. Litvak, Asymmetry of convex polytopes and vertex index of symmetric convex bodies (2008). Although Theorem 3.2 prints the weaker m²/(2k), its proof on PDF p.8 (zero-index p7) explicitly proves Σ_i∥-p_i∥_P≥m(m−1)/(2k−1). Specializing to a d-simplex with m=d+1, k=1 yields d(d+1) EXACTLY. The authors then explicitly show in their Section 4 that for K=-K⊂P one has Σ_i∥p_i∥_K≥Σ_i∥-p_i∥_P. Therefore the central theorem here is a direct corollary of the published proof, despite different theorem headlines. The simplex difference-body equality example is the immediate centered-simplex standard sharpness computation; this does not restore originality to the covered lower-bound claim. Earlier self-review erred by comparing only the weaker printed theorem. Reject without repair or extra certificates.

## value

FAIL

Minimal-vertex outer approximation and the tetrahedral difference-body example are natural geometric problems, but the exact inequality is already a corollary of the 2008 published d+k-vertex asymmetry proof, and the equality family is elementary barycentric gauge arithmetic. The presented package adds no motivated independent structural theorem beyond recomputing that published lower bound, and does not settle the unrestricted T−T vertex-index problem. A known deduction is not made valuable research by adding a new restricted-invariant name.

The dated certificate retains the supplied scientific assessment, sources and limitations.
