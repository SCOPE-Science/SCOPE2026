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
# Exact reproducibility

Run the standalone standard-library checkers from the same directory as this document:

```sh
python3 verify_direct.py
python3 verify_klein.py
```

The first checker enumerates all full cyclic Fourier coefficients using integer cyclotomic-residue counts at palettes of size three, four, and five, including both a shared-center butterfly and two triangles connected through a bridge. The second uses a full exact fast Walsh–Hadamard transform on \((\mathbb Z/2\mathbb Z)^2\) palettes and independently predicts the complete multiplicity histogram by a product of local factor multisets. It compares nonisomorphic block trees with equal block totals.

These are finite checks only; the proof for every block count and every finite abelian palette follows from orthogonality, rooted-block factorization and the triangular change of Fourier variables. No separate external mathematical audit is claimed.
