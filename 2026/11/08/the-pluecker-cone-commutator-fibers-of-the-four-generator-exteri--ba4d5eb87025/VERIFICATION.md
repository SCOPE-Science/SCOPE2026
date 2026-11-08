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
# Verification and reproducibility

This package includes complete standalone `verify.cpp` and `verify.py`. The former tests all \(3^{16}=43{,}046{,}721\) odd-component ordered pairs over \(\mathbb F_3\), each of the \(3^7=2187\) possible output values, and all four fiber categories. The latter independently counts the \(q^8\) ordered vector pairs over \(\mathbb F_q\) for \(q=3,5\) and compares 10,000 direct full sixteen-coordinate Grassmann products per field against the formula. Both checks returned `VERIFY_OK`.

Commands, from the extracted package directory:
```
python3 verify.py
g++ -O3 -std=c++17 verify.cpp -o verify
./verify
```

No special external mathematical packages are needed. The C++ exhaustive test is for \(q=3\), not for infinitely many fields; the Python exhaustive vector wedge checks are for \(q=3,5\), with deterministic randomized full-product checks in both. All odd prime powers are covered by the written linear-algebra proof, not by finite extrapolation. Independent mathematical audit was not performed.
