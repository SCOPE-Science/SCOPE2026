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

Complete radius-one binary Hamming balls intersect iff center distance is at most two. Distinct Dyck centers have equal weight and hence even distance, so disjoint-ball packings are exactly distance-at-least-four codes. Independently enumerated sources by the equivalent zero-based up-step position bounds p_i <= 2i, rebuilt all balls including unaltered outputs and non-Dyck outputs, checked the integer witnesses, and verified both sparse rational LP certificates by every primal and dual inequality. The (source count, integer witness size, matching primal/dual objective) triples were (1,1,1),(2,1,1),(5,2,2),(14,4,4),(42,10,10),(132,22,26). In the sixth case there were 726 outputs, with 68 nonzero primal weights and 51 nonzero dual weights. For the crucial separate integer upper bound, a fresh bitmask decision search on the graph formed by literal disjoint balls found a 22-clique after 8716 calls and excluded a 23-clique after 137602 calls. Each reverse traversal uses the proper coloring of its remaining prefix, so the prefix color count bounds a clique extension and the skipped branches cannot attain the target. For n <= 5 the LP upper bounds already match the integer witnesses. Thus the first gap is 26-22=4 and the ratio is 13/11. The frozen C++ prefix-color logic was also inspected; neither its recorded node count nor the optional MILP result was used as evidence of the upper bound.

## originality

PASS

No distinct inspected result establishes or implies the exact constrained full-ball substitution profile. The known Catalan basis construction identifies the integer graph but does not compute this independence number or the full-ball packing LP. An indexed same-date result is not dismissed on its date: the deletion and adjacent-swap theorems are compared by their distinct channel assumptions and values. The pass applies to the exact finite profile and gap, not to the graph or LP framework, and is not a historical priority certification.

## value

PASS

The complete ball-packing LP is the natural relaxation for unrestricted binary one-bit substitution on this structured balanced language. Determining the first instance where it overestimates the integer code size by four, including after rounding, gives a concrete limit on using that bound to certify optimality. The earlier exact equality range is part of that boundary claim rather than an arbitrary cutoff.

The dated certificate retains the supplied scientific assessment, sources and limitations.
