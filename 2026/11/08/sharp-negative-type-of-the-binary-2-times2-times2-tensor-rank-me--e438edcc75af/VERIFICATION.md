---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

PASS: definitions fix V=(F_2^2)^⊗3, tensor-rank as XOR-sum count of nonzero simples, distance rank(X−Y), and squared-distance Hilbert embedding. Independently regenerated 27 simple eight-bit masks, all 256 ranks, and all 255 Walsh characters: shell counts (1,27,162,66) and signatures/multiplicities (-9,18,-10):12, (-5,2,2):54, (-1,2,-2):108, (3,-14,10):54, (11,2,-14):27. Every rank-three mask is a sum of rank-two and rank-one. For a nonzero frequency the multiplier is K1+2^α K2+3^α K3; elementary inequalities show (-5,2,2) is the first crossing as α grows. Hence α_* is the unique root 2^α+3^α=5/2 (0.24767108819784361), with zero-sum nullity precisely 54 and minimal Euclidean dimensions 255 before and 201 at criticality. Finite exhaustive rank enumeration covers this exact 256-point domain, while the exponent inequality supplies all real α>0; rank shell samples alone are not a proof of the continuum parameter.

## originality

PASS

PASS best-of-knowledge: the 2011 Bremner–Stavrou primary paper enumerates exactly the rank shells and tensor orbits, but does not study the rank-powered kernel or Walsh negative-type threshold. The 2026 Byrne–François primary Theorem 42 gives the Cayley rank-one adjacency spectrum and its coding-theoretic applications, not the full rank-two/rank-three Walsh kernels, all-powered-distance sign interval or 54-dimensional endpoint. The earlier coding-theory spectral object is an input, not a theorem that directly implies the combined-powered sign classification. Exact Resultary searches found no prior matching exponent or 201-dimensional endpoint beyond the submission. Historical equivalence hidden in a broader tensor-metric theorem remains a residual risk; the retrieved 2026 text has extensive relevant material rather than mere abstracts.

## value

PASS

PASS: the 256-point binary 2x2x2 tensor-rank metric is a canonical smallest genuine three-way tensor space; a complete sharp negative-type exponent and embedding dimension resolve a natural geometric invariant. A finite exact spectral result of this size is legitimate because its rank-metric and Hilbert-space questions are motivated, not an arbitrary catalogue.

The dated certificate retains the supplied scientific assessment, sources and limitations.
