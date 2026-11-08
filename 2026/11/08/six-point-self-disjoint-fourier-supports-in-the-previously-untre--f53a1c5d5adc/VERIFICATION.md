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

# Reproducible exact verification

To verify the finite-field part, compile the included `CHECK.cpp` with a C++17 compiler and run it:

```sh
c++ -O2 -std=c++17 CHECK.cpp -o check
./check
```

Expected final line:

```text
CHECK_OK exact_principal_minors=213053 prime=1000000093 primitive_root=993004909
```

The code verifies primality of the coefficient modulus, the primitive seventh-root condition, the six-point witness over the chosen residue field, and all \(\sum_{j=0}^4\binom{48}{j}=213053\) principal minors on subsets containing the origin with cardinality at most five. Counts by cardinality are respectively \(1,48,1128,17296,194580\). Exact integer arithmetic is used for all calculations. Since the computation establishes only nonzero determinants in a residue field, its logically valid direction is **nonzero reduction implies nonzero complex cyclotomic determinant**; the converse is neither asserted nor needed.

The infinite family is verified by the exact polynomial factorization in `RESULT.md` and elementary quadratic reciprocity; finite computations are not an infinite proof. The construction and small-field exclusion use the same fixed standard coordinate pairing. Independent external verification has not been performed.
