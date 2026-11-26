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

The dark space is the sum, over distinct adjacency eigenspaces, of the trap-orthogonal directions. It reduces both terms of the generator. On its orthogonal complement the eigenvalue identity Im(z)||v||² = −gamma |v_0|² rules out any nondecaying eigenvector, so finite-dimensional Jordan blocks do not affect the limit. Only the lower hub/uniform-rim eigenvalue can coincide with a nonuniform Fourier energy, and it is strictly negative. At the collision, the hub eigenvector has rim weight a²=λ/[2(λ−1)] and hub weight b²=1−a²; the degenerate trap projection has squared norm (a²+d)/n. Removing it leaves b²d/(a²+d), exactly as claimed. The negative Fourier energies are distinct, including −2 at the even endpoint. With τ=1 the collision requires n≤8, and exact small-size comparisons leave n=3 and n=8. The uploaded checker and requirements were inspected, not executed. The independent rational Krylov check in /workspace/review-evidence/independent_checks.py reproduced ranks and masses for unit spokes n=3..9, and for n=12 at τ=1/2 (rank 7, mass 2/3) and τ=51/100 (rank 8, mass 0); the general proof, not this finite test, handles all parameters.

## originality

FAIL

The October 13 weighted-wheel record gives the exact collision locus and, in proof equations (3)–(4), every full adjacency spectral projector, explicitly including the projector at the collision. Applying the established single-trap projection identity to those entries yields the survival law by direct substitution, not merely by analogy between two observables. The bright dimension counts the same distinct trap-visible projectors, and τ=1 is an elementary specialization. No distinct surviving theorem in the frozen finding was identified.

## value

FAIL

Loss survival is a meaningful observable, but the surviving candidate contribution would only re-express the already tabulated spectral projectors using the standard rank-one trap formula. The unit-weight corollary is a bounded direct substitution, and there is no independent dynamical estimate or structurally new regime in the frozen result to retain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
