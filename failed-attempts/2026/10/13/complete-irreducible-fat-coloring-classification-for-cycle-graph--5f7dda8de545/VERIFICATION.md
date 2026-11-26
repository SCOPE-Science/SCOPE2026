---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

On the connected 2-regular cycle, a nontrivial FAT partition has 2*alpha in {1,2} and beta+(k-1)*alpha=1. The alpha=1 case alternates, and with alpha=1/2 the only possibilities are two equally counted neighbor colors or the proper three colors. In the former case the same-color edges alternate with the different-color edges; closing the cycle also requires an even number of color changes, hence 4 divides n. The two choices of initial edge status give distinct indexed partitions even after forgetting palette names. The proper three-color rule forces period three and one unlabeled partition. Where periods two and three coexist, a class modulo three crosses parity. Where periods four and three coexist, a class modulo three crosses each paired bipartition (0 and 3 for 0011; 1 and 4 for 0110). Thus no nontrivial partition is strictly refined by another FAT partition. The trivial partition is maximal only when alone. This gives the count for all n>=3 and contradicts the explicit published count on C_4 already.

## originality

FAIL

The correction of Beers–Mulas Example 5.12 is valid, but the mathematical classification is a direct restriction and finite-cycle descent of the earlier complete perfect-coloring theorem for the infinite path (Parshina–Lisitsyna, Proposition 3). That paper explicitly lists 2112 among the perfect binary periods. Selecting the constant diagonal/off-diagonal quotient parameters, counting allowable shifts and comparing the listed periods under refinement mechanically gives the asserted count. The later incorrect count does not erase that earlier mathematical coverage; this review does not assert that the earlier paper uses FAT terminology or already prints the correction as such.

## value

PASS

The two additional maximal partitions give a concrete counterexample at C_4 and a sharp boundary for the failure of a published statement about all cycles. The correction matters because maximum palette size does not determine maximality under refinement. The value is in the explicit witness and its interpretation, not novelty of the period classification or merely recomputing a known exact invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
