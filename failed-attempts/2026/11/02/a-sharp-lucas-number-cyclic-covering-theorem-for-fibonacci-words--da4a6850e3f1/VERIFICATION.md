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

With h=n−1 the indexed windows of any circular host trace a closed walk on the full binary shift graph. Subtracting one copy of each required edge leaves integral flow with supply on legal vertices that start in 1 and end in 0, and demand on those that start in 0 and end in 1. The initial run length r at a supply vertex forces at least r shifts before reaching any demand vertex, even along forbidden edges. Appending r ones reaches the legal demand vertex 0u1^r from 1^r0u and is bijective by peeling the full trailing run of ones at the destination. Legal vertices are strongly connected via the all-ones vertex; the augmentation is therefore Eulerian and gives an avoidance-preserving cover. Independently, counting a supply vertex with a marked initial one is equivalent to counting a supply vertex of some length k from 2 to h by deleting the ones before the mark. There are F_(k−1) such vertices: for k≥3 they have the form 1w10, with w any valid (k−3)-word; k=2 gives one. Hence the excess is sum_{k=2}^h F_(k−1)=F_(h+1)−1, also zero at h=1. The mandatory count F_(n+2) gives the stated Lucas identity. The source scripts were inspected, not executed; their finite checks are not the all-n proof.

## originality

FAIL

The earlier Oct. 18 indexed result computes the identical cyclic-host optimum under a host avoidance constraint, after bit complementation. Its proof uses a leading-symbol potential whose one-step inequality in fact holds on every edge of the full de Bruijn graph. Therefore its identical lower bound extends directly to unrestricted hosts, with zero mandatory imbalance at newly allowed vertices. Independently, contracting every maximal cyclic zero run to a single zero maps any unrestricted cover to an avoiding cover without losing a required window. The enlarged optimization domain consequently gives the same theorem by a direct reduction, not a distinct extremal fact.

## value

FAIL

The covering invariant is natural, but the exact evaluation is already available from the constrained theorem by run contraction, or by its unchanged potential argument. The unrestricted wording adds no new cost regime, obstruction, or construction; the equivalent alternate proof and finite checks do not create a substantively new result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
