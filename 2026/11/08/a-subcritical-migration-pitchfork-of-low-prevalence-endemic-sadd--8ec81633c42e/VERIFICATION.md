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

# Reproduction and verification

Run `python verify.py` with SymPy installed. The script executes standalone with no external file inputs or network, and prints `VERIFY_OK` only after checking the exact equilibrium coordinates, reaction Jacobian, spectrum, normalized left/right eigenvectors, the quadratic polarization identity, the mean slaving term, the critical cubic solvability identity and its strict negative sign. This verifies all nontrivial rational and radical computations appearing in the theorem.

The mathematical local existence and stability statements are established by the implicit-function / Lyapunov–Schmidt argument and continuity of noncritical eigenvalues in `RESULT.md`; a finite checker cannot substitute for these theorems. Direct nonlinear numerical equilibrium solves near the critical migration rate were used as a diagnostic, not as a global enumeration or proof of an infinite branch. Independent external audit has not been performed.
