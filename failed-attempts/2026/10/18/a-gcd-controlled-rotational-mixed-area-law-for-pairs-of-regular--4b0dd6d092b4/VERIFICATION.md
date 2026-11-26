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

The theorem is mathematically correct. In the classical mixed-area identity the first polygon's normals have angles π/n+2πj/n and the common side length is 2R sin(π/n). At each normal the rotated second polygon contributes S times the cosine of the signed offset from the nearest vertex. Modulo 2π/m, the step 2π/n has order N=n/d and fills the grid of spacing 2δ with multiplicity d. Centering its representatives yields x+(2k−N+1)δ, k=0,…,N−1; the range is the reduced support interval with harmless endpoint ties. Summing the finite geometric series gives d sin(π/m) cos x/sin δ, hence the claimed area and exact extrema. In the proof at line 61, 'parallel' must mean coincident outward normals, not undirected parallelism (opposite normals can occur away from the minimum, e.g. triangles at θ=π). Directly the coincidence angles are θ≡π/n−π/m mod 2δ, the minimizing phase since Nδ=π/m. The two equally spaced normal sets then share exactly d directions, and polygon Minkowski addition takes the union of their normals, proving the stated side counts including aligned angles. For uniform rotation |x| is uniform on [0,δ], so the stated decreasing cosine pushforward, moments and normalized limit follow by integration and Taylor expansion. The local wording defect does not invalidate any final claim. No replacement is supplied because the result fails the originality/value checks.

## originality

FAIL

A distinct same-day published SCOPE excluded-area result demonstrably contains the exact folded-cosine law, extrema and full orientation distribution for the same arbitrary integer orders and positive radii, after the angle substitution θ→θ−π. The exact coefficients and phases match, not just terminology or parameters. Priority within the shared date is not established; this is failure to establish a distinct substantive result against verified equivalent coverage, not a claim that the frozen record was proved later or its theorem proved false. The elementary corresponding normal count and normalized-limit rephrasing do not rescue a distinct result. The later exact Minkowski-sum record additionally states the side-count conclusions, but is not used to infer earlier priority.

## value

FAIL

The geometric invariant itself is natural and useful. This record does not supply a separately useful new invariant or boundary beyond the already available equivalent exact angle law and its random-orientation consequences. The remaining side-count statement is the elementary congruence and union of the two regular normal grids, and the all-sequence weak limit follows directly from the known exact CDF; neither is a nonroutine surviving advance on its own.

The dated certificate retains the supplied scientific assessment, sources and limitations.
