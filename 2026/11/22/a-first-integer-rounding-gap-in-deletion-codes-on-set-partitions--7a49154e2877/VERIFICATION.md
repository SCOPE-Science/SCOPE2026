---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Exact verification

Execute `python3 verify.py` next to `CERTIFICATES.json`. This regenerates all restricted-growth sources of lengths two through six, compares the length-four to length-six source lists to a separate construction from set-block insertion, and checks every six-point deletion incidence against inverse insertion from the receiver side. It then runs a maximum-clique search with a provably safe greedy-color pruning condition.

Expected integer results: code capacities \((1,2,3,6,14)\) at lengths two through six, with 452,972 visited recursive nodes at length six; a size-four covering of total 3; a size-five dual covering of \(25/4\); a 14-source explicit code covering 45 distinct five-point outputs; and a 41-support fractional packing of \(972/64=243/16\). The final line is `VERIFY_OK`.

All certificate inequalities are checked with integers. The algorithm contains the complete finite search and needs no optimization solver, external downloads, or stored logs. Its finite scope does not establish a formula for larger sizes or the exact fractional optimum at size six. Independent mathematical audit has not been performed.
