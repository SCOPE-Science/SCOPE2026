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

The proof is symbolic and does not rely on numerical extrapolation. The certificate uses the linear-algebra model \(xy=B(x,y)v\), identifies the radical with the annihilator, and reconstructs all supported diagrams by orthogonal changes on the nondegenerate quotient followed by radical shears. The only non-elementary standard input is the transitivity of the orthogonal group on nonzero vectors of a fixed quadratic norm (Witt extension), including isotropic vectors. No computational test certifies that theorem in all dimensions.

# Reproduction

With Python and SymPy 1.14.0 installed, execute `python checks/replay.py` from the directory containing this document. The checker performs exact symbolic Gram-matrix checks, verifies that the old square vector has the requested support in the new orthogonal natural basis, and confirms the predicted support-pattern counts for dimensions \(d=1,2,3\) and radical dimensions \(r=0,1,2\) where the algebraic type is possible. Its recorded output is `checks/output.txt`, concluding `VERIFY_OK constructed_patterns=124`. Source code and output are both included, not referenced outside this package.

# Boundaries

The checker constructs permitted examples only in the stated finite range; necessity and the arbitrary-dimensional converse are proved in the accompanying theorem. It does not enumerate all natural bases, certify priority, or constitute an independent audit. The theorem is restricted to algebraically closed fields of characteristic different from two and rank-one square.
