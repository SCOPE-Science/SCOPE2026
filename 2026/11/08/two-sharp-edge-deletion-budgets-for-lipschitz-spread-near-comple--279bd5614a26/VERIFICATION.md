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

Graph diameter≤2 follows from Δ(H)<n/2. Strictly convex variance on anchored Lipschitz polytope forces connected tight-edge spanning graph at a maximizing vertex and integral 0/1/2 values. Opposite levels A,B form an H-biclique and have exact n² variance numerator n(a+b)−(a−b)². For ab≤k≤(n−2)/2, t=a+b≤ab+1≤n/2 and monotonicity proves star envelope and unique strict extremizers. For a,b≤r<n/2, equality at a=b=r forces an isolated H-Krr component. Floor threshold and n=4 boundary hold. Independent exact enumeration and symbolic/integer checks corroborate all formulas; proof is all n.

## originality

PASS

The two exact adversarial budget envelopes and strict equality rigidity survive literature comparison. Prior no-K2,2 complement theorem contains star specializations but is inapplicable to the r≥2 biclique extremizer; classical integrality is credited. Best-knowledge originality PASS.

## value

PASS

Sharp resilience budgets explain how many arbitrary missing edges or missing neighbors a complete graph tolerates before its Lipschitz variance can increase, with extremal star versus balanced biclique geometry. Two different natural perturbation norms, exact transition and rigidity make this a meaningful infinite-graph-family classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
