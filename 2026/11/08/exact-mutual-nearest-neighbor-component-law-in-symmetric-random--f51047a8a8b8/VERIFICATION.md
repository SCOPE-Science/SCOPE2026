---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

A strict minimum-weight directed nearest-neighbor walk in a finite undirected complete graph cannot cycle around length >=3, since along such a cycle each edge must be strictly smaller than its predecessor. Every weak functional component therefore contains exactly one 2-cycle. For k prescribed disjoint mutual-pair edges, condition on their k weights and count 2(n-2k) incident edges to nonpaired vertices per pair plus 4 cross edges between any two candidate pairs. Ordering selected weights gives integrand ∏(1-x_i)^[2(n-2k)+4(i-1)], and exponential spacing integration yields product denominators j(2n-2j-1), canceling k!. Binomial matchings give complete factorial moments and exact PGF, mean and variance. Reconstructed n=4 all 6!=720 distinct edge rankings independently: X=1 in 576 and X=2 in 144, as PGF predicts. n=2 deterministic X=1. Finite tests supplement the exact all-n integral proof.

## originality

PASS

PASS for simultaneous specified disjoint-pair event probabilities and full component-count generating polynomial. Earlier public Aldous 2023 calculation concerns only extreme perfect mutual matching event, and earlier tourist walk results establish the single reciprocal-pair marginal; neither alone supplies the intermediate-k factorial moments or variance. Frieze–Pegden analyzes random weighted graph spanners, not complete component distribution. No prior published stronger joint-law formula was identified in accessible documents. Unlocated classic random-link probability formulas remain a real historical-priority risk.

## value

PASS

Symmetric random-link nearest-neighbor dynamics is a canonical complete-graph probabilistic model. The natural count of weak components equals number of mutual two-cycles, and a complete exact finite law reveals global underdispersion (variance/mean→1/4) despite positive correlation for disjoint candidate pairs. Both all-k dependence structure and counterintuitive variance can be reused in random mapping and nearest-neighbor analysis; not a routine restatement of the known mean or perfect matching extreme.

The dated certificate retains the supplied scientific assessment, sources and limitations.
