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

# Reproducibility

Run `python3 verify.py` using the Python 3 standard library. The checker recomputes type-B Eulerian rows through degree 512 from their exact recurrence and independently verifies the signed Worpitzky finite coefficient formula through degree 32. It tests the coefficientwise modulus \(2^{1+\nu_2(n(n-1))}\) and one-descent sharpness for all rows from 2 through 512. It checks every interior two-adic valuation and its multiplicity in each power-of-two row through 512.

Output observed: `PASS 134479 exact assertions; rows 1..512, independent finite formulas through 32`.

The universal mathematical proof is in `RESULT.md`; exhaustive finite checking of the tested rows does not establish the unrestricted theorem. No independent audit or external mathematical certification has been performed.
