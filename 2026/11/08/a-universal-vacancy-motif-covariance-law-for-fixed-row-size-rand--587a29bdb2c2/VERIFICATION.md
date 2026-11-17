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

Each ordered injection of motif left and right vertices has a product of row-specific falling-factorial inclusion probabilities, so ET_H=(n)_k sum_alpha prod_j (r_alpha(j))_(t_j)/(n)_(t_j). Conditioning one given right label to be absent preserves row independence and replaces n with n-1 for all rows. As no motif right vertex is isolated, conditioned embeddings avoid that label; the ratio E[T|vac]/ET is (1-k/n)/prod_j(1-t_j/n), independent of r_i, m. Summing vacancy indicators yields the claimed normalized covariance. For f(x)=1-prod_j(1-t_j x), f''<0 when s>=2 and 0<x<1/k; hence f(x)/x strictly decreases, proving the stated exactly-one real sign crossing with the e<=k, max t_j=k endpoints handled separately. The shared-leaf double-d-star specializes algebraically to (n-d^2)/(n-d)^2; independently verified this rational simplification. The supplied verify_incidence.py enumerates actual row subsets for seven cases; no finite enumeration is used to justify general n, motif or heterogeneous row patterns.

## originality

PASS

Best-of-knowledge source and statement comparison distinguishes independent uniform fixed-row-size incidence embeddings from fixed-total-edge ER or uniform-hypergraph motif counts, and from projected random intersection graphs. The Palm conditioning ratio depends on left degree multiset and yields a natural exact square n=d^2 sign boundary; no inspected earlier Resultary or primary source establishes this all-motif fixed-row law. Inaccessible 1999 primary full text remains an explicit risk, not evidence of novelty by absence nor reason alone to fail O.

## value

PASS

The covariance between unused labels and arbitrary non-induced incidence motifs is a naturally motivated dependence question in fixed-degree/row-size random incidence networks. The exact cancellation of all host row-size parameters, the complete at-most-one-real-transition classification, and the infinite family with an integer square threshold n=d² are structural, reusable facts not merely a small simulation or a known-table recomputation. The statement carefully excludes degenerate normalizations and distinguishes integer sign changes from the real threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
