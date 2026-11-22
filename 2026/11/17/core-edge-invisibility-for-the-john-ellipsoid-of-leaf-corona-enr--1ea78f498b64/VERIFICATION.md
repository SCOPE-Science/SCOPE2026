---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

Since every vertex is in an edge and G is bipartite, the signed stable-set polytope equals {|x_a|+|x_b|<=1 : ab edge}. Independent coordinate sign reflections force unique John ellipsoid diagonal centered at 0. Squared semiaxes u optimize strictly concave sum log u_v under all edge sums u_a+u_b<=1. Candidate u_core=1/(p+1), u_leaf=p/(p+1) has every leaf sum 1 and every core sum<=1. Positive dual multipliers lambda_leaf=(p+1)/p solve leaf/core gradients exactly; concavity supporting hyperplanes prove GLOBAL unique optimum for arbitrary core edges. Core facet support sqrt(1/(p_i+1)+1/(p_j+1)) equals 1 iff both p_i=p_j=1, else <=sqrt(5/6), producing stated clearance /sqrt(2) and 4 signed facets per edge. Product semiaxes gives volume; claims checked against edge facet irredundancy. Independent exact rational enumeration of all bipartite core-edge subsets r<=5, p_i in {1,2,3}, gave 49,365 core-edge dual/feasibility checks; finite corroboration, not proof beyond formula.

## originality

PASS

The specific final scientific assertion is not known to be a mere restatement of the inspected broader theorems; the comparisons explicitly distinguish known methods/formal or rational information from the residual exact theorem. This is a best-of-knowledge priority assessment, not a proof of absence.

## value

PASS

An explicit all-core-edge shielding theorem with heterogeneous leaf multiplicities, complete facet contact classification, and uniform positive clearance provides a useful and surprising exact convex-geometric answer. General John variational characterization alone does not state which graph edges become irrelevant or when they cease contact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
