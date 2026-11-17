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

Uniform-seed expectation equals 1+2/N times sum of pair connectivity probabilities. Coupling ordinary deletion to bridge deletion adds one edge, so bridge strictly dominates ordinary. For gateway removal E_G=1+(m-1)q_m; for bridge removal pair counts yield E_B=1+[C(m-1,2)q_(m-1)+C(m,2)q_m+p(1+(m-1)q_m)]/m. Near zero E_G-E_B=(m-2)p/m+O(p²); at p=1 equals -1/m. With m=3 q3=p+p²-p³, difference p(2p³-5p²+p+1)/3; substitute p=t/(1+t) to get 1+4t-t³ and exactly one positive root. Independent exhaustive percolation for m=2,3 gives 421 bounded validations and analytic proof treats all m.

## originality

PASS

Best-of-knowledge novel exact graph-specific vaccine switch with a complete m=3 classification and all-m existence. Earlier modular-immunization work uses a network community/fragmentation or approximate message-passing objective, while five-vertex first-onset work concerns other graph types and must not be misrepresented as a seven-vertex global minimum. Different two-cycle community graph is not a reduction to two cliques.

## value

PASS

An exact bridge-versus-gateway switch is a natural, mathematically nontrivial small counterexample to degree-only or betweenness-only immunization ranking. The m>=3 structural existence and uniquely solved seven-vertex first family member give a reusable benchmark for network contagion optimization; no global minimality is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
