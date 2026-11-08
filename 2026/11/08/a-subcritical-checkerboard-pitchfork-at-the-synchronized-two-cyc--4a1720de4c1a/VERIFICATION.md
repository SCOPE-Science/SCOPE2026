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
# Reproducibility and limits

Run `python3 verify_pitchfork.py` with Python 3 and NumPy available. The program implements the two-colour update from the defining map, computes the exact critical coefficient, constructs full-ring Jacobians separately at the two temporal phases, and checks all relevant eigenvalue counts. It independently performs 124 assertions, using six even ring sizes and three distances below the critical coupling. The numerical root-finding step is only an experiment and is not a substitute for the analytic implicit-function theorem or the Lyapunov–Schmidt argument.

The proof in `RESULT.md` establishes all fixed even \(N\ge4\), exact local uniqueness, and the asymptotic coefficients. The exactness depends on the algebraic formulas and strict inequalities in that proof, not on floating-point output. Testing does not certify existence for every \(N\), a global basin, neutral endpoint dynamics, or historical originality beyond the inspected comparisons.
