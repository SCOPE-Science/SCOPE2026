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

# Exact finite verification

The two C++17 source files in this package contain standalone complete enumerators. The first examines all \(6^9=10077696\) choices of nine local permutations and checks whether the induced successor permutation is a single \(27\)-cycle; the second enumerates all directed Euler tours of the nine-vertex ternary overlap graph after anchoring its unique edge `000`. Both independently build the BWT run-count pair and test all exact frequencies with assertions.

Commands:

```text
g++ -O2 -std=c++17 verify_orientations.cpp -o verify_orientations
g++ -O2 -std=c++17 verify_euler.cpp -o verify_euler
./verify_orientations
./verify_euler
```

Observed outputs begin `ORIENTATION_CERTIFICATE_OK 373248` and `EULER_CERTIFICATE_OK 373248` respectively, and the eighteen subsequent comma-separated rows agree exactly. These runs were performed with the source files supplied here. The known independent total-count identity is \((3!)^9/3^3=373248\).

The source programs constitute a finite exhaustive certificate, not an infinite extrapolation. No independent external mathematical audit or formal proof-assistant validation has been conducted.
