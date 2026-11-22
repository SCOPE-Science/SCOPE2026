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

# Reproducible checks

Run `python3 check.py` using only the Python standard library. The checker enumerates all canonical injective tuple-orbit signatures independently of the generating-function computation: each coordinate enters a previously identified old class with remaining capacity, an existing unrepresented class with available capacity, or a new unrepresented class first appearing at this coordinate. Direct recursive enumeration counts one representative for every possible orbit invariant. A separate exact-rational computation evaluates the formal product and recovers all partial capacities through logarithmic coefficients.

Recorded output in `check_output.txt` comprises 2,018 direct orbit-coefficient matches, 300 exact inverse-reconstruction matches for \(q\in\{2,3,4,5,6\}\), and exact sharpness-witness tests at each of these five class sizes. The program implements rational arithmetic via `fractions.Fraction`; it uses no numerical tolerance, random seed or external package.

The tests are finite. The proof in `RESULT.md` covers every \(q\ge2\), all finite named bases, and all nonnegative tuple arities, by orbit classification, formal power series, triangular inversion and explicit witnesses. No independent audit has been performed.
