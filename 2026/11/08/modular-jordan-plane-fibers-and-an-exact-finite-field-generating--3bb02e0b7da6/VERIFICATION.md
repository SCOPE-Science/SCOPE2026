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

# Verification record

The principal algebraic arguments establish the theorem for all matrix sizes and all finite fields. Direct finite checks reconstruct the original equation rather than accepting a precomputed list of conjugacy classes.

Run `python3 artifacts/check_jordan_plane.py` with Python 3 and its standard library. Its output must match `artifacts/check_results.txt` exactly. The checker enumerates every candidate \(Y\) in the listed small prime fields, forms the linear map \(X\mapsto XY-YX\), determines whether \(Y^2\) lies in its image by modular Gaussian elimination, counts all \(X\) from the nullity, and compares with exact rational-coefficient extraction from the generating product. For \(\mathbb F_4\) in dimension two, the checker uses the irreducible polynomial \(z^2+z+1\) to build a four-element field and explicitly tests all ordered matrix pairs.

Recorded totals: \(R_{3,2}=2192\), \(R_{3,3}=95499\), \(R_{2,4}=1216\), \(R_{2,5}=1225\). The output also includes all other checked dimensions. Tests are exhaustive only for the specific dimensions and fields listed, not for unbounded dimensions or all finite fields. The symbolic argument supplies the general proof.

No independent mathematical audit, third-party replication, or certification has been performed.
