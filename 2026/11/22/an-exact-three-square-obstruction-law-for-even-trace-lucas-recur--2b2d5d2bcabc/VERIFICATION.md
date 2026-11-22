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

# Reproducibility and limits

Run `python check.py` with Python 3.8 or newer and no external libraries. The checker independently evaluates two recurrences: exact integers for 22,680 instances and residues modulo a power of two for another 1,664,000 instances, covering even traces through 128, odd companions through 129 and positive indices through 400. It compares Legendre obstructions computed from resulting terms against the explicit index-only formula.

A second check counts three-square obstructions in the first 16,384 indices for five representative parameter choices, one for each proved density phase. Output should report all assertions passing, and list the densities `1/24`, `1/12`, `1/6`, `7/24`, `1/3`. These checks were executed on the supplied checker source. For the modular loop, the program asserts that no term vanishes at its chosen modulus; consequently the required low valuation and odd-unit bits are visible.

The proof of the infinite theorem is contained in `RESULT.md` and does not depend on extrapolating from finite tests. Exact descriptions outside positive even-trace and positive odd-companion parameters are not claimed. Scientific priority has not been independently certified.
