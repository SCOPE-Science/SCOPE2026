---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

PASS: In T_n=L(K_n), a selected edge set S initially observes every K_n edge touching an S endpoint, leaving only edges among isolated vertices U; if |U|≤2 one forcing step completes, while |U|≥3 no observed edge has a unique unobserved neighbor. Minimal successful S are a one-isolate matching (odd n) or two-isolate star forest. The exponential formula counts each labeled star/matching minimal set and inclusion-exclusion counts all valid sets. The TAR proof connects every smaller minimal configuration by bounded add-then-delete exchanges, first reducing large stars to minimum matchings and then connecting exposed-label matchings with one spare edge, while minimal sets at current maximum budget k are isolated. This yields c_n(q_n)=m_n,q_n, c_n(k)=1+m_n,k for q_n<k≤n−3, and c_n(k)=1 for k≥n−2. Independent direct power-domination and TAR graph BFS checks for n=4,5,6 reproduced every budget profile through n−2.

## originality

PASS

PASS, qualified: published Oct26 full result already establishes the identical power-domination criterion, exact star-forest/matching minimal classification, and complete set polynomial, so none of those foundational components is novel. The surviving theorem is the entire budget-indexed TAR component profile and exact first/permanent connected budget n−2. Bjorkman et al. 2026 general bounds imply only a lower bound via upper-minimal size plus one, not the intermediate component counts or a family-specific connectedness proof. Resultary searches found no earlier triangular-graph power-domination TAR profile.

## value

PASS

PASS: A complete reconfiguration component phase diagram for a natural infinite graph family is mathematically useful in its own right. The exact number of isolated minimal configurations at each budget, connectivity of all other configurations, and sharp threshold n−2 go substantially beyond the known enumeration of feasible placements and general TAR bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
