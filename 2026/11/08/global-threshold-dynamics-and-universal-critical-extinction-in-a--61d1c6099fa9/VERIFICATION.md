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
# Verification record

The analytic proof of all positive-orbit statements is in RESULT.md. For an independently repeatable finite consistency check of the model algebra, run `python3 verify.py` with SymPy and SciPy.

The checker verifies exactly, in symbolic arithmetic, the Bendixson–Dulac identity and the critical Jacobian coefficients at a rational parameter choice. It evaluates three regimes of the same equations using adaptive high-accuracy integration. At the critical parameters \((r,a,\alpha,k,\beta,\delta,c,m,\eta)=(2,1,1,1,2,1/2,1/2,1/2,1)\), it checks \(U=1\) and \(A=B=C=3/2\), then compares \(t v(t)\) and \(t[1-u(t)]\) with the predicted value \(2/3\) at \(t=10000\). It also checks the coexistence and subcritical-extinction examples.

Expected success indicator: `VERIFY_OK exact_dulac=1 exact_critical_coefficients=3 critical_long_time=1 coexistence=1 subcritical=1`.

No finite simulation proves universal global convergence, excludes all trajectories, or establishes a limit. Those conclusions are proved in RESULT.md via scalar comparison, Bendixson–Dulac, planar limit-set structure, and reciprocal asymptotics. An independent audit has not been performed.
