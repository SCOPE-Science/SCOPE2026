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

Analytic verification: the squared-coordinate vector field preserves \(u+v+w\) and the weighted product \(H=u^cv^bw^a\). Strict concavity gives a regular periodic foliation. Vertex passage times are respectively \(\log(1/H)/(2ab)\), \(\log(1/H)/(2ac)\), and \(\log(1/H)/(2bc)\), each up to a bounded error; connecting arcs contribute bounded time. Normalized spherical area pushes forward to Dirichlet \((1/2,1/2,1/2)\), whose negative weighted-product moments have threshold \(1/(2\max\{a,b,c\})\).

A standalone numerical/algebraic checker is included as `check.py`. Its finite integration tests validate period normalization for two parameter triples but are not substitutes for the analytic proof. These checks do not constitute an independent audit.
