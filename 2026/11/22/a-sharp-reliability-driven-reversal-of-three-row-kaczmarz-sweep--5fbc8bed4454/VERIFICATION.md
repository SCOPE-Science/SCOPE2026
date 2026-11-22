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

# Reproduction

Run `python verify.py` with Python 3 and SymPy. Exact symbolic operations verify the six permutation classes, the three nested erasure recursions, all eight erasure masks, the decisive trace/determinant differences and the quintic crossover. The script checks the isolating interval with rational endpoints and the relevant upper eigenvalue branches, and evaluates supplementary rational delivery probabilities. Recorded standard output is in `verification_output.txt`.

# Scope and limits

Finite mask enumeration is exhaustive for a single three-attempt sweep. Symbolic identities and the analytic positive-root argument, rather than sampled floating-point eigenvalues, establish the continuum-in-probability result. No numerical roundoff guarantees, different row geometries or multi-sweep claims are included. Independent validation has not been performed.
