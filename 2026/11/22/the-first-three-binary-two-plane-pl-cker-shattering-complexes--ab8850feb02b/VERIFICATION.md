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

# Reproducibility and scope

The package includes `verify_plucker_python.py`, `verify_plucker_cpp.cpp`, and `checks.txt`. Execute the Python program with Python 3, and the C++ program with a C++17 compiler, for example:

```sh
python3 verify_plucker_python.py
g++ -O2 -std=c++17 verify_plucker_cpp.cpp -o verify_plucker
./verify_plucker
```

Both independently produce exactly the lines in `checks.txt` for ambient \(n=4,5,6\). The Python implementation assigns each input coordinate one of four binary column types and computes all minor masks by pairwise distinct-nonzero tests. The C++ implementation independently forms all ordered pairs of unequal nonzero binary row vectors and calculates each minor from its determinant. The programs exhaust all \(2^6\), \(2^{10}\), and \(2^{15}\) Boolean query supports and explicitly enumerate their realized traces. They test maximality, canonicalize each facet graph under all label permutations, and form/binary-eliminate the simplicial boundary matrices over \(\mathbb F_2\). All generated support-polynomial coefficients and finite homology ranks match. The constructive \(K_{2,n-2}\) trace witness holds for all \(n\ge3\).

The assertion of completeness is limited to orders four, five and six. Neither executable claims to verify arbitrary \(n\) nor integral homology; no external independent audit has been performed. Only research source text and scientific output are included.
