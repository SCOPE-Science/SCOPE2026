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

# Verification

Run `python3 check_dihedral.py` in an environment with NumPy. For each of the primes \(3,5,7,11\), the script enumerates every three-element support of the order-\(2p\) dihedral group, constructs the complex regular convolution matrix from group multiplication (not the Fourier-block formulas), and checks all three claimed coefficient levels for that support. It executes exactly 6,132 tests and finishes with `DIHEDRAL_THREE_POINT_PASS cases 6132`.

The code computes numerical ranks by singular-value decomposition with threshold `1e-7`. Consequently its finite data are not certificates for exact ranks or arbitrary primes. Exact proof relies on the representation-theoretic direct sum, Chebotarev nonvanishing minors, and the explicit cosine-determinant equation. The three coefficient constructions are symbolic and valid for all odd primes. No independent mathematical audit has been performed.
