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

# Verification and reproducibility

The included `checker.py` and `verification_certificate.json` are an independently runnable *computational diagnostic*, not a formal certificate of the universal inequalities. Run `python checker.py` with Python 3 and SymPy installed in the same directory as these two files. The script recomputes the exact period-matrix trace, determinant, characteristic-polynomial factorization, discriminant, tie-point and half-exchange identities, and compares the sign of the quadratic with the directly calculated Perron eigenvalue on 707 rational parameter pairs. It also verifies four exact parameter-sign examples. The observed terminal report was `PASS` with 721 assertions.

The unrestricted result follows from the analytic argument in `RESULT.md`: the smaller eigenvalue remains below the sedentary benchmark for every \(d\); the characteristic polynomial then reduces the comparison to the sign of a convex quadratic; its exact discriminant yields the thresholds and the whole migration-benefit interval. Diagnostics cannot prove uniqueness, exhaust the continuum, or establish historical priority. For \(r>2+\sqrt3\), the proof asserts only that all global optimizers lie in the winning interval, not uniqueness within it.

The binary calendar and the direct-exchange versus equal-pool distinction are part of the theorem's scope. No empirical ecological validation or independent audit has been performed.
