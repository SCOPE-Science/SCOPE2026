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

Reproduction uses Python 3 standard library and a C++17 compiler (only for the independent full-family comparison).

```
python3 verify_doob.py
c++ -O3 -std=c++17 doob_census.cpp -o doob_census
./doob_census 0 1 4
./doob_census 1 1 4
```

The first program confirms `DOOB_NEIGHBORHOOD_SHATTER_PASS templates=7 family_samples=13`. The independent C++ full 64-vertex census returns the coefficients `1,64,1152,6912,0` and `1,64,1152,6400,0` for the quaternary Hamming three-cube and the one-Shrikhande-one-complete-factor Doob graph, respectively. The Python code separately enumerates all centered quadruples in the three two-factor templates and all relevant centered triple configurations in four three-factor templates. The universal theorem depends on the reduction in the written proof, not a finite-prefix extrapolation. No independent mathematical audit has been performed.
