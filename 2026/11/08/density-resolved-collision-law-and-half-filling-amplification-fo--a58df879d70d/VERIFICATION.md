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

The exact source files `verify_transfer.py`, `verify_direct.py`, and `verify_density.py` are independently executable with Python 3; symbolic determinant verification additionally requires SymPy. Outputs from the actual runs are included as `verify_transfer.out`, `verify_direct.out`, and `verify_density.out`.

`verify_transfer.py` constructs the 16-state paired-input matrix from the eight entries of the Rule-184 truth table, computes and factors its characteristic polynomial over the exact polynomial ring, checks initial traces and palindromicity, and prints the Perron and variance constants. `verify_direct.py` uses a separate simultaneous particle-transport implementation, enumerates all \(2^n\) inputs for every \(3\le n\le16\), groups the exact output fibers by particle number, and matches their squared multiplicities coefficient by coefficient to a polynomial Newton recurrence. `verify_density.py` evaluates the central coefficient of that recurrence through length \(200\) and compares the resulting exact integers to the claimed local-limit and conditional-probability asymptotics.

The infinite-length statements do not follow from the finite checks. Their proof requires the formal matrix-trace identity, the factored characteristic polynomial, and the Perron–Frobenius/Fourier coefficient argument in `RESULT.md`. The accessible comparison literature treats local-block preimages and traffic flow; exact duplication in unavailable historical texts cannot be excluded. Independent audit has not been performed.
