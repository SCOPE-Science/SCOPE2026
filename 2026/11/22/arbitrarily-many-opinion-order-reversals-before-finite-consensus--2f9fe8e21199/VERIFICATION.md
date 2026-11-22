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

Run `python checker.py` with Python 3 standard-library dependencies only. All arithmetic is rational (built-in `fractions.Fraction`): no tolerance-based equality decisions are used. The program verifies exact matrix-power identities at powers 6 and 12, all pairwise gaps in the first twelve cyclic steps, complete endogenous gate trajectories for four positive confidence scales, the exact first consensus times 17, 29, 41, 53, and all 64 binary reverse-gate combinations in two consecutive updates. Its expected final verdict is:

`PASS: two exact matrix identities, 12 phase gaps, 4 full gated trajectories, 64 scrambling products.`

The proof of the infinite family uses the exact scaling conjugacy, not extrapolation from four samples. Exact gap and gate tables are given in `RESULT.md`. Scientific review has been performed without independent certification; no external audit evidence is asserted.
