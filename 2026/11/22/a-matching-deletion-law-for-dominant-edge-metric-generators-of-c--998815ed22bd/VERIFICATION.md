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

The proof is a structural classification, not an extrapolation from finite data. The public source files `verification/verify_bfs.py` and `verification/verify_witness.cpp` independently evaluate all admissible sensor sets using graph distances, without calling the formula as an acceptance test. Each compares the resulting omitted-cardinality polynomial with the closed formula and fails on a coefficient mismatch. The Python verifier also checks all inclusion-minimal sensor-set coefficients against the stated second polynomial by testing every one-vertex deletion.

Checks executed from the supplied sources:

```
python3 verification/verify_bfs.py
# PASS: 71 cases, m,n>=3, m+n<=11, 0<=t<=min(m,n)
g++ -O2 -std=c++17 verification/verify_witness.cpp -o verify_witness
./verify_witness
# PASS: 108 cases, m,n>=3, m+n<=12, 0<=t<=min(m,n)
```

Both methods explicitly enumerate all vertex subsets in each tested graph. The Python method reconstructs edge-distance vectors; the C++ method uses per-edge-pair distinguishing-vertex bitmasks. The universal statement relies on the five-step proof and not on the bounded checks. The scientific theorem has received only the stated self-review; no independent audit has been performed.
