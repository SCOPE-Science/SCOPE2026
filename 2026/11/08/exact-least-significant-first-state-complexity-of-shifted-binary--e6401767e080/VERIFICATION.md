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

# Verification of shifted digit-sum automaton state complexity

Run `python3 check.py` from the directory containing this document and the checker. The script uses the Python standard library and reproduces the following observed four-line result:

```
PASS: formula/reachability/independent DFAO minimization: 903
PASS: binary interval extremum identities: 2047
PASS: power-of-two shift exact formulas: 96
PASS: direct residual identities: 30600 (11 n-values each)
```

It enumerates all shifts in the closed range \(0\le c\le128\) and all moduli \(2\le m\le8\), compares the proposed reachable parameter set with an independent breadth-first traversal, and minimizes the resulting DFAO using fixed-point refinement by outputs and child classes. For all bit widths through ten, it checks the digit-interval extrema against literal finite enumeration. For selected larger moduli and shifts of the form \(2^k\), it verifies the closed formula. Finally it checks the kernel identity for finite digits and sample values of the unprocessed input.

The infinite proof does not rely on these bounded tests: it uses the exact quotient/remainder decomposition at every input length, an interval property of binary digit sums, and a variable-power-of-two distinguishing argument for every pair of distinct residual parameters. The test count is not an exhaustive enumeration of all possible shifts, moduli or binary inputs. Neither code nor self-review constitutes independent verification.
