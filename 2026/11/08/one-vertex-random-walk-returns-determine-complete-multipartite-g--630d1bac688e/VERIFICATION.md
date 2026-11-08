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

# Verification procedure and limits

Run `python3 verify.py` using Python's standard library. It independently constructs all labeled-by-part simple random-walk transition matrices over integer partitions of each order from 2 through 11, computes exact return sequences through time \(2N-1\), and compares each with the exact quotient-chain prediction. It checks that no different rooted multipartition at the same order gives the same truncated return sequence, and independently evaluates full and quotient matrix resolvents at two rational spectral parameters. The algebraic inversion of the quotient resolvent is checked at the same points, and the zero-space partwise projection is tested by rational matrix products. The bipartite ambiguity when the order is unknown is checked for multiple integer pairs.

Recorded execution: `VERIFY_OK 25856 exact-rational checks`; uniqueness signature counts by \(N=2,\ldots,11\) were respectively 1, 3, 6, 11, 18, 29, 44, 66, 96, 138.

These calculations do not certify all graph orders or settle historical novelty. The universal claim rests on the explicit algebraic proof in `RESULT.md`. No external mathematical audit was performed.
