---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1,
  "record_status": "passed"
}
---
# Verification

The unchanged `CHECK.py` in the accompanying original package uses Python 3 and NumPy. It constructs the stationary density and backward Poisson corrector by Fourier collocation, then evaluates the continuous and jump contributions to diffusivity. The supplied verifier checks 18 finite-amplitude cases against the predicted leading coefficient and checks 27 quadratic root, optimization, and sign cases. These are numerical and algebraic consistency checks, not a proof by enumeration. The analytic derivation in `RESULT.md` establishes the coefficient for each fixed set of positive parameters, including parameters where it vanishes. It does not establish the finite-amplitude sign at zeros of that coefficient or give a uniform amplitude bound.
