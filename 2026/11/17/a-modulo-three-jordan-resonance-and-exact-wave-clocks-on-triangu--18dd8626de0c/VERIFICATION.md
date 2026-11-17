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

# Verification record

The source files `verify_johnson.py` and `verify_direct.py` are standalone and included alongside this document. The former uses Python 3 and NumPy, and the latter only the standard library. Exact captured outputs are embedded as `matrix_output.txt` and `direct_output.txt`.

Running `OPENBLAS_NUM_THREADS=1 python verify_johnson.py` constructs the 2-subset graph independently from intersecting endpoint pairs and forms the full two-time-level transition. It reduces all integer matrix operations modulo three and tests \(\dim\ker(T_n^t-I)\) for each \(1\le t\le L_n\), at every \(n\) from 3 to 10, together with the identity at the predicted order and failure of the identity at proper divisors. All checks passed, including dimensions up to 90.

Running `python verify_direct.py` implements time updates by directly summing neighboring vertex states. It enumerates all \(3^6=729\) states at \(n=3\) and finds \(9\), \(234\), and \(486\) states of least periods 1, 3, and 9, respectively. It also verifies return within the stated clock for 120 reproducibly seeded initial states at each \(n=4,5,6,7,8\). All direct-update checks passed.

These are finite diagnostics, not a substitute for the all-parameter proof; their outputs do not independently certify novelty or the mathematical review. The unlimited statement follows from the exact incidence rank and Jordan proof in `RESULT.md`. Independent audit remains not performed.
