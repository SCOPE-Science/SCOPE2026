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

The proof uses square completion for the real Gaussian transform, linear independence of finitely many real exponentials, linear independence of distinct-frequency complex exponentials, and a nonzero-analytic-determinant genericity argument. No computer computation is used to extrapolate from finite rank examples to general supports.

Run `python verify_gaussian_scans.py` with SymPy installed. The checker builds matrices with exact algebraic entries, after deleting only explicitly nonzero positive column factors; nodes represented by integer \(r\) correspond to physical time \(x=r\log(2)/\pi\). It checks: (1) the \(9\)-by-\(9\) Sidon two-line determinant, (2) rank deficiency eight for a three-shift progression on two lines, and (3) full rank nine on three lines. The expected output is `GAUSSIAN_SCAN_RANK_CHECK_PASS 3`.

All mathematical conclusions outside these finite examples are established in `RESULT.md`; no numerical-conditioning bound, rank-one nonlinear minimality theorem, or external independent audit is supplied.
