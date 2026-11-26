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

The constrained factor graph is strongly connected by routing through the zero vertex. Closed walks and cyclic factors agree, including the wraparound and the k=2 case. At a nonzero vertex the added outgoing and incoming counts are respectively the first-bit-zero and last-bit-zero indicators, canceling the original imbalance; at the zero vertex both additions vanish. Thus Euler traversal gives the candidate with F_k-1 extras. The rightmost-one position drops by at most one per arc, and drops by one exactly when a zero is appended to a nonzero source; summation against fixed excess divergence gives the lower bound and forces the support of every optimal excess vector onto these arcs. They are acyclic with outdegree at most one, so even a signed divergence-zero difference vanishes by processing vertices in topological order. This proves rigidity of the multiplicities, not uniqueness of the cyclic word. The frozen verify.py and VERIFICATION.md were inspected, not executed: the reported brute-force searches and Euler traces are finite corroboration, not the all-k proof.

## originality

FAIL

The October 18 Resultary theorem gives the identical all-k optimum and the identical multiplicities for a constructed optimum. Its very same sharp lower-bound certificate mechanically implies uniqueness of that multiplicity vector: all optimal extras are on tight arcs for the leading-zero potential; a tight arc cannot start with 1, so every target has at most one tight predecessor (prepend 0 to the truncated target). The potential strictly decreases along each such arc. A signed divergence-zero vector on this graph vanishes by reverse topological elimination. This is exactly the frozen outdegree argument under reversal and potential complementation, not a surviving independent result.

## value

FAIL

The optimum and the identity of forced factors are meaningful invariants, but the former is already stated and the latter is immediate from the same published instance-specific optimality certificate. Reversing the shift and spelling out elimination of a signed circulation does not yield a separate substantive finding. No scientifically distinct repair is supported.

The dated certificate retains the supplied scientific assessment, sources and limitations.
