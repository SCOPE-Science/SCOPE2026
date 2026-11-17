---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

JR violation is equivalent to a candidate having at least q=ceil(n/k) supporters unrepresented by W. Laminarity makes distinct supporter sets of cardinality q pairwise disjoint, so r≤floor(n/q)≤k. Any all-quota committee omitting a quota class leaves all q voters of that block unrepresented; thus every such class is mandatory and every DR committee covers exactly U, the union of quota blocks. Selecting one from each is feasible exactly when M≥k (since r≤k), with remaining candidates quota-sized. JR then reduces to |S_c\U|<q for every candidate. Counting labeled nonempty selections by class yields [z^k] product_i((1+z)^w_i−1). Empty classes, duplicate supports, k≥n (q=1), and nonlaminar boundary accounted for; an independent k=5 pair-block enumeration found 32 DR committees among 252 total, matching 2^k/C(2k,k).

## originality

PASS

Chingoma et al. (2026) introduce DR and prove unrestricted hardness but do not in accessible statements establish the laminar-candidate-support exact-count and common-coverage classification. The November 2 prior SCOPE candidate-interval dynamic program counts DR committees on a distinct ballot domain, not all laminar candidate supporter sets, nor a unique represented voter union. An older near-quota tractable result covers a subcase but does not dominate the laminar residual criterion. Primary Chingoma full text inaccessible here, explicitly retained as a material risk.

## value

PASS

An exact feasibility criterion, complete generating-function count, and invariant represented-voter set for a natural hierarchical approval domain are useful structural results within hard committee-selection problems. The pair-block example also quantifies an exponentially small success fraction under uniform lotteries. This is more than a routine renaming of JR; laminarity enforces a strong rigidity theorem and polynomial counting.

The dated certificate retains the supplied scientific assessment, sources and limitations.
