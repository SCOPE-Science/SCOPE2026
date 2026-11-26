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

For a Hermitian hopping matrix the sink cyclic space and its orthogonal complement reduce H and the single-site damping. On the complement evolution is unitary. On the cyclic space an eigenvector of the damped generator with Re eigenvalue zero would have no sink component (take the real part of the Rayleigh quotient) and hence be an H eigenvector orthogonal to the whole cyclic space. Thus every generator eigenvalue on the cyclic space has strictly negative real part, which gives norm decay even without diagonalizability. Independently compute the cyclic space by scaling J out of H. Let δ=w−1, A'=a₁+r_A, B'=b₀+r_B. H a₁=B′ and H²a₁=(n+δ)a₀+nA′; H³a₁=[n(m−1)+(n+δ)]B′+δ(n+δ)b₀. For w>0, w≠1, δ(n+δ)≠0, so b₀ and r_B are cyclic. H b₀ and H r_B/(n−1) differ by δa₀, so a₀, A′ and hence r_A are cyclic. Conversely the five orbit sums form an invariant subspace; all five are orthogonal and nonzero under m,n≥3. At w=1 the first three powers span a₁, the uniform A vector and the uniform B vector, which close under H, so the rank is three. Orthogonal projection onto the orbit sums gives the displayed diagonal captures; trace divided by m+n gives the maximally mixed result. Taking t→∞ at fixed defect is essential; finite-time norm is continuous in w.

## originality

PASS

Credit the exact clean bipartite projector and the general bright/cyclic criterion to prior work. The supported addition is the complete arbitrary-size rank-two jump at every nonzero defect within the stated domain and the explicit defective projector, not a general discovery that edge perturbations can improve trapping.

## value

PASS

For a natural perturbation of a standard coherent network, the result does more than show generic enhancement: it rules out exceptional permitted nonzero defects, determines which exact components become capturable, and quantifies a discontinuous infinite-time observable despite continuous finite-time evolution. It gives exact sitewise predictions even for starts away from the trap or defective edge, which a rank count or the known unweighted law cannot provide.

The dated certificate retains the supplied scientific assessment, sources and limitations.
