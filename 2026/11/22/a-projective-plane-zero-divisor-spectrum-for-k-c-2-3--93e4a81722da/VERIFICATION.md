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

# Reproduction of mathematical checks

Use Python 3 to execute `python3 checker.py` in the directory containing this file and the checker. The essential finite-field arithmetic, multiplication checks, projective-plane incidence checks, and determinant comparisons use only Python's standard library. If NumPy is present, the script also constructs the complete 127-vertex adjacency matrix over \(\mathbb F_2\), computes its real eigenvalues, and compares all of them with the asserted multiplicity-factorization. The included `CHECK_OUTPUT.txt` records the output from an environment where NumPy was available.

The source code independently multiplies in the basis \(x,y,z,xy,xz,yz,xyz\) and compares those products against the projective-block formula. It enumerates all 127 nonzero radical elements and all 8,001 unordered pairs of distinct vertices for \(q=2\). For \(q=4\) it enumerates the 16,383 vertex block assignments and samples 25,000 ordered pairs; for \(q=8\) it samples 10,000 ordered pairs. It also verifies \(NN^\top=qI+\mathbf1\mathbf1^\top\) by explicit finite-field projective geometry at \(q=2,4,8\).

These executions check finite cases only. The all-field theorem relies on the algebraic squarefree-degree decomposition, the incidence matrix identity, exhaustive invariant-subspace dimension count, and symbolic determinant-sign argument in RESULT.md. They are not independent formal certification. No claim is made about fields of odd characteristic or more than three generators.
