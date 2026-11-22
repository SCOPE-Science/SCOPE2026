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

The two included standalone programs enumerate the same mathematical objects by independently written algorithms; both must print a PASS line. Run:

```text
python3 verify_python.py
c++ -std=c++17 -O2 -Wall -Wextra verify_cpp.cpp -o verify_cpp
./verify_cpp
```

They construct \(X=\{0,1,2\}^3\) and all 27 distance-three spheres, enumerate all supports up to four vertices, and check that the respective numbers of shattered supports are 1, 27, 351, 216, 0. The complete support criterion proves that a non-shattered four-support excludes every larger support. Both verifiers compute the mod-two boundary rank by exact bitwise Gaussian elimination, without floating-point arithmetic; the rank is 133. They also check the geometric triple characterization and the count 189 of maximal edges.

Independent audit: not performed. Integral homology and a general-dimension exact topology formula are not certified.
