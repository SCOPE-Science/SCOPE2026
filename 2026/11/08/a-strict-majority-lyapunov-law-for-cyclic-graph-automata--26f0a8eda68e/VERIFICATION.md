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

Fix any moved eligible subset S. For kappa>=3, an edge internal to S contributes at most once to successor-neighbor counts; hence |P| >= sum theta_v-|I| where P are boundary edges whose unmoved endpoint has mover successor color and I internal edges. Boundary monochromatic gain equals |P|-|Q|; since Q is subset of remaining boundary, >=2|P|-|B| >= sum(2theta_v-d_v). Monochromatic edge potential Phi increases at least eta|S|>0, giving total update budget floor((|E|-Phi0)/eta) and synchronous fixation. K_{m,m,m} at theta=m=d/2 cycles with 3 colors; kappa=2 bipartite alternating counterexample; Moore torus L>=3 degree8 theta5 gives eta2 and |E|=4L^2, at most 2L^2 updates. Independent exhaustive fresh checks of all 3-color states and eligible batches on every labeled simple graph n=2..4 agreed. Finite checks do not replace the exact potential proof.

## originality

PASS

Older Moore automata and cyclic-network studies discuss thresholds, periods or probabilistic fixation, not this exact arbitrary-finite-graph arbitrary-batching monochromatic-edge Lyapunov inequality in inspected sources. However Matamala–Goles 1997 highly relevant full text inaccessible (Oxford institution VPN disconnected); it may implicitly cover theorem. Best-of-knowledge qualified PASS, NOT a complete priority certification.

## value

PASS

A global finite-graph quantitative fixation theorem using strict local majority and a sharp universal failure boundary, covering arbitrary asynchronous eligible batches and deterministic worst-case update budgets. The multicolor condition is substantive because binary oscillations persist even at full neighbor threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
