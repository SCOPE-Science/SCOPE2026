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

# Reproducibility and boundaries

Run `python3 verification.py` with standard-library Python 3. The code constructs ballot words from first principles, computes every distinct one-deletion output set directly and checks graph edges for lengths 2–10. Separately it counts marked alternating factors by dynamic programming, and independently expands the proposed algebraic generating functions by exact integer convolution up to length 60. All calculations use integers, no floating point.

The expected per-length `(same-layer, cross-layer)` values for lengths 2–10 are `(0,0), (1,0), (3,1), (9,2), (23,8), (54,16), (128,46), (278,92), (632,233)`. A successful run ends with the message `DP and formal series agree for 0 <= n <= 60; deletion-set census agrees for 2 <= n <= 10.`

Finite computation is not an all-length certificate. The proof's crucial unbounded facts are the unique alternating mismatch interval for an ambiguous pair, the nonnegative-path flip, the ballot-prefix/first-passage decompositions and the formal generating-function identities. Singularity transfer supports the asymptotics. Independent mathematical validation has not been performed.
