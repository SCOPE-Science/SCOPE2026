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
# Verification details

The theorem is proved analytically in `RESULT.md`; the executable `check_cesaro.py` is an independent direct numerical evaluation of stated integral formulas and randomly signed variation measures. Execute with Python, SciPy and mpmath available using `python check_cesaro.py`.

The checker independently quadratures the jump-defect kernel against the claimed optimized closed form for twelve iteration counts; tests six deliberately displaced jump locations per count; tests 960 signed multijump inequalities with numerical integration; and evaluates the large-order deficiency at five increasing orders. The finite experiments do not establish a universal theorem or exhaustive priority. The exact unique critical point and global BV extension follow from the proofs, not these tests.

No external proof certificate or independent audit is claimed. Historical comparison includes full accessible primary texts and limited public indexed summaries as described in `REVIEW.md` and `AUDIT.json`.
