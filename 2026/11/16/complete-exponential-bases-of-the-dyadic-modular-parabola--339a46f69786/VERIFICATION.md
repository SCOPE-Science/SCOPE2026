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

# Verification

The included `check_spectra.py` was executed with Python 3. It checked all \(2^{2k}\) Gauss sums at each of \(k=1,2,3,4,5\), using the exact cyclotomic cancellation criterion, confirming nonvanishing in the same-first-parity/opposite-second-parity case and exact reduction for even-even differences. Independent exhaustive maximum-clique enumeration recovered exactly \(4,64,16384\) orthogonal bases at \(k=1,2,3\), agreeing with the theorem. Marker: `DYADIC_PARABOLA_COMPLETE_SPECTRA_PASS`. The program makes no claim of exhaustive enumeration for all exponents; correctness for all exponents comes from the written proof. Independent review is not performed.
