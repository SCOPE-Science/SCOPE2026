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

The following commands use standard Python 3 and C++17, without external libraries:

```
python3 verify.py
python3 recurrence.py
python3 homology.py
c++ -O2 -std=c++17 verify.cpp -o verify_cpp
./verify_cpp
```

These commands were executed from the extracted standalone programs. The Python exhaustive checker forms all even-shore cut signatures for \(n=3,4,5,6\) and tests every edge subset. The C++17 checker instead computes a binary linear rank of the selected edge columns. They agree with the forest criterion for every support (up to \(2^{15}\) supports at \(n=6\)). Both programs report identical complete face polynomials. An unrelated component recurrence agrees with the labeled exponential formula through \(n=10\); a direct binary simplicial boundary calculation confirms the top Betti values at \(n=4\) and \(n=6\).

Outputs are ordinary finite mathematical checks, not infinite proofs or independent peer audit. General correctness relies on the linear-algebra, tree-parity, and matroid-shellability proof in RESULT.md.
