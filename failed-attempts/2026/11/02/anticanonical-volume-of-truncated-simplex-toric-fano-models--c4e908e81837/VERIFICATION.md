---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The volume and Q-Fano assertions are correct. At a vertex of Q_n, n independent coordinate bounds must be active. Two lower bounds are infeasible and n upper bounds force the remaining coordinate to be -2n; the complete vertex list thus has one coordinate i at -(2n-1), one free coordinate j at 1 and all others at 2. The list has n(n+1) primitive vertices; zero is interior. The negative polar is the anticanonical polytope, with normal fan the stated face fan (using the inward-normal convention). Independently of the proposed cap argument, the facet of the polar corresponding to (i,j) consists of -u_i/(2n-1) and u_k/2 for k distinct from i,j. Coning each such facet to zero gives a simplex of normalized volume 1/[(2n-1)2^(n-1)] because the unscaled vectors, up to one sign, are exactly the coordinate-function basis omitting u_j. Their interiors are disjoint and they exhaust the polar. This gives the formula, the three low-dimensional degrees, and asymptotic n/2^n, including n=2. The cap proof can also be justified: every pairwise barycentric sum is positive on the polar generators, so an edge from the single apex outside facet i intersects its supporting plane within that simplex facet.

## originality

FAIL

The numerical expression was not located verbatim, but it follows mechanically from the prior construction's explicit primitive ray and polar vertex data, using the standard toric degree identity and equal basis determinants. This is not merely a related family: the explicit lattice isomorphism below identifies the exact variety. The rejection is for direct implication, not for locating a prior verbatim formula or inferring priority from a search miss.

## value

FAIL

The family is naturally motivated by its small alpha invariant, and its exact degree can be a useful datum. But here the exact degree is already a routine determinant calculation from the published polar and facet data. The exponential decay is a direct restatement of that calculation, not a separate estimate or obstruction, and the record gives no distinct volume question that the calculation resolves. No genuine surviving non-routine claim is isolated by relabeling this family or by improving the cap proof.

The dated certificate retains the supplied scientific assessment, sources and limitations.
