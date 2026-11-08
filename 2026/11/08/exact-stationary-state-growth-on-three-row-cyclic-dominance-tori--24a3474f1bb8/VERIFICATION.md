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
# Reproduction instructions

Run `python verify_strip.py` under Python 3.10+ with SymPy installed. The program requires no external data and no network access. It constructs its 100-state matrix independently of the displayed polynomial lists, then checks all coefficients of the claimed characteristic factorization exactly, verifies both recurrent components and a self-loop in the main component, verifies matrix-trace counts through length ten, independently exhausts all \(3^9\) and \(3^{12}\) ordered states on actual Moore tori, and isolates the leading real root in \((8.6245,8.6246)\) with rational evaluations and a Sturm count. Execution completed with four lines beginning `VERIFY_OK`.

The all-length proof is the local constraint and trace identity, not a finite experiment. The symbolic characteristic identity is an exact finite certificate, not an approximate eigenvalue fit. The growth asymptotic uses the primitive-component Perron–Frobenius theorem. No claims are made about convergence of arbitrary cellular-automaton trajectories, broader strips, or independent scientific audit.
