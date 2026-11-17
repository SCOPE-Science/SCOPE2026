---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

Every difference |v_j-v_i| telescopes across positive adjacent house-value gaps. At prefix r, the cross-cut edge count equals r(N-r)-sum_i x_i(r)(n_i-x_i(r)). The within-part term has strictly decreasing marginal priorities n_i-2k-1. Choosing largest r globally maximizes the term; one common sorted priority order attains every cut maximum simultaneously. Strictly positive gaps require every such optimum, proving iff with tied-level choices. Each part contributes at most one priority per level, yielding product_w m_w! words times product_i n_i! labelled allocations. Independent brute-force direct edge-cost enumeration checked 364 instances and 408204 complete part-label words on small q=3..5, N<=8, two distinct strictly increasing valuation patterns; finite verification is corroboration only.

## originality

PASS

PASS best-of-knowledge: Hosseini et al. (2023) Theorems 4.5–4.7 treat complete bipartite graphical house allocation, not this q>=3 complete optimiser classification. Rajan et al. 2020 complete multipartite-to-path wirelength optimizes the equal-spacing scalar cost and may contain stronger arrangements; full paper not available from lawful routes, so it is a significant explicit priority risk, not conclusive coverage. Actual searched prior records do not furnish the arbitrary positive-gap iff and labelled optimum multiplicity.

## value

PASS

PASS: classifying every minimizer and exact labelled multiplicity on a natural family q>=3 under arbitrary strictly ordered values is meaningful beyond the known minimum for equal spacing; the exchange/cut priority principle offers an exact implementable characterization rather than a random finite table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
