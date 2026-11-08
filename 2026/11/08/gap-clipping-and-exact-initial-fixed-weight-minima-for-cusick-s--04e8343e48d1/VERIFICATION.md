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
The exact C++17 enumerator `verify_extrema.cpp` checks every canonical tuple of positive adjacent gaps \(1,\dots,k+1\) at each weight \(1\le k\le8\), comparing integer numerators at the common power-of-two denominator. It verifies the complete set of minimizing tuples, not only one candidate. The separate Python `reference_check.py` uses exact `Fraction` carry transitions and independently enumerates weights one through five, independently tests 210 seeded gap-clipping instances through eight, and compares nine direct digit-sum prefix frequencies. Neither program depends on a network, private file, proprietary package, or an unembedded artifact.

Observed primary output:
```
k=1 candidates=1 c_min=3/4 minimizers=1 PASS
k=2 candidates=3 c_min=5/8 minimizers=5 PASS
k=3 candidates=16 c_min=19/32 minimizers=11,13 PASS
k=4 candidates=125 c_min=73/128 minimizers=27 PASS
k=5 candidates=1296 c_min=9/16 minimizers=107 PASS
k=6 candidates=16807 c_min=567/1024 minimizers=219 PASS
k=7 candidates=262144 c_min=2239/4096 minimizers=439,475 PASS
k=8 candidates=4782969 c_min=8839/16384 minimizers=951 PASS
VERIFY_OK all_4782969_weight8_patterns=yes exact_integer_arithmetic=yes
```

Observed independent reference output:
```
INDEPENDENT_EXHAUSTION_OK k=1..5 count= 1441
INDEPENDENT_GAP_COMPRESSION_OK random_cases= 210
INDEPENDENT_DIGIT_SUM_CHECK_OK count= 9
REFERENCE_VERIFY_OK
```

Compile and run with `g++ -O2 -std=c++17 verify_extrema.cpp -o verify_extrema && ./verify_extrema`; run `python3 reference_check.py`. The routines check exact finite computations, not mathematical uniqueness in the infinite domain by themselves. The unrestricted conclusion follows from the included symbolic carry-clipping argument. The small direct digit-frequency checks serve only as corroboration; those finite prefixes do not establish natural-density limits.
