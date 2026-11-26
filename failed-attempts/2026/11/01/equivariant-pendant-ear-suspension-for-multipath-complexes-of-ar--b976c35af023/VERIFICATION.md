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

In RESULT.md lines 40–58, p_i excludes q_i by the two-cycle condition and b_i by indegree at v_i. Adding a_i then fits the free outgoing slot and ends at the fresh leaf w_i, so creates no directed cycle. The reverse statement holds for q_i and b_i. All additions use disjoint new vertices and no root, so they work simultaneously even with repeated roots and a cyclic base. The replacement is therefore simplicial and contiguous to the identity, and the linear homotopy fixes the stated join pointwise and commutes with the specified symmetries. Each cone-link deletion is an elementary-collapse sequence: for a lower face containing the deleted vertex but not its dominator, all cofaces other than its paired enlargement have already been removed in descending order. Deleting attachment vertices does not delete any dominator. The reduced join-chain shift is integral and includes the augmented empty-arc case. Each zero-cycle has shifted degree one; their join gives the arm-permutation sign, and reversal negates each of the m factors. The submitted checker was inspected only as finite corroboration.

## originality

FAIL

Two earlier published catalogue records materially cover the claim. The October 18 record already proves the entire displayed subdivided-star collapse, sphere and integral character, even allowing one arm. More decisively, the October 25 forest proof explicitly proves the identical pair of local dominations and the identical residual join. Its argument uses only the degree-two fresh midpoint, fresh terminal leaf, directed two-cycle prohibition, and the two degree slots at the midpoint, not the global forest hypothesis. Extracting those local steps gives the arbitrary-base collapse, including repeated roots, with no new obstruction to check. The earlier statements do not literally assert the equivariant strong deformation retraction, but the standard vertex replacement at each domination gives exactly the submitted map: both inner directions map to the corresponding compatible outer directions, whose images contain no other replaced vertices. These replacements commute, and arrow reversal interchanges the two pairs. Hence contiguity and symmetry of the resulting map are direct consequences of the same local folds. This is demonstrated prior coverage/implication, not a rejection based on the unavailability of a paper.

## value

FAIL

An arbitrary-base suspension rule is a useful structural observation. Here the earlier dominated-vertex proof already does the local work independently of the base, and the fixed join, simultaneous retraction and suspension character follow by applying those same folds and permuting their factors. The remaining advance is a restatement with elementary symmetry bookkeeping, not a further motivated classification or operation. The frozen canonical application is itself already an exact published result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
