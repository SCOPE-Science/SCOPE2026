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

For n>=3, rung edges are precisely edges contained in no triangles, forcing Aut(K_n square K_2)=S_n x C2. A matching is uniquely (R,A,B) with n-|R|=2h. The stabilizer of A classifies B by alternating-cycle partition lambda; cycle factors 2^(t-1)(t-1)! yield the orbit weight. A four-cycle is either within one clique or a 2-rung rectangle: direct count is 2h(h-1)+C(k,2)+m1(lambda). Counting rung-changing flips at the higher-rung endpoint gives the undirected edge census, not double-counting. The separate constructive switching argument connects all states, including odd n. Independent new direct graph generation for n=3,4,5,6 obtained (vertices,edges) (4,3),(16,30),(56,130),(376,1860) with exact local degree checks; finite tests only corroborate the general proof.

## originality

PASS

Best-of-knowledge PASS for the complete degree/orbit/census theorem. Standard simultaneous-pair-one-factor alternating cycle classification and switching connectivity are known, as are general flip dynamics on decorated graphs. The inspected descriptions of Dyer–Jerrum–Müller, Bošković and matching-flip literature do not establish the shared-edge m1(lambda) degree law and full orbit-size distribution for the prism. The 2026 general decorated-clique flip paper could conceal relevant specializations; its full text was not accessible. Retain historical priority risk rather than treating search absence as proof.

## value

PASS

The state space of perfect matchings under local 4-cycle flips on K_n square K2 is natural. The nontrivial dependence on shared horizontal edges and alternating-cycle type provides a complete degree distribution and symmetry orbit census for an infinite family, useful for exact local move statistics; connectivity is only context. This is not an arbitrary parameter slice or a claimed mixing theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
