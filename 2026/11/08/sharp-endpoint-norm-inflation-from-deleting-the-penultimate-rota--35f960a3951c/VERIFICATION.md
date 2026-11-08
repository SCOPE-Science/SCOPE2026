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

# Reproducibility and verification

Run `python verify.py` with Python 3, SymPy and mpmath from the directory containing this file. The script recomputes exact closed formulas for the weighted complete and punctured kernels from their finite character sums over five cutoff values and ten angles each, and tests their leading-term decompositions. It checks the absolute angular integral split at \(\pi/6\) and \(5\pi/6\), and it quadratures the full norm at \(L=6,16,40\) against the two asymptotic constants.

Expected success marker: `SO3_PENULTIMATE_PASS`. The finite numerical tests do not prove the asymptotic for all cutoffs. Its infinite-\(L\) validity follows from the exact trigonometric identities, the uniform \(O(\log L)\) error integral and the bounded-variation oscillatory-mean argument in `RESULT.md`. No formal proof-system certificate or independent audit was performed.
