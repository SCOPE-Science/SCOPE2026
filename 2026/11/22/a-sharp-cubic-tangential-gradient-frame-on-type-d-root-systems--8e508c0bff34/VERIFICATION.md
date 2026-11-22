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

The proof in RESULT.md applies to every integer \(d\ge3\); the computational checks are finite corroboration, not a substitute for proof or external certification.

Run `python check.py` in a directory containing this document and the standalone checker. The script requires only the Python standard library and reconstructs every cubic harmonic in its chosen basis from homogeneous polynomial coefficients, evaluates the complete type-\(D\) root orbit, and compares sampled-gradient and sphere-Dirichlet bilinear forms with exact rational arithmetic.

The checked complete Gram matrices are for dimensions \(3\) through \(7\), and the checked diagonal entries are for dimensions \(8\) and \(9\). This covers all three symmetry sectors, the exceptional dimension \(4\), the sharp optimum at dimension \(8\), and the spectral-order transition at dimension \(9\). It does not check all higher dimensions computationally, and the spectral ordering for arbitrary dimensions is proved by the factorizations given in RESULT.md.
