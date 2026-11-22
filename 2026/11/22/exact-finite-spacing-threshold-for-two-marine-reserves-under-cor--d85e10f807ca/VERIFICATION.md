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

# Verification procedures and limits

Run `python3 verify.py` from the directory containing this file. The checker uses only the Python 3 standard library and reports `12532 checks passed` on the packaged bytes. It reconstructs the transient transition matrix, checks the exact determinant formula and diagonal bound over exact-rational grids, compares the direct Perron eigenvalue with the exact sign inequality over deterministic parameter samples, checks the unique critical-ratio calculation, and tests the exact \(k=2\) quadratic interval.

The analytic proof in `RESULT.md` establishes the full continuous ranges \(0<r<1\), \(\alpha,\mu>0\) and \(d\ge0\), not merely the finite tests. The code's finite random samples are diagnostics, not exhaustive certification. Full-text inspection of Blowes and Connolly (2012) was unavailable; the priority comparison to that work remains bounded by accessible abstract evidence. Independent audit has not been performed.
