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

# Computational verification

Run from the directory containing these files:

```
python3 code/reduced_checker.py
c++ -O2 -std=c++17 -Wall -Wextra -pedantic code/direct_checker.cpp -o direct_checker
./direct_checker
```

The exact binomial-weighted checker enumerates 437 parameter pairs covering \(s<r\), \(s=r\), and \(s>r\), for \(2\le r\le50\). Each of the \((r+1)(s+1)\) count-and-hub classes contributes its exact combinatorial multiplicity, not a Monte Carlo estimate. The other checker constructs explicit graph-neighbor lists, directly iterates all binary configurations in 49 pairs, and checks 1,395,984 labelled initial states. The captured output files are `evidence/reduced_output.txt` and `evidence/direct_output.txt`.

Checks cover exact fixed and primitive-two-cycle populations across regimes, sharp maximum entry times, and exact all-population formulas for \(s>r\). The proof supplies all-parameter justification independently of the finite computations. No third-party validation or automated proof-assistant certification has been performed.
