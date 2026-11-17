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

The main proof is analytic and does not rely on finite experiments to establish the infinite theorem. The included `checker.py` is executable with the Python standard library and performs exact rational binomial-recursion tests, reproducible finite weighted-tail tests, and finite-cycle mean and convergence diagnostics. Execute `python3 checker.py` after extracting the files. Boundary cases (all-zero operator, zero weights in a line, cycles of length one, infinitely many components, \(0<p<1\)) are handled in the proof. Earlier code outputs and unavailable literature are not represented as certificates. No independent audit was performed.
