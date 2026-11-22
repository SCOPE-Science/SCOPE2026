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

# Verification scope

The proof is self-contained subject to standard finite-field character orthogonality, the magnitude of nondegenerate quadratic Gauss sums, and a bounded fourth-order Taylor remainder. The central first- and second-order moments and the cubic-correlation bound are explicitly derived in RESULT.md. Both moment identities were recomputed by direct finite sums with `python3 verify_erasure.py` for 48 examples: nine primes up to 43, several erasure patterns of sizes one, two and three, and the extension field of nine elements.

The diagnostic residual is scaled by the predicted \(q^{-3/2}\) rate. These finite examples check signs and normalization but are not an infinite-case proof. The constants in the uniform remainder are not optimized; the expansion is asserted only for \(q\ge16h^2\). The higher-order \(q^{-3/2}\) coefficient and any classification of its geometric dependence are not claimed. Independent mathematical review has not been performed.
