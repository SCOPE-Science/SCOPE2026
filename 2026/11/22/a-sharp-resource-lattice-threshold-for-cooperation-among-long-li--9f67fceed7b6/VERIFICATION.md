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

# Verification of the finite-state model statement

`verify.py` uses the four exact jump-rate formulas to construct the substochastic generator on all positive-stock states. Run `python verify.py` with NumPy and SciPy available. It checks 90 small population/capacity/parameter configurations; for the threshold-positive ones it verifies that the all-cooperator generator has the strictly largest spectral bound among the strategy blocks, and that the corresponding right Perron eigenvector is strictly increasing in resource stock. It also checks generator signs and row sums, integer threshold arithmetic in exact rational numbers, and an explicit conditional-convergence example.

A successful run prints `PASS: 90 parameter families` followed by two check descriptions. These are finite tests only. The general proof uses the finite-state Perron theorem, a strictly monotone survival eigenvector, and positive reachability. The extinction tail follows a finite-state absorption argument. There is no numerical or computer-assisted claim of an exhaustive classification of unbounded parameters or population sizes. The conditional statement holds at fixed finite \(N,K\); the order of limits is not interchangeable with the large-population limit.
