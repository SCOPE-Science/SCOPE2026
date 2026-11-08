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

# Reproducibility

The result is an exact finite-state classification of labelled order-five Latin squares under one four-cell intercalate move. The packaged C++17 source `latin5_cert.cpp` independently checks all \(161{,}280\) states, every local move, all components, all isotopies of the non-group seed, consistency of the three parity bits, and the exact seed distance histogram. The packaged Python 3 source `latin5_verify.py` constructs states from reduced Latin squares rather than from full-row enumeration; its move generator uses a different two-row permutation predicate and its symmetry argument builds the even-isotopy orbit using explicit three-cycle generators.

Run:

```sh
c++ -std=c++17 -O2 latin5_cert.cpp -o latin5_cert
./latin5_cert
python3 latin5_verify.py
```

The expected output includes `states=161280`, `isolated=17280`, `mobile_components=8`, `sector_size=18000`, `edges=288000`, and `diameter=radius=13`. Both programs independently assert the complete fourteen-term distance histogram. The input domain is exhaustive; no probability, sampling, or timeout inference is used. These checks establish the stated finite claim but cannot independently guarantee novelty in the entire mathematical literature or behaviour outside order five.
