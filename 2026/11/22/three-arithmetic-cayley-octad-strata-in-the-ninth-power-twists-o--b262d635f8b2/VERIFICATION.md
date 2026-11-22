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

# Reproduction and exact limits

Run the two included standard C++17 verifiers in a directory containing their complete source files:

```sh
g++ -std=c++17 -O2 verify_picard_theta.cpp -o theta_check
./theta_check
g++ -std=c++17 -O2 verify_picard_lines.cpp -o lines_check
./lines_check
```

The first builds exactly \(1{,}451{,}520\) symplectic transformations, identifies \(28\) odd and \(36\) even theta forms, and checks an order-nine element with centralizer nine, whose powers have the asserted cycles. The second enumerates every projective line over \(\mathbb F_{19}\), testing a homogeneous quartic restriction for being a scalar multiple of the square of a quadratic; only coefficients \(c=4,15\) have \(28\) rational bitangents. The complete infinite-field assertion is obtained by the Kummer and centralizer proof in `RESULT.md`; no finite enumeration substitutes for it. No external independent validation is asserted.
