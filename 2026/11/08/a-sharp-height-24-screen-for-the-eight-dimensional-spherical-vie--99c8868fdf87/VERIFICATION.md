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

The statement concerns **all** positive eight-coordinate integer directions of height at most \(24\). The exact finite optimum, not any global optimum, is certified.

```sh
c++ -O2 -std=c++17 verify_view8.cpp -o verify_view8
./verify_view8 24
python3 verify_view8_independent.py
```

The first program outputs:

```text
EXACT_ENUM B=24 nondecreasing_tuples=7888725 max=8/17 optimizing_tuples=2
1 2 3 4 5 7 9 11  gcd=1
2 4 6 8 10 14 18 22  gcd=2
```

The second program outputs:

```text
EXACT_INDEPENDENT_OK hero=8/17 small_sorted_vectors=3003 deterministic_large_vectors=300
```

The exact C++ algorithm enumerates each nondecreasing tuple once, and for each of them traverses all breakpoint cells within \([0,1/2]\) using rational cross-product order. It updates the quadratic projection numerator with integer arithmetic. The independent Python script uses `fractions.Fraction`, explicitly clips every quadratic minimizer to its own cell, and compares against the projection formula. All core source files are standalone and included; no auxiliary data or external service is required.

The explicit vector has \(Q=306\), with smallest cell numerator \(576\) and minimizing parameters \(8/51\) and \(25/51\), yielding \(576/(4\cdot306)=8/17\). Simultaneous breakpoint events and repeated coordinates are included. The finite census does **not** examine vectors of height greater than \(24\); it is not a proof that the unrestricted dimension-eight constant equals \(8/17\).
