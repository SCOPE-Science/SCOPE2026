---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

For fixed-size uniformly sampled surviving primary set K, secondary inactivity a_i=C(q-d_i,k)/C(q,k), pair inactivity a_ij=C(q-|N_i∪N_j|,k)/C(q,k); covariance yields exactly Var(Y_k)=sum a_i(1-a_i)+2sum(a_ij-a_i a_j). The two displayed 4x5 neighborhood matrices have identical labeled secondary degrees (4,2,1,1), primary degrees (3,2,1,1,1), eight edges, and each is connected, hence trees. Independent exact subset enumeration confirms variance A=(16/25,17/20,89/100,16/25), B=(16/25,21/20,69/100,6/25) and strict -1/5,+1/5 sign reversal at budgets k=2 and k=3. Independently reran exhaustive complete incidence-matrix enumeration for every 2<=p,q with p+q<=8 using integer variance numerators, 70,479 connected labeled graphs, 352 bidegree classes and 403 distinct class profiles: none reverse, including relaxed matching by sorted degrees. Trivial one-vertex guild is uniquely star. This is a finite *exhaustive* cutoff, with full enumerator loops inspected, not a sampled experiment.

## originality

PASS

Best-of-knowledge targeted statement comparison against actual published same-object sources. The existing general principles and any known same-size phenomena are explicitly credited; the surviving contribution is the precise additional scoped statement (see four checks and residual risks).

## value

PASS

A motivated, exact minimal connected-tree counterexample to a natural degree-based robustness heuristic: every labeled species keeps its degree and all expected fixed-budget richness values, yet the risk-variance ordering reverses with primary-survival budget. The connected nine-species/eight-edge sharp cutoff is a useful small ecological network extremal benchmark even though it does not predict real ecosystems; not a routine recomputation of an iid-extinction ranking.

The dated certificate retains the supplied scientific assessment, sources and limitations.
