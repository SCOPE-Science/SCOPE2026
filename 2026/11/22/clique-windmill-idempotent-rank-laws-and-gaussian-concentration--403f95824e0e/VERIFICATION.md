---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

An idempotent partial function fixes every element of its image F. The inverse image of a singleton may consist of an adjacent pair, so each extra source must neighbor its fixed target and be unique for that target. An adjacent fixed pair forbids extras on either vertex, by the inverse image of the target edge. Conversely these conditions suffice for all vertex and edge faces of the one-dimensional complex. With hub undefined, the independent blade contribution is (1+z)^s+s(s−1)z; only a singleton fixed set in a blade allows an extra source. If the hub is sent to a fixed point in blade i there are s_i choices at rank one for that blade and no other extra source may map to that target. When the hub is fixed there are z(1+z)^S partial identities and Sz extra one-source maps with the hub alone fixed. These cases are exhaustive and disjoint, cover size-one blades, and include the empty map. For equal fixed s≥2 the term mszB_s^(m−1) has mass msb_s^(m−1); the remaining mass divided by it is O_s(1/m), yielding the stated total-variation bound to the discrete iid-sum law. Differentiation gives the asserted moments with positive variance, and the center differs by only a constant from that of the discrete comparison, enabling the iid CLT. In the friendship case the distribution on 0,1,2 has weights 1,4,1 out of 6, giving mean 1 and variance 1/3.

## originality

PASS

The arbitrary-graph fiber criterion and the all-size-one star special case are established and excluded from the novel contribution. The retained claim is the explicit heterogeneous clique-blade polynomial and the consequent equal-blade rank law. The strongest inspected statements do not provide these windmill counts for noninjective partial maps or that rank law.

## value

PASS

The image-rank invariant is meaningful for the noninjective idempotents of this monoid. The exact formula treats arbitrary heterogeneous clique sizes and isolates the hub's role both combinatorially and asymptotically. The leading term is not the naive independent-blades contribution: the moving hub dominates and yields the discrete rank law to first order, from which the Gaussian scaling follows. This is useful beyond re-evaluating the known star counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
