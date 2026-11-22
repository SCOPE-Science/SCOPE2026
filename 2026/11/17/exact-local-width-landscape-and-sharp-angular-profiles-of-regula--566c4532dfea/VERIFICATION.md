---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

For the regular simplex represented by coordinate vertices in the zero-sum subspace H_N, directional width is max u_i−min u_i. Any normalized direction with an intermediate coordinate can strictly decrease width by shifting that coordinate away from its mean while retaining range, so a local minimum must be two-level. A cut of size t yields width sqrt(N/[t(N−t)]). The tangent to a two-level normal has zero sums within both cut blocks; for angles θ<arctan(w/√2) cross-block order is fixed. Sharp zero-sum block bounds ||x||²≤r(r−1)(max x)² imply min over unit tangent v of max_high v−min_low v is 1/sqrt(max{t(t−1),s(s−1)}), attained by the one-exception vector in the larger block. Therefore exact finite-angle envelope is w cosθ+γ sinθ, giving strict local minima, and no others. An independent 7,329 integer zero-sum block probes and 4 partitions with 500 angular probes each corroborated the closed bound, not extrapolation. N≥3, oriented antipodes counted separately, open angle cutoff only.

## originality

PASS

BEST-OF-KNOWLEDGE PASS for all balanced/unbalanced strict local minimizers and sharp finite-angle envelopes. Known complementary-face distances and global balanced optimum are credited. The November 1 near-minimum-width tangent-polytope theorem already contains sharp first-order slope at globally minimizing balanced cuts, so this component is covered; its theorem does not classify all unbalanced strict traps nor provide the exact nonzero finite-angle profile at each.

## value

PASS

The presence and quantitative sharpness of suboptimal local traps in a canonical simplex width optimization is relevant to nonconvex directional optimization. The complete every-dimension local landscape and attained finite-angle stability modulus, including unbalanced cuts excluded from prior near-global analyses, are natural exact geometric invariants with a clear mathematical use beyond the known global width.

The dated certificate retains the supplied scientific assessment, sources and limitations.
