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

# Reproducibility checks

Run `python3 verify.py` using Python 3 and the standard library only. The script reconstructs all \(2^{n+1}\) majority states on the wheel for \(3\le n\le15\), checks period-dividing-two states and actual hub changes, computes the cyclic-word polynomial independently by a four-state matrix trace for \(2\le L\le28\), compares the binomial formula, and evaluates exact integer counts through \(n=60\).

Observed execution:

```text
PASS: 27 independent polynomial/transfer comparisons; 13 full-state enumerations; 58 all-size exact integer audits; 12 reference counts
3 8 2 3 3
4 6 2 2 0
5 12 2 5 5
6 24 2 11 9
7 44 2 21 21
8 70 2 34 32
9 134 2 66 66
10 156 2 77 75
11 442 2 220 220
12 456 2 227 225
13 1432 2 715 715
14 1672 2 835 833
```

Each displayed data row contains the rim length, total period-dividing-two states, fixed-point count, strict two-cycle orbit count, and hub-changing period-two orbit count. The arbitrary-size proof is structural and uses cyclic combinatorics; the finite state enumeration is not an infinite certificate. No independent external audit is claimed.
