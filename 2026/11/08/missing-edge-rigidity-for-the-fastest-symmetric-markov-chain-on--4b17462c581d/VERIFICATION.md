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

# Verification and boundaries

The exact Python checker `verify.py` uses only `fractions.Fraction`, with no floating-point eigensolver. It verifies 55 canonical deleted-matching graphs from 3 through 15 vertices, confirms admissibility of the constructed stochastic kernels, and checks their squared centered-operator identities entry by entry. It independently evaluates 3,080 rational missing-neighbor bounds for \(3\le N\le79\).

Command: `python3 verify.py`.

Expected output: `VERIFY_OK matching_cases=55 bound_cases=3080`.

The infinite statements are proved algebraically in `RESULT.md`: the lower bound uses column sparsity and Cauchy--Schwarz; strictness uses a vertex missing at least two neighbors; sufficiency uses an explicit orthogonal involution. The checker is corroboration of these identities, not an exhaustive finite enumeration of all graphs or an independent mathematical audit.
