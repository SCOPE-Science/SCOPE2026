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

The analytic proof reduces the eight-state tilted generator by rotations and global sign reversal, then selects the Perron root of a real \(2\times2\) matrix. The stationary endpoint entropy term changes only the diagonal conjugacy and not the asymptotic scaled generating function. Exact finite-state checks of the original stationary balance and numerical eigenvalue comparisons were independently performed.

Reproduction: run `python verification.py` using Python 3 and NumPy. There are no external data files. All real-valued parameter checks sample the strict interior \(|\gamma_e|<1\), \(|\gamma_o|<1\). These computations test finite parameter grids; they are not a proof of all-parameter validity, which is supplied by the reduction and the characteristic polynomial in RESULT.md.
