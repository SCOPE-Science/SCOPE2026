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

For three ordered distinct targets the witness-weighted product D_i D_j D_k sums exactly over one incoming comparison per target. A constraint pattern on v involved points has probability p^d, with p the linear-extension fraction for one uniform coordinate. I independently generated witness identifications by restricted-growth labels and counted extensions by a subset recursion (replay: python3 /workspace/branches/verify4_private.py). The three-edge maxima for v=3,4,5,6 are 0, 1/4, 1/6, 1/8; only the single external common predecessor achieves 1/4 at v=4, and all other v=4 patterns have p≤1/8. The disjoint-pair and common-predecessor terms have exactly (n)_6 and (n)_4 embeddings for ordered targets. They give λ³ and λ². In removing extra choices, D−1_{D≥1}≤binom(D,2), and telescoping the product bounds the difference by the four-edge pattern count with two distinct predecessors at one target. Its maxima are 0, 1/8, 3/20, 1/9, 1/12 at v=3 through 7, all with 2^v p²<1. Thus every error tends to zero when d=2 log₂ n+O(1). The advertised counts 51 and 124 reproduce for the script's relabelled keys; if one takes a full quotient by external relabelling there are 37 and 62 classes instead. This convention does not affect coverage or maxima. Continuous common marginals can be reduced coordinatewise with no ties almost surely. Weak convergence plus the different limit of E(N)_3 establishes failure of uniform integrability of the third factorial powers.

## originality

PASS

The distinct contribution supported by the inspected evidence is the exact third-factorial defect for the unweighted vertex statistic. Its known Poisson law and first two moment limits, and a separate calculation for ordered comparable pairs, do not imply it. No distinct exact indexed record was verified. The old random-order paper was inaccessible and remains a genuine historical-priority limitation, not evidence against coverage or a reason to stop the audit.

## value

PASS

The defect is at the first higher factorial moment not controlled by the known two-moment Poisson approximation. It identifies a concrete rare three-target configuration and distinguishes the vertex count from the apparently interchangeable edge count. This explains a natural limitation of sparse-limit approximations, rather than adding only a numerical coefficient to a known convergence theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
