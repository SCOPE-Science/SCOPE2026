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

# Verification details

Run the standalone, standard-library-only script with \(\texttt{python3 verify.py}\). Its observed output is recorded in \(\texttt{verification_output.txt}\). The checker uses exact rational arithmetic, finite-dimensional monomial sphere integrals, and representative rational orthogonal frames. It independently evaluates \(\mathbb E\|G\|^2\) and \(\mathbb E G\) via the explicit spherical monomial formula, compares mean/variance/risk to the claimed tensor equalities, checks harmonic trace cancellation, tests direct central-difference function values, and verifies sharp positive-radius examples. It passed 1967 exact rational assertions.

The proof of the theorem for arbitrary dimension is the symbolic pairing-and-orthogonality argument in RESULT.md. Exact checks for finitely many dimensions are not an infinite proof. This verification does not establish publication priority and is not an independent audit.
