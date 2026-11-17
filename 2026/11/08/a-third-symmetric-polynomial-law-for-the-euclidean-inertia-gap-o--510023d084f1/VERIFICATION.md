---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

The transfer x_v -> y_v=x_v-max(previous layer) is an invertible unit-Jacobian piecewise-affine bijection and couples volume-uniform points. Within each layer, random within-layer order-statistic ranks and Dirichlet(1,...,1) spacings give the exact covariance-entry difference s_g(N-s_g-m_g)/((N+1)^2(N+2)) for any two labels in that layer. Summing m_g identical variance gaps counts e3(m_1,...,m_k) once over triples of distinct layers. For k<=2 an explicit coordinate reflection is a Euclidean isometry; k>=3 the positive trace gap precludes congruence. Elementary smoothing of two layer sizes differing by >=2 proves sharp fixed-N,k extremizers. Independently specializing the full general-poset linear-extension formula with deterministic ranks a=s_g,b=s_g+m_g+1 reproduces exactly this diagonal variance and e3 for compositions (1,1,1),(2,3,4),(4,1,2,1),(2,2,2,2). Source checker used independent rational simplex integrals in 127 compositions, not the Dirichlet formula; finite tests are not an all-N proof.

## originality

PASS

A general all-poset coordinatewise-variance theorem published in the same November 8 corpus supplies a rank/linear-extension formula whose deterministic-rank specialization immediately reproduces the diagonal variance and e3 numerator; these components are emphatically NOT independently new after that theorem. Crucially that full general-result text explicitly calls the ordinal-sum exact inertia expression a previously obtained strict special case, rather than claiming antecedence. Exact publication order within the shared date/aggregate Git commit is unverified, and the submitted complete within-layer off-diagonal covariance identity and sharp fixed-height optimization are not in the broader general theorem. On that evidence this older specialized finding retains a qualified best-of-knowledge originality PASS, with no assertion that its headline improves on the now-published general result.

## value

PASS

The exact symmetric e3 inertia formula, all-entry within-layer covariance block structure, rank bound and sharp balancing/extremal layer compositions give a natural metric classification of canonical order/chain polytope pairs. The formula is no longer new relative to the full general-poset theorem, but the reported specialized antecedence and extra covariance/extremizer information make its historical mathematical contribution substantive rather than a bare textbook numerical exercise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
