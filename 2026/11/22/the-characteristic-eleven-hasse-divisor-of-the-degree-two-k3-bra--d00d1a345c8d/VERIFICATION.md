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

# Reproducibility and boundaries

Run `python3 VERIFY.py` using Python 3.9 or later. No external packages, network requests or randomness are used. The program computes the characteristic-eleven coefficient tables of the tenth power of the defining sextic, once homogeneously and again in an affine chart, and verifies that they give the same complete ten-by-ten matrix. It checks each of the ten nonzero entries, the exact determinant polynomial identity, singular-parameter exclusion, and all ten smooth rational parameter ranks. For rational parameters it independently computes stabilized rank after twenty ordinary matrix iterates (the semilinear twist is trivial over the prime field). It prints a deterministic success marker and a coefficient-parameter list.

The geometric statements are proved by the matrix's three scalar blocks and three two-cycles: nonzero scalar twists under Frobenius remain nonzero, so stable rank agrees with one-step rank at all algebraic parameters. The factorization and separability of the cubic equations give the full geometric and degree-two Frobenius orbit counts. The program is a finite certificate for the explicit identities, not an infinite-field enumeration, and no independent audit is claimed.
