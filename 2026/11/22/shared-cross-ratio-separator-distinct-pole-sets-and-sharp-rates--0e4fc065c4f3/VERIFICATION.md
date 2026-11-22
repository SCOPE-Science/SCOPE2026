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

# Verification

The standalone `verify_quadratic_ehrlich_aberth.py` requires Python 3 and SymPy. Run it in the same directory as this document using `python verify_quadratic_ehrlich_aberth.py`. It checks the two exact coordinate updates by symbolic rational simplification, the transformed invariant laws, the cross-ratio exponents, return-matrix eigenvalue identities and direct native-versus-closed-form iterates on exact rational initial states. It also checks a nonroot Jacobi two-cycle and divisibility data used in the all-period construction.

The proof in `RESULT.md` is symbolic and uniform over simple quadratics, nonroot complex starts and all nonnegative iteration counts on forward-regular trajectories. Its periodic-point construction and limiting constants are not inferred from the verifier's finite tests. No floating-point or higher-degree stability statement is established, and no independent audit was performed.
