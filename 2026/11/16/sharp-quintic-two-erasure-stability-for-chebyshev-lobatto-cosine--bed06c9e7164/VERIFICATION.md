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

The analytical proof in `RESULT.md` establishes the theorem for every integer \(N\ge4\) and every pair of distinct deleted nodes. Its critical steps are the orthonormal type-I cosine identity, the complementary minor singular-spectrum identity, the exact two-by-two determinant, and a strict global comparison of all erasure pair classes.

The included script `check_dct1.py` reconstructs the full DCT-I matrix directly and compares full and complementary singular values. It passed **52,800** deterministic assertions, covering every deletion pair for \(4\le N\le52\), direct surviving-matrix checks for \(4\le N\le20\), symmetry and unique worst pairs, and high-degree asymptotic checks. Run `python3 check_dct1.py`; it requires Python and NumPy.

Finite computations do not substitute for the proof for unbounded \(N\), do not show that every prior paper has been read, and do not perform an external or independent audit. The historical-priority risk is specifically discussed in `REVIEW.md` and `RESULT.md`.
