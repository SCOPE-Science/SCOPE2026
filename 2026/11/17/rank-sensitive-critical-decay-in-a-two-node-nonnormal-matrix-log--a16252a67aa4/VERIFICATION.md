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

# Verification and reproduction

Run `python3 checker.py` from this folder with the Python standard library. The script runs exact rational checks of the two-by-two inverse recurrence for ten finite comparison steps, exact rank-one checks over 18 finite steps, exact one-step trace amplification identities, and 50-digit decimal long-horizon diagnostics for two coupling strengths and three initial rank classes. The analytic proof in RESULT.md establishes all infinite-time limits. Exact arithmetic for finitely many steps and numerical agreement at 20,000 steps do not imply any infinite-time assertion by themselves.

Verified example outputs at 20,000 steps with \(c=1\): full-rank scaled entries approximately \((3.993495,5.981093,11.942412)\), transverse rank-one \((2.99955,2.99955,2.99955)\), and eigenline rank-one \((0.99933,0,0)\). These are not interval enclosures of the limiting constants. Only the stated two-by-two regime and strictly subidentity initial domain are claimed. Independent audit has not been performed.
