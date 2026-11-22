---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification record

The exact finite classification has a fully enumerable domain: each labelled graph with at most five vertices is represented by its complete edge bitmask. Every missing edge is considered; an insertion is included only when both graphs are triangle-free. Exact rational comparisons decide whether the adjacent-pair type proportion rises, ties or falls. All edge-mask cases are exhausted and every decreasing five-point marked pair is canonicalized under all 120 permutations of the five vertices.

The supplied `verification/verify.py` checks the independence-set formula by a subset-zeta computation. It independently checks all full two-new-point adjacency diagrams of the two five-point and one connected six-point witnesses using direct triangle testing, reproducing their exact nonadjacent and adjacent type counts. The result includes a numerical census and two finite graph witnesses. The unbounded persistence statement uses an algebraic factorization and is not inferred from finite tests.

Replay with `python3 verification/verify.py`; compare its stdout to `verification/output.txt`. This record contains no claim of independent mathematical audit or formal proof assistant certification. Historical novelty is provisional.
