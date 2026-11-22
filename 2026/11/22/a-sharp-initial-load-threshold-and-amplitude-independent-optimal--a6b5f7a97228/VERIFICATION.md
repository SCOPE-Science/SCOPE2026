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

The theorem follows from elementary closed-form interval dynamics, an explicit derivative identity and a global strict sign argument. The script `check.py` requires only the Python standard library, uses a fixed random seed, and evaluates 1,000 parameter sets through 71,003 assertions. Those tests check a discretized global comparison, numerical derivative agreement, exact regret formulas, and the claimed dependence on enhanced removal. The all-positive-parameter theorem is **not** inferred from finite tests; the proof supplies its quantifiers and all boundary cases.

Canonical case: \(q=b=1\), \(a=3\), \(T=4\), \(h=1\), \(C_0=0\). Optimal start \(\tau_*=1.5\), with \(J(0)\approx2.578509392222\) and \(J(\tau_*)\approx2.196190111820\). Approximate improvement relative to immediate start is \(14.827143\%\).

Independent audit has not been performed; this numerical replay does not constitute an external verification or an empirical validation of the physical model.
