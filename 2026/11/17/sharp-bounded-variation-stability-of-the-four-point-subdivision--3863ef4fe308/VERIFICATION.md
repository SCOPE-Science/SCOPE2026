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

# Reproduction and limits

Compile `verify_fourpoint.cpp` using `g++ -O3 -std=c++17 verify_fourpoint.cpp -o verify_fourpoint`. Running `./verify_fourpoint 22` yields the following exact integer values:

```
level=22
denominator=309485009821345068724781056
variation_numerator=402935131604148261256695280
second_difference_numerator=223063136467054424320
upper_numerator=402935354667284728311119600
```

The numerator sums represent \(V_{22}\) and \(W_{22}\) over the common denominator \(16^{22}\). These are finite integer computations; the separate analytical inequality \(0\le L(1/16)-V_{22}\le W_{22}\) certifies the infinite limit. An independent Python rational implementation matched the exact recurrence and both sums for levels zero through eight. The C++ program requires a standard GNU/Clang compiler supporting signed 128-bit integers and uses memory proportional to the number of refined edges. It refuses levels above 22 to avoid integer-overflow risks.

No external audit or independent certification is claimed.
