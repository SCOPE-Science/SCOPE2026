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
# Verification

The theorem is proved for every \(n\ge4\) in RESULT.md by four disjoint light/heavy cases. To reproduce its independent finite corroboration with standard Python 3 and C++17:

```sh
g++ -std=c++17 -O3 verify_prism.cpp -o verify_prism
./verify_prism
python3 verify_prism.py
```

The direct C++ verifier evaluates the actual graph adjacency and closed-neighborhood sums for all \(4^{2n}\) assignments for each \(2\le n\le6\), comparing all coefficients for \(4\le n\le6\). The Python program counts allowed column states at each fixed pair of row totals and compares the complete polynomial through \(n=9\). The programs do not establish an infinite theorem by themselves; their role is independent finite agreement with the proof.

Expected terminal checks: `DIRECT_NEIGHBORHOOD_CERTIFICATE_OK` and `LAYER_SUM_CONVOLUTION_CERTIFICATE_OK`. No external/independent mathematical audit has been performed.
