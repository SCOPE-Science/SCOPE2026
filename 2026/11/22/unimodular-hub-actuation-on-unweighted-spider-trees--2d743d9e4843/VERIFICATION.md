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

# Reproduction and boundaries

With Python 3 and SymPy installed, place `RESULT.md` and `check.py` in the same directory and run `python check.py`. The script uses integer Laplacians and polynomial resultants; it requires no data files or network access. It tests 120 unordered grounded-path pairs with lengths from one through sixteen, three-arm profiles with arms in one through six, four-arm profiles with arms in one through four, and representative invariance and integer-inverse cases (218 assertions total). All assertions passed in the performed check.

The unrestricted proof is in `RESULT.md`. Finitely many passing assertions cannot certify all spider sizes; conversely, the proof does not depend on sampling. The sign of the determinant depends on ordering and sign conventions; the theorem concerns its absolute value. The integer input consequence uses \(I-L\) and does not claim this matrix is a stable stochastic transition. No independent mathematical validation was performed.
