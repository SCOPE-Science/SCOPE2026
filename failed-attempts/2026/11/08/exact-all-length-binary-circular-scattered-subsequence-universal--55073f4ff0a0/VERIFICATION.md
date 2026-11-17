---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

The fixed binary alphabet, rooted/indexed words, single common rotation and n=1,2 boundary are explicit. Greedy complete-alphabet arches are equivalent to disjoint unequal-adjacency edges; cutting a cyclic matching at an omitted edge gives the same maximal index. Even transition parity gives exactly two lifts; the 3-state transfer matrix T(v) has characteristic polynomial x[x^2-x-(v+v^2)u], with an even all-marked duplicate requiring subtraction of 2u^(n/2). Coefficient extraction yields N(n,0)=2 and N(n,k)=2^k*n/(n-k)*binom(n-k,k)-2*[n=2k]. Reconstructed this argument and independently enumerated all 2^n words, all rotations and target subsequences for n=1..8; every count agrees. Finite enumeration corroborates, while the transfer identity proves every length.

## originality

FAIL

The all-length distribution and even-length correction are already published with precisely the same binary circular-index definition and stronger moment formulas (October 25), and independently again as the identical bivariate series (October 26). The submitted cycle-matching and transfer-matrix proof is mathematically equivalent; a different presentation is not an original theorem.

## value

FAIL

The main claimed mathematical census is fully pre-covered. The new account offers no separately motivated unknown exact parameter, structural theorem or improvement beyond re-expression of the same cycle matching, transfer matrix and full distribution; correctness and reproducibility cannot rescue scientific value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
