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

# Verification of the finite domination and learning claims

The exact finite domain has fourteen vertices, twenty-one minimum dominating concepts and \(2^{14}\) possible vertex-query supports. Both programs visit the full finite domains, not a sample. The two incidence models are nonzero-vector/dual-vector geometry and cyclic difference-set geometry.

From this directory execute:

```sh
python3 verify_binary.py
c++ -std=c++17 -O2 -Wall -Wextra verify_cyclic.cpp -o verify_cyclic
./verify_cyclic
```

Recorded outputs are `python_output.txt` and `cpp_output.txt`. Both confirm the minimum cardinality four, twenty-one optima, full face counts \((1,14,70,0,\ldots)\), graph-complement criterion, and exact online rank three. The Python verifier also explicitly checks all eight paths in a stated depth-three decision tree, while the C++ verifier computes online dimension by an independent recurrence. The underlying finite proof and quantifier boundaries appear in `RESULT.md`. No higher-order or unrestricted graph-family assertion is tested or claimed.
