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

The all-order theorem is established by the two exact separation-mask lemmas in `RESULT.md`, not by exhaustive computation. The first finds a pair of edges with exactly the distinguisher mask of each same-shore vertex pair; the second finds a same-shore vertex-pair mask contained in the mask of each edge pair. The parity argument handles opposite-shore pairs. Nonnegative constraint containment proves every integer threshold and the fractional statement.

`artifacts/verify.py` uses Python 3 standard library only. Running `python3 artifacts/verify.py` enumerated connected bipartite graphs of diameter at most three with bipartition sizes \((2,2),(2,3),(3,3),(3,4),(4,4)\), exactly 8,701 graphs, and checked both mask lemmas by explicit distance matrices for every applicable pair. The verifier also reconstructs the six-cycle with a pendant leaf and confirms its edge/vertex signature difference at diameter four.

Finite enumeration was restricted to the stated bipartition sizes and is not an infinite proof or a census of all bipartite graphs on eight vertices. Literature priority cannot be certified by a negative search result. No independent mathematical audit or third-party validation was performed.
