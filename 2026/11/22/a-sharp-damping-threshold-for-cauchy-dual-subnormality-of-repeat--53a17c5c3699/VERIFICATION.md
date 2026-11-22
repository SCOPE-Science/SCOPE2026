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

# Reproducibility and scope

Run `python verify.py` with the Python standard library from this directory. The local checker passed 344 finite tests, including rational exact forward-difference identities, product telescoping, critical-root bisection, stationary-value checks, moment quadratures and sign sampling around the critical threshold.

The root \(z_2\) is characterized as the unique solution of \(\tan z=z\) in \((2\pi,5\pi/2)\). The damping threshold \(\rho_*\) is the unique solution of the displayed scalar equation in `RESULT.md`; its defining equation, not its decimal approximation, is used in the proof.

Verification of the unbounded family of shift moments and the entire parameter range uses the analytic polynomial-difference and critical-minimum arguments in `RESULT.md`, not a finite search. No independent audit or external proof certificate has been performed.
