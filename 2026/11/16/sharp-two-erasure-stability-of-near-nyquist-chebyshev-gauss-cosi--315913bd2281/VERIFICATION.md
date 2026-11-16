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

# Verification of the mathematical claim

The complete DCT-II matrix is orthogonal with the stated Gauss–Chebyshev normalization. The complementary \(2\times2\) block has squared Frobenius norm \(T_{j,k}\) and squared determinant \(D_{j,k}\); this provides an exact independently recomputable spectrum. The proof in RESULT.md checks nonvanishing for distinct nodes, strict global endpoint-pair minimality, every four-node boundary case and the large-dimension asymptotic coefficient.

A standalone `check_dct.py` checker passed **5,346** finite assertions using direct DCT matrix constructions for sizes 4–20; it also evaluates all erasure pairs via the explicit complementary formula for sizes 21, 30, 50, 100 and 200, and checks the asymptotic coefficient at larger sizes. Run `python3 check_dct.py` with NumPy installed. The exact proof, not finite enumeration, establishes the statement for every integer \(N\ge4\).

The 2021 DCT irregular-interpolation paper is a potentially relevant historical priority risk because only its abstract could be inspected. No external or independent validation is asserted.
