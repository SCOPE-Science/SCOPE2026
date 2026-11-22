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

# Verification of the reported theorem

Execute \(\texttt{python check.py}\) with Python 3. The standard-library calculations use rational alternating Taylor bounds on \(\exp(-u)\), after integer rescaling \(u/m\in(0,1]\), and positive integer powers. The run checked eight sign inequalities, endpoint comparison inequalities, the exponential majorant and a strict derivative-gap bound; it completed 61 exact-rational assertions. Optional SciPy root finding produces approximations only and can be skipped.

The finite checks do **not** establish the global zero-count or uniqueness: those follow from the analytic \(F''\)-root bound, Rolle's theorem, the envelope identity and strict inequality of branch derivatives as proved in RESULT.md. The only computational premises used by the proof are finite strict inequalities at rational inputs; those are checked with provable rational intervals. The code does not claim exhaustive search over arbitrary model parameters. There is no external certification or independent audit.
